
.. _C-Standardbibliothek:

Die C-Standardbibliothek
========================

Im folgenden Abschnitt sind diejenigen C-Bibliotheken beschrieben, die jederzeit
vom ``gcc``-Compiler gefunden werden und somit in C-Programme mittes
``#include`` eingebunden werden können, ohne dass weitere Pfadanpassungen
notwendig sind.

.. Seit C11:
.. stdbool.h
.. Mit Datentyp bool und Konstanten true und false

.. index:: assert.h
.. _assert.h:

``assert.h`` -- Einfache Tests
------------------------------

* ``void assert(logical_expression);``

  Diese Funktion kann -- wie eine ``if``-Bedingung --  an beliebigen Stellen im
  Code eingesetzt werden. Ergibt der angegebene logische Ausdruck allerdings
  keinen wahren (von Null verschiedenen) Wert, so bricht ``assert()`` das
  Programm ab und gibt auf dem ``stderr``-Kanal als Fehlermeldung aus, welche
  Zeile beziehungsweise notwendige Bedingung den Absturz verursacht hat.
  
.. index:: math.h
.. _math.h:

``math.h`` -- Mathematische Funktionen 
---------------------------------------


.. index:: sin()
.. _sin():

* ``double sin(double x)``

    Gibt den :ref:`Sinus <gwm:Winkelfunktionen am Einheitskreis>`-Wert eines in :ref:`Radiant <gwm:Kreisbogen>`
    angegebenen :math:`x`-Werts an. 

.. index:: cos()
.. _cos():

* ``double cos(double x)``

    Gibt den :ref:`Cosinus <gwm:Winkelfunktionen am Einheitskreis>`-Wert eines in :ref:`Radiant <gwm:Kreisbogen>`
    angegebenen :math:`x`-Werts an. 

.. index:: tan()
.. _tan():

* ``double tan(double x)``

    Gibt den :ref:`Tangens <gwm:Winkelfunktionen am Einheitskreis>`-Wert eines in :ref:`Radiant <gwm:Kreisbogen>`
    angegebenen :math:`x`-Werts an. 

.. index:: asin()
.. _asin():

* ``double asin(double x)``

    Gibt den :ref:`Arcus-Sinus <gwm:Arcus-Funktionen>`-Wert eines :math:`x`-Werts an,
    wobei :math:`x \in [-1;+1]` gelten muss.

.. index:: acos()
.. _acos():

* ``double acos(double x)``

    Gibt den :ref:`Arcus-Cosinus <gwm:Arcus-Funktionen>`-Wert eines :math:`x`-Werts an,
    wobei :math:`x \in [-1;+1]` gelten muss.

.. index:: atan()
.. _atan():

* ``double atan(double x)``

    Gibt den :ref:`Arcus-Tangens <gwm:Arcus-Funktionen>`-Wert eines :math:`x`-Werts an.

..  ???
..  * ``double atan2(double x, double y)``
..  arctan(y/x) im Bereich [-p, +p].

.. index:: sinh()
.. _sinh():

* ``double sinh(double x)``

    Gibt den Sinus-Hyperbolicus-Wert eines :math:`x`-Werts an.

.. index:: cosh()
.. _cosh():

* ``double cosh(double x)``

    Gibt den Cosinus-Hyperbolicus-Wert eines :math:`x`-Werts an.

.. index:: tanh()
.. _tanh():

* ``double tanh(double x)``

    Gibt den Tangens-Hyperbolicus-Wert eines :math:`x`-Werts an.

.. index:: exp()
.. _exp():

* ``double exp(double x)``

    Gibt den Wert der :ref:`Exponentialfunktion <gwm:Exponentialfunktionen>`
    :math:`e ^{x}` eines :math:`x`-Werts an.

.. index:: log()
.. _log():

* ``double log(double x)``

    Gibt den Wert der natürlichen :ref:`Logarithmusfunktion
    <gwm:Logarithmusfunktionen>` :math:`\ln{(x)}` an, wobei :math:`x > 0` gelten
    muss.

.. index:: log10()
.. _log10():

* ``double log10(double x)``

    Gibt den Wert des :ref:`Logarithmus <gwm:Logarithmusfunktionen>` zur Basis
    :math:`10` an, wobei :math:`x > 0` gelten muss. 

.. index:: pow()
.. _pow():

* ``double pow(double x)``

    Gibt den Wert von :math:`x^y` an. Ein Argumentfehler liegt vor, wenn
    :math:`x=0` und :math:`y<0` gilt, oder wenn :math:`x<0` und :math:`y` nicht
    ganzzahlig ist.

.. index:: sqrt()
.. _sqrt():

* ``double sqrt(double x)``

    Gibt den Wert der Quadratwurzel eines :math:`x`-Werts an, wobei :math:`x \le
    0`.

.. index:: ceil()
.. _ceil():

* ``double ceil(double x)``

    Gibt den kleinsten ganzzahligen Wert als ``double`` an, der nicht kleiner
    als :math:`x` ist.

.. index:: floor()
.. _floor():

* ``double floor(double x)``

    Gibt den größten ganzzahligen Wert als ``double`` an, der nicht größer als
    :math:`x` ist.

.. index:: fabs()
.. _fabs():

* ``double fabs(double x)``

    Gibt den Absolutwert :math:`|x|` eines :math:`x`-Werts an.

.. index:: ldexp()
.. _ldexp():

* ``double ldexp(double x, n)``

    Gibt den Wert des Ausdrucks :math:`x \cdot 2^n` an.

.. index:: frexp()
.. _frexp():

