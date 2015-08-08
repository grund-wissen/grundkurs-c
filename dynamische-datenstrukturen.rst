
.. _Dynamische Datenstrukturen:

Dynamische Datenstrukturen
==========================

In C sind nur die in den Abschnitten :ref:`Elementare Datentypen <Elementare
Datentypen>` und :ref:`Zusammengesetzte Datentypen <Zusammengesetzte
Datentypen>` beschriebenen Datentypen vordefiniert. Damit können allerdings
weitere Datentypen abgeleitet werden, die für manche Einsatzbereiche besser
geeignet sind.


.. _Verkettete Listen:

Verkettete Listen
-----------------

Eine verkettete Liste besteht aus einer Vielzahl von Elementen, bei der jedes
Element einen Zeiger seinen Nachfolger enthält; bei einer doppelt verketteten
Liste besitzt jedes Element zusätzlich einen Zeiger auf seinen Vorgänger. Eine
derartige Struktur bietet eine einfache Möglichkeit zusätzliche Elemente in
die Liste aufzunehmen oder Elemente wieder aus der Liste zu entfernen.
Verkettete Listen können somit dynamisch wachsen oder schrumpfen.


.. _Einfach verkettete Listen:

.. rubric:: Einfach verkettete Listen

Bei einer einfach verketteten Liste hat jedes Element einen Zeiger, der auf
seinen unmittelbaren Nachfolger zeigt; der Zeiger des letzten Elements zeigt auf
``NULL``. Verkettete Listen haben stets einen Zeiger, der auf das erste Element
("Head") zeigt, und oftmals auch einen Zeiger auf das letzte Element der Liste
("Tail"). 

Die einzelnen Elemente einer verketteten Liste haben den Datentyp ``struct``. Da
sie allerdings bereits bei ihrer Deklaration einen Pointer auf ein weiteres
Element mit gleichem Datentyp angeben, muss der Name der Struktur dem Compiler
schon im Vorfeld bekannt sein. Man kann dies auf folgendem Weg erreichen:

.. code-block:: c

    struct element_prototype 
    {
        // Eigentlicher Inhalt (hier: int):
        int value;

        // Zeiger auf das nächste Element:
        element_prototype * next;
    };

    typedef element_prototype element_type;

Bei dieser Deklarationsform wird der Strukturname, in diesem Fall
``element_prototype``, *vor* der eigentlichen Deklaration angegeben. Der
Compiler kennt von diesem Moment an zwar noch nicht die Größe der Struktur,
aber zumindest ihren Namen sowie ihren Datentyp, was für die Erstellung eines
Pointers bereits genügt. Anschließend kann der Strukturtyp mittels ``typedef``
umbenannt werden, um im Folgenden anstelle von ``struct element_prototype``
einfacher ``element_type`` für die Bezeichnung des Datentyps schreiben zu
können.

Um mittels der Element-Struktur eine verkettete Liste zu erstellen, müssen
mindestens zwei Elemente definiert werden: Das Head-Element ``e0`` sowie ein
weiteres Element ``e1``, das im Fall von nur zwei Einträgen zugleich auch das
Schluss-Element ist:

.. code-block:: c

    // Zeiger auf Elemente deklarieren:
    element_type *e0, *e1;

    int init_list()
    {
        // Dynamischen Speicherplatz für Elemente reservieren:
        e0 = (element_type *) malloc(sizeof *e0);
        e1 = (element_type *) malloc(sizeof *e1);

        // Fehlerkontrolle:
        if (e0 == NULL) || (e1 == NULL)
            return 1;

        // Referenzen anpassen:
        e0->next = e1;
        e1->next = NULL;

        // Normaler Rückgabewert:
        return 0;
    }

Möchte man ein weiteres Element in die verkettete Liste aufnehmen, so muss
einerseits der Speicherplatz für das zusätzliche Element reserviert werden.
Andererseits muss der Zeiger des Elements, hinter dem das neue Element
eingefügt werden soll, aktualisiert werden:

.. code-block:: c

    element_type * insert_element_after(element_type *e, int value_new)
    {
        // Zeiger auf neues Element deklarieren:
        element_type *e_new            

        // Dynamischen Speicherplatz für neues Element reservieren:
        e_new = (element_type *) malloc(sizeof *e_new);

        // Fehlerkontrolle: Kein Speicherplatz verfügbar:
        if (e_new == NULL)
            return NULL;

        // Inhalt des neuen Elements zuweisen:
        e_new->value = value_new;

        // Referenzen anpassen:
        e_new->next = e->next;
        e->next = e_new;

        // Zeiger auf neues Element zurückgeben:
        return e_new;
    }

Der Zeiger des neuen Elements ``e_new`` muss nach dem Einfügen auf die Stelle
verweisen, auf die der Zeiger des Vorgänger-Elements ``e`` bislang gezeigt hat.
Dafür muss der Zeiger des Vorgänger-Elements ``e`` nach dem Einfügen auf das
neue Element ``e_new`` verweisen. 

Um das Nachfolger-Element eines bestimmten Element aus einer einfach verketteten
Liste zu entfernen, muss einerseits der Zeiger des dieses Elements auf das
übernächste Element umgelenkt werden; andererseits muss der dynamisch
reservierte Speicherplatz für das zu entfernende Element wieder freigegeben
werden:

.. code-block:: c

    int delete_element_after(element_type *e)
    {
        // Fehlerkontrolle (e letztes Element der Liste):
        if (e->next == NULL)
            return 1;

        // Referenzen anpassen:
        e->next = e->next->next; 

        // Speicherplatz freigeben:
        free(e->next);

        // Normaler Rückgabewert:
        return 0;
    }

Soll nicht das Nachfolger-Element eines angegebenen Elements, sondern dieses
selbst gelöscht werden, so muss zuerst der Vorgänger des Elements ermittelt
werden. Dies kann man erreichen, indem man vom Head-Element aus die Zeigerwerte
der einzelnen Elemente mit dem Zeigerwert des angegebenen Elements vergleicht:

.. code-block:: c

    element_type * find_previous_element(element_type *e)
    {
        // Temporären und Vorgänger-Zeiger deklarieren:
        element_type *e_pos;  
        element_type *e_prev;

        // Temporären Zeiger auf Head-Element setzen:
        e_pos = e0;

        // Temporären Zeiger mit Zeigern der Listenelemente vergleichen:
        while ( (e_pos != NULL) && (e_pos != e) )
        {
            e_prev = e_pos;         // Zeiger auf bisheriges Element zwischenspeichern
            e_pos  = e_pos->next;   // Temporären Zeiger iterieren
        }

        // Die while-Schleife wird beendet, wenn die Liste komplett durchlaufen
        // oder das angegebene Element gefunden wurde; in letzterem Fall zeigt 
        // e_pos auf das angegebene Element, e_prev auf dessen Vorgänger.

        // Fall 1: Liste wurde erfolglos durchlaufen (Element e nicht in Liste):
        if ( (e_pos == NULL) && (e_prev != e) )
            return NULL;

        // Fall 2: Element e ist erstes Element der Liste:
        else if (e_pos == e0)
            return NULL;
                
        // Fall 3: Element e0 wurde an anderer Stelle gefunden:
        else
            return e_prev;
    }

Das Löschen eines Elements kann mit Hilfe der obigen Funktion beispielsweise
folgendermaßen implementiert werden:

.. code-block:: c

    int delete_element(element_type *e)
    {
        // Vorgänger-Zeiger deklarieren:
        element_type *e_prev;
        
        // Position des Vorgänger-Elements bestimmen:
        e_prev = find_previous_element(e)

        // Fehlerkontrolle: Element e nicht in Liste:
        if ( (e_prev == NULL) && e != e0)
            return 1;
        
        // Angegebenes Element wurde gefunden:

        if (e == e0)        // Angegebenes Element ist erstes Element der Liste
        { 
            e0 = e0->next;      // Neues Head-Element festlegen
        }
        else                    // Angegebenes Element ist nicht erstes Element
        {
            e_prev->next = e->next; // Vorgänger-Element mit 
        }                               // Nachfolger-Element verketten

        // Speicherplatz freigeben:
        free(e);

        // Normaler Rückgabewert:
        return 0;
    }

