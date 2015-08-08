.. _Funktionen für Felder und Zeichenketten:

Funktionen für Felder und Zeichenketten
=======================================


.. _Dynamische Speicherreservierung:

``malloc()`` und ``calloc()`` -- Dynamische Speicherreservierung
----------------------------------------------------------------

Soll die Größe eines Feldes erst zur Laufzeit bestimmt werden, so ermöglichen es
die Funktionen ``malloc()`` und ``calloc()`` aus der Standard-Bibliothek
:ref:`stdlib.h <stdlib.h>`, nach Möglichkeit ein entsprechend großes Stück an
freiem Speicherplatz ("memory") zu finden und für das Feld zu reservieren
("allocate").

Der Speicher eines Programms setzt sich allgemein zusammen aus einem Teil namens
"Stack", der für statische Variablen reserviert ist, und einem dynamischen Teil
namens "Heap", auf den mittels ``malloc()`` oder ``calloc()`` zugegriffen werden
kann.

Bei der Verwendung dieser Funktionen kann :ref:`valgrind <valgrind>` als
"Debugger" für dynamischen Speicherplatz eingesetzt werden.

.. index:: malloc(), free()
.. _malloc():

.. rubric:: Die Funktion ``malloc()``

Als Ergebnis gibt die Funktion ``malloc()`` einen Zeiger auf die nutzbare
Speicheradresse zurück, oder ``NULL``, falls keine Speicherreservierung möglich
war. Bei jeder neuen Speicherreservierung sollte der Rückgabewert geprüft und
gegebenenfalls eine Fehlermeldung ausgegeben werden. Im erfolgreichen Fall hat
der zurück gegebene Zeiger den Typ ``void *`` und wird üblicherweise vom
Programmierer mittels des ``cast``-Operators in einen Zeiger vom gewünschten Typ
umgewandelt.

Um beispielsweise einen dynamischen Speicherplatz für ein Array mit :math:`50`
``int``-Werten zu erhalten, kann man folgendes eingeben:

.. code-block:: c

    numbers = (int *) malloc(50 * sizeof(int));

An die Funktion ``malloc()`` wird allgemein die zu reservierende Speichergröße
in Bytes als Argument übergeben; für beispielsweise :math:`50` Werte vom
Datentyp ``int`` ist damit auch das Fünfzigfache der Größe dieses Datentyps
nötig. Der Rückgabewert von ``malloc()``, nämlich ``void *``, wird mit Hilfe des
Casts ``(int *)`` in einen Zeiger auf ``int`` umgewandelt.

Wird der Speicher nicht mehr benötigt, so muss er manuell mittels ``free()``
wieder freigegeben werden. Als Argument wird dabei der Name des variablen
Speichers angegeben, also beispielsweise ``free(numbers)``. In C gibt es keinen
"Garbage Collector", der nicht mehr benötigte Speicherbereiche automatisch
wieder freigibt; es ist also Aufgabe des Programmierers dafür zu sorgen, dass
Speicher nach dem Gebrauch wieder freigegeben wird und somit kein Speicherleck
entsteht.

.. index:: calloc()
.. _calloc():

.. rubric:: Die Funktion ``calloc()``

Neben der Funktion ``malloc()`` gibt es in der Standardbibliothek :ref:`stdlib.h
<stdlib.h>` eine weitere Funktion zur dynamischen Speicherreservierung namens
``calloc()``. Beim Aufruf dieser Funktion wird als erstes Argument die Anzahl
der benötigten Variablen, als zweites Argument die Größe einer einzelnen
Variablen in Bytes angegeben. Bei einer erfolgreichen Reservierung wird, wie bei
``malloc()``, ein ``void *``-Zeiger auf den reservierten Speicher zurückgegeben,
andernfalls ``NULL``. Der Unterschied zwischen ``malloc()`` und ``calloc()``
liegt darin, dass ``calloc()`` alle Bits im Speicherbereich auf ``0`` setzt und
dadurch sicherstellt, dass zuvor mit ``free()`` freigegebene Daten zufällig
weiterverarbeitet werden.

Auch bei der Verwendung von ``calloc()`` muss Speicher, der nicht mehr benötigt
wird, manuell mittels ``free()`` wieder freigegeben werden.


.. index:: realloc()
.. _realloc():

.. rubric:: Die Funktion ``realloc()``

Mit der Funktion ``realloc()`` kann ein mit ``malloc()`` oder ``calloc()``
reservierter Speicherbereich nachträglich in seiner Größe verändert werden.

Als erstes Argument gibt man bei ``realloc()`` einen Zeicger auf einen bereits
existierenden dynamischen Speicherbereich an, als zweites die gewünschte neue
Größe des Speicherbereichs. Kann der angeforderte Speicher nicht an der
bisherigen Adresse angelegt werden, weil dort kein ausreichend großer
zusammenhängender Speicherbereich mehr frei ist, dann verschiebt ``realloc()``
den vorhandenen Speicherbereich an eine andere Stelle im Speicher, an der noch
genügend Speicher frei ist.

.. code-block:: c

    numbers = (int *) realloc(numbers, 100 * sizeof(int));