* ``double frexp(double x, int *exp)``

    Zerlegt :math:`x` in eine normalisierte Mantisse im Bereich
    :math:`[\frac{1}{2}\,;\, 1]`, die als Ergebnis zurückgegeben wird, und eine
    Potenz von :math:`2`, die in ``*exp`` abgelegt wird. Ist :math:`x` gleich
    Null, sind beide Teile des Resultats Null.

.. index:: modf()
.. _modf():

* ``double modf(double x, double *ip)``

    Zerlegt :math:`x` in einen ganzzahligen Teil und einen Rest, die beide das
    gleiche Vorzeichen wie :math:`x` besitzen. Der ganzzahlige Teil wird bei
    ``*ip`` abgelegt, der Rest wird als Ergebnis zurückgegeben.

.. index:: fmod()
.. _fmod():

* ``double fmod(double x, double y)``

    Gibt den Gleitpunktrest von :math:`\frac{x}{y}` an, mit dem gleichen
    Vorzeichen wie :math:`x`. Wenn :math:`y` gleich Null ist, hängt das Resultat
    von der Implementierung ab.


.. index:: cmath.h
.. _cmath.h:

``cmath.h`` -- Mathematische Funktionen für komplexe Zahlen
-----------------------------------------------------------

* ``double creal(double complex z)``

    Gibt den Realteil der komplexen Zahl :math:`z` als Ergebnis zurück.


* ``double cimag(double complex z)``

    Gibt den Imaginärteil der komplexen Zahl :math:`z` als Ergebnis zurück.

* ``double cabs(double complex z)``

    Behandelt die komplexe Zahl :math:`z` wie einen zweidimensionalen Vektor in
    der Zahlenebene; gibt den Betrag (die Länge) dieses Vektors als Ergebnis
    zurück.

.. index:: casin()
.. _casin():

* ``double casin(double complex z)``

    Gibt den Arcus-Sinus-Wert der komplexen Zahl :math:`z` an.

.. wobei :math:`x \in [-1;+1]` gelten muss.

.. index:: cacos()
.. _cacos():

* ``double cacos(double complex z)``

    Gibt den :ref:`Arcus-Cosinus <gwm:Arcus-Funktionen>`-Wert der komplexen Zahl
    :math:`z` an, wobei der Realteil von :math:`z` im Bereich :math:`[-1;+1]`
    liegen muss.

.. index:: catan()
.. _catan():

* ``double catan(double complex x)``

    Gibt den :ref:`Arcus-Tangens <gwm:Arcus-Funktionen>`-Wert einer komplexen
    Zahl :math:`z` an.

.. index:: string.h
.. _string.h:

``string.h`` -- Zeichenkettenfunktionen
---------------------------------------

In der Definitionsdatei ``<string.h>`` gibt es zwei Gruppen von Funktionen für
Felder und Zeichenketten. Die Namen der ersten Gruppe von Funktionen beginnen
mit ``mem``; diese sind allgemein zur Manipulation von Feldern vorgesehen. Die
Namen der zweiten Gruppe von Funktionen beginnen mit ``str`` und ist speziell
für Zeichenketten gedacht, die mit dem Zeichen ``\0'`` abgeschlossen sind.

Wichtig: Bei der Verwendung der ``mem``- und ``str``-Funktionen muss der
Programmierer darauf achten, dass sich die Speicherplätze der zu kopierenden
oder zu vergleichenden Zeicherketten nicht überlappen, da das Verhalten der
Funktionen sonst nicht definiert ist.

.. _mem-Funktionen:

.. rubric:: mem-Funktionen

Die ``mem``-Funktionen sind zur Manipulation von Speicherbereichen gedacht. Sie
behandeln den Wert ``\0`` wie jeden anderen Wert, daher muss immer eine
Bereichslänge angegeben werden.

.. index:: memcpy()
.. _memcpy():

* ``void * memcpy(void *str_1, const void *str_2, size_t n)``

    Kopiert die ersten :math:`n` Zeichen aus dem Array ``str_2`` in das Array
    ``str_1``; gibt ``str_1`` als Ergebnis zurück.

.. index:: memmove()
.. _memmove():

* ``void * memmove(void *str_1, const void *str_2, size_t n)``

    Kopiert ebenso wie :ref:`memcpy() <memcpy()>` die ersten :math:`n` Zeichen
    des Arrays ``str_2`` in das Array ``str_1``; gibt ``str_1`` als Ergebnis
    zurück. ``memmove()`` funktioniert allerdings auch, wenn sich die
    Speicherplätze beider Arrays überlappen.

.. index:: memcmp()
.. _memcmp():

* ``int memcmp(const void *str_1, const void *str_2, size_t n)``

    Vergleicht die ersten :math:`n` Zeichen des Arrays ``str_1`` mit dem Array
    ``str_2``; gibt als Ergebnis einen Wert :math:`<0` zurück falls ``str_1 <
    str_2`` ist, den Wert :math:`0` für ``str_1 == str_2``, oder einen Wert
    :math:`>0` falls ``str_1 > str_2`` ist. 

    Die Bereiche werden nach den ASCII-Codes der Anfangsbuchstaben verglichen,
    nicht lexikalisch.

.. index:: memchr()
.. _memchr():

* ``void * memchr(const void *str, char c, size_t n)``

    Gibt einen Zeiger auf das erste Byte mit dem Wert ``c`` im Array ``str``
    zurück, oder ``NULL``, wenn das Byte innerhalb der ersten :math:`n` Zeichen
    nicht vorkommt.

.. index:: memset()
.. _memset():

* ``void * memset(void *str, char c, size_t n)``

    Setzt die ersten :math:`n` Bytes des Arrays ``str`` auf den Wert ``c``; gibt
    ``str`` als Ergebnis zurück.

