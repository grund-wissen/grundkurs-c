
.. index:: Variable
.. _Definition von Variablen:

Definition von Variablen
========================

Ein wesentlicher Vorteil eines Computer-Programms gegenüber einem Taschenrechner
besteht darin, dass es (nahezu beliebig viele) Werte und Zeichen in
entsprechenden Platzhaltern ("Variablen") speichern und verarbeiten kann.

Da ein Computer-Prozessor nur mit Maschinencode arbeiten kann, müssen intern
sowohl Zahlen wie auch Text- und Sonderzeichen als Folgen von Nullen und Einsen
dargestellt werden. Dies ist aus der Sichtweise eines Programmierers zunächst
nur soweit von Bedeutung, als dass er wissen muss, dass ein und dieselbe Folge
von Nullen und Einsen vom Computer wahlweise als Zeichen oder als Zahl
interpretiert werden kann. Der Programmierer muss dem Computer somit mitteilen,
wie der Inhalt einer Variable zu interpretieren ist.

.. index:: Deklaration, Definition
.. _Deklaration, Definition, Initialisierung:

Deklaration, Definition, Initialisierung
----------------------------------------

Um Variablen benutzen zu können, muss der Datentyp der Variablen (z.B. ``int``
für ganze Zahlen) dem Compiler mitgeteilt werden ("Deklaration"). Muss dabei
auch Speicherplatz reserviert werden (was meist der Fall ist, wenn sich die
Deklaration nicht auf Variablen externer Code-Bibliotheken bezieht), so spricht
man von einer Definition einer Variablen. 