Offensichtlich ist das Löschen eines bestimmten Elements bei einfach
verketteten Listen mit einigem Rechenaufwand verbunden, da im ungünstigsten Fall
die gesamte Liste durchlaufen werden muss. Das Suchen nach einem bestimmten Wert
in der Liste funktioniert auf ähnliche Weise:

.. code-block:: c

    element_type * search_content(int value)
    {
        // Temporären Zeiger definieren:
        element_type *e_pos = e0;

        // Wert des Elements e_pos mit angegebenem Wert vergleichen:
        while ( (e_pos->value != value) &&  (e_pos != NULL) )
        {
            e_pos  = e_pos->next;   // Temporären Zeiger iterieren
        }

        // Die while-Schleife wird entweder beendet, wenn die Liste komplett
        // durchlaufen oder der angegebene Wert gefunden wurde; in ersten Fall ist
        // e_pos gleich NULL, im zweiten Fall zeigt e_pos auf das entsprechende
        // Element.

        return e_pos;
    }

Auch beim Suchen eines bestimmten Werts muss die verkettete Liste im
ungünstigsten Fall komplett durchlaufen werden. Um eine verlinkte Liste wieder
zu löschen, werden nacheinander die einzelnen Elemente mittels ``free()`` wieder
freigegeben:

.. code-block:: c

    void delete_list()
    {
        // Temporäre Zeiger definieren:
        element_type *e_pos;
        element_type *e_tmp;

        // Temporären Zeiger auf Head-Element setzen:
        e_pos = e0;

        // Alle Elemente der Liste durchlaufen:
        while ( e_pos != NULL )
        {
            e_tmp = e_pos->next;    
            free(e_pos);
            e_pos = tmp;
        }



.. _Doppelt verkettete Listen:

.. rubric:: Doppelt verkettete Listen

Enthält jedes jedes Element einer verketteten Liste nicht nur einen Zeiger auf
seinen Nachfolger, sondern ebenso einen Zeiger auf seinen Vorgänger, so spricht
man von einer doppelt verketteten Liste. Die Deklaration eines Listenelements
sowie die Erzeugung einer Liste ist im Wesentlichen mit der einer einfach
verketteten Liste identisch:

.. code-block:: c

    struct element_prototype 
    {
        // Eigentlicher Inhalt (hier: int):
        int value;

        // Zeiger auf das vorheriges und nächste Element:
        element_prototype * prev;
        element_prototype * next;
    };

    typedef element_prototype element_type;

.. code-block:: c

    // Zeiger auf Elemente deklarieren:
    element_type *e0, *e1;

    int init_list()
    {
        // Dynamischen Speicherplatz für Elemente reservieren:
        e0 = (element_type *) malloc(sizeof *e0);
        e1 = (element_type *) malloc(sizeof *e1);

        // Fehlerkontrolle:
        if (e0 == NULL) || (e1 == NULL)
            return 1;

        // Referenzen anpassen:
        e0->prev = NULL;
        e0->next = e1;

        e1->prev = e0;
        e1->next = NULL;

        // Normaler Rückgabewert:
        return 0;
    }

Ein Vorteil von doppelt verketteten Listen liegt darin, dass man sowohl vor- als
auch rückwärts in der Liste nach Inhalten suchen kann. Ebenso kann man -- im
Vergleich zu einfach verketteten Listen --  ein bestimmtes Listenelement mit
weniger Aufwand an einer bestimmten Stelle einfügen oder löschen.

..  Oesch 106

.. Zirkuläre Listen