.. _str-Funktionen:

.. rubric:: str-Funktionen

.. index:: strcpy()
.. _strcpy():

* ``char * strcpy(char *str_1, const char *str_2)``

    Kopiert eine Zeichenkette ``str_2`` in ein Array ``str_1``, inklusive
    ``\0``; gibt ``str_1`` als Ergebnis zurück.

.. index:: strncpy()
.. _strncpy():

* ``char * strncpy(char *str_1, const char *str_2, size_t n)``

    Kopiert höchstens :math:`n` Zeichen aus der Zeichenkette ``str_2`` in die
    Zeichenkette ``str_1``, und gibt ``str_1`` als Ergebnis zurück. Dabei wird
    ``str_1`` mit ``\0`` abgeschlossen, wenn ``str_2`` weniger als :math:`n`
    Zeichen hat.

.. index:: strcat()
.. _strcat():

* ``char * strcat(char *str_1, const char *str_2)``

    Hängt die Zeichenkette ``str_2`` hinten an die Zeichenkette ``str_1`` an;
    gibt ``str_1`` als Ergebnis zurück.

.. index:: strncat()
.. _strncat():

* ``char * strncat(char *str_1, const char *str_2, size_t n)``

    Fügt höchstens :math:`n` Zeichen der Zeichenkette ``str_2`` hinten an die
    Zeichenkette ``str_1`` an und schließt ``str_1`` mit ``\0`` ab. Gibt
    ``str_1`` als Ergebnis zurück.

.. index:: strcmp()
.. _strcmp():

* ``int strcmp(const char *str_1, const char *str_2)``

    Vergleicht die beiden Zeichenketten ``str_1`` und ``str_2`` miteinander;
    gibt als Ergebnis einen Wert :math:`<0` zurück falls ``str_1 < str_2`` ist,
    den Wert :math:`0` für ``str_1 == str_2``, oder einen Wert :math:`>0` falls
    ``str_1 > str_2`` ist. 

    Die Zeichenketten werden nach den ASCII-Codes der Anfangsbuchstaben
    verglichen, nicht lexikalisch.

.. index:: strncmp()
.. _strncmp():

* ``int strncmp(const char *str_1, const char *str_2, size_t n)``

    Vergleicht höchstens :math:`n` Zeichen der Zeichenkette ``str_1`` mit der
    Zeichenkette ``str_2``; gibt einen Wert :math:`<0` zurück falls ``str_1 <
    str_2`` ist, den Wert :math:`0` für ``str_1 == str_2``, oder einen Wert
    :math:`>0` falls ``str_1 > str_2`` ist.

    Die Zeichenketten werden nach den ASCII-Codes der Anfangsbuchstaben
    verglichen, nicht lexikalisch.

.. index:: strchr()
.. _strchr():

* ``char * strchr(const char *str, char c)``

    Gibt einen Zeiger auf das erste Zeichen ``c`` in der Zeichenkette ``str`` als
    Ergebnis zurück, oder ``NULL``, falls ``c`` nicht in der Zeichenkette
    enthalten ist.

.. index:: strrchr()
.. _strrchr():

* ``char * strrchr(const char *str, char c)``

    Gibt einen Zeiger auf das letzte Zeichen ``c`` in der Zeichenkette ``str``
    als Ergebnis zurück, oder ``NULL``, falls ``c`` nicht in der Zeichenkette
    enthalten ist.

.. index:: strspn()
.. _strspn():

* ``size_t strspn(const char *str_1, const char *str_2)``

    Gibt die Anzahl der Zeichen am Anfang der Zeichenkette ``str_1`` als
    Ergebnis zurück, die in dieser Reihenfolge ebenfalls in der Zeichenkette
    ``str_2`` vorkommen.

.. index:: strcspn()
.. _strcrspn():

* ``size_t strcspn(const char *str_1, const char *str_2)``

    Gibt die Anzahl der Zeichen am Anfang der Zeichenkette ``str_1`` als
    Ergebnis zurück, die in dieser Reihenfolge *nicht* in der Zeichenkette
    ``str_2`` vorkommen.

.. index:: strpbrk()
.. _strpbrkn():

* ``char * strpbrk(const char *str_1, const char *str_2)``

    Gibt einen Zeiger auf die Position in der Zeichenkette ``str_1`` als
    Ergebnis zurück, an der irgendein Zeichen aus der Zeichenkette ``str_2``
    erstmals vorkommt, oder ``NULL``, falls keines dieser Zeichen vorkommt.

.. index:: strstr()
.. _strstr():

* ``char * strstr(const char *str_1, const char *str_2)``

    Gibt einen Zeiger auf erstes Vorkommen von der Zeichenkette ``str_2``
    innerhalb der Zeichenkette ``str_1`` als Ergebnis zurück, oder ``NULL``,
    falls diese nicht vorkommt. 
    
..  (Suchen eines Strings in anderem String)


.. index:: strlen()
.. _strlen():

* ``size_t strlen(const char *str)``

    Gibt die Länge der Zeichenkette ``str`` ohne ``\0`` an.

.. index:: strerror()
.. _strerror():

* ``char * strerror(size_t n)``

    Gibt einen Zeiger auf diejenige Zeichenkette als Ergebnis zurück, die dem
    Fehler mit der Nummer :math:`n` zugewiesen ist.

.. index:: strtok()
.. _strtok():

* ``char * strtok(char *str_1, const char *str_2)``

    Durchsucht die Zeichenkette ``str_1`` nach Zeichenfolgen, die durch Zeichen aus
    der Zeichenkette ``str_2`` begrenzt sind.

.. TODO bessere Erklärung?



