.. meta:: 
    :description: Curses
    :keywords:  Curses, NCurses, Tutorial, Howto, Einführung, Text User Interface

.. index:: Curses
.. _Curses:

Curses
======

Die C-Bibliothek Curses beziehungsweise ihre neuere Version NCurses bietet die
Möglichkeit, textbasierte Benutzeroberflächen zu erzeugen. Curses wird daher in
vielen Shell-Programmen verwendet, darunter :ref:`aptitude <gwl:apt>`,
:ref:`cmus <gwl:cmus>`, :ref:`mc <gwl:mc>`, usw.

.. index:: initscr(), refresh(), endwin()
.. _Curses starten und beenden:

Curses starten und beenden
--------------------------

Um Curses zu starten, muss zunächst die Funktion ``initscr()`` aufgerufen
werden. Diese Funktion erzeugt einen leeres Fenster und weist ihm den Namen
``stdscr`` ("standard screen") zu. Damit das neue Fenster angezeigt wird, muss
anschließend die Funktion ``refresh()`` aufgerufen werden, so dass das
Shell-Fenster aktualisiert wird und die Änderungen sichtbar werden.

Mit der ``refresh()``-Anweisung werden in Curses zwei Teilfunktionen aufgerufen:
Zunächst werden mittels der ersten Funktion ``wnoutrefresh()`` nur die
veränderten Teile eines Curses-Fensters in einem "virtuellen" Fenster
aktualisiert. Anschließend wird dieses mittels der zweiten Funktion
``douptate()`` auf den Bildschirm übertragen. Somit wird immer nur der Teil des
Fensters aktualisiert, der tatsächlich verändert wurde; dies ist wesentlich
effizienter, als wenn ständig das gesamte Shell-Fenster aktualisiert werden
müsste.

Um ein Curses-Programm wieder zu beenden, verwendet man die Funktion
``endwin()``. Diese löscht den Bildschirm und stellt automatisch die
vorgefundenen Shell-Einstellungen wieder her. Da ``endwin()`` insgesamt
zahlreiche Aufräumarbeiten übernimmt, sollte Curses stets mit dieser Funktion
beendet werden.

Ein minimalese Curses-Programm, das nur kurz einen leeren Bildschirm erzeugt,
auf diesem "Hallo Welt" ausgibt und sich nach kurzer Zeit selbst beendet, kann
folgendermaßen aussehen:

.. code-block:: c

    // Datei: curses-beispiel-1.c

    #include <ncurses.h>

    int main(void)
    {
        initscr();
        printw("Hallo Welt!");
        refresh();
        napms(3000);
        endwin();
        return 0;
    }
    
In diesem Beispiel wurde zudem die Curses-Funktion ``napms()`` verwendet, die
eine weitere Ausführung des Programms um die angegebene Anzahl in Millisekunden
verzögert.


.. index:: addch(), addstr(), printw()
.. _Ausgeben und Einlesen von Text:

Ausgeben und Einlesen von Text
------------------------------

Zur Ausgabe von Text gibt es in Curses im Wesentlichen drei Funktionen:

* Mittels ``addch(c)`` kann ein einzelnes Zeichen auf dem Bildschirm ausgegeben
  werden.

* Mittels ``addstr(*str)`` kann eine ganze Zeichenkette auf dem Bildschirm
  ausgegeben werden. (Dabei wird intern die Funktion ``addch()`` aufgerufen, bis
  die Zeichenkette abgearbeitet ist.)

* Mittels ``printw()`` kann Text in der gleichen Weise in einem Curses-Fenster
  ausgegeben werden, wie dies mittels der Funktion :ref:`printf() <printf()>`
  auf dem Standard-Ausgang der Fall ist.

.. index:: move(), getmaxyx()

