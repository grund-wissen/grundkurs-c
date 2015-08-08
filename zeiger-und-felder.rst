.. _Zeiger und Felder:

Zeiger und Felder
=================

In vielen Fällen ist es nützlich, Variablen nicht direkt anzusprechen, sondern
anstatt dessen so genannte Zeiger ("Pointer") zu nützen. Bei einem solchen
Zeiger handelt es sich um eine eigenständige Variable, deren Inhalt die
Speicheradresse einer anderen Variablen ist.

.. index:: Zeiger, Pointer
.. _Zeiger:

Zeiger
------

Bei der Definition eines Zeigers wird festgelegt, für welchen Datentyp der
Zeiger vorgesehen ist. Die Definition eines Zeigers ähnelt dabei weitgehend der
einer normalen Variablen, mit dem Unterschied, dass zur eindeutigen
Kennzeichnung vor den Namen der Zeigervariablen ein ``*`` geschrieben wird:

.. code-block:: c

    int *n;

Es dürfen wiederum mehrere Zeiger auf einmal definiert werden; hierzu werden die
einzelnen Namen der Zeigervariablen durch Kommatas getrennt und die Definition mit
einem abschließenden Strichpunkt beendet.

.. code-block:: c

    int *x, *y, *z;


.. index:: Adressoperator
.. _Adressoperator:

.. rubric:: Der Adressoperator ``&``

Um einer Zeigervariablen einen Inhalt, d.h. die eine gültige Speicheradresse
zuzuweisen, wird der so genannte Adressoperator ``&`` verwendet. Wird dieser
Operator vor eine beliebige Variable geschrieben, so gibt er die zugehörige
Speicheradresse aus. Diese kann wie gewöhnlich in der Variablen auf der linken
Seite des ``=``-Zeichens gespeichert werden:

.. code-block:: c

    int num = 256;
    int *p_num;

    p_num = &num;