.. index:: stdio.h
.. _stdio.h:

``stdio.h`` -- Ein- und Ausgabe
-------------------------------

Die Datei ``stdio.h`` definiert Typen und Funktionen zum Umgang mit Datenströmen
("Streams"). Ein Stream ist Quelle oder Ziel von Daten und wird mit einer Datei
oder einem angeschlossenen Gerät verknüpft. 

Unter Windows muss zwischen Streams für binäre und für Textdateien
unterschieden werden, unter Linux nicht. Ein Textstream ist eine Folge von
Zeilen, die jeweils kein oder mehrere Zeichen enthalten und jeweils mit ``'\n'``
abgeschlossen sind.

Ein Stream wird mittels der Funktion ``open()`` mit einer Datei oder einem Gerät
verbunden; die Verbindung wird mittels der Funktion ``close()`` wieder
aufgehoben. Öffnet man eine Datei, so erhält man einen Zeiger auf ein Objekt vom
Typ ``FILE``, in welchem alle Information hinterlegt sind, die zur Kontrolle des
Stream nötig sind.

Wenn die Ausführung eines Programms beginnt, sind die drei Standard-Streams
``stdin``, ``stdout`` und ``stderr`` bereits automatisch geöffnet.

.. _Dateioperationen:

.. rubric:: Dateioperationen

Die folgenden Funktionen beschäftigen sich mit Datei-Operationen. Der Typ
``size_t`` ist der vorzeichenlose, ganzzahlige Resultattyp des
``sizeof``-Operators.

.. index:: fopen()
.. _fopen():

* ``FILE *fopen(const char *filename, const char *mode)``

    Öffnet die angegebene Datei; gibt als Ergebnis einen Datenstrom zurück,
    oder ``NULL`` falls das Öffnen fehlschlägt. 
    
    .. _mode:

    Als Zugriffsmodus ``mode`` kann angegeben werden: 

    - ``"r"``: Textdatei zum Lesen öffnen
    - ``"w"``: Textdatei zum Schreiben neu erzeugen (gegebenenfalls alten Inhalt
      wegwerfen) 
    - ``"a"``: Text anfügen; Datei zum Schreiben am Dateiende öffnen oder erzeugen 
    - ``"r+"``: Textdatei zum Ändern öffnen (Lesen und Schreiben) 
    - ``"w+"``: Textdatei zum Ändern erzeugen (gegebenenfalls alten Inhalt wegwerfen) 
    - ``"a+"``: Datei neu erzeugen oder zum Ändern öffnen und Text anfügen
      (Schreiben am Ende)

.. index:: freopen()
.. _freopen():

* ``FILE *freopen(const char *filename, const char *mode, FILE *stream)``

    Öffnet die angegebene Datei für den angegebenen :ref:`Zugriffsmodus <mode>`
    und verknüpft den Datenstrom ``stream`` damit. Als Ergebnis wird ``stream``
    zurück gegeben, oder ``Null`` falls ein Fehler auftritt. 
    
    Mit ``freopen()`` ändert man normalerweise die Dateien, die mit ``stdin``,
    ``stdout`` oder ``stderr`` verknüpft sind.

.. index:: fflush()
.. _fflush():

* ``int fflush(FILE *stream)``

    Sorgt bei einem Ausgabestrom dafür, dass gepufferte, aber noch nicht
    geschriebene Daten geschrieben werden; bei einem Eingabestrom ist der Effekt
    undefiniert. Die Funktion gibt normalerweise ``NULL`` als Ergebnis zurück,
    oder ``EOF`` (Konstante mit Wert ``-1``), falls ein Schreibfehler auftritt. 
  
    ``fflush(NULL)`` bezieht sich auf alle offenen Dateien.

.. index:: feof()
.. _feof():

* ``int feof(FILE *stream);``

    Prüft, ob der angegebene File-Pointer auf das Ende einer Datei zeigt. Die
    Funktion gibt normalerweise ``0`` als Ergebnis zurück, oder einen Wert
    ungleich Null, wenn das Ende der Datei erreicht ist.

.. index:: ferror()
.. _ferror():

* ``int ferror(FILE *stream);``

    Jede ``FILE``-Struktur besitzt eine Steuervariable ("Flag") namens
    ``error``. ``ferror()`` prüft, ob dieses Flag gesetzt ist, was
    beispielsweise durch einen Fehler beim Lesen oder Schreiben verursacht wird.
    Die Funktion gibt normalerweise ``0`` als Ergebnis zurück, oder einen Wert
    ungleich Null, wenn das Fehler-Flag des File-Pointers gesetzt ist.
    

* ``int ferror(FILE *stream);``

.. index:: fclose()
.. _fclose():

* ``int fclose(FILE *stream)``

    Schreibt noch nicht geschriebene Daten für ``stream``, wirft noch nicht
    gelesene, gepufferte Eingaben weg, gibt automatisch angelegte Puffer frei und
    schließt den Datenstrom. Die Funktion gibt normalerweise ``NULL`` als Ergebnis
    zurück, oder ``EOF`` (Konstante mit Wert ``-1``), falls ein Fehler auftritt.

.. index:: remove()
.. _remove():

* ``int remove(const char *filename)``

    Löscht die angegebene Datei, so dass ein anschließender Versuch, sie zu
    öffnen, fehlschlagen wird. Bei einem Fehler gibt die Funktion einen von Null
    verschiedenen Wert zurück.

.. index:: rename()
.. _rename():

* ``int rename(const char *oldname, const char *newname)``

    Ändert den Namen einer Datei. Bei einem Fehler gibt die Funktion einen von
    Null verschiedenen Wert zurück.