In C werden Variablen stets zu Beginn einer Datei oder zu Beginn eines neuen,
durch geschweifte Klammern begrenzten Code-Blocks definiert. Sie sind im
Programm gültig, bis die Datei beziehungsweise der jeweilige Code-Block
abgearbeitet ist. [#]_

Eine Definition von Variablen erfolgt nach folgendem Schema:

.. code-block:: c

    int n;

Es dürfen auch mehrere gleichartige Variablen auf einmal definiert werden;
hierzu werden die einzelnen Namen der Variablen durch Kommatas getrennt und die
Definition mit einem abschließenden Strichpunkt beendet.

.. code-block:: c

    int x,y,z;

.. index:: Initialisierung

Wird einer Variablen bei der Definition auch gleich ein anfänglicher Inhalt
("Initialwert") zugewiesen, so spricht man auch von einer Initiation einer
Variablen. [#INI]_

.. _Zuweisungsoperator:
.. index:: Zuweisungsoperator

.. code-block:: c

    int c = 256;

In C wird das Ist-Gleich-Zeichen ``=`` als Zuweisungsoperator genutzt, der
den Ausdruck auf der rechten Seite in die Variablen auf der linken Seite
abspeichert. [#IG]_ Eine erneute Angabe des Datentyps einer Variablen würde beim
Übersetzen sogar eine Fehlermeldung des Compilers zur Folge haben, da in diesem
Fall von einer (versehentlichen) doppelten Vergabe eines Variablennamens
ausgegangen wird.

Variablennamen dürfen in C maximal 31 Stellen lang sein. Sie können aus den
Buchstaben ``A-Z`` und ``a-z``, den Ziffern ``0-9`` und dem Unterstrich
bestehen. Die einzige Einschränkung besteht darin, dass am Anfang von
Variablennamen keine Ziffern stehen dürfen; Unterstriche am Anfang von
Variablennamen sind zwar erlaubt, sollten aber vermieden werden, da diese
üblicherweise für Bibliotheksfunktionen reserviert sind.

In C wird allgemein zwischen Groß- und Kleinschreibung unterschieden,
beispielsweise bezeichnen ``a`` und ``A`` zwei unterschiedliche Variablen. Im
Allgemeinen werden Variablen und Funktionen in C-Programmen fast immer klein
geschrieben.

Ist einmal festgelegt, um welchen Datentyp es sich bei einer Variablen handelt,
wird die Variable im Folgenden ohne Angabe des Datentyps verwendet.

.. index:: char, int, short, long, float, double 
.. _Elementare Datentypen:

Elementare Datentypen
---------------------

Als grundlegende Datentypen wird in C zwischen folgenden Arten unterschieden: 

.. list-table:: 
    :name: tab-datentypen
    :widths: 50 50 50

    * - Typ
      - Bedeutung
      - Speicherbedarf
    * - char
      - Ein einzelnes Zeichen
      - 1 Byte (= 8 Bit)
    * - int
      - Eine ganzzahlige Zahl
      - 4 Byte (= 32 Bit)
    * - short
      - Eine ganzzahlige Zahl
      - 2 Byte (= 16 Bit)
    * - long
      - Eine ganzzahlige Zahl
      - 8 Byte (= 64 Bit)
    * - float 
      - Eine Fließkomma-Zahl
      - 4 Byte (= 32 Bit)
    * - double
      - Eine Fließkomma-Zahl
      - 8 Byte (= 64 Bit)

.. index:: sizeof()

Der Speicherbedarf der einzelnen Datentypen hängt von der konkreten
Rechnerarchitektur ab; in der obigen Tabelle sind die Werte für
:math:`32`-Bit-Systeme angegeben, die für Monocore-Prozessoren üblich sind. Auf
anderen Systemen können sich andere Werte für die einzelnen Datentypen ergeben.
Die Größe der Datentypen auf dem gerade verwendeten Rechner kann mittels
``sizeof()`` geprüft werden:

.. code-block:: c

    // Datei: sizeof.c

    #include <stdio.h>

    void main()
    {
        printf("Size of char:   %lu\n", sizeof(char)  );
        printf("Size of int:    %lu\n", sizeof(int)   );
        printf("Size of short:  %lu\n", sizeof(short) );
        printf("Size of long:   %lu\n", sizeof(long)  );
        printf("Size of float:  %lu\n", sizeof(float) );
        printf("Size of double: %lu\n", sizeof(double));
    }

In diesem Beispiel-Programm werden nach dem Compilieren mittels ``gcc -o sizeof
sizeof.c`` und einem Aufruf von ``./sizeof`` die Größen der einzelnen Datentypen
in Bytes ausgegeben. Hierzu wird bei der Funktion ``printf()`` das
Umwandlungszeichen ``%lu`` verwendet, das durch den Rückgabewert von
``sizeof()`` (entspricht ``long integer``) ersetzt wird.

Einen "Booleschen" Datentyp, der die Wahrheitswerte ``True`` oder ``False``
repräsentiert, existiert in C nicht. Stattdessen wird der Wert Null für
``False`` und jeder von Null verschiedene Wert als ``True`` interpretiert. 

Komplexere Datentypen lassen sich aus diesen elementaren Datentypen
durch Aneinanderreihungen (:ref:`Felder <Felder>`) oder Definitionen von
Strukturen (struct) erzeugen. Zusätzlich existiert in C ein Datentyp namens
``void``, der null Bytes groß ist und beispielsweise dann genutzt wird, wenn
eine Funktion *keinen* Wert als Rückgabe liefert.

.. todo:

..  e-Notation von Gleitkommazahlen.
..  Ein Zahlenwert, der mit einer Ziffer außer 0 beginnt, gilt als Dezimalzahl .
..  Dezimale Werte können die Ziffern 0 bis 9 und ein führendes Minus- oder
..  Pluszeichen enthalten.

..  Ein Zahlenwert, die mit der Ziffer 0 beginnt, interpretiert der Compiler als
..  oktale Ganzzahl Oktale Konstanten können die Ziffern 0 bis 7 und ein führendes
..  Minus- oder Pluszeichen enthalten. Achtung: 033 ist somit nicht 33 Dezimal,
..  sondern 33 Oktal, also 27.

..  Hexadezimale Zahlenwerte werden durch ein führendes 0x gekennzeichnet. 

..  Fliesskommakonstanten werden durch einen Dezimalpunkt und/oder die
..  Exponentialschreibweise als solche kenntlich gemacht.

.. _Modifier:

.. rubric:: Modifier

Alle grundlegenden Datentypen (außer ``void``) können zusätzlich mit einem der
folgenden "Modifier" versehen werden:

.. index:: signed, unsigned
    
* ``signed`` bzw. ``unsigned``:

    Ohne explizite Angabe dieses Modifiers werden Variablen üblicherweise als
    ``signed``, d.h. mit einem Vorzeichen versehen, interpretiert.
    Beispielsweise lassen sich durch eine 1 Byte (8 Bit) große Variable vom Typ
    ``signed char`` Werte von ``-128`` bis ``+128`` abbilden, durch eine
    Variable vom Typ ``unsigned char`` Werte von ``0`` bis ``255``. Diese Werte
    werden dann üblicherweise als ASCII-Codes interpretiert.

.. index:: extern
    
* ``extern``:

    Dieser Modifier ist bei der Deklaration einer Variablen nötig, wenn diese
    bereits in einer anderen Quellcode-Datei definiert wurde. Für externe
    Variablen wird kein neuer Speicherplatz reserviert. Gleichzeitig wird durch
    den ``extern``-Modifier dem Compiler mitgeteilt, in den zu Beginn
    eingebundenen Header-Dateien nach einer Variablen dieses Namens zu suchen
    und den dort reservierten Speicherplatz gemeinsam zu nutzen.

.. index:: static
.. _static:
    
* ``static``:

    Eine Variable ist üblicherweise nur innerhalb des jeweiligen durch
    geschweifte Klammern begrenzten Codeblocks gültig, innerhalb dessen sie
    definiert wurde. 

    Wird eine Variable, beispielsweise als Zählvariable, innerhalb einer
    :ref:`Funktion <Funktionen>` definiert, so wird ihre Speicherstelle
    gelöscht, sobald der Aufruf der Funktion beendet ist. Wird bei der
    Definition einer solchen "lokalen" Variable jedoch der Modifier ``static``
    verwendet, so liegt ihr Wert auch beim nächsten Aufruf der gleichen Funktion
    unverändert vor.

    Auch Variablen, die gleich zu Beginn einer Datei definiert werden, können
    mit dem Modifier ``static`` versehen werden. Auf eine solche Variable können
    dann alle Funktionen dieser Datei zugreifen, für Funktionen anderer Dateien
    ist sie hingegen nicht sichtbar. 
    
    Umgekehrt ist jede Funktion und jede außerhalb einer Funktion definierte
    Variable "global", wenn sie nicht mit ``static`` versehen wurde. Globale
    Variablen sollten, sofern möglich, vermieden werden, da sie von vielen
    Stellen aus manipuliert werden können und im Zweifelsfall die Fehler
    verursachende Stelle im Code nur schwer gefunden wird.

.. index:: auto, register
    
* ``auto`` bzw. ``register``:

    Ohne explizite Angabe dieses Modifiers werden Variablen üblicherweise als
    ``auto`` interpretiert; diese Angabe wird automatisch vom Compiler ergänzt
    und daher grundsätzlich weggelassen. Wird eine Variable hingegen mit dem
    Modifier ``register`` versehen, so ist dies eine Empfehlung des Programmiers
    an den Compiler, diese Variable nicht im (externen) Arbeitsspeicher, sondern
    im Prozessorspeicher abzulegen. Dadurch kann in seltenen Fällen ein
    schnellerer Zugriff auf die Variable erreicht werden. Da der
    Prozessorspeicher jedoch meist sehr begrenzt ist, wird der
    ``register``-Modifier nur selten (und ausschließlich fuer numerische
    Variablen) eingesetzt und vom Compiler gegebenenfalls als ``auto``
    umgeschrieben.

.. index:: const

* ``const``:

    Mit ``const`` können Variablen bezeichnet werden, auf die nur lesend
    zugegriffen werden sollte. Schreibzugriffe auf solche Konstanten sind zwar
    möglich, sollten jedoch vermieden werden, da das Ergebnis undefiniert ist.
    Das Schlüssewort ``const`` wird somit zur besseren Lesbarkeit verwendet und
    erlaubt es dem Compiler, gewisse Optimierungen vorzunehmen.

    Neben dem Schlüsselwort ``const`` können Konstanten ebenfalls mittes der
    Präprozessor-Direktive ``define`` festgelegt werden.

    Bei einzelnen ASCII-Zeichen, also beispielsweise Buchstaben von ``'a'`` bis
    ``z`` beziehungsweise ``'A'`` bis ``'Z'`` sowie Sonderzeichen und Umlauten
    handelt es sich in C ebenfalls um Konstanten.

.. index:: volatile

* ``volatile``

    Es gibt Variablen, die sich ändern können, ohne dass der Compiler dies
    vermuten würde. Üblicherweise werden solche Variablen vom Compiler aus
    Optimierungsgründen durch eine Konstante ersetzt und nicht stets erneut
    eingelesen. Mit dem Schlüsselwort ``volatile`` hingegen zwingt man den
    Compiler, den Wert dieser Variablen bei jeder Benutzung erneut aus dem
    Speicher zu lesen und mehrfaches Lesen nicht wegzuoptimieren. Das ist
    beispielsweise wichtig bei Variablen, die Zustände von Hardwarekomponenten
    anzeigen, oder bei Variablen, die durch Interruptroutinen verändert werden.

    *Beispiel:*

    .. code-block:: c
    
       volatile int Tastenzustand;

       Tastenzustand = 0;
       while (Tastenzustand == 0)  
       {
           // Warten auf Tastendruck
       }

    Ohne das Schlüsselwort ``volatile`` könnte der Compiler im obigen Beispiel
    eine Endlosschlaufe erzeugen, da er nicht wissen kann, dass sich der Zustand
    Tastenzustand während der Schleife ändern kann.

..  Ab C99: Mit ``restrict`` können Zeiger gekennzeichnet werden, bei denen der
..  Programmierer garantiert, dass innerhalb ihrer Lebensdauer nie mehrere Zeiger
..  auf die selben Werte zeigen. Das eröffnet dem Compiler weitere
..  Optimierungsmöglichkeiten. Ein Compiler muss den Modifier akzeptieren, kann ihn
..  aber ignorieren.

.. raw:: html

    <hr />
    
.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die einzige Ausnahme bewirkt hierbei das Schlüsselwort :ref:`static <static>`.

.. [#INI] Die Initialisierung, d.h. die erstmalige Zuweisung eines Werts an eine
    Variable, kann auch erst zu einem späteren Zeitpunkt erfolgen. 

.. [#IG] Der Wertevergleich, wie er in der Mathematik durch das
    Ist-Gleich-Zeichen ausgedrückt wird, erfolgt in C durch den Operator ``==``. 

..  .. [#] Siehe Sichtbarkeit von Variablen.