In diesem Beispiel ist ``p_num`` ein Zeiger auf eine Integer-Variable, hat also
selbst den Datentyp ``int *``. Entsprechend gibt es auch Zeiger auf die anderen
Datentypen, beispielsweise ``float *``, ``char *`` usw. [#]_

Ein Zeiger, dem noch keine Speicheradresse zugewiesen würde oder der auf eine
ungültige Speicheradresse zeigt, bekommt in C automatisch den Wert ``NULL``
zugewiesen. [#]_


.. index:: Inhaltsoperator
.. _Inhaltsoperator:

.. rubric:: Der Inhaltsoperator ``*``

Möchte man den Zeiger wiederum dazu nutzen, um auf den Inhalt der
Speicheradresse zuzugreifen, kann der sogenannte Inhaltsoperator ``*`` verwendet
werden. Angewendet auf eine bereits deklarierte Variable gibt dieser den zur
Speicheradresse gehörigen Inhalt aus. 

Erzeugt man beispielsweise einen Zeiger ``b``, der auf eine Variable ``a``
zeigt, so ist ``*b`` identisch mit dem Wert von ``a``:

.. code-block:: c

    int a;
    int *b;

    a = 15;
    b = &a;

    printf("Die Adresse von a ist %u!\n" ,  b);
    printf("Der Wert    von a ist %i!\n" , *b);
    
Das Symbol ``*`` hat in C somit zwei grundlegend verschiedene Verwendungsarten.
Einerseits ist es nötig um bei der Deklaration Zeigervariablen von normalen
Variablen zu unterscheiden. Im eigenlichen Programm bezeichnet ``*``
andererseits einen Operator, der es ermöglicht den Inhalt der in der
Zeigervariablen abgelegten Speicherstelle abzufragen.

.. _Zeiger-Initialisierung:

Der ``*``-Operator kann auch für Wertzuweisungen, also auf der linken Seite des
Istgleich-Zeichens benutzt werden. Hierbei muss der Programmierer allerdings
unbedingt darauf achten, dass der jeweilige Zeiger bereits initiiert (nicht
``NULL``) ist, sondern auf eine gültige Speicherstelle zeigt: 

.. code-block:: c

    int a;
    int *b;

    // Zeiger NIEMALS ohne Initialisierung
    // auf die linke Seite schreiben:
    // *b = 15;             // Fataler Fehler, Speicheradresse nicht bekannt!
    // !!!

    // Zeiger IMMER erst initialisieren:
    b  = &a;                // Der Zeiger zeigt jetzt auf die Adresse von a
    *b = 15;                // Zuweisung in Ordnung!

Wäre der Zeiger auf der linken Seite gleich ``NULL``, so würde die Wertzuweisung
an eine undefinierte Stelle erfolgen; im schlimmsten Fall würde eine andere für
das Programm wichtige Speicheradresse überschrieben werden. Ein solcher Fehler
kann vom Compiler nicht erkannt werden, kann aber mit großer Wahrscheinlichkeit
ein abnormales Verhalten des Programms oder einen Absturz zur Folge haben.



.. index:: Array, Feld
.. _Felder:

Felder
------

Als Feld ("Array") bezeichnet man eine Zusammenfassung von mehreren Variablen
gleichen Datentyps zu einem gemeinsamen Speicherbereich. 

Bei der Definition eines Arrays muss einerseits der im Array zu speichernde
Datentyp angegeben werden, andererseits wird zusätzlich in eckigen Klammern die
Größe des Arrays angegeben. Damit ist festgelegt, wie viele Elemente in dem
Array maximal gespeichert werden können. [#]_ Die Syntax lautet somit
beispielsweise:

.. code-block:: c

    int numbers[10]; 

    // Definition und Zuweisung zugleich:
    int other_numbers[5] = { 10, 11, 12, 13, 14 };

Wird ein Array bei der Definition gleich mit einem konkreten Inhalt
initialisiert, so kann die explizite Größenangabe entfallen und anstelle dessen
ein leeres Klammerpaar ``[]`` gesetzt werden.

Der Hauptvorteil bei der Verwendung von Arrays liegt darin, eine Vielzahl
gleichartiger Datei über eine einzige Variable (den Namen des Arrays) ansprechen
zu können. Auf die einzelnen Elemente eines Feldes kann nach im eigentlichen
Programm mittels des so genannten Selektionsoperators ``[]`` zugegriffen werden.
Zwischen die eckigen Klammern wird dabei ein (ganzzahliger) Laufindex ``i``
geschrieben. 

Hat ein Array insgesamt ``n`` Elemente, so kann der Laufindex ``i`` alle
ganzzahligen Werte zwischen ``0`` und ``n-1`` annehmen. Das erste Element hat
also den Index ``0``, das zweite den Index ``1``, das letzte schließlich den
Index ``n-1``. Somit kann der Inhalt jeder im Array gespeicherten Variablen
ausgelesen oder durch einen anderen ersetzt werden:

.. code-block:: c

    int numbers[5]; 

    numbers[0] =  3;
    numbers[1] =  5;
    numbers[2] =  8;
    numbers[3] = 13;
    numbers[4] = 21;

    printf("Die vierte Nummer des Feldes 'num' ist %i.\n", numbers[3]);

Eine Besonderheit von Arrays in C ist es, dass der Compiler beim Übersetzen
nicht prüft, ob bei der Verwendung eines Laufindex die Feldgrenzen eingehalten
werden. Im Fall eines Arrays ``numbers`` mit fünf Elementen könnte
beispielsweise mit ``numbers[5] = 1`` ein Eintrag  in einen Speicherbereich
geschrieben werden, der außerhalb des Arrays liegt. Auf korrekte Indizes muss
somit der Programmierer achten, um Programmfehler zu vermeiden.


.. rubric:: Mehrdimensionale Felder

Ein Array kann wiederum Arrays als Elemente beinhalten. Beispielsweise kann man
sich eine Tabelle aus einer Vielzahl von Zeilen zusammengesetzt denken, die
ihrerseits wiederum eine Vielzahl von Spalten bestehen können. Beispielsweise
könnte ein solches Tabellen-Array, das als Einträge jeweils Zahlen erwartet,
folgendermaßen deklariert werden: [#]_

.. code-block:: c

    // Tabelle mit 3 Zeilen und je 4 Spalten deklarieren:
    int zahlentabelle[3][4];   

Auch in diesem Fall laufen die Indexwerte bei :math:`n` Einträgen nicht von
:math:`1` bis :math:`n`, sondern von :math:`0` bis :math:`n-1`. Der erste
Auswahloperator greift ein Zeilenelement heraus, der zweite eine bestimmte
Spalte der ausgewählten Zeile. Auch eine weitere Verschachtelung von Arrays nach
dem gleichen Prinzip ist möglich, wobei der Zugriff auf die einzelnen Werte
meist über :ref:`for <Schleifen>`-Schleifen erfolgt.

.. _Zeiger auf Felder:

.. rubric:: Zeiger auf Felder

In C sind Felder und Zeiger eng miteinander verwandt: Gibt man den Namen einer
Array-Variablen ohne eckige Klammern an, so entspricht dies einem Zeiger auf die
erste Speicheradresse, die vom Array belegt wird; nach der Deklaration ``int
numbers[10];`` kann also beispielsweise als abkürzende Schreibweise für das
erste Element des Feldes anstelle von ``&numbers[0]`` auch die Kurzform
``numbers`` benutzt werden. [#]_

Da alle Elemente eines Arrays den gleichen Datentyp haben und somit gleich viel
Speicherplatz belegen, unterscheiden sich die einzelnen Speicheradressen der
Elemente um die Länge des Datentyps, beispielsweise um ``sizeof(int)`` für ein
Array mit ``int``-Werten oder ``sizeof(float)`` für ein Array mit
``float``-Werten. Ausgehend vom ersten Elemnent eines Arrays erhält man somit
die weiteren Elemente des Feldes, indem man den Wert des Zeigers um das
:math:`1, 2, \ldots, n-1`-fache der Länge des Datentyps erhöht:

.. code-block:: c

   int numbers[10]; 
   int *numpointer;

   // Pointer auf erstes Element des Arrays:
   numpointer = &numbers;                       // oder: &numbers[0]

   // Pointer auf zweites Element des Arrays:
   numpointer = &numbers + sizeof(int);         // oder: &numbers[1]

   // Pointer auf drittes Element des Arrays:
   numpointer = &numbers + 2 * sizeof(int);     // oder: &numbers[2]

Beim Durchlaufen eines Arrays ist eine Erhöhung des Zeigers in obiger Form auch
mit dem :ref:`Inkrement-Operator <Inkrement und Dekrement>` möglich: Es kann
also auch ``numpointer++`` statt ``numpointer = numpointer + sizeof(int)``
geschrieben werden, um den Zeiger auf das jeweils nächste Element des Feldes zu
bewegen; dies wird beispielsweise in :ref:`for <Schleifen>`-Schleifen genutzt.
Ebenso kann das Feld mittels ``numpointer--`` schrittweise rückwärts
durchlaufen werden; auf das Einhalten der Feldgrenzen muss der Programmierer
wiederum selbst achten.

Da es sich bei Speicheradressen um ``unsigned int``-Werte handelt, können zwei
Zeiger auch ihrer Größe nach verglichen werden. Hat man beispielsweise zwei
Pointer ``numpointer_1`` und ``numpointer_2``, die beide auf ein Elemente eines
Arrays zeigen, so würde ``numpointer_1 < numpointer_2`` bedeuten, dass der
erste Pointer auf ein Element zeigt, das sich weiter vorne im Array befindet.
Ebenso kann in diesem Fall mittels ``numpointer_2 - numpointer_1`` die Anzahl
der Elemente bestimmt werden, die zwischen den beiden Pointern liegen.

Andere mathematische Operationen sollten auf Zeiger nicht angewendet werden;
ebenso sollten Array-Variablen, obwohl sie letztlich einen Zeiger auf das erste
Element des Feldes darstellen, niemals direkt inkrementiert oder dekrementiert
werden, da das Array eine feste Stelle im Speicher einnimmt. Stattdessen
definiert man stets einen Zeiger auf das erste Element des Feldes und
inkrementiert diesen, um beispielsweise in einer Schleife auf die einzelnen
Elemente eines Feldes zuzugreifen.


.. index:: String, Zeichenkette
.. _Zeichenketten:

Zeichenketten
-------------

Zeichenketten ("Strings"), beispielsweise Worte und Sätze, stellen die wohl
häufigste Form von Arrays dar. Eine Zeichenkette besteht aus einer
Aneinanderreihung einzelner Zeichen (Datentyp ``char``) und wird stets mit einer
binären Null (``'\0'``) abgeschlossen. Beispielsweise entspricht die
Zeichenkette ``"Hallo!"`` einem Array, das aus ``'H'``, ``'a'``, ``'l'``,
``'l'``, ``'o'``, ``'!'`` und dem Zeichen ``'\0'`` besteht. Dieser Unterschied
besteht allgemein zwischen Zeichenketten, die mit doppelten Hochkommatas
geschrieben werden, und einzelnen Zeichen, die in einfachen Hochkommatas
dargestellt werden. 

Die Deklaration einer Zeichenkette entspricht der Deklaration eines
gewöhnlichen Feldes:

.. code-block:: c

    // Deklaration ohne Initialisierung:
    char string_one[15];

    // Deklaration mit Initialisierung:
    char string_two[] = "Hallo Welt!"

Bei der Festlegung der maximalen Länge der Zeichenkette muss beachtet werden,
dass neben den zu speichernden Zeichen auch Platz für das String-Ende-Zeichen
``'\0'`` bleiben muss. Als Programmierer muss man hierbei selbst darauf achten,
dass die Feldgröße ausreichend groß gewählt wird.

Wird einer String-Variablen nicht bereits bei der Deklaration eine Zeichenkette
zugewiesen, so ist dies anschliessend zeichenweise (beispielsweise mittels einer
:ref:`Schleife <Schleifen>`) möglich:

.. code-block:: c

    string_one[0] = 'H';
    string_one[1] = 'a';
    string_one[2] = 'l';
    string_one[3] = 'l';
    string_one[4] = 'o';
    string_one[5] = '!';
    string_one[6] = '\0';

Eine Zuweisung eines ganzen Strings an eine String-Variable in Form von
``string_one = "Hallo!"`` ist nicht direkt möglich, sondern muss über die
Funktion :ref:`strcpy() <strcpy()>` aus der Standard-Bibliothek :ref:`string.h
<string.h>` erfolgen:

.. code-block:: c

    // Am Dateianfang:
    #include <string.h>

    // ...

    // String-Variable deklarieren:
    char string_one[15];

    // Zeichenkette in String-Variable kopieren:
    strcpy(string_one, "Hallo Welt!");

    // Zeichenkette ausgeben:
    printf("%s\n", string_one);

Anstelle der Funktion ``strcpy()`` kann auch die Funktion ``strncpy()``
verwendet werden, die nach der zu kopierenden Zeichenkette noch einen
``int``-Wert :math:`n` erwartet; diese Funktion kopiert maximal :math:`n`
Zeichen in die Zielvariable, womit ein Überschreiten der Feldgrenzen
ausgeschlossen werden kann.

..  Die beiden Notationen ``*mystring`` und ``mystring[]`` sind äquivalent!

.. _ASCII-Codes:

.. rubric:: ASCII-Codes und Sonderzeichen

Die einzelnen Zeichen (Datentyp ``char``) werden vom Computer intern ebenfalls
als ganzzahlige Werte ohne Vorzeichen behandelt. Am weitesten verbreitet ist die
so genannte ASCII-Codierung ("American Standard Code for Information
Interchange"), deren Zuweisungen in der folgenden :ref:`ASCII-Tabelle
<tab-ascii>` abgebildet sind. Wird beispielsweise nach der Deklarierung ``char
c;`` der Variablen ``c`` mittels ``c = 120`` ein numerischer Wert zugewiesen, so
liefert die Ausgabe von ``printf("%c\n", c);`` den zur Zahl ``120`` gehörenden
ACII-Code, also ``x``.

.. index:: ASCII-Tabelle
.. _tab-ascii:

+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| Dez | ASCII   | Dez | ASCII   | Dez | ASCII  | Dez | ASCII | Dez | ASCII | Dez | ASCII | Dez | ASCII | Dez | ASCII   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 0   | ``NUL`` | 16  | ``DLE`` | 32  | ``SP`` | 48  | ``0`` | 64  | ``@`` | 80  | ``P`` | 96  |  \`   | 112 | ``p``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 1   | ``SOH`` | 17  | ``DC1`` | 33  | ``!``  | 49  | ``1`` | 65  | ``A`` | 81  | ``Q`` | 97  | ``a`` | 113 | ``q``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 2   | ``STX`` | 18  | ``DC2`` | 34  | ``"``  | 50  | ``2`` | 66  | ``B`` | 82  | ``R`` | 98  | ``b`` | 114 | ``r``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 3   | ``ETX`` | 19  | ``DC3`` | 35  | ``#``  | 51  | ``3`` | 67  | ``C`` | 83  | ``S`` | 99  | ``c`` | 115 | ``s``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 4   | ``EOT`` | 20  | ``DC4`` | 36  | ``$``  | 52  | ``4`` | 68  | ``D`` | 84  | ``T`` | 100 | ``d`` | 116 | ``t``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 5   | ``ENQ`` | 21  | ``NAK`` | 37  | ``%``  | 53  | ``5`` | 69  | ``E`` | 85  | ``U`` | 101 | ``e`` | 117 | ``u``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 6   | ``ACK`` | 22  | ``SYN`` | 38  | ``&``  | 54  | ``6`` | 70  | ``F`` | 86  | ``V`` | 102 | ``f`` | 118 | ``v``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 7   | ``BEL`` | 23  | ``ETB`` | 39  | ``'``  | 55  | ``7`` | 71  | ``G`` | 87  | ``W`` | 103 | ``g`` | 119 | ``w``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 8   | ``BS``  | 24  | ``CAN`` | 40  | ``(``  | 56  | ``8`` | 72  | ``H`` | 88  | ``X`` | 104 | ``h`` | 120 | ``x``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 9   | ``HT``  | 25  | ``EM``  | 41  | ``)``  | 57  | ``9`` | 73  | ``I`` | 89  | ``Y`` | 105 | ``i`` | 121 | ``y``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 10  | ``LF``  | 26  | ``SUB`` | 42  | ``*``  | 58  | ``:`` | 74  | ``J`` | 90  | ``Z`` | 106 | ``j`` | 122 | ``z``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 11  | ``VT``  | 27  | ``ESC`` | 43  | ``+``  | 59  | ``;`` | 75  | ``K`` | 91  | ``[`` | 107 | ``k`` | 123 | ``{``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 12  | ``FF``  | 28  | ``FS``  | 44  | ``,``  | 60  | ``<`` | 76  | ``L`` | 92  | ``\`` | 108 | ``l`` | 124 | ``|``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 13  | ``CR``  | 29  | ``GS``  | 45  | ``-``  | 61  | ``=`` | 77  | ``M`` | 93  | ``]`` | 109 | ``m`` | 125 | ``}``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 14  | ``SO``  | 30  | ``RS``  | 46  | ``.``  | 62  | ``>`` | 78  | ``N`` | 94  | ``^`` | 110 | ``n`` | 126 | ``~``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 15  | ``SI``  | 31  | ``US``  | 47  | ``/``  | 63  | ``?`` | 79  | ``O`` | 95  | ``_`` | 111 | ``o`` | 127 | ``DEL`` |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+

Die zu den Zahlen ``0`` bis ``127`` gehörenden Zeichen sind bei fast allen
Zeichensätzen identisch. Da der ASCII-Zeichensatz allerdings auf die englische
Sprache ausgerichtet ist und damit keine Unterstützung für Zeichen anderer
Sprachen beinhaltet, gibt es Erweiterungen des ASCII-Zeichensatzes für die
jeweiligen Länder.

Neben den Obigen ASCII-Zeichen können Zeichenketten auch so genannte
"Escape-Sequenzen" als Sonderzeichen beinhalten. Der Name kommt daher, dass zur
Darstellung dieser Zeichen ein Backslash-Zeichen ``\`` erforderlich ist, das die
eigentliche Bedeutung des darauf folgenden Zeichens aufhebt. Einige wichtige
dieser Sonderzeichen sind in der folgenden Tabelle aufgelistet.

.. list-table:: 
    :name: tab-sonderzeichen
    :widths: 20 50 

    * - Zeichen
      - Bedeutung
    * - ``\n``
      - Zeilenwechsel ("new line")
    * - ``\t``
      - Tabulator (entspricht üblicherweise 4 Leerzeichen)
    * - ``\b``
      - Backspace
    * - ``\\``
      - Backslash-Zeichen
    * - ``\"``
      - Doppeltes Anführungszeichen
    * - ``\'``
      - Einfaches Anführungszeichen

Eine weitere Escape-Sequenz ist das Zeichen ``'\0'`` als Endmarkierung einer
Zeichenkette, das verständlicherweise jedoch nicht innerhalb einer
Zeichenketten stehen darf. 




..  Innerhalb eines Strings können ebenfalls die Character-Escape-Sequenzen
..  verwendet werden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Es gibt auch ``void *``-Zeiger, die auf keinen bestimmten Datentyp
    zeigen. Solche Zeiger werden beispielsweise von der Funktion ``malloc()``
    bei einer :ref:`dynamischen Reservierung von Speicherplatz <Dynamische
    Speicherreservierung>` als Ergebnis zurückgegeben. Der Programmierer muss in
    diesem Fall dem Zeiger selbst den gewünschten Datentyp zuweisen.

.. [#] Der Grund für die Verwendung eines ``NULL``-Zeigers (einer in der Datei
    ``stddef.h`` definierten Konstanten mit dem Wert :math:`0`) liegt darin,
    dass eine binär dargestellte Null in C niemals als Speicheradresse verwendet
    wird. 

    Manchmal wird der ``NULL``-Pointer von :ref:`Funktionen <Funktionen>`, die
    gewöhnlich einen bestimmten Zeiger als Ergebnis liefern, zur Anzeige einer
    erfolglosen Aktion verwendet. Liegt kein Fehler vor, so ist der Rückgabewert
    die Adresse eines Speicherobjektes und somit von ``0`` verschieden. 

.. [#] Die Größe von Feldern kann nach der Deklaration nicht mehr verändert
    werden. Somit muss das Feld ausreichend groß gewählt werden, um alle zu
    erwartenden Werte speichern zu können. Andererseits sollte es nicht unnötig
    groß gewählt werden, da ansonsten auch unnötig viel Arbeitsspeicher
    reserviert wird.

    Soll die Größe eines Feldes erst zur Laufzeit festgelegt werden, so müssen
    die Funktionen ``malloc()`` bzw. ``calloc()`` verwendet werden.

.. [#] Eine direkte Initialisierung eines mehrdimensionalen Arrays ist ebenfalls
    unmittelbar möglich; dabei werden die einzelnen "Zeilen" für eine bessere
    Lesbarkeit in geschweifte Klammern gesetzt. Beispielsweise kann gleich bei
    der Definition ``int zahlentabelle[3][4] = { {3,4,1,5}, {8,5,6,9},
    {4,7,0,3} };`` geschrieben werden. 

.. [#] Legt man bei der Deklaration eines Feldes seine Groesse nicht fest, um
    diese erst zur Laufzeit mittels :ref:`malloc() <Dynamische
    Speicherreservierung>` zu reservieren, so kann bei der Deklaration anstelle
    von ``int numbers[];`` ebenso ``int *numbers;`` geschrieben werden.


