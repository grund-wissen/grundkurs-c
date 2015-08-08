
.. _Dateien und Verzeichnisse:

Dateien und Verzeichnisse
=========================

Jede Ein- und Ausgabe von Daten erfolgt in C über Datenkanäle ("Files"). Beim
Programmstart werden automatisch die Standard-Files ``stdin``, ``stdout`` und
``stderr`` geöffnet und mit dem Bildschirm verknüpft. Somit muss in Programmen
nur die Standard-Bibliothek :ref:`stdio.h <stdio.h>` eingebunden werden, damit
Daten beispielsweise mittels :ref:`printf() <printf()>` auf dem Bildschirm
ausgegeben oder mittels :ref:`scanf() <scanf()>` von der Tastatur eingelesen
werden können. [#]_


.. index:: File-Pointer, Stream
.. _Dateien und File-Pointer:

Dateien und File-Pointer
------------------------

Auf Dateien wird in C grundsätzlich über ``FILE``-Objekte zugegriffen: Sämtliche
Datenfunktionen benötigen oder liefern einen Zeiger auf ein solches Objekt. Am
Anfang der Quellcode-Datei muss also zunächst ein solcher File-Pointer,
bisweilen auch "Stream" genannt, definiert werden:

.. code-block:: c

    #include <stdio.h> 

    FILE *fp;

Um eine Datei zu öffnen, wird die Funktion ``fopen()`` verwendet. Als erstes
Argument wird hierbei der Pfadname der zu öffnenden Datei übergeben, als zweites
ein Zeichen, das den Zugriffsmodus auf die Datei angibt:

* ``"r"``: Textdatei zum Lesen öffnen
* ``"w"``: Textdatei zum Schreiben neu erzeugen (gegebenenfalls alten Inhalt
  wegwerfen) 
* ``"a"``: Text anfügen; Datei zum Schreiben am Dateiende öffnen oder erzeugen 
* ``"r+"``: Textdatei zum Ändern öffnen (Lesen und Schreiben) 
* ``"w+"``: Textdatei zum Ändern erzeugen (gegebenenfalls alten Inhalt wegwerfen) 
* ``"a+"``: Datei neu erzeugen oder zum Ändern öffnen und Text anfügen
  (Schreiben am Ende)

Als Ergebnis gibt ``fopen()`` einen File-Pointer auf die Datei zurück, oder
``NULL``, falls beim Öffnen ein Fehler aufgetreten ist. 

.. code-block:: c

    fp = fopen("/path/to/myfile","r");

    if (fp == NULL)
        fprintf(stderr,"Datei konnte nicht geoeffnet werden.\n");

Wird der Zugriff auf eine Datei nicht mehr benötigt, so sollte sie mittels
``fclose()`` wieder geschlossen werden. Hierbei muss als Argument der zur
geöffneten Datei gehörende File-Pointer angegeben werden, also beispielsweise
``fclose(fp)``. Bei einem Schreibzugriff ist das Schließen einer Datei mittels
``fclose()`` Pflicht, da hierdurch unter anderem die Modifikationszeit der
Datei aktualisiert wird.

.. rubric:: Existenz einer Datei prüfen

In C gibt es keine eigenständige Funktion, um die Existenz einer Datei zu
prüfen. Man kann allerdings die Funktion ``fopen()`` auch zu diesem Zweck
nutzen:

.. code-block:: c

    // Existenz einer Datei prüfen
    // Rückgabewert: 1 falls Datei existiert, 0 sonst.
    int file_exists(char *filename)
    {
        FILE *fp;
        int result;

        fp = fopen(filename, "r");
        if (fp == NULL)
        {
            result = 0;
        } 
        else
        {
            result = 1;
            fclose(fp);
        }

        return result;
    }

Hierbei wurde als Zugriffsmodus ``"r"`` gewählt, da die Datei nicht verändert
werden soll und die Methode auch mit schreibgeschützten Dateien funktionieren
soll. Die Rückgabewerte wurden im obigen Beispiel so gewählt, damit sie an einer
anderen Stelle im Code innerhalb einer ``if``-Abfrage genutzt werden können.


.. _Daten in eine Datei schreiben:

Daten in eine Datei schreiben
-----------------------------

Wie bereits im Abschnitt :ref:`Ausgabe und Eingabe <Ausgabe und Eingabe>`
beschrieben wurde, gibt es in C mehrere Möglichkeiten, um Daten von der
Tastatur beziehungsweise vom Bildschirm ("stdin") einzulesen. Ebenso gibt es in
C mehrere Möglichkeiten, um Inhalte aus Dateien einzulesen oder dorthin zu
schreiben. Die einzelnen Funktionen sind dabei den bereits behandelten
Funktionen sehr ähnlich.

.. rubric:: ``fprintf()`` -- Daten formatiert schreiben

Mit ``fprintf()`` können normale Zeichenketten, Sonderzeichen und Werte von
Variablen mittels Platzhaltern in formattierter Weise in eine Datei geschrieben
werden. Die Syntax entspricht dabei derjenigen von :ref:`printf() <printf()>`,
wobei als erstes Argument der Name eines File-Pointers angegeben werden muss:

.. code-block:: c

    FILE *fp;

    // Datei öffnen:
    fp = fopen(filename, "w");

    // Daten schreiben:
    fprintf(fp, "Teststring!\n");

    // Datei schließen:
    fclose(fp);

Sollen bei der Verwendung von ``fprintf()`` mehrere Zeilen auf einmal
geschrieben werden, so müssen diese mittels des Neue-Zeile-Zeichens ``\n``
getrennt werden. Am Ende des Schreibvorgangs muss die Datei wieder mittels
``fclose()`` geschlossen werden, damit die Modifikationszeit angepasst wird.

.. rubric:: ``fputs()`` -- Einzelne Zeichenketten schreiben

Mit ``fputs()`` können normale Zeichenketten in eine Datei geschrieben werden.
Sonderzeichen in den Zeichenketten sind erlaubt, ein Ersetzen von Platzhaltern
durch Werte von Variablen hingegen nicht. 

.. rubric:: ``fputc()`` -- Einzelne Zeichen schreiben

.. In identischer Weise wie ``fputc()`` kann auch die Funktion ``putc()``
.. verwendet werden; diese unterscheidet sich nur in ihrer Implementierung von
.. ``fputc()``. Die meisten Programmierer verwenden allerdings ``fputc()``


..  frwrite     Schreibt Datenblock in das File



.. _Daten aus einer Datei einlesen:

Daten aus einer Datei einlesen
------------------------------

Auch die Funktionen zum Einlesen von Daten aus einer Datei ähneln denen im
Abschnitt :ref:`Ausgabe und Eingabe <Ausgabe und Eingabe>` beschriebenen
Funktionen zum Einlesen von Daten vom Bildschirm.

.. rubric:: ``fgetc()`` -- Daten zeichenweise einlesen

Die Funktion ``fgetc()`` liest ein einzelnens Zeichen aus einer Datei ein und
gibt es als ``int``-Wert zurück. Vor Verwendung von ``fgetc()`` muss wiederum
zunächst ein File-Pointer mittels :ref:`fopen() <fopen()>` bereitgesetellt
werden:

Die Funktion ``fgetc()`` wird häufig in Verbindung mit einer ``while``-Schleife
eingesetzt, wobei als Abbruchfunktion die Funktion ``feof()`` genutzt wird:
Diese prüft, ob der angegebene File-Pointer auf das Ende der Datei zeigt und
gibt in diesem Fall einen Wert ungleich Null zurück.


..  ferror      Prüft Fehlerbedingungen


..  feof        Prüft ob Ende des Files erreicht ist
..  ftell       Postion des Datenzeigers lesen
..  fgetpos     Position des Filezeigers ermitteln
..  fseek       Datenzeiger auf neue Position setzen

..  fread       Liest Datenblock aus dem File
..  fscanf      Daten formatiert aus File lesen
..  fflush      Ausgabepuffer leeren
..  fgetc       Ein Zeichen vom File lesen (Funktion)
..  fgets       String aus einem File lesen
..  getc        Ein Zeichen vom File lesen (Makro)

..  Fclose      File schliessen

.. EOF

.. Zugriffsfunktionen Krucker 91

.. while ( ( grade = getchar() ) != EOF )

..  
    fputc(int c, FILE *stream) schreibt das als unsigned char interpretierte
    Zeichen ``c`` in den angegebenen Stream.
    Bei einer fehlerfreien Ausfuehrung liefert es das Zeichen ``c`` als
    Rueckgabewert zurueck, andernfalls EOF. Im letzteren Fall wird das
    Error-Flag fuer den stream gesetzt.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Programme, deren einzige Aufgabe darin besteht, Daten vom Bildschirm
    einzulesen, zu verarbeiten, und wieder auf dem Bildschirm auszugeben, werden
    bisweilen auch als "Filter" bezeichnet. Derartige Programme können unter
    Linux mittels des :ref:`Pipe-Zeichens <gwl:Pipelines>` verbunden werden,
    beispielsweise kann so in einer Shell ``programm_1 | programm_2 |
    programm_3`` eingegeben werden. 