.. index:: tmpfile()
.. _tmpfile():

* ``FILE * tmpfile(void)``

    Erzeugt eine temporäre Datei mit Zugriffsmodus ``"wb+"``, die automatisch
    gelöscht wird, wenn der Zugriff abgeschlossen wird, oder wenn das Programm
    normal zu Ende geht. Als Ergebnis gibt ``tmpfile()`` einen Datenstrom
    zurück, oder ``NULL`` falls die Datei nicht erzeugt werden konnte.

.. index:: tmpnam()
.. _tmpnam():

* ``char * tmpnam(char s[L_tmpnam])``

    ``tmpnam(NULL)`` erzeugt eine Zeichenkette, die nicht der Name einer
    existierenden Datei ist, und gibt einen Zeiger auf einen internen
    Vektor im statischen Speicherbereich als Ergebnis zurück. 

    ``tmpnam(s)`` speichert die Zeichenkette in ``s`` und gibt ``s`` als
    Ergebnis zurück; in ``s`` müssen wenigstens ``L_tmpnam`` Zeichen abgelegt
    werden können. 
    
    Bei jedem Aufruf erzeugt die Funktion einen anderen Namen; man kann
    höchstens von ``TMP_MAX`` verschiedenen Namen während der Ausführung des
    Programms ausgehen. Zu beachten ist, dass ein Name und keine Datei
    erzeugt wird.

.. TODO: Synonym für "Vektor"?

.. index:: setvbuf()
.. _setvbuf():

* ``int setvbuf(FILE *stream, char *buf, int mode, size_t size)``

    Kontrolliert die Pufferung bei einem Datenstrom; die Funktion muss
    aufgerufen werden, bevor gelesen oder geschrieben wird, und vor allen
    anderen Operationen. Hat ``mode`` den Wert ``_IOFBF``, so wird vollständig
    gepuffert, ``_IOLBF`` sorgt für zeilenweise Pufferung bei Textdateien und
    ``_IONBF`` verhindert Puffern. Wenn ``buf`` nicht gleich ``NULLi`` ist, wird
    ``buf`` als Puffer verwendet; andernfalls wird ein Puffer angelegt. ``size``
    legt die Puffergröße fest. 

    Bei einem Fehler gibt die Funktion einen von Null verschiedenen Wert zurück.

.. index:: setbuf()
.. _setbuf():

* ``void setbuf(FILE *stream, char *buf)``

    Wenn ``buf`` den Wert ``NULL`` hat, wird der Datenstrom nicht gepuffert;
    andernfalls ist ``setbuf`` äquivalent zu ``(void) setvbuf(stream, buf,
    _IOFBF, BUFSIZ)``.

Ändern bedeutet, dass die gleiche Datei gelesen und geschrieben werden darf;
``fflush()`` oder eine Funktion zum Positionieren in Dateien muss zwischen einer
Lese- und einer Schreiboperation oder umgekehrt aufgerufen werden. Dateinamen
sind auf ``FILENAME_MAX Zeichen`` begrenzt, höchstens ``FOPEN_MAX`` Dateien
können gleichzeitig offen sein.

..  Enthält mode nach dem ersten Zeichen noch b, also etwa "rb" oder "w+b",
..  dann wird auf eine binäre Datei zugegriffen. 

.. rubric:: Aus- und Eingabe

* ``int fputs(const char *str, FILE *stream)``

    Schreibt die Zeichenkette ``str`` in die mit dem File-Pointer angegebene
    Datei. Als Ergebnis gibt die Funktion einen nicht-negativen Wert als
    Ergebnis zurück, oder ``EOF`` (Konstante mit Wert ``-1``), wenn ein Fehler
    aufgetreten ist.

.. index:: fprintf()
.. _fprintf():

* ``int fprintf(FILE *stream, const char *format, ...)``

    Die Funktion ``fprintf()`` wandelt Ausgaben um und schreibt sie in ``stream``
    unter Kontrolle von ``format``. Als Ergebnis gibt sie die Anzahl der
    geschriebenen Zeichen zurück; der Wert ist negativ, wenn ein Fehler
    aufgetreten ist.

* ``int printf(const char *format, ...)``

    ``printf(...)`` ist äquivalent zu ``fprintf(stdout, ...)``.
    Die formatierte Ausgabe der ``printf()``-Funktion ist im Abschnitt
    :ref:`Ausgabe und Eingabe <Ausgabe und Eingabe>` näher beschrieben.

.. index:: sprintf()
.. _sprintf():

* ``int sprintf(char *s, const char *format, ...)``

    Die Funktion ``sprintf()`` funktioniert wie ``printf()``, nur wird die Ausgabe
    in das Zeichenarray ``s`` geschrieben und mit ``\0`` abgeschlossen. ``s``
    muss groß genug für das Resultat sein. Im Ergebniswert wird ``\0`` nicht
    mitgezählt.

..  .. index:: vprintf()
..  .. _vprintf():

..  * | ``vprintf(const char *format, va_list arg)``, 
..  | ``vfprintf(FILE *stream, const char *format, va_list arg)``, 
..  | ``vsprintf(char *s, const char *format, va_list arg)``

..  Die Funktionen ``vprintf()``, ``vfprintf()`` und ``vsprintf()`` sind
..  äquivalent zu den entsprechenden ``printf()``-Funktionen, jedoch wird die
..  variable Argumentenliste durch ``arg`` ersetzt. Dieser Wert wird mit dem
..  Makro ``va_start`` und vielleicht mit Aufrufen von ``va_arg`` initialisiert.


.. index:: stdlib.h
.. _stdlib.h:

``stdlib.h`` -- Hilfsfunktionen 
--------------------------------

Die Definitionsdatei ``<stdlib.h>`` vereinbart Funktionen zur Umwandlung von
Zahlen, für Speicherverwaltung und ähnliche Aufgaben.

.. index:: atof()
.. _atof():

* ``double atof(const char *s)``

    Wandelt die Zeichenkette ``s`` in ``double`` um. Beendet die Umwandlung beim
    ersten unbrauchbaren Zeichen.

.. index:: atoi()
.. _atoi():

* ``int atoi(const char *s)``

    Wandelt die Zeichenkette ``s`` in ``int`` um. Beendet die Umwandlung beim
    ersten unbrauchbaren Zeichen.

.. index:: atol()
.. _atol():

* ``long atol(const char *s)``

    Wandelt die Zeichenkette ``s`` in ``long`` um. Beendet die Umwandlung beim
    ersten unbrauchbaren Zeichen.

.. index:: strtod()
.. _strtod():

* ``double strtod(const char *s, char **endp)``

    Wandelt den Anfang der Zeichenkette ``s`` in ``double`` um, dabei wird
    Zwischenraum am Anfang ignoriert. Die Umwandlung wird beim ersten
    unbrauchbaren Zeichen beendet. Die Funktion speichert einen Zeiger auf den
    eventuell nicht umgewandelten Rest der Zeichenkette bei ``*endp``, falls
    ``endp`` nicht ``NULL`` ist. Falls das Ergebnis zu groß ist, (also bei einem
    Overflow), wird als Resultat ``HUGE_VAL`` mit dem korrekten Vorzeichen
    geliefert; liegt das Ergebnis zu dicht bei Null (also bei einem Underflow),
    wird Null geliefert. In beiden Fällen erhält ``errno`` den Wert ``ERANGE``.

.. index:: strtol()
.. _strtol():

* ``long strtol(const char *s, char **endp, int base)``

    Wandelt den Anfang der Zeichenkette ``s`` in ``long`` um, dabei wird
    Zwischenraum am Anfang ignoriert. Die Umwandlung wird beim ersten
    unbrauchbaren Zeichen beendet. Die Funktion speichert einen Zeiger auf den
    eventuell nicht umgewandelten Rest der Zeichenkette bei ``*endp``, falls
    ``endp`` nicht ``NULL`` ist. Hat ``base`` einen Wert zwischen :math:`2` und
    :math:`36`, erfolgt die Umwandlung unter der Annahme, dass die Eingabe in
    dieser Basis repräsentiert ist. 

    Hat ``base`` den Wert Null, wird als Basis :math:`8`, :math:`10` oder
    :math:`16` verwendet, je nach ``s``; eine führende Null bedeutet dabei oktal
    und ``0x`` oder ``0X`` zeigen eine hexadezimale Zahl an. In jedem Fall stehen
    Buchstaben für die Ziffern von :math:`10` bis ``base-l``; bei Basis ``16``
    darf ``0x`` oder ``0X`` am Anfang stehen. Wenn das Resultat zu groß werden
    würde, wird je nach Vorzeichen ``LONG_MAX`` oder ``LONG_MIN`` geliefert und
    ``errno`` erhält den Wert ``ERANGE``.

.. index:: strtoul()
.. _strtoul():

* ``unsigned long strtoul(const char *s, char **endp, int base)``

    Funktioniert wie ``strtol()``, nur ist der Resultattyp ``unsigned long`` und
    der Fehlerwert ist ``ULONG_MAX``.

.. index:: rand()
.. _rand():

* ``int rand(void)``

    Gibt als Ergebnis eine ganzzahlige Pseudo-Zufallszahl im Bereich von
    :math:`0` bis ``RAND_MAX`` zurück; ``RAND_MAX`` ist mindestens ``32767``.

.. index:: srand()
.. _srand():

* ``void srand(unsigned int seed)``

    Benutzt ``seed`` als Ausgangswert für eine neue Folge von
    Pseudo-Zufallszahlen. Der erste Ausgangswert ist :math:`1`.

.. index:: calloc()
.. _calloc():

* ``void * calloc(size_t nobj, size_t size)``

    Gibt als Ergebnis einen Zeiger auf einen Speicherbereich für einen Vektor
    von ``nobj`` Objekten zurück, jedes mit der Größe ``size``, oder ``NULL``,
    wenn die Anforderung nicht erfüllt werden kann. Der Bereich wird mit
    Null-Bytes initialisiert.

.. index:: malloc()
.. _malloc():

* ``void * malloc(size_t size)``

    Gibt einen Zeiger auf einen Speicherbereich für ein Objekt der Größe
    ``size`` zurück, oder ``NULL``, wenn die Anforderung nicht erfüllt werden
    kann. Der Bereich ist nicht initialisiert.

.. index:: realloc()
.. _realloc():

* ``void * realloc(void *p, size_t size)``

    Ändert die Größe des Objekts, auf das der Pointer ``p`` zeigt, in ``size`` ab.
    Bis zur kleineren der alten und neuen Größe bleibt der Inhalt unverändert.
    Wird der Bereich für das Objekt größer, so ist der zusätzliche Bereich
    uninitialisiert. ``realloc()`` liefert einen Zeiger auf den neuen Bereich oder
    ``NULL``, wenn die Anforderung nicht erfüllt werden kann; in diesem Fall wird
    der Inhalt nicht verändert.

.. index:: free()
.. _free():

* ``void free(void *p)``

    Gibt den Bereich frei, auf den der Pointer ``p`` zeigt; die Funktion hat
    keinen Effekt, wenn ``p`` den Wert ``NULL`` hat. ``p`` muss auf einen Bereich
    zeigen, der zuvor mit ``calloc()``, ``malloc()`` oder ``realloc()`` angelegt
    wurde.

