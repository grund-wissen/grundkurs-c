
.. _Ausgabe und Eingabe:

Ausgabe und Eingabe
===================

Das Ausgeben und Einlesen von Daten über den Bildschirm erfolgt häufig mittels
der Funktionen ``printf()`` und ``scanf()``. [#]_ Beide Funktionen sind Teil der
:ref:`Standard-Bibliothek <C-Standardbibliothek>` :ref:`stdio.h <stdio.h>`, so
dass diese zu Beginn der Quellcode-Datei mittels ``include <stdio.h>``
eingebunden werden muss. [#]_ 

.. Ausgabe auf den Bildschirm
.. --------------------------

.. Im diesem Abschnitt werden die häufigsten Funktionen für eine direkte Ausgabe
.. von Text auf dem Bildschirm näher beschrieben.


.. index:: printf()
.. _printf():

``printf()`` -- Daten formatiert ausgeben
-----------------------------------------

Die Funktion ``printf()`` dient grundsätzlich zur direkten Ausgabe von
Zeichenketten auf dem Bildschirm; beispielsweise gibt ``printf("Hallo Welt!")``
die angegebene Zeichenkette auf dem Bildschirm aus. Innerhalb der Zeichenketten
können allerdings Sonderzeichen sowie Platzhalter für beliebige Variablen und
Werte eingefügt werden.

.. list-table:: 
    :name: tab-escape-sequenzen
    :widths: 20 50 

    * - Zeichen
      - Bedeutung
    * - ``\n``
      - Neue Zeile
    * - ``\t``
      - Tabulator (4 Leerzeichen)
    * - ``\\``
      - Backslash-Zeichen ``\``
    * - ``\'``
      - Einfaches Anführungszeichen
    * - ``\"``
      - Doppeltes Anführungszeichen


..  \ooo oktale Zahl
..  \xhh hexadezimale Zahl


Die in der obigen Tabelle angegebenen Sonderzeichen werden auch
"Escape-Sequenzen" genannt, da sie nur mittels des vorangehenden
Backslash-Zeichens, das ihre sonstige Bedeutung aufhebt, innerhalb einer
Zeichenkette dargestellt werden könen.

Ein Platzhalter besteht aus einem ``%``-Zeichen, gefolgt von einem oder mehreren
Zeichen, welche den Typ der auszugebenden Werte oder Variablen angeben und
gleichzeitig festlegen, wie die Ausgabe formatiert werden soll. Damit kann
beispielsweise bestimmt werden, wie viele Stellen für einen Wert reserviert
werden sollen, ob die Ausgabe links- oder rechtsbündig erfolgen soll, und/oder
ob bei der Ausgabe von Zahlen gegebenenfalls führende Nullen angefügt werden
sollen. 

.. code-block:: c

    // Den Wert Pi auf sechs Nachkommastellen genau ausgeben:

    printf("Der Wert von Pi ist %.6f...\n", 3.141592653589793) 
    // Ergebnis: Der Wert von Pi ist 3.141593...

    // Maximal dreistellige Zahlen rechtsbündig ausgeben:

    printf("%3i:\n%3i:\n%3i:\n", 1, 10, 100);
    // Ergebnis:
    //   1:
    //  10:
    // 100:

    // Maximal dreistellige Zahlen linksbündig ausgeben:

    printf("%3i:\n%3i:\n%3i:\n", 1, 10, 100);
    // Ergebnis:
    // 1  :
    // 10 :
    // 100:

    // Einstelligen Zahlen eine Null voranstellen:

    printf("%02i.:\n%02i.:\n%02i.:\n", 8, 9, 10);
    // Ergebnis:
    // 08.:
    // 09.:
    // 10.:


In den obigen Beispielen wurden der Funktion ``printf()`` zwei oder mehr
Argumente übergeben. Beim ersten Argument handelt es sich um einen so genannten
Formatstring, bei den folgenden Argumenten um die auf dem Bildschirm
auszugebenden Werte. Falls diese, wie im ersten Beispiel,  mehr Nachkommastellen
haben als in der Formatierung vorgesehen (Die Angabe ``%.6f`` steht für einen
Wert vom Datentyp ``float`` sechs Nachkommastellen), so wird der Wert
automatisch auf die angegebene Genauigkeit gerundet.

Zur Festlegung des Datentyps einer auszugebenden Variablen gibt es allgemein
folgende Umwandlungszeichen:

.. list-table:: 
    :name: tab-umwandlungszeichen
    :widths: 10 10 70

    * - Zeichen
      - Argument
      - Bedeutung
    * - ``d, i``
      - ``int``
      - Dezimal-Zahl mit Vorzeichen.
    * - ``o`` 
      - ``int``
      - Oktal-Zahl ohne Vorzeichen (und ohne führende Null).
    * - ``x, X`` 
      - ``int``
      - Hexadezimal-Zahl ohne Vorzeichen (und ohne führendes ``0x`` oder
        ``0X``), also ``abcdef`` bei ``0x`` oder ``ABCDEF`` bei ``0X``.
    * - ``u``
      - ``int``
      - Dezimal-Zahl ohne Vorzeichen.
    * - ``c``
      - ``int`` 
      - Ein einzelnes Zeichen (``unsigned char``).
    * - ``s``
      - ``char *``
      - Zeichen einer Zeichenkette bis zum Zeichen ``\0``, oder bis zur 
        angegebenen Genauigkeit.
    * - ``f``
      - ``double``
      - Dezimal-Zahl als ``[-]mmm.ddd``, wobei die angegebene Genauigkeit die
        Anzahl der ``d`` festlegt. Die Voreinstellung ist ``6``, bei ``0``
        entfällt der Dezimalpunkt.
    * - ``e, E`` 
      - ``double``
      - Dezimal-Zahl als ``[-]m.dddddde±xx`` oder ``[-]m.ddddddE±xx``, wobei die
        angegebene Genauigkeit die Anzahl der ``d`` festlegt. Die Voreinstellung
        ist ``6``, bei ``0`` entfällt der Dezimalpunkt.
    * - ``g, G`` 
      - ``double``
      - Dezimal-Zahl wie wie ``%e`` oder ``%E``. Wird verwendet, wenn der
        Exponent kleiner als die angegebene Genauigkeit ist; unnötige Nullen am
        Schluss werden nicht ausgegeben.
    * - ``p``
      - ``void *``
      - Zeiger (Darstellung hängt von Implementierung ab).
    * - ``n``
      - ``int *``
      - Anzahl der aktuell von ``printf()`` ausgegebenen Zeichen.

Die obigen Formatangaben lassen sich durch Steuerzeichen ("flags") zwischen dem
``%``- und dem Umwandlungszeichen weiter modifizieren:

* ``Zahl``: Minimale Feldbreite festlegen: Das umgewandelte Argument wird in
  einem Feld ausgegeben, das mindestens so breit ist, bei Bedarf aber auch
  breiter. Hat das umgewandelte Argument weniger Zeichen als die Feldbreite
  es verlangt, so werden auf der linken Seite Leerzeichen eingefügt. 

* ``.Zahl``: Genauigkeit von Gleitkommazahlen festlegen: Gibt die maximale
  Anzahl von Zeichen an, die nach dem Dezimalpunkt ausgegeben werden
* ``-``: Ausrichten des umgewandelten Arguments am linken Rand des Ausgabefeldes
  (Leerzeichen werden bei Bedarf nicht links, sondern rechts eingefügt)
* ``+``: Ausgabe einer Zahl stets mit Vorzeichen
* ``Leerzeichen``: Ausgabe eines Leerzeichens vor einer Zahl, falls das erste
  Zeichen kein Vorzeichen ist
* ``0``: Zahlen bei der Umwandlungen bis zur Feldbreite mit führenden Nullen
  aufüllen

Anstelle einer Zahl kann auch das Zeichen ``*`` als Feldbreite angegeben werden.
In diesem Fall wird die Feldbreite durch eine zusätzlich an dieser Stelle in der
Argumentliste angegebenen ``int``-Variablen festgelegt:

.. code-block:: c

    int zahl = 1000;
    int breite = 5;

    printf("Der Wert von der Variable \"zahl\" ist: %*d", breite, zahl);

Die Formatangaben ``%e`` und ``%g`` können gleichermaßen zur Ausgabe von
Gleitkomma-Zahlen in der Zehnerpotenz-Schreibweise verwendet werden. Sie
unterscheiden sich nur bei Zahlen mit wenig Nachkommastellen. Beispielsweise
würde die Ausgabe ``printf("%g\n", 2.15);`` als Ergebnis ``2.15`` anzeigen,
während  ``printf("%e\n", 2.15);`` als Ergebnis ``2.150000e+00`` liefern würde.

Soll eine ``long``-Variante eines Integers ausgegeben werden, so muss vor das
jeweilige Umwandlungszeichen ein ``l`` geschrieben werden, beispielsweise ``lu``
für ``long unsigned int`` oder ``ld`` für ``long int``; für ``long double``
wird ``L`` geschrieben.

Soll das ``%``-Zeichen innerhalb einer Zeichenkette selbst ausgegeben werden, so
muss an dieser Stelle ``%%`` geschrieben werden.

Soll über mehrere Zeilen hinweg Text mittels ``printf()`` ausgegeben werden, so
ist meist es für eine bessere Lesbarkeit empfehlenswert, für jede neue Zeile
eine eigene ``printf()``-Anweisung zu schreiben. 


.. index:: puts()
.. _puts():

``puts()`` -- Einzelne Zeichenketten ausgeben
---------------------------------------------

Sollen nur einfache Zeichenketten (ohne Formatierung und ohne Variablenwerte)
ausgegeben werden, so kann anstelle von ``printf()`` auch die Funktion
``puts()`` aus der Standard-Bibliothek :ref:`stdio.h <stdio.h>` verwendet
werden. Die in der Tabelle :ref:`Escape-Sequenzen <tab-escape-sequenzen>`
aufgelisteten Sonderzeichen können auch bei ``puts()`` verwendet werden, es muss
jedoch am Ende einer Ausgabezeile kein ``\n`` angehängt werden; ``puts()`` gibt
automatisch jeden String in einer neuen Zeile aus.


.. index:: putchar()
.. _putchar():

``putchar()`` -- Einzelne Zeichen ausgeben
------------------------------------------

Mittels ``putchar()`` können einzelne Zeichen auf dem Bildschirm ausgegeben
werden. Diese Funktion wird nicht nur von den anderen Ausgabefunktionen
aufgerufen, sondern kann auch verwendet werden, wenn beispielsweise eine Datei
zeichenweise eingelesen und nach Anwendung eines Filters wieder zeichenweise auf
dem Bildschirm ausgegeben werden soll. [#]_

.. Einlesen vom Bildschirm
.. -----------------------

.. Im diesem Abschnitt werden die häufigsten Funktionen näher beschrieben, mit
.. denen Text direkt vom Bildschirm beziehungsweise von der Tastatur eingelesen
.. werden kann.

.. index:: scanf()
.. _scanf():

``scanf()`` -- Daten formatiert einlesen
----------------------------------------

Die Funktion ``scanf()`` kann als flexible Funktion verwendet werden, um Daten
direkt vom Bildschirm beziehungsweise von der Tastatur einzulesen. Dabei wird
bei ``scanf()``, ebenso wie bei ``printf()``, ein Formatstring angegeben, der
das Format der Eingabe festlegt. Die Funktion weist dann die eingelesen Daten,
die dem Format entsprechen, vom Bildschirm ein und weist ihnen eine oder mehrere
Programmvariablen zu. Im Formatstring können die gleichen
:ref:`Umwandlungszeichen <tab-umwandlungszeichen>` wie bei ``printf()``
verwendet werden.

Die Eingabe mittels ``scanf()`` erfolgt "gepuffert", d.h. die mit der Tastatur
eingegebenen Zeichen werden zunächst in einem Zwischenspeicher ("Puffer") des
Betriebsystems abgelegt. Erst, wenn der Benutzer die ``Enter``-Taste drückt,
wird der eingegebene Text von ``scanf()`` verarbeitet.

Bei der Zuweisung der eingelesenen Daten wird bei Benutzung der Funktion
``scanf()`` nicht der jeweilige Variablenname, sondern stets die zugehörige
Speicheradresse angegeben, an welcher die Daten abgelegt werden sollen; diese
kann leicht mittels des :ref:`Adress-Operators <Adressoperator>` ``&`` bestimmt
werden. Um also beispielsweise einen ``int``-Wert vom Bildschirm einzulesen,
gibt man folgendes ein:

.. code-block:: c

    int n;

    // Benutzer zur Eingabe auffordern:
    printf("Bitte einen ganzzahligen Wert eingeben: ")

    // Eingegebenen Wert einlesen:
    scanf("%i", &n);
    
Sobald der Benutzer seine Eingabe mit ``Enter`` bestätigt, wird im obigen
Beispiel die eingegebene Zahl eingelesen und am Speicherplatz der Variablen
``n`` hinterlegt. 

Zum Einlesen von Zeichenketten muss dem Variablennamen kein ``&`` vorangestellt
werden, da es sich bei einer Zeichenkette um ein :ref:`Array <Felder>` handelt.
Dieses wiederum entspricht einem :ref:`Zeiger <Zeiger>` auf den ersten Eintrag,
und ab eben dieser Stelle soll die eingelesene Zeichenkette abgelegt werden.
Beim Einlesen von Daten in Felder muss allerdings beachtet werden, dass der
angegebene Zeiger bereits :ref:`initialisiert <Zeiger-Initialisierung>` wurde.
Eine simple Methode, um dies sicherzustellen, ist dass eine String-Variable
nicht mit ``char *mystring;``, sondern beispielsweise mit ``char
mystring[100];`` definiert wird. 

.. index:: Whitespace
.. rubric:: Whitespace als Trennzeichen


Mit einer einzelnen ``scanf()``-Funktion können auch mehrere Werte gleichzeitig
eingelesen werden, wenn mehrere Umwandlungszeichen im Formatstring und
entsprechend viele Speicheradressen als weitere Argumente angegeben werden. Beim
Einlesen achtet ``scanf()`` dabei so genannte Whitespace-Zeichen (Leerzeichen,
Tabulator-Zeichen oder Neues-Zeile-Zeichen), um die einzelnen Daten voneinander
zu trennen. Soll der Benutzer beispielsweise zwei beliebige Zahlen eingeben, so
können diese mit einem einfachen Leerzeichen zwischen ihnen, aber ebenso in
zwei getrennten Zeilen eingegeben werden.

.. code-block:: c

    int n1, n2;

    // Benutzer zur Eingabe auffordern:
    printf("Bitte zwei beliebige Werte eingeben: ")

    // Eingegebene Werte einlesen:
    scanf("%f %f", &n1, &n2);


.. index:: fflush()
.. rubric:: ``fflush()`` -- Zwischenspeicher löschen

Da die Daten bei Verwendung von ``scanf()`` zunächst in einen Zwischenspeicher
eingelesen werden, können Probleme auftreten, wenn der Benutzer mehr durch
Whitespace-Zeichen getrennte Werte eingibt, als beim Aufruf der Funktion
``scanf()`` verarbeitet werden. Die restlichen Werte verbleiben in diesem Fall
im Zwischenspeicher und würden beim nächsten Aufruf von ``scanf()`` noch vor der
eigentlich erwarteten Eingabe verarbeitet werden. Eine Abhilfe hierfür schafft
die Funktion ``fflush()``, die nach jedem Aufruf von ``scanf()`` aufgerufen
werden sollte und ein Löschen aller noch im Zwischenspeicher abgelegten Werte
bewirkt.

Beim Einlesen von Zeichenketten mittels ``%s`` ist das wortweise Einlesen von
``scanf()`` oftmals hinderlich, da in der mit ``%s`` verknüpften Variable nur
Text bis zum ersten Whitespace-Zeichen (Leerzeichen, Tabulator-Zeichen oder
Neues-Zeile-Zeichen) gespeichert wird. Ganze Zeilen, die aus beliebig vielen
Wörtern bestehen, sollten daher bevorzugt mittels ``gets()`` oder ``fgets()``
eingelesen werden.

    
.. index:: gets(), fgets()
.. _gets() und fgets():

``gets()`` und ``fgets()`` -- Einzelne Zeichenketten einlesen
-------------------------------------------------------------

Um eine Textzeile auf einmal einzulesen, kann  die Funktion ``gets()`` aus der
Standard-Bibliothek :ref:`stdio.h <stdio.h>` verwendet werden. Diese Funktion
liest eine Textzeile vom Bildschirm ein und speichert sie in der angegebenen
Variablen ein:

.. code-block:: c

    int mystring[81]; 

    gets(mystring);

Ein Neues-Zeile-Zeichen ``\n`` am Ende des Eingabestrings wird von ``gets()``
automatisch abgeschnitten, das Zeichen ``\0`` zum Beenden der Zeichenkette
automatisch angefügt. Wichtig ist allerdings bei der Verwendung von ``gets()``,
dass der angegebene String-Pointer auf ein ausreichend großes Feld zeigt. Im
obigen Beispiel darf die eingelesene Zeile somit nicht mehr als :math:`80`
Zeichen haben, da auch noch Platz für das Zeichen ``\0`` bleiben muss. Werden
die Feldgrenzen überschritten, kann dies ein unkontrolliertes Verhalten des
Programms oder gar einen Programmabsturz zur Folge haben. [#]_

Als bessere Alternative zu ``gets()`` kann die Funktion ``fgets()`` verwendet
werden, welche die Anzahl der maximal eingelesenen Zeichen beschränkt:

.. code-block:: c

    int mystring[81]; 
    int n = 80;

    fgets(mystring, n, stdin);

Im Unterschied zu ``gets()`` speichert ``fgets()`` das Neue-Zeile-Zeichen ``\n``
mit in der eingelesenen Zeichenkette, was unter Umständen bei der Längenangabe
:math:`n` berücksichtigt werden muss. Die Funktion ``fgets()`` gibt, wenn eine
Zeichenkette erfolgreich eingelesen wurde, einen Zeiger als Ergebnis zurück, der
mit der Speicheradresse der angegebenen Stringvariablen übereinstimmt; bei einem
Fehler wird ``NULL`` als Ergebnis zurück gegeben.

..  Der eingelesene String kann anschließend mit sscanf() konvertiert werden.

.. _Einzelne Zeichen mit getchar() einlesen:

Um eine Textzeile auf einmal einzulesen, kann  die Funktion ``gets()`` aus der
Standard-Bibliothek :ref:`stdio.h <stdio.h>` verwendet werden. Diese Funktion
liest eine Textzeile vom Bildschirm ein und speichert sie in der angegebenen
Variablen ein:

``getchar()`` -- Einzelne Zeichen einlesen
------------------------------------------

Um einzelne Zeichen vom Standard-Eingang (Bildschirm bzw. Tastatur) zu lesen,
kann die Funktion ``getchar()`` verwendet werden. [#]_ Ebenso wie bei der Funktion
``scanf()`` gibt die Funktion erst dann das gelesene Zeichen als Ergebnis
zurück, wenn der Benutzer die ``Enter``-Taste drückt; dies lässt sich
beispielsweise für eine Abfrage der Art ``[Yn]`` für ``"Yes"`` oder ``"No"``
nutzen, wobei üblicherweise der groß geschriebene Buchstabe als Vorauswahl gilt
und gesetzt wird, wenn keine explizite Eingabe vom Benutzer erfolgt.

Wird das Zeichen nach einer Umlenkung des Standard-Eingangs (beispielsweise
mittels :ref:`freopen() <freopen()>`) nicht von der Tastatur, sondern von einer
Datei eingelesen, so wird so lange jeweils ein einzelnens Zeichen
zurückgegeben, bis ein Fehler auftritt oder die Funktion auf das Ende des 
Datenstroms bzw. der Datei trifft; in diesem Fall wird ``EOF`` als Ergebnis
zurückgegeben. 

.. getc(), fgetc()
.. Einlesen aus anderem Stream

.. ungetc() Zeichen zurückstellen
.. Zweck: Einlesen kann beispielsweise an dieser Stelle beendet werden, Zeichen
.. wird jedoch nicht verworfen, sondern ist erstes Zeichen beim nächsten Einlesen 
.. ungetc(ch, stdin)

... to be continued ...

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Um Daten von Dateien anstelle vom Bildschirm einzulesen, gibt es weitere
    Funktionen, die im Abschnitt :ref:`Dateien und Verzeichnisse <Dateien und
    Verzeichnisse>` näher beschrieben sind.

.. [#] Genau genommen erfolgt bei der Funktion ``printf()`` die Ausgabe auf den
    Standard-Ausgang (``stdout``). Bei diesem handelt es sich als Voreinstellung
    um den Bildschirm, in speziellen Fällen kann jedoch mittels der Funktion
    :ref:`freopen() <freopen()>` auch eine beliebige Datei oder ein
    angeschlossenes Gerät als Standard-Ausgang festgelegt werden.

    Ebenso liest die Funktion ``scanf()`` vom Standard-Eingang (``stdin``) ein,
    der als Voreinstellung wiederum dem Bildschirm entspricht.

.. [#] Streng genommen handelt es sich bei ``putchar()`` nicht um eine Funktion,
    sondern um ein :ref:`Makro <Makro>`: Letztlich wird ``putchar(Zeichen)`` vom
    Präprozessor durch einen Funktionsaufruf von ``fputc(Zeichen, stdin)``
    ersetzt. Die Funktion ``fputc()`` wird im Abschnitt :ref:`Dateien und
    Verzeichnisse <Dateien und Verzeichnisse>` näher beschrieben.

.. [#] Im neuen C11-Standard wird ``gets()`` aufgrund seiner Fehleranfälligkeit
    nicht mehr als Standard gelistet, den ein Compiler abdecken *muss*. Da die
    Funktion in sehr vielen Programmcodes vorkommt, wird ``gcc`` wohl auch in
    absehbarer Zukunft diese Funktion unterstützen. In C11 wurde dafür die
    ähnliche Funktion ``gets_s()`` im optionalen Teil von ``stdio.h``
    aufgenommen, die jedoch ebenfalls nicht jeder Compiler zwingend unterstützen
    muss. Dies ist ein weiterer Grund, bevorzugt ``fgets()`` zu verwenden.

.. [#] Streng genommen handelt es sich bei ``getchar()`` nicht um eine Funktion,
    sondern um ein :ref:`Makro <Makro>`. Letztlich wird ``getchar()`` vom
    Präprozessor durch einen Funktionsaufruf von ``fgetc(stdin)`` ersetzt. 
    Die Funktion ``fputc()`` wird im Abschnitt :ref:`Dateien und Verzeichnisse
    <Dateien und Verzeichnisse>` näher beschrieben.