Damit der Text an der richtigen Stelle im Curses-Fenster erscheint, kann man
mittels der Funktion ``move()`` den Cursor an eine bestimmte Stelle bewegen. Als
erstes Argument wird dabei die Zeilennummer ``y``, als zweites die
Spaltennummer ``x`` angegeben, also ``move(y,x)``. [#]_ Da Curses, wie in C
üblich, bei der Nummerierung mit Null beginnt, entspricht ``move(0,0)`` einem
Bewegen des Cursors in die obere linke Ecke; die erlauben Maximalwerte für die
Zeilen- und Spaltennummer in ``move()`` sind entsprechend um :math:`1` kleiner
als die Zeilen- und Spaltenanzahl des Fensters. Diese beiden Werte können
mittels der Funktion ``getmaxyx(stdscr, maxrow, maxcol)`` bestimmt werden, wobei
``maxrow`` und ``maxcol`` im Voraus als ``int`` deklariert werden müssen: [#]_

.. code-block:: c

    // Datei: curses-beispiel-2.c

    #include <ncurses.h>

    int maxrow, maxcol;


    int main(void)
        {
        initscr();

        // Größe des Curses-Fensters bestimmen:
        getmaxyx(stdscr, maxrow, maxcol);

        // Größe des Curses-Fensters ausgeben:
        move(0,0);
        printw("Das Fenster hat %d Zeilen und %d Spalten.", maxrow, maxcol);
        refresh();

        napms(3000);
        endwin();
        return 0;
        }

.. index:: mvaddch(), mvaddstr(), mvprintw()

Die Kombination von ``move()`` mit einer der Print-Anweisungen kommt in
Curses-Anwendungen sehr häufig vor; daher gibt es zu den drei Ausgabefunktionen
``addch()``, ``addstr()`` und ``printw()`` auch die kombinierten Funktionen
``mvaddch()``, ``mvaddstr()`` und ``mvprintw()``. Diesen wird beim Aufruf
zunächst die gewünschte Position des Cursor angegeben, die übrigen Argumente
sind mit den Basisfunktionen identisch. Beispielsweise sind die folgenden beiden
Aufrufe identisch:

.. code-block:: c

    // Text in Zeile 0, Spalte 3 ausgeben:
    move(0,3)
    addstr("Hallo Curses!")

    // Kurzschreibweise:
    mvaddstr(0, 3, "Hallo Curses!")

.. index:: getch(), getstr(), getnstr(), scanw()
.. _getch():

Zur Eingabe von Text gibt es in Curses ebenfalls drei grundlegende Funktionen:

* Mittels ``getch(c)`` kann ein einzelnes Zeichen vom Bildschirm eingelesen
  werden; das Zeichen wird dabei automatisch eingelesen, ohne dass die
  ``Enter``-Taste gedrückt werden muss.

* Mittels ``getstr(*str)`` und ``getnstr(*str, n)`` kann eine ganze Zeichenkette
  vom Curses-Fenster eingelesen werden, wie es mit :ref:`gets() <gets() und
  fgets()>` von der Standard-Eingabe der Fall ist. Die Funktion ``getnstr()``
  beschränkt die Anzahl an eingelesenen Zeichen dabei auf ``n`` Stück, so dass
  sichergestellt werden kann, dass das Array, in dem die Zeichenkette abgelegt
  werden soll, ausreichend groß ist.

* Mittels ``scanw()`` kann Text in der gleichen Weise von einem Curses-Fenster
  eingelesen werden, wie dies mittels der Funktion :ref:`scanf() <scanf()>` aus
  dem Standard-Eingang der Fall ist.

..  Das obige Beispielprogramm wird durch Drücken einer beliebigen Taste beendet.

Als Standard geben alle Eingabefunktionen die vom Benutzer eingegebenen Zeichen
unmittelbar auf dem Bildschirm aus, auch ohne dass dazu die
``refresh()``-Funktion aufgerufen werden müsste; zusätzlich stoppt das Programm,
bis die Eingabe vom Benutzer erfolgt ist. Ist dies nicht gewünscht, so müssen
diese Einstellung, wie im folgenden Abschnitt beschrieben, deaktiviert werden.


.. _Modifizierung der Ein- und Ausgabe:

.. rubric:: Modifizierung der Ein- und Ausgabe

In Curses gibt es folgende Funktionen, die das Verhalten des Programms
hinsichtlich Eingabe und Ausgabe anzupassen: 

.. index:: raw(), cbreak()
.. _raw und cbreak():

* ``raw()`` und ``cbreak()``:

  Normalerweise speichert die Shell die Eingabe des Benutzers in einem Puffer, bis
  ein Neues-Zeile-Zeichen oder ein Carriage-Return-Zeichen (Enter-Taste)
  erscheint. Die meisten interaktiven Programme benötigen die eingegebenen
  Zeichen allerdings unmittelbar. Die beiden Funktionen ``raw()`` und ``cbreak()``
  deaktivieren beide das Puffern von eingegebenen Zeichen, wobei sie sich in einem
  Detail unterscheiden: Eingegebene Zeichen wie ``Ctrl z`` ("Suspend") oder ``Ctrl
  c`` ("Interrupt"), die von der Shell normalerweise als Kontrollsequenzen
  interpretiert werden, werden auch bei der Verwendung von ``cbreak()`` zunächst
  von der Shell ausgewertet. Bei Verwendung von ``raw()`` werden auch diese
  Zeichen direkt ans Programm weitergeleitet und dort interpretiert.


.. index:: echo(), noecho()
.. _echo() und noecho():

* ``echo()`` und ``noecho()``:

  Diese beiden Funktionen beeinflussen, ob vom Benutzer eingegebene Zeichen
  unmittelbar auf dem Bildschirm erscheinen sollen oder nicht. Diese Funktionen
  sind insbesondere in Verbindung mit der Curses-Funktion :ref:`getch() <getch()>`
  von Bedeutung, um beispielsweise in interaktiven Programmen die unnötige
  Wiedergabe der vom Benutzer gedrückten Tasten auf dem Bildschirm zu vermeiden.
  Meist wird ``noecho()`` zu Beginn des Programms aufgerufen, und der Echo-Modus
  nur im Bedarfsfall (beispielsweise beim zeichenweise Einlesen von Text)
  aktiviert.


.. index:: keypad()
.. _keypad():

* ``keypad()``:

  Diese Funktion sollte von jedem interaktiven Curses-Programm aufgerufen werden,
  denn sie ermöglicht die Verwendung der Funktions- und Pfeiltasten. Um
  beispielsweise die Funktion für den Standard-Bildschirm ``stdscr`` zu
  aktivieren, gibt man ``keypad(stdscr, TRUE);`` ein. [#]_


.. index:: curs_set()
.. _curs_set():

* ``curs_set()``:

  Diese Funktion kann verwendet werden, um den Cursor unsichtbar oder wieder
  sichtbar zu machen. Mit ``curs_set(0);`` wird der Cursor unsichtbar, mit
  ``curs_set(1);`` wieder sichtbar.

..  2 : very visible.

.. index:: halfdelay()
.. _halfdelay():

* ``halfdelay(n)``:

  Mit dieser nur in Ausnahmefällen verwendeten Funktion kann festgelegt werden,
  dass beim dem Einlesen eines Zeichens miitels :ref:`getch() <getch()>` oder
  einer Zeichenkette maximal :math:`n` Zehntel Sekunden gewartet wird. Wird in
  dieser Zeit kein Text eingegeben, so fährt das Programm fort. Dies kann
  beispielsweise für eine Timeout-Funktion bei einer Passwort-Eingabe verwendet
  werden.

.. index:: nodelay()
.. _nodelay():

* ``nodelay()``:

  Diese Funktion wird von den meisten interaktiven Curses-Programm zu Beginn
  aufgerufen, denn sie verhindert, dass das Programm bei der Verwendung der
  Funktion :ref:`getch() <getch()>` anhält. Anstelle dessen liefert ``getch()``
  kontinuierlich den Wert ``ERR`` (entspricht dem Wert ``-1``) zurück, sofern
  der Benutzer keine Taste gedrückt hat.

Mit Hilfe von ``nodelay(stdscr, TRUE)`` kann beispielsweise eine ``mainloop()``
programmiert werden, die einzelne von der Tastatur aus eingegebene Zeichen über
eine :ref:`switch <Fallunterscheidungen>`-Anweisung mit bestimmten Anweisungen
verknüpft: [#]_

.. code-block:: c

    // Datei: curses-beispiel-3.c

    #include <ncurses.h>
   
    int main()
    {
        int c;
        int quit = FALSE;

        initscr();
        cbreak();
        noecho();
        keypad(stdscr, TRUE);
        nodelay(stdscr, TRUE);

        mvprintw(0,0, "Bitte Taste eingeben oder Programm mit \'q\' beenden.");

        while( !quit )
        {
            c = getch();
            switch(c)
            {
                case ERR:
                    napms(10);
                    break;
                case 'q':
                    quit = TRUE;
                    break;

                default:
                    mvprintw(3, 0, "ASCII-Code des Zeichens: %3d;", c);
                    mvprintw(3, 30, "Zeichen wird dargestellt als: \'%c\'.", c);
                    break;
            }

            refresh();
        }

        endwin();
        return 0;
    }

Im obigen Beispielprogramm wird zunächst Curses gestartet und das
Bildschirm-Verhalten angepasst. Anschließend wird mittels der
``while``-Schleife kontinuierlich eine Tastatureingabe vom Benutzer abgefragt:

* Wird keine Taste gedrückt (Rückgabewert: ``ERR``), so wartet das Programm
  durch Aufruf von ``napms(10)`` zehn Millisekunden lang, bis es mit der
  Ausführung fortfährt. Ohne eine derartige Verzögerung würde das Programm
  die Schleife kontinuierlich mit maximaler Geschwindigkeit abarbeiten und somit
  ständig maximale CPU-Last verursachen; mit "nur" zehn Millisekunden Pause
  reduziert sich die CPU-Auslastung auf circa :math:`1\%`.

* Wird eine beliebige Taste außer ``q`` gedrückt, so wird der :ref:`ASCII-Wert
  <ASCII-Codes>` des Zeichens und das Zeichen selbst ausgegeben. Die Darstellung
  funktioniert nur bei alphabetischen und numerischen Zeichen wie gewohnt, bei
  Funktions- und Sondertasten kann zumindest der ASCII-Wert des eingegebenen
  Zeichens abgefragt werden.

* Entspricht das eingegebene Zeichen dem Zeichen ``q`` (beziehungsweise dem
  ASCII-Wert ``113``), so wird die Variable ``quit`` auf ``TRUE`` gesetzt. Damit
  ist die Negation ``!quit`` gleich ``FALSE``, und die Schleife wird nicht
  fortgesetzt.

Schließlich wird das Curses-Programm mittels ``endwin()`` beendet.


.. _Editor-Funktionen:

Editor-Funktionen
-----------------

Die Curses-Bibliothek stellt, da sie auf textbasierte Programme ausgerichtet
ist, einige Funktionen bereit, die das Eingeben von Text ziemlich komfortabel
gestalten.

Um einzelne Zeichen oder Zeilen einzugeben oder zu löschen, gibt es in Curses
folgende Funktionen:

* ``insch()``

  Mit ``insch(c)`` kann ein einzelnes Zeichen an der Stelle des Cursors
  eingefügt werden; der Rest der Zeile wird dabei automatisch um eine
  Zeichenbreite nach rechts verschoben.

* ``delch()``

  Mit ``delch()`` wird das Zeichen an der Stelle des Cursors gelöscht; der Rest
  der Zeile wird dabei automatisch um eine Zeichenbreite nach links verschoben.

* ``insertln()``

  Mit ``insertln()`` kann eine neue Zeile an der Stelle des Cursors
  eingefügt werden; alle folgenden Zeilen werden dabei automatisch um eine
  Zeile nach unten verschoben.

* ``deleteln()``

  Mit ``deleteln()`` wird die Zeile an der Stelle des Cursors gelöscht; alle
  folgenden Zeilen werden dabei automatisch um eine Zeile nach oben verschoben.

Möchte man an der gleichen Stelle am Bildschirm aufeinanderfolgend Textstellen
mit unterschiedlicher Länge ausgeben, so werden durch ``refresh();`` nur die
jeweils neu darzustellenden Zeichen auf dem Bildschirm aktualisiert; wird
an der gleichen Startpositiion zunächst eine lange und danach eine kurze
Textstelle ausgegeben, so bleibt bei der Ausgabe der kurzen Textstelle ein Rest
der langen Textstelle bestehen.

Um den Bildschirm zu säubern, gibt es daher in Curses folgende Funktionen:

* ``clrtoeol()``

  Mit ``clrtoeol()`` werden alle Zeichen von der Cursor-Position aus bis zum
  Ende der Zeile gelöscht ("clear to end of line"). 

* ``clrtobot()``

  Mit ``clrtobot()`` werden alle Zeilen von der Cursor-Position aus bis zum Ende
  des Fensters gelöscht ("clear to bottom of window"). 

* ``erase()`` und ``clear()``

  Mit ``erase()`` und ``clear()`` werden alle Zeichen auf dem gesamten Fenster
  gelöscht. Beide Funktionen sind nahezu identisch, ``clear()`` ist allerdings
  etwas "gründlicher" und bewirkt, dass das Fenster beim nächsten Aufruf von
  ``refresh()`` komplett neu ausgegeben wird.

..  Eine weitere, etwas seltener eingesetzte Editier-Funktion ist ``ungetch()``.
..  Diese Funktion bewirkt, dass das mit ``getch()`` eingegebene Zeichen wieder
..  verworfen wird. Damit kann, sofern :ref:`nodelay() <nodelay()>` nicht aktiviert
..  ist, auf die Eingabe eines *beliebigen* Zeichens gewartet werden, das keine
..  sonstige Auswirkung auf den weiteren Ablauf des Programms hat.



.. _Attribute und Farben:

Attribute und Farben
--------------------

Text kann in Curses auf den meisten Shells auch farbig oder fettgedruckt
dargestellt werden. Eine solche Modifizierung wird mittels der folgenden
Funktionen vorgenommen werden:

.. index:: attron()

* ``attron(attr)``

  Mit dieser Funktion wird das angegebene Attribut ``attr`` aktiviert.

.. index:: attroff()

* ``attroff(attr)``

  Mit dieser Funktion wird das angegebene Attribut ``attr`` deaktiviert.

.. index:: attrset()

* ``attrset(attr)``

  Mit dieser Funktion wird das angegebene Attribut ``attr`` aktiviert; alle
  sonstigen Attribute werden deaktiviert.

Die obigen Funktionen wirken sich auf die weitere Darstellung aller
Zeichenketten aus. Um den ausgegebenen Text wieder in "normaler" Form
darzustellen, kann ``attrset(A_NORMAL)`` verwendet werden. Eine Übersicht aller
Textattribute ist in der folgenden Tabelle zusammengestellt. 

.. list-table:: 
    :name: tab-curses-text-attributes
    :widths: 50 50 

    * - ``A_NORMAL``
      - Normaler Text
    * - ``A_BOLD`` 
      - Text in Fettschrift und mit erhöhter Helligkeit 
    * - ``A_DIM`` 
      - Text mit verringerter Helligkeit (wird nicht von jeder Shell
        unterstützt)
    * - ``A_REVERSE``
      - Text mit vertauschter Vorder- und Hintergrundfarbe
    * - ``A_UNDERLINE`` 
      - Unterstrichener Text 
    * - ``A_BLINK`` 
      - Blinkender Text (wird nicht von jeder Shell unterstützt)
    * - ``A_STANDOUT`` 
      - Hervorgehobener Text (entspricht meist ``A_REVERSE``)

Um mehrere Attribute miteinander zu kombinieren, können diese entweder
nacheinander mittels ``attron()`` aktiviert werden, oder in einer einzigen
``attrset()``-Anweisung durch ein binäres Oder verbunden werden; beispielsweise
wird durch ``attrset(A_UNDERLINE | A_BOLD);`` Text künftig unterstrichen und in
Fettdruck ausgegeben.


.. index:: start_color()
.. rubric:: Farbiger Text

Um Text farbig auszugeben, sollte zunächst geprüft werden, ob eine farbige
Darstellung von der Shell unterstützt wird. Dazu gibt es in Curses die Funktion
``has_colors()``, die entweder ``TRUE`` oder ``FALSE`` als Ergebnis liefert. Ist
farbiger Text auf der Shell möglich, so kann in Curses die Farbunterstützung
mittels der Funktion ``start_color()`` freigeschaltet werden; dabei werden
zugleich die in der folgenden Tabelle angegebenen Farbnamen als symbolische
Konstanten definiert.

.. list-table:: 
    :name: tab-curses-farben 
    :widths: 50 50 50

    * - Nummer 
      - Name
      - Farbe
    * - :math:`0` 
      - ``COLOR_BLACK``
      - Schwarz 
    * - :math:`1` 
      - ``COLOR_RED``
      - Rot
    * - :math:`2`
      - ``COLOR_GREEN``
      - Grün
    * - :math:`3`
      - ``COLOR_YELLOW``
      - Gelb
    * - :math:`4`
      - ``COLOR_BLUE``
      - Blau
    * - :math:`5`
      - ``COLOR_MAGENTA``
      - Magenta
    * - :math:`6`
      - ``COLOR_CYAN``
      - Cyan
    * - :math:`7`
      - ``COLOR_WHITE``
      - Weiss

.. index:: init_pair()

Aus diesen üblicherweise 8 Farben können mittels ``init_pair()`` anschließend
so genannte "Farb-Paare" definiert werden. In einem solchen Paar besteht aus
einer Farbnummer für den Vordergrund (der Schriftfarbe) und einer Farbnummer für
den Hintergrund, wobei anstelle der Nummern auch die oben aufgelisteten
symbolischen Konstanten verwendet werden können. Beispielsweise wird mit
``init_pair(1, COLOR_YELLOW, COLOR_BLUE)`` ein Farben-Paar mit der Nummer ``1``
definiert, bei dessen Verwendung Text in gelber Farbe auf blauem Hintergrund
ausgegeben wird.

Jedes so definierte Farbenpaar kann mittels ``attron()`` beziehungsweise
``attrset()`` als Text-Attribut aktiviert werden:

.. code-block:: c

    if ( has_colors() == FALSE )
        printw("Kein farbiger Text moeglich!");
    else
        start_color();
    
    init_pair(1, COLOR_YELLOW, COLOR_BLUE );
    attrset( COLOR_PAIR(1) );
        
    printw("Farbiger Text, sofern moeglich!");
    
Neben der Angabe von ``COLOR_PAIR(n)``, die für das Farben-Paar mit der Nummer
:math:`n` steht, können ebenfalls weitere Attribute mittels eines binärem Oders
angegeben werden. Wird ein Farbenpaar mit dem Attribut ``A_BOLD`` kombiniert, so
erscheint der Text nicht nur fettgedruckt, sondern auch in einer etwas helleren
Farbe; aus Schwarz wird als Vordergrundfarbe beispielsweise Grau. Bei einer
gezielten Verwendung kann damit das Farbspektrum etwas erweitert werden.

Es ist auch möglich dem Hintergrund ein Farben-Paar zuzuweisen; damit ändert
sich das Aussehen des Curses-Fensters, auch wenn kein Text ausgegeben wird. Die
Attribute für den Hintergrund werden mit der Funktion ``bkdg()`` gesetzt. Wird
neben einem Farbenpaar und einem binärem Oder zusätzlich ein beliebiges Zeichen
angegeben, so wird der Hintergrund standardmäßig mit diesem Zeichen bedruckt:

.. code-block:: c

    bkgd( COLOR_PAIR(1) | '+' );

In diesem Fall würde mit den obigen Definitionen das Curses-Fenster blau
erscheinen und an allen Stellen ohne Text mit gelben ``+``-Zeichen aufgefüllt
werden.

.. _Fenster und Unterfenster:

Fenster und Unterfenster
------------------------

In vielen interaktiven Programmen kann man zwischen verschiedenen
Ansichtsfenstern wechseln, um beispielsweise eine Datei aus einem
Filebrowser-Fenster auszuwählen oder eine Hilfe-Seite zu betrachten. Für eine
bessere Übersichtlichkeit im Quellcode und eine bessere Effizienz ist es
empfehlenswert, für jeden derartigen Zweck ein eigenes Fenster zu verwenden, das
bei einem Wechsel nicht neu geschrieben, sondern nur wieder aktualisiert werden
muss.

.. index:: newwin()
.. _newwin():

Ein neues Fenster wird mittels der Funktion ``newwin()`` erstellt. Als
Rückgabewert liefert diese Funktion entweder einen Zeiger auf ein
``WINDOW``-Objekt, oder ``NULL``, falls beim Erstellen des Fensters ein Fehler
aufgetreten ist. Als Argumente für ``newwin()`` werden die Anzahl an Zeilen und
Spalten sowie die Startposition der oberen linken Ecke des Fensters angegeben:

.. code-block:: c

    int nrows = 5;
    int ncols = 20;
    int starty = 3;
    int startx = 5;

    mywin = newwin(nrows, ncols, starty, startx);
    wrefresh(mywin);

Ein neues Fenster darf nicht größer sein als das Standard-Fenster ``stdscr``,
und muss mindestens eine Zeile und eine Spalte beinhalten. Gibt man allerdings
``newwin(0,0,0,0);`` ein, so wird ein neues Fenster erzeugt, das genauso groß
ist wie das Fenster ``stdscr``. Damit das neue Fenster auf dem Bildschirm
sichtbar wird, muss die Funktion ``wrefresh()`` mit dem entsprechenden Namen des
Fensters aufgerufen werden. Bei Bedarf müssen zudem die Funktionen
:ref:`keypad() <keypad()>` und :ref:`nodelay <nodelay()>` für das jeweilige
Fenster aufgerufen werden.

Die Funktionen ``move()``, ``addch``, ``addstr()``, ``printw()``, ``getch()``,
``getstr()`` lassen sich auf ein existierende Fenster werden, wenn an ihren
Funktionsname vorne ein ``w`` angehängt und als erstes Argument ein Zeiger auf
das zu bearbeitende Fenster übergeben wird, also beispielsweise ``waddstr(mywin,
"Text")``.

Bei der Verwendung von mehreren sich überlappenden Fenstern ist nicht
sichergestellt, dass der Text von Curses wie erwartet dargestellt wird. Es wird
daher dringend empfohlen, entweder neue Fenster mit voller Fenstergröße zu
erzeugen, oder das Standard-Fenster nicht zu benutzen und dafür mehrere nicht
überlappende Fenster zu verwenden. Das Fenster, das zuletzt mit einem Aufruf
von ``wrefresh()`` aktualisiert wurde, wird als "oberstes" angezeigt und
verdeckt gegebenenfalls andere Fenster.

Um ein Fenster wieder zu schließen, wird die Funktion ``delwin()`` verwendet,
wobei als Argument wiederum ein Zeiger auf ein Fenster übergeben wird, also
beispielsweise ``delwin(mywin)``. Das Fenster, das nach dem Löschen aktiv
angezeigt werden soll, muss dabei mittels ``wrefresh()`` aktualisiert werden.
Gegebenenfalls muss es dazu erst mittels ``touchwin(win_name)`` zur vollständigen
Aktualisierung vorgemerkt werden, falls ansonsten keine Änderungen vorgenommen
wurden.

..  Centering text:

..  1. Figure out how wide the screen is.
..  2. Figure out how wide your title text is.
..  3. Subtract the title text length from the screen width. The value left over
   ..  needs to be shared equally as spaces on either side of the title.
..  4. Divide the value left over by two. That’s the number of characters to space
   ..  over to center the title.

.. _Unterfenster erstellen:

.. rubric:: Unterfenster erstellen

Neben Fenstern können in Curses auch so genannte Unterfenster erstellt werden.
Diese können dazu verwendet werden, um einen Teil des Hauptfensters leichter
ansteuern oder mit anderen Farb- und Textattributen versehen zu können. Der
Inhalt eines Unterfensters hingegen stimmt mit dem Inhalt des Hauptfensters an
der jeweiligen Stelle überein.

Ein neues Unterfenster kann, ebenso wie mit :ref:`newwin() <newwin()>` ein neues
Fenster erstellt wird, mittels ``subwin()`` erzeugt werden, wobei als erstes
Argument der Name des übergeordneten Fensters und als weitere Argumente die
Anzahl an Zeilen und Spalten sowie die Startposition der oberen linken Ecke
angegeben werden: 

.. code-block:: c

    // Neues Unterfenster erstellen:
    my_subwin = subwin(mywin, nrows, ncols, starty, startx);

    // Alternativ auch möglich:
    my_subwin = derwin(mywin, nrows, ncols, starty, startx);

Die zweite Möglichkeit ein Unterfenster zu erstellen bietet die Funktion
``derwin()``, wobei in diesem Fall die Werte ``starty`` und ``startx`` relativ
zum übergeordneten Fenster (und nicht relativ zum Hauptfenster ``stdscr``)
angegeben werden.

Alle Funktionen, die auf ein "richtiges" Fenster angewendet werden können,
lassen sich auch auf ein Unterfenster anwenden. Unterfenster haben einen eigenen
Cursor und eigene Text- und Farbattribute; sie können selbst wiederum
Ausgangspunkt für neue Unterfenster sein.

Mittels ``delwin(subwindow_name)`` wird ein Unterfenster wieder geschlossen.
Bevor ein (Haupt-)Fenster geschlossen wird, sollten zuerst auf diese Weise alle
Unterfenster geschlossen werden, um Speicherlecks zu vermeiden (die Hauptfenster
haben keine Informationen darüber, ob sie Unterfenster beinhalten und können
diese somit nicht automatisch löschen). Der Inhalt des Subfensters, der dem
Inhalt des Hauptfensters entspricht, bleibt beim Löschen erhalten. [#]_

.. index:: Pad
.. _Pads:

Pads
----

Neben normalen Fenstern gibt es in Curses auch so genannte "Pads". Während die
Funktionen für Pads weitgehend mit den für normale Fenster identisch sind, ist
ihre Größe nicht auf die Größe des Hauptfensters beschränkt; die maximale Größe
eines Pads ist allerdings auf 32767 Zeilen beziehungsweise Spalten beschränkt.

Ein neus Pad wird folgendermaßen erzeugt:

.. code-block:: c

    int nrows = 1000;
    int ncols = 1000;
    WINDOW *mypad;

    // Neues Pad erstellen:
    mypad = newpad(nrows, ncols);

Mittels den für Fenster üblichen Ausgabefunktionen, beispielsweise
``waddstr()``, kann Text auf einem Pad angezeigt werden. Damit die Änderungen
auf dem Bildschirm sichtbar werden, kann allerdings nicht ``wrefresh()``
verwendet werden, da zusätzlich angegeben werden muss, von welcher Stelle aus
das Pad angezeigt werden soll: Üblicherweise ist ein Pad größer als der
Bildschirm, es kann somit nur ein Ausschnitt des Pads angezeigt werden. Dies
wird bei der Funktion ``prefresh()`` berücksichtigt:

.. index:: prefresh()

.. code-block:: c

    prefresh(padname, pad_ymin, pad_xmin, ymin, xmin, ymax, xmax);

Hierbei bezeichnen ``pad_ymin`` und ``pad_xmin`` die Koordinaten der oberen
linken Ecke innerhalb des Pads, von der aus der Inhalt angezeigt werden soll.
Die übrigen Argumente geben die Koordinaten des Bereichs an, in dem das Pad
relativ zum Hauptfenster angezeigt werden soll.

.. index:: Subpad

.. rubric:: Subpads

Ebenso wie Fenster ein oder mehrere Unterfenster haben können, können Pads
auch ein oder mehrere Subpads beinhalten. Ebenso wie bei den Unterfenstern
ist der Inhalt eines Subpads mit dem Hauptpad identisch, das Subpad kann
allerdings beispielsweise eigene Attribute und Farben aufweisen.

Ein neues Subpad kann mittels ``subpad()`` erzeugt werden: [#]_

.. code-block:: c

    int nrows = 1000;
    int ncols = 1000;
    int subrows = 50;
    int subrows = 50;
    WINDOW *mypad, *my_subpad;

    // Neues Pad erstellen:
    mypad = newpad(nrows, ncols);

    // Neues Subpad erstellen:
    // Allgemeine Syntax: subpad(nrows, ncols, starty, startx)
    my_subpad = subpad(mypad, 0, 0, 10, 10);

Bei der Verwendung von Pads und Subpads ist zu beachten, dass diese nicht
innerhalb des Hauptfensters verschoben werden dürfen; die ``mvwin()``-Funktion
kann somit nicht auf Pads angewendet werden. Ebenso sind die
``scroll()``-Funktionen für Pads nicht definiert.

.. Bei Pads verboten: mvwin(), scroll(), scrl(), subwin(), wrefresh(),
.. wnoutrefresh()

.. pechochar(): zeigt buchstaben direkt an, dabei kein prefresh() nötig.

.. pnoutrefresh() and doupdate(): Effizientere Aktualisierungen 

.. wbgd(colorpair)

Mittels ``delwin(padname)`` kann ein (Unter-)Pad wieder gelöscht werden. Auch
hierbei sollten zunächst alle Subpads und erst zuletzt das Hauptpad gelöscht
werden, um Speicherlecks zu vermeiden.


.. _Debugging von Curses-Programmen:

Debugging von Curses-Programmen
-------------------------------

Curses-Programme nutzen die Shell als Ein- und Ausgabefenster; sie lassen sich
daher nicht innerhalb der gleichen Shell aufrufen und mit dem :ref:`gdb
<gdb>`-Debugger analysieren. Folgender Trick schafft hier Abhilfe:

* Man öffnet ein zweites Shell-Fenster und gibt dort ``tty`` ein, um sich die
  Nummer dieser Shell anzeigen zu lassen; das Ergebnis lautet beispielsweise
  ``/dev/pts/23``. Anschließend gibt man in diesem Fenster ``sleep
  1000000000000000000000`` ein, um alle weiteren Eingaben an diese Shell für
  eine lange Zeit zu ignorieren. (Bei Bedarf kann der Schlafmodus mittels ``Strg
  C`` abgebrochen werden.)

* Im ersten Shell-Fenster kann man dann im Projektverzeichnis wie gewohnt ``gdb
  programmname`` eingeben, um den Debugger zu starten. Als erste
  Debugger-Anweisung wird dann der Eingabe-und-Ausgabe-Port des zu debuggenden
  Programms auf den Bezeichner des zweiten Shell-Fensters festgelegt:

  .. code-block:: c
  
      tty /dev/pts/23

  Nun kann ``run`` eingeben werden, um das Programm im Debugger ablaufen zu
  lassen. Die Ausgabe des Programms erfolgt dabei im zweitem Shell-Fenster.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:
    
.. [#] Eine "Spalte" in Curses der Breite eines Textzeichens; die meisten
    Fenster haben daher mehr Spalten als Zeilen. 

.. [#] Für die Größe des Hauptfensters ``stdscr`` sind in Curses auch die
    Makros ``LINES`` und ``COLS`` definiert, die vom Compiler durch die beim
    Programmstart vorliegenden Werte ersetzt werden.

.. Resizing?

.. [#] Die Konstanten ``TRUE`` und ``OK`` beziehungsweise ``FALSE`` sind in der
    Datei ``ncurses.h`` als ``1`` beziehungsweise ``0`` definiert.

.. [#] Mit ``nodelay(stdscr, FALSE)`` kann das ursprüngliche Verhalten von
    ``getch()`` wieder hergestellt werden.

..  http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html

.. [#] Umgekehrt wird allerdings durch Funktionen wie ``wclear()`` der Inhalt
    beim Löschen des Inhalts eines Fensters automatisch auch der Inhalt aller
    Unterfenster gelöscht.

.. [#] Ein Pad kann ein Subpad, aber kein Unterfenster beinhalten. Man kann
    innerhalb eines Pads also mittels ``subpad()`` ein Subpad erzeugen, jedoch
    nicht mittels ``subwin()`` ein Unterfenster.
