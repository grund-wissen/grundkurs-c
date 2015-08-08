Einführung: Editieren und Übersetzen
=====================================

Um ein lauffähiges C-Programm zu erzeugen, muss zunächst mit einem Texteditor
eine Quelltext-Datei angelegt und mit Code gefüllt werden. Anschließend wird
ein Compiler gestartet, der den Quellcode in Maschinen-Code übersetzt und ein
lauffähiges Programm erstellt.

Als klassisches Beispiel soll hierzu ein minimales Programm dienen, das
lediglich ``"Hallo, Welt!"`` auf dem Bildschirm ausgibt. Hierzu wird mit einem
Texteditor folgender Code in eine (neue) Datei ``hallo.c`` geschrieben:

.. code-block:: c

    // Datei: hallo.c                   /* 1. */

    #include <stdio.h>                  /* 2. */

    void main()                         /* 3. */
    {
        printf("Hallo, Welt!\n");       /* 4. */
    }

Das obige Programm enthält folgende Komponenten:

.. index:: Kommentar

#. Eine mit ``//`` eingeleitete Zeile am Dateianfang stellt einen Kommentar dar.
   Sie wird beim Übersetzen durch den Compiler ignoriert und dient lediglich
   der besseren Lesbarkeit. Ebenso werden Textbereiche, die durch ``/*`` und
   ``*/`` begrenzt sind, als Kommentare für Erklärungen oder Hinweise genutzt.
   [#KOM]_

#. Mit der Anweisung ``#include <stdio.h>`` wird dem Compiler mitgeteilt, die
   Standard-Input-Output-Bibliothek ``stdio.h`` zu laden. [#PRAE]_ Diese von vielen
   C-Programmen genutzte "Sammlung" an Quellcode stellt u.a. Funktionen für die
   Ausgabe von Text auf dem Bildschirm bereit.

#. Die Funktion ``main()`` startet das Hauptprogramm, das sich innerhalb der
   folgenden geschweiften Klammern befindet. Jedes C-Programm verfügt über
   eine derartige ``main()``-Funktion. [#VOID]_ 

#. Durch den Aufruf der Funktion ``printf()`` wird auf dem Bildschirm der in
   doppelten Hochkommatas stehende Text ausgegeben. Die Zeichenfolge ``\n``
   steht dabei als Zeichen für eine neue Zeile. Der Aufruf der Funktion muss,
   wie jede C-Anweisung, mit einem Strichpunkt ``;`` beendet werden.

Um die Datei in lauffähigen Maschinen-Code zu übersetzen, wechselt man in einer
Shell in den Ordner der Quellcode-Datei und ruft den Compiler ``gcc`` auf:

.. code-block:: bash

    gcc hallo.c -o hallo

Durch die Option ``-o hallo`` wird dabei die Output-Datei, d.h. das fertige
Programm, mit ``hallo`` benannt. Ist der Compilier-Vorgang abgeschlossen, kann
das neu geschriebene Programm im gleichen Ornder aufgerufen werden:

.. code-block:: bash

    ./hallo

    # Ergebnis: Hallo, Welt!

Damit ist das erste C-Programm fertig gestellt. In den folgenden Abschnitten
werden weitere Eigenschaften und Funktionen der Programmiersprache C erläutert
sowie einige nützliche Werkzeuge und Programmiertechniken vorgestellt.

..  Syntax-Prüfung, d.h. Test, ob grammatikalische Regeln eingehalten wurden.

.. raw:: html

    <hr />
    
.. only:: html

    .. rubric:: Anmerkungen:

.. [#KOM] In vielen Programmen werden ausschließlich Kommentare verwendet, die
    mit den Zeichenfolgen ``/*`` und ``*/`` begrenzt sind. Hierdurch wird eine
    Kompatibilität mit alten C-Compiler-Versionen sicher gestellt. Im obigen
    Tutorium wird hingegen -- nach persönlichem Geschmack -- die
    ``//``-Variante für (einzeilige) Kommentare verwendet. 

    Zusätzliche Kommentare der Form ``/* 1. */`` dienen in diesem Tutorium als
    Marker, um im Text auf die jeweiligen Stellen im Quellcode eingehen zu
    können.

.. [#PRAE] Genauer gesagt gilt die Anweisumg dem Präprozessor, einem Teil des
    Compilers.

.. [#VOID] Die Bezeichung ``void`` besagt lediglich, dass die Funktion keinen
    Rückgabe-Wert liefert, der anderweitig im Programm zu verwenden wäre.