Als Ergebnis gibt die Funktion ``realloc()`` ebenfalls einen ``void *``-Zeiger
auf den reservierten Speicherbereich zurück, wenn die Speicherreservierung
erfolgreich war, andernfalls ``NULL``. Übergibt man an ``realloc()`` einen
``NULL``-Pointer als Adresse, so ist ``realloc()`` mit ``malloc()`` identisch
und gibt einen Zeiger auf einen neu erstellten dynamischen Speicherbereich
zurück.


.. index:: memcmp(), strcmp()
.. _Vergleiche von Feldern:

``memcmp()`` und ``strcmp()`` -- Vergleiche von Feldern
-------------------------------------------------------

In C kann man den Inhalt zweier Felder nicht direkt vergleichen, es kann hierfür
also nicht ``array_1 == array_2`` geschrieben werden. Bei diesem Test würden
lediglich, da der Name eines Feldes auf das erste im Feld gespeicherte Element
verweist, die Speicheradressen zweier Variablen verglichen werden, jedoch nicht
deren Inhalt. 

Für einen inhaltlichen Vergleich müssen alle Einzelelemente der Felder
miteinander verglichen werden. Dies kann automatisch mit der Funktion
:ref:`memcmp() <memcmp()>` aus der Standardbibliothek :ref:`string.h <string.h>`
durchgeführt werden. Bei identischen Feldern wird der Wert :math:`0` als
Ergebnis zurückgegeben. Stößt die Funktion im ersten Feld auf einen Wert, der
größer ist als im zu vergleichenden Feld, so wird ein positiver Wert :math:`>0`
zurückgegeben, im umgekehrten Fall ein negativer Wert :math:`<0`.

Handelt es sich bei den Feldern um Zeichenketten, so sollte anstelle von
``memcmp()`` bevorzugt die Funktion ``strcmp()`` verwendet werden. Diese prüft
ebenfalls Zeichen für Zeichen, ob die beiden angegebenen  Zeichenketten
übereinstimmen. Anders als bei ``memcmp()`` wird jedoch das Überprüfen der
Feldinhalte beendet, sobald das String-Ende-Zeichen ``\0`` erreicht wird.
Mögliche Inhalte der Felder hinter diesem Zeichen werden somit nicht verglichen.

.. beispiel

.. strcmp()

..  #include <string.h>

..  if (strcmp(eingabe,"beenden") == 0)


.. index:: memcpy(), strcpy(), strncpy()
.. _Kopieren von Feldern:

``memcpy()`` und ``strcpy()`` -- Kopieren von Feldern
-----------------------------------------------------

Der Funktion ``strcpy()`` wird als erstes Argument der Name des Zielstrings, als
zweites Argument eine dorthin zu kopierende Zeichenkette übergeben:

.. code-block:: c

    char target_string[50];

    strcpy(target_string, "Hallo Welt!");

    puts(target_string);
    // Ergebnis: "Hallo Welt!"

Der Zielstring wird von ``strcpy()`` automatisch mit dem
Zeichenkette-Ende-Zeichen ``'\0'`` abgeschlossen. Wichtig ist zu beachten, dass
``strcpy()`` nicht prüft, ob der Zielstring ausreichend groß ist; reicht der
Platz dort nicht aus, werden die Bytes einer anschließend im Speicher abgelegten
Variablen überschrieben, was unvorhersehbare Fehler mit sich bringen kann. Als
Programmierer muss man somit entweder selbst darauf achten, dass nicht
Zielstring ausreichend groß ist, oder die Funktion :ref:`strncpy() <strncpy()>`
verwenden, welcher als drittes Argument die Anzahl :math:`n` der zu kopierenden
Zeichen übergeben wird.


.. index:: strcat(), strncat()
.. _Verknüpfen von Zeichenketten:

``strcat()`` -- Verknüpfen von Zeichenketten
--------------------------------------------

Der Funktion ``strcat()`` wird als erstes Argument der Name des Zielstrings, als
zweites Argument eine dort anzufügenden Zeichenkette übergeben:

.. code-block:: c

    char target_string[50];

    strcpy(target_string, "Hallo Welt!");;
    strcat(target_string, " Auf Wiedersehen!");

    puts(target_string);
    // Ergebnis: "Hallo Welt! Auf Wiedersehen!"

``strcat()`` überschreibt automatisch das Zeichenkette-Ende-Zeichen ``'\0'``
des Zielstring mit dem ersten Zeichen des anzuhängenden Strings und schließt
nach dem Anfügen der restlichen Zeichen den Zielstring wiederum mit ``'\0'``
ab.

Ebenso wie bei ``strcpy()`` muss auch bei Verwendung von ``strcat()`` auf einen
ausreichend grossen Zielstring geachtet werden. Als Alternativ kann die Funktion
``strncat()`` verwendet werden, der als drittes Argument eine Anzahl :math:`n`
an anzuhängenden Zeichen übergeben wird.


..  
    Umwandlungsfunktionen
    
    atoi aus stdlib: Wandelt Zahlen-Strings in Zahlen um; sprintf() kann
    u.a. Zahlen in Text umwandeln
    
    mynumber = atoi("2463");
    sprintf(mystring, "%i", mynumber);