.. index:: abort()
.. _abort():

* ``void abort(void)``

    Sorgt für eine anormale, sofortige Beendigung des Programms.
   
.. index:: exit()
.. _exit():

* ``void exit(int status)``

    Beendet das Programm normal: Dabei werden :ref:`atexit()
    <atexit()>`-Funktionen in der umgekehrten Reihenfolge ihrer Hinterlegung
    aufgerufen, Puffer offener Dateien werden geschrieben, offene Ströme
    abgeschlossen, und die Kontrolle geht an die Umgebung des Programms zurück.
    Welcher ``status`` an die Umgebung des Programms geliefert wird, hängt von
    der Implementierung ab, aber ``Null`` gilt als erfolgreiches Ende. Die Werte
    ``EXIT_SUCCESS`` (Wert: ``0``) und ``EXIT_FAILURE`` (Wert: ``1``) können
    ebenfalls angegeben werden.

.. index:: atexit()
.. _atexit():

* ``int atexit(void (*fcn)(void))``

    Hinterlegt die Funktion ``fcn``, damit sie aufgerufen wird, wenn das
    Programm normal endet, und liefert einen von Null verschiedenen Wert, wenn
    die Funktion nicht hinterlegt werden kann.

.. index:: system()
.. _system():

* ``int system(const char *s)``

    Gibt die Zeichenkette ``s`` an die Umgebung zur Ausführung. Hat ``s`` den
    Wert ``NULL``, so liefert ``system()`` einen von Null verschiedenen Wert,
    wenn es einen Kommandoprozessor gibt. Wenn ``s`` von ``NULL`` verschieden
    ist, dann ist der Resultatwert implementierungsabhängig.

.. index:: getenv()
.. _getenv():

* ``char * getenv(const char *name)``

    Gibt die zu ``name`` gehörende Zeichenkette aus der Umgebung als Ergebnis
    zurück, oder ``NULL``, wenn keine Zeichenkette existiert. Die Details hängen
    von der Implementierung ab.

.. index:: bsearch()
.. _bsearch():

* ``void * bsearch(const void *key, const void *base, size_t n, size_t
  size, int (*cmp)(const void *keyval, const void *datum))``

    Durchsucht ``base[0]`` bis ``base[n-l]`` nach einem Eintrag, der gleich
    ``*key`` ist. Die Funktion ``cmp`` muss einen negativen Wert liefern, wenn ihr
    erstes Argument (der Suchschlüssel) kleiner als ihr zweites Argument (ein
    Tabelleneintrag) ist, Null, wenn beide gleich sind, und sonst einen positiven
    Wert. 

    Die Elemente des Arrays base müssen aufsteigend sortiert sein. In ``size``
    muss die Größe eines einzelnen Elements übergeben werden. ``bsearch()`` gibt
    als Ergebnis einen Zeiger auf das gefundene Element zurück, oder ``NULL``,
    wenn keines existiert.

.. index:: qsort()
.. _qsort():

* ``void qsort(void *base, size_t n, size_t size, int (*cmp)(const void *,
  const void *))``

    Sortiert ein Array ``base[0]`` bis ``base[n-1]`` von Objekten der Größe
    ``size`` in aufsteigender Reihenfolge. Für die Vergleichsfunktion ``cmp`` gilt
    das gleiche wie bei bsearch.

.. index:: abs()
.. _abs():

* ``int abs(int x)``

    Gibt den den absoluten Wert (Betrag) :math:`|x|` von :math:`x` als ``int`` an.

.. index:: labs()
.. _labs():

* ``long labs(long x)``

    Gibt den absoluten Wert (Betrag) :math:`|x|` von :math:`x` als ``long`` an.

.. index:: div()
.. _div():

* ``div_t div(int n, int z)``

    Gibt den Quotienten und Rest von :math:`\frac{n}{z}` an. Die Ergebnisse
    werden in den ``int``-Komponenten ``quot`` und ``rem`` einer Struktur vom
    Typ ``div_t`` abgelegt.

.. index:: ldiv()
.. _ldiv():

* ``ldiv_t ldiv(long n, long z)``

    Gibt den Quotienten und Rest von :math:`\frac{n}{z}` an. Die Ergebnisse
    werden in den ``long``-Komponenten ``quot`` und ``rem`` einer Struktur vom
    Typ ``ldiv_t`` abgelegt.



``time.h`` -- Funktionen für Datum und Uhrzeit
----------------------------------------------

Die Definitionsdatei ``time.h`` vereinbart Typen und Funktionen zum Umgang mit
Datum und Uhrzeit. Manche Funktionen verarbeiten die Ortszeit, die von der
Kalenderzeit zum Beispiel wegen einer Zeitzone abweicht. ``clock_t`` und
``time_t`` sind arithmetische Typen, die Zeiten repräsentieren, und ``struct
tm`` enthält die Komponenten einer Kalenderzeit:

.. code-block:: c

    struct tm 
    {
        // Sekunden nach der vollen Minute (0, 61) 
        // (Die zusätzlich möglichen Sekunden sind Schaltsekunden)
        int tm_sec;

        // Minuten nach der vollen Stunde (0, 59)
        int tm_min;

        // Stunden seit Mitternacht (0, 23)
        int tm_hour;

        // Tage im Monat (1, 31)
        int tm_mday;

        // Monate seit Januar (0, 11)
        int tm_mon;

        // Jahre seit 1900
        int tm_year;

        // Tage seit Sonntag (0, 6)
        int tm_wday;

        // Tage seit dem 1. Januar (0, 365)
        int tm_yday;

        // Kennzeichen für Sommerzeit
        int tm_isdst;
    }

