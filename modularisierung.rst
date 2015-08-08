.. _Modularisierung:

Modularisierung
===============

Jedes umfangreichere Programm wird normalerweise in mehrere Dateien ("Module")
aufgeteilt. In einem Modul werden zusammengehörige Datenstrukturen und
Funktionen zu einer logischen Einheit kombiniert.

.. index:: Schnittstelle

Jedes Modul besitzt eine Schnittstelle mit "globalen" Variablen und Funktionen und Variablen
des Moduls, auf die auch von einer anderen Datei aus
zugegriffen werden kann. Die anderen Funktionen und Variablen sind "lokal", sie
haben also keine direkten Auswirkungen auf andere Module.

.. ("Application Programming Interface", kurz: "API")
.. Aufnahmekapazität für lokale Funktions- und Variablennamen ("Stack")
.. begrenzt, üblicherweise auf 2048 Bytes.

Jedes Modul sollte möglichst wenig Funktionen oder Variablen in seiner
Schnittstelle definieren, damit Änderungen an lokalen Funktionen keine
Änderungen in anderen Code-Teilen zur Folge haben. Beispielsweise betrifft die
Änderung einer globalen Funktionen bezüglich ihres Namens oder ihrer Anzahl an
Argumenten alle Code-Teile, in denen die Funktion benutzt wird.

.. _Header-Datei:
.. index:: Header-Datei

Die Schnittstelle eines Moduls (einer ``.c``-Datei) wird üblicherweise in einer
gleichnamigen Headerdatei (einer ``.h``-Datei) definiert. In einer solchen Datei
werden Variablen und Funktionen lediglich deklariert, eine Header-Datei enthält
somit keinen ausführbaren Code.

Die Verwendung von Header-Dateien ist dann sinnvoll, wenn eine Variable oder
eine Funktion von mehreren Dateien aus benutzt werden soll.

..  In C sind alle Variablen global, die nicht explizit als lokal (``static``)
..  definiert werden. In einem anderen Modul definierte Variablen müssen in jedem
..  Modul in dem sie verwendet werden als extern deklariert werden (Geschieht
..  normalerweise durch Einbinden der Headerdatei):

..  .. code-block:: c

    ..  extern int globalvar;   // Reserviert keinen Speicherplatz;
    ..  extern float f;         // die Variable ist in einem anderen Modul 

..  Üblicherweise wird das Schlüsselwort extern in Headerdateien (.h) verwendet und
..  nicht innerhalb der Implementationsdatei (.c).

..  In C sind alle Funktionen global, wenn sie nicht explizit als lokal (static) definiert werden.
..  Funktionen, die in einem anderen Modul definiert sind, sollten in jedem Modul in
..  dem sie verwendet werden als externer Prototyp aufgeführt werden (extern
..  deklariert werden) :

..  .. code-block:: c

    ..  extern int f1(int a, int b) // Funktion ist woanders definiert 


..  Wird eine Header-Datei doppelt oder mehrfach in ein Modul eingebunden ( direkt
..  und indirekt), so kann dies zu Problemen führen.

..  Unterprogramme aus zusammenhängenden Aufgabengebieten werden in sogenannten
..  Bibliotheken (engl. libraries) zusammengefasst


