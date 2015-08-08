
.. _Zusammengesetzte Datentypen:

Zusammengesetzte Datentypen
===========================

.. index:: typedef
.. _typedef:

``typedef`` -- Synonyme für andere Datentypen
---------------------------------------------

Mit dem Schlüsselwort ``typedef`` kann ein neuer Name für einen beliebigen
Datentyp vergeben werden. Die Syntax lautet dabei wie folgt:

.. code-block:: c

    typedef datentyp neuer_datentyp

Beispielsweise kann mittels ``typedef int integer`` ein "neuer" Datentyp namens
``integer`` erzeugt werden. Dieser kann anschliessend wie gewohnt bei
Deklarationen von Variablen verwendet werden, beispielsweise wird durch
``integer num_1;`` eine neue Variable als Integer-Wert deklariert.

Die Verwendung von ``typedef`` ist insbesondere bei der Definition von
zusammengesetzten Datentypen hilfreich.



..  Bei der Verwendung eines Zeiger ps auf eine Datenstruktur muss man beim
..  Komponentenzugriff ebenfalls aufpassen. ``*ps.elem`` liefert wegen dem Vorrang
..  ``.`` vor ``*`` nicht das richtige Ergebnis. Entweder man klammert
..  ``( *ps).elem`` oder man verwendet den Pfeiloperator ``ps->elem``.

.. index:: enum
.. _enum:
.. _Aufzählungen:

``enum`` -- Aufzählungen
------------------------

Aufzählungen ("enumerations") bieten neben :ref:`#define
<Präprozessor-Anweisungen>`-Anweisungen eine einfache Möglichkeit, einzelnen
Begriffen eine Nummer zuzuweisen und sie somit im Quellcode als leicht lesbare
Bezeichner verwenden zu können.

Bei der Deklaration eines ``enum``-Typs werden die einzelnen Elemente der
Aufzählung durch Komma-Zeichen getrennt aufgelistet. Sie bekommen dabei, sofern
nicht explizit andere Werte angegeben werden, automatisch die Nummern ``0, 1, 2,
...`` zugewiesen; bei expliziten Wertzuweisungen wird der Wert für jedes
folgende Element um ``1`` erhöht.

.. code-block:: c

    typedef enum 
    {
        const1, const2, const3, ...
    } enum_name;

    # Beispiel:

    typedef enum 
    {
        MONTAG = 1, DIENSTAG, MITTWOCH, DONNERSTAG, FREITAG, SAMSTAG, SONNTAG
    } wochentag;
    
Allgemein müssen die Elemente eines ``enum``-Typs unterschiedliche Werte
besitzen. Oftmals werden die aufgelisteten Elemente zudem in Großbuchstaben
geschrieben, um hervorzuheben, dass es sich auch bei ihnen um (ganzzahlige)
Konstante handelt. 

Nach der obigen Deklaration ist beispielsweise ``wochentag`` als neuer Datentyp
verfügbar, der stets durch einen "benannten" ``int``-Wert repräsentiert wird:

.. code-block:: c

    wochentag heute = DIENSTAG;

    // Die zugewiesene Nummer ausgeben:

    printf("Heute ist der %d. Tag der Woche\n", heute);
    // Ergebnis: Heute ist der 2. Tag der Woche.

    // Funktionen definieren:

    wochentag morgen(wochentag heute)
    {
        if (heute == SONNTAG)
            return 1;
        else
            return heute++;
    }

Es können somit nach der Deklaration des ``enum``-Datentyps auch dessen Elemente
als numerische Konstante im C-Code verwendet werden.


.. beispiel: fehlercodes


.. index:: struct
.. _struct:
.. _Strukturen:

``struct`` -- Strukturen
------------------------