``tm_isdst`` ist positiv, wenn Sommerzeit gilt, Null, wenn Sommerzeit nicht
gilt, und negativ, wenn die Information nicht zur Verfügung steht.

.. index:: clock()
.. _clock():

* ``clock_t clock(void)``

    Gibt die Rechnerkern-Zeit an, die das Programm seit Beginn seiner Ausführung
    verbraucht hat, oder ``-1``, wenn diese Information nicht zur Verfügung
    steht. 
    
    ``clock()/CLOCKS_PER_SEC`` ist eine Zeit in Sekunden.

.. index:: time()
.. _time():

* ``time_t time(time_t *tp)``

    Gibt die aktuelle Kalenderzeit an,  oder ``-1``, wenn diese nicht zur
    Verfügung steht. Wenn ``tp`` von ``NULL`` verschieden ist, wird der
    Resultatwert auch bei ``*tp`` abgelegt.

.. index:: difftime()
.. _difftime():

* ``double difftime(time_t time2, time_t timel)``

    Gibt die Differenz der Zeitangaben ``time2 - timel`` in Sekunden an.

.. index:: mktime()
.. _mktime():

* ``time_t mktime(struct tm *tp)``

    Wandelt die Ortszeit in der Struktur ``*tp`` in Kalenderzeit um, die so
    dargestellt wird wie bei ``time()``. Die Komponenten erhalten Werte in den
    angegebenen Bereichen. ``mktime()`` gibt die Kalenderzeit als Ergebnis
    zurück, oder den Wert ``-1``, wenn diese nicht dargestellt werden kann.

.. index:: strftime()
.. _strftime():

* ``size_t strftime(char *s, size_t smax, const char *fmt, const struct tm *tp)``

    Formatiert Datum und Zeit aus ``*tp`` in der Zeichenkette ``s`` gemäß
    ``fmt``, analog zu einem ``printf``-Format. Gewöhnliche Zeichen
    (insbesondere auch das abschließende ``\0``) werden nach ``s`` kopiert.
    Jedes ``%...`` wird gemäß der unten folgenden Liste ersetzt, wobei Werte
    verwendet werden, die der lokalen Umgebung entsprechen. 
  
    Es werden höchstens ``smax`` Zeichen in der Zeichenkette ``s`` abgelegt. Als
    Ergebnis gibt ``strftime()`` die Anzahl der resultierenden Zeichen zurück, mit
    Ausnahme von ``\0``. Wenn mehr als ``smax`` Zeichen erzeugt wurden, gibt
    ``strftime`` den Wert Null als Ergebnis zurück.
        
    Umwandlungszeichen für den Formatstring ``fmt``:

    .. list-table:: 
        :name: tab-strftime
        :widths: 20 50 20 50 
    
        * - ``%a`` 
          - abgekürzter Name des Wochentags.
          - ``%A`` 
          - voller Name des Wochentags.
        * - ``%b`` 
          - abgekürzter Name des Monats.
          - ``%B`` 
          - voller Name des Monats.
        * - ``%c`` 
          - lokale Darstellung von Datum und Zeit.
          - ``%d`` 
          - Tag im Monat (01 - 31).
        * - ``%H`` 
          - Stunde (00 - 23).
          - ``%I`` 
          - Stunde (01 - 12).
        * - ``%j`` 
          - Tag im Jahr (001 - 366).
          - ``%m`` 
          - Monat (01 - 12).
        * - ``%M`` 
          - Minute (00 - 59).
          - ``%p`` 
          - lokales Äquivalent von AM oder PM.
        * - ``%S`` 
          - Sekunde (00 - 61).
          - ``%U`` 
          - Woche im Jahr (Sonntag ist erster Tag) (00 - 53).
        * - ``%w`` 
          - Wochentag (0 - 6, Sonntag ist 0).
          - ``%W`` 
          - Woche im Jahr (Montag ist erster Tag) (00 - 53).
        * - ``%x`` 
          - lokale Darstellung des Datums.
          - ``%X`` 
          - lokale Darstellung der Zeit.
        * - ``%y`` 
          - Jahr ohne Jahrhundert (00 - 99).
          - ``%Y`` 
          - Jahr mit Jahrhundert.
        * - ``%Z`` 
          - Name der Zeitzone, falls diese existiert.
          - ``%%``
          - %. (Gibt ein % aus)


Die folgenden vier Funktionen liefern Zeiger auf statische Objekte, die von
anderen Aufrufen überschrieben werden können.

.. index:: asctime()
.. _asctime():

* ``char * asctime(const struct tm *tp)``

    Konstruiert aus der Zeit in der Struktur ``*tp`` eine Zeichenkette folgender
    Form: ``Sun Jan 3 15:14:13 1988\n\0``

.. index:: ctime()
.. _ctime():

* ``char * ctime(const time_t *tp)``

    Verwandelt die Kalenderzeit ``*tp`` in Ortszeit; dies ist äquivalent zu
    ``asctime(localtime(tp))``

.. index:: gmtime()
.. _gmtime():

* ``struct tm * gmtime(const time_t *tp)``

    Verwandelt die Kalenderzeit ``*tp`` in Coordinated Universal Time (UTC). Die
    Funktion liefert ``NULL``, wenn UTC nicht zur Verfügung steht. Der Name
    ``gmtime`` hat historische Bedeutung.

.. index:: localtime()
.. _localtime():

* ``struct tm * localtime(const time_t *tp)``

    Verwandelt die Kalenderzeit ``*tp`` in Ortszeit. 





