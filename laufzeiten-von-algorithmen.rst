
Laufzeiten von Algorithmen
==========================

Bisweilen können für die selbe Aufgabe mehrere Lösungen gefunden werden, die
sich teilweise jedoch erheblich in ihrer Effizienz unterscheiden. Bei der
Effizienz-Analyse eines Algorithmus, also  eines "Rezepts" zur Lösung eines
Problems, ist es insbesondere von Interesse, wie sich die Laufzeit in
Abhängigkeit von der Anzahl :math:`n` der zu bearbeitenden Daten ändert.

Zur Analyse von Laufzeiten sind prinzipiell zweierlei Vorgehensweisen möglich:

* Mittels eines *Benchmarks* wird ein Programm oder Algorithmus mit einem
  möglichst typischen Satz an Daten aufgerufen und dabei die benötigte Zeit
  gemessen. 

  Ein Werkzeug, das hierfür unter Linux genutzt werden kann, ist :ref:`gprof
  <gprof>`. Dieses Programm misst nicht nur die Laufzeit eines Programms und der
  im Programmverlauf aufgerufenen Funktionen, sondern zählt auch, wie häufig die
  einzelnen Funktionen aufgerufen wurden. Damit erhält man einen guten
  Überblick, welche Funktionen für eine weitergehende Analyse "wichtig" sind. 

* Mit einer *Laufzeit-Analyse* kann anhand der Struktur des Quellcodes,
  beispielsweise anhand der Anzahl an Schleifendurchläufen, Lese- oder
  Schreibvorgängen, die Größenordnung der Laufzeit eines Algorithmus in
  Abhänigkeit von der Anzahl :math:`n` an zu bearbeiteten Daten abgeschätzt
  werden.

.. _Big-O-Notation:

Die "Big-O"-Notation
--------------------

Wie lange die Ausführung eines Algorithmus tatsächlich benötigt, hängt nicht
zuletzt von der Rechenleistung des Computers ab, auf dem der Code ausgeführt
wird; Benchmarks müssen daher auf einem einheitlichen System durchgeführt und
unter Angabe der Rechnerleistung (CPU, RAM, usw.) angegeben werden. Allgemeinere
Vergleiche sind hingegen möglich, welche die Laufzeit :math:`t` eines
Algorithmus allgemein als Funktion :math:`t(n)` des Datenumfangs :math:`n`
ausgedrückt wird. Wird beispielsweise im Verlauf eines Programms eine Funktion
mit einer konstanten Laufzeit :math:`c` insgesamt :math:`n` mal aufgerufen, so
ergibt sich dadurch eine Laufzeit von :math:`t(n) = c \cdot n`.

Beim Zählen von Laufzeiten wird üblicherweise die vereinfachende Vereinbarung,
dass die folgenden Prozess-Schritte zur Ausführung jeweils eine Zeiteinheit
benötigen:

* Jede Wertzuweisung 
* Jeder Wertevergleich 
* Jede Iteration einer Schleifenvariablen


.. Durchschnitt und Worst-Case

.. merge-sort viel schneller als selection sort

... to be continued ...