Strukturen ("structs") ermöglichen es in C mehrere Komponenten zu einer Einheit
zusammenenzufassen, ohne dass diese den gleichen Datentyp haben müssen (wie es
bei einem :ref:`Array <Felder>` der Fall ist. Der Speicherplatzbedarf einer
Struktur entspricht dabei dem Speicherplatzbedarf ihrer Komponenten. In dem
meisten Fällen lassen sich Strukturen folgendermaßen definieren:

.. code-block:: c

    typedef struct 
    {
        // ... Deklaration der Komponenten ...

    } struct_name;

    // Beispiel:

    typedef struct 
    {
        char name[50];
        int laenge;
        int breite;
        int hoehe;
    } gegenstand;

Nach der Deklaration einer Struktur kann diese als neuer Datentyp verwendet
werden. Die einzelnen Komponenten werden nicht dabei durchnummeriert, sondern
lassen sich mittels des Strukturzugriff-Operators ``.`` über bei der Definition
vergebene Schlüsselwörter ansprechen:

.. code-block:: c

    // Struktur-Objekt definieren:

    gegenstand tisch = 
    {
        "Schreibtisch", 140, 60, 75
    };
    
    // Informationen zum Objekt ausgeben:

    printf( "Der Gegenstand \"%s\" ist %d cm hoch.\n", tisch.name, tisch.hoehe );
    // Ergebnis: Der Gegenstand "Schreibtisch" ist 75 cm hoch.

Handelt es sich bei einer Struktur-Komponente um einen Zeiger, beispielsweise
eine Zeichenkette, so muss der Inhalts-Operator ``*``  vor den Strukturnamen
geschrieben werden. Im obigen Beispiel würde man also nicht ``tisch.*name``
schreiben (was beim Compilieren einen Fehler verursachen würde), sondern
``*tisch.name``, da der Strukturzugriff-Operator ``.`` eine höhere
:ref:`Priorität <Rangfolge der Operatoren>` besitzt. Zuerst wird also der
Strukturzugriff ausgewertet, wobei sich eine Variable vom Typ ``char *`` ergibt;
anschließend kann diese mit dem Inhaltsoperator dereferenziert werden. Bei
``*strukturname.komponente`` kann somit der Punkt wie ein Teil des
Veriablennamens gelesen werden.

Strukturen können andere Strukturen als Komponenten enthalten; rekursive
Strukturen, die sich selbst als Komponente beinhalten, sind nicht möglich. Eine
Struktur kann allerdings einen :ref:`Zeiger <Zeiger>` auf sich selbst enthält,
so dass beispielsweise so genannte Verkettungen möglich sind. Darauf wird im
Abschnitt :ref:`Dynamische Datenstrukturen <Dynamische Datenstrukturen>` näher
eingegangen.


.. _Zeiger auf Strukturen:

.. rubric:: Zeiger auf Strukturen

Eine Struktur wird selten direkt als Argument an eine Funktion übergeben, da
hierbei der gesamte Strukturinhalt kopiert werden müsste. Stattdessen wird
üblicherweise ein Zeiger auf die Struktur an die Funktion übergeben.

Hat man beispielsweise eine Struktur ``mystruct`` mit den Komponenten ``int a``
und ``int b`` und ein bereits existierendes ``mystruct``-Objekt ``x_1``, so kann
man mittels ``mystruct * x_1_pointer = &x_1;`` einen :ref:`Zeiger <Zeiger>` auf
die Struktur definieren. Mittels eines solchen Pointers kann man auf folgende
Weise auf die Komponenten der Struktur zugreifen:

.. code-block:: c

    // Struktur deklarieren:
    typedef struct 
    {
        int a;
        int b;
    } mystruct;

    // Struktur-Objekt erzeugen:
    mystruct x = {3, 5};

    // Pointer auf Struktur-Objekt erzeugen:
    mystruct * xpointer = &x;

    // Wertzuweisung mittels Pointer:
    (*xpointer).a = 5;

Im obigen Beispiel sind die Klammmern um ``*x_1_pointer`` notwendig, da der
Strukturzugriff-Operator ``.`` eine höhere :ref:`Priorität
<tab-rangfolge-operatoren>` hat als der Inhalts-Operator ``*``. Da Strukturen
und somit auch Zeiger auf Strukturen sehr häufig vorkommen und diese
Schreibweise etwas umständlich ist, gibt es in C folgende Kurzschreibweise:

.. code-block:: c

    (*xpointer).a == xpointer->a
    // Ergebnis: TRUE

Mit dem Pfeil-Operator ``->`` kann also in gleicher Weise auf die Komponenten
eines Struktur-Pointers zugegriffen werden wie mit ``.`` auf die Komponennten
der Struktur selbst.


.. index:: union
.. _Alternativen:

``union`` -- Alternativen
-------------------------

Mittels des Schlüsselworts ``union`` lässt sich ein zusammengesetzter Datentyp
definieren, bei dem sich die bei der Deklaration angegebenen Elemente einen
gemeinsamen Speicherplatz teilen: Es kann dabei zu jedem Zeitpunkt nur eine der
angegebenen Komponenten aktiv sein. Der Speicherplatzbedarf einer Union
entspricht somit dem Speicherplatzbedarf der größten angegebenen Komponente. Die
Deklaration einer ``union`` erfolgt nach folgendem Schema:

.. code-block:: c

    typedef union 
    {
        // ... Deklaration der Komponenten ...

    } union_name;
    
    // Beispiel:

    typedef union
    {
        char text[20];
        int ganzzahl;
        float kommazahl;
    } cell_value;

Nach der Deklaration einer Union kann diese als neuer Datentyp verwendet werden.
Der Zugriff auf die einzelnen möglichen Elemente, die eine Union-Variable
beinhaltet, erfolgt wie bei Strukturen, mit dem ``.``-Operator:

.. code-block:: c

    // Union-Variablen deklarieren:

    cell_value cell_1 = {"Hallo Welt!"};
    cell_value cell_2 = {42};
    cell_value cell_3 = {2.35813};

    // Auf Inhalt einer Union zugreifen:

    printf("%s\n", cell_1.text)

Im Falle eines Zeigers auf eine ``union``-Variable kann, ebenso wie bei
:ref:`Zeigern auf Strukturen <Zeiger auf Strukturen>`, mit dem Pfeil-Operator
``->`` auf die einzelnen Komponenten zugegriffen werden.

Unabhängig davon, welche Komponente aktuell in einer ``union``-Variable mit
einem Wert versehen ist, können stets alle möglichen Komponenten der Union
abgefragt werden; dabei wird der aktuell gespeicherte Wert mittels eines
automatischen :ref:`Casts <Cast-Operator>` in den jeweiligen Datentyp
umgewandelt. Da diese Umwandlung zu unerwarteten Ergebnissen führen kann, kann
es hilfreich sein, für die einzelnen Datentypen der Union-Komponenten
symbolische Konstanten zu vergeben. Fasst man dann sowohl den aktuellen Typ der
Union-Variablen sowie die Union-Variable zu einer Struktur zusammen, so lässt
sich bei komplexeren Datentypen nicht nur Speicherplatz sparen, es kann auch
mittels einer :ref:`case <case>`-Anweisung gezielt Code in Abhängigkeit vom
aktuellen Wert aufgerufen werden:

.. code-block:: c

    typedef enum
    {
        STRING=0, INTEGER=1, FLOAT=2
    } u_type;

    typedef struct 
    {
        u_type type;
        cell_value value;
    } cell_content;

    cell_content my_cell;

    my_cell.type = FLOAT;
    my_cell.value = 3.14;

    switch (my_cell.type)
    {
        case STRING:
            printf("In dieser Zelle ist die Zeichenkette %s gespeichert.", *my_cell.value);

        case INT:
            printf("In dieser Zelle ist die int-Zahl %d gespeichert.", my_cell.value);

        case FLOAT:
            printf("In dieser Zelle ist die float-Zahl %f gespeichert.", my_cell.value);
    }

Auf diese Weise könnte in einem "echten" Programm die Ausgaben eines Wertes
aufgrund nicht nur seines Datentyps, sondern beispielsweise auch aufgrund von
Darstellungsoptionen (Anzahl an Kommastellen, Prozentwert, usw.) angepasst
werden.


