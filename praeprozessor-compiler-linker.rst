
.. _Präprozessor, Compiler und Linker:

Präprozessor, Compiler und Linker
=================================

Ein klassischer C-Compiler besteht aus drei Teilen: Einem Präprozessor, dem
eigentlichen Compiler, und einem Linker: 

* Der Präprozessor bereitet einerseits den Quellcode vor (entfernt
  beispielsweise Kommentare und Leerzeilen); andererseits kann er mittels der im
  nächsten Abschnitt näher beschriebenen Präprozessor-Anweisungen Ersetzungen im
  Quellcode vornehmen.
* Der Compiler analysiert den Quellcode auf lexikalische oder syntaktische
  Fehler, nimmt gegebenenfalls Optimierungen vor und wandelt schließlich die
  aufbereiteten Quellcode-Dateien in binäre Objekt-Dateien (Endung: ``.o``) um.
* Der Linker ergänzt die Objekt-Dateien um verwendete Bibliotheken und setzt
  die einzelnen Komponenten zu einem ausführbaren Gesamt-Programm zusammen.

.. Syntax-Prüfer im Compiler: "Parser" (Goll 94f).

.. index:: Präprozessor
.. _Präprozessor-Anweisungen:

Präprozessor-Anweisungen
------------------------

Der Präprozessor lässt sich im Wesentlichen durch zwei Anweisungen steuern, die
jeweils durch ein Hash-Symbol ``#`` zu Beginn der Anweisung gekennzeichnet sind
und ohne einen Strichpunkt abgeschlossen werden:

.. _#include:
.. index:: #include

``#include`` -- Einbinden von Header-Dateien
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Mittels ``#include`` können weitere Quellcode-Teile in das Programm
integriert werden. Diese Dateien werden vom Präprozessor eingelesen und an
Stelle der ``#include``-Anweisung in die Datei geschrieben.

Unterschieden wird bei ``#include``-Anweisungen zwischen Bibliotheken, die sich
in einem Standardpfad im System befinden und dem Compiler bekannt sind, und
lokalen :ref:`Header-Dateien <Header-Datei>`, die sich üblicherweise im gleichen
Verzeichnis befinden. Die Bibliotheken aus dem Standard-Pfad erhalten um ihren
Namen eckige Klammern, die Namen der lokalen Header-Dateien werden in doppelte
Anführungszeichen gesetzt:

.. code-block:: c

    // Standard-Bibliothek stdio.h importieren:
    #include <stdio.h>

    // Lokale Header-Datei input.h importieren:
    #include "input.h"

.. index:: #define
.. _#define:

``#define`` -- Definition von Konstanten und Makros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mittels ``#define`` können Konstanten oder Makros definiert werden. Bei der
Definition einer Konstanten wird zunächst der zu ersetzende Name anschließend
der zugehörige Wert angegeben:

.. code-block:: c

    #define HALLO "Hallo Welt!"
    #define PI 3.1415 

Eine Großschreibung der Konstantennamen ist nicht zwingend nötig, ist in der
Praxis jedoch zum Standard geworden, um Konstanten- von Variablennamen
unterscheiden zu können. Nicht verwendet werden dürfen allerdings folgende
Konstanten, die im Präprozessor bereits vordefiniert sind:

* ``__LINE__``: Ganzzahl-Wert der aktuellen Zeilennummer 
* ``__FILE__``: Zeichenkette mit dem Namen der kompilierten Datei
* ``__DATE__``: Zeichenkette mit aktuellem Datum 
* ``__TIME__``: Zeichenkette mit aktueller Uhrzeit

Eine Festlegung mittels ``#define`` bleibt allgemein bis zum Ende der
Quelldatei bestehen. Soll eine erneute Definition einer Konstanten ``NAME``
erfolgen, so muss die bestehende Definition erst mittels ``#undef NAME``
rückgängig gemacht werden.

.. index::  Makro 
.. _Makro:

Bei der Definition eines Makros mittels ``#define`` wird zunächst der Name des
Makros angegeben. In runden Klammern stehen dann, wie bei der Definition einer
:ref:`Funktion <Funktionen>`, die Argumente, die das Makro beim Aufruf
erwartet. [#]_ Unmittelbar anschließend wird der Code angegeben, den das Makro
ausführen soll.


.. code-block:: c

    #define QUADRAT(x) ((x)*(x))

Bei der Definition von Makros muss beachtet werden, dass der Präprozessor die
Ersetzungen nicht wie ein Taschenrechner oder Interpreter, sondern wie ein
klassischer Text-Editor vornimmt. Steht im Quellcode beispielsweise die Zeile
``result = QUADRAT(n)``, so wird diese durch den Präprozessor gemäß dem obigen
Makro zu ``result = ((n)*(n))`` erweitert. In diesem Fall erscheinen die
Klammern als unnötig. Steht allerdings im Quellcode die Zeile ``result =
QUADRAT(n+1)``, so wird diese mit Hilfe der Klammern zu ``((n+1)*(n+1))``
erweitert. Ohne die zusätzlichen Klammern in der Makro-Definition würde der
Ausdruck zu ``n+1*n+1`` erweitert werden, was ein falsches Ergebnis liefern
würde.

Innerhalb von Makro-Definitionen kann ein spezieller Operatoren verwendet
werden: Der Operator ``#`` kann auf einen Argumentnamen angewendet werden und
setzt den Namen der konkret angegebenen Variablen in doppelte Anführungszeichen:
[#]_

.. code-block:: c

    #define QUADRAT(x) print("Der Quadrat-Wert von %s ist %i.\n", #x, (x)*(x))

Ein Minimalbeispiel für dieses Makro könnte folgendermaßen aussehen:

.. code-block:: c

    // Datei: makro-beispiel-1
    // Compilieren: gcc -o makro-beispiel-1 makro-beispiel-1
    // Aufruf: ./makro-beispiel-1

    // Ergebnis beim Aufruf: Der Quadrat-Wert von num ist 121.

    #include <stdio.h>

    #define QUADRAT(x) printf("Der Quadrat-Wert von %s ist %i.\n", #x, (x)*(x))

    void main()
    {
        int num=11;

        QUADRAT(num);
    }

Ist eine ``#define``-Anweisung zu lange für eine einzelne Code-Zeile, so kann
die Anweisung an einer Whitespace-Stelle mittels ``\`` unterbrochen und in der
nächsten Zeile fortgesetzt werden. Eventuelle Einrückungen (Leerzeichen,
Tabulatoren) werden dabei vom Präprozessor automatisch entfernt.

Ein entscheidender Vorteil von ``#define``-Anweisungen ist, dass so definierte
Konstanten oder Makros an beliebigen Stellen im Code eingesetzt werden können
und zugleich bei Bedarf nur an einer einzigen Stelle im Programm geändert
werden müssen.
  
.. _#ifdef:
.. index:: #if, #ifdef, #ifndef

``#if``, ``#ifdef``, ``#ifndef`` -- Bedingte Compilierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mittels ``#if``, ``#ifdef`` oder ``#ifndef`` können Teile einer Datei zur
"bedingten Compilierung" vorgemerkt werden. Ein solcher Code-Teil wird nur
dann vom Compiler berücksichtigt, wenn die angegebene Bedingung erfüllt ist.

Beispielsweise kann auf diese verhindert werden, dass Header-Dateien oder
Quellcode-Bibliotheken mehrfach geladen werden. Beispielsweise kann man in
einer Header-Datei ``input.h`` gleich zu Beginn prüfen, ob eine Konstante
``INPUT_H`` definiert ist. Falls nicht, so kann wird der folgende Code
berücksichtigt, wobei darin auch die Konstante ``INPUT_H`` mit dem Wert ``1``
definiert wird: 

.. code-block:: c

    // Datei: input.h

    #ifndef INPUT_H

    #define INPUT_H = 1

    // ... eigentlicher Inhalt ...

    //#endif

Die Variable ``INPUT_H`` ist nur beim ersten Versuch, die Datei mittels
``#include`` zu importieren, nicht definiert. Ein mehrfaches Importieren wird
somit verhindert. Ebenso kann beispielsweise mittels ``#ifdef DEBUG`` ein
Code-Teil nur zu Testzwecken eingefügt werden (der durch eine Zeile ``#define
DEBUG 1`` am Beginn der Datei aktiviert wird). Es kann auch ein Teil eines
Codes nur in Abhängigkeit von einer Versionsnummer ausgeführt werden,
indem beispielsweise ``#if VERSION < 1.0`` geprüft wird.

Ob weitere Präprozessor-Anweisungen vom Compiler unterstützt werden, hängt von
dessen Version und vom konkreten Betriebsystem ab. Üblicherweise werden daher
nur die oben genannten Anweisungen verwendet.

..  #pragma
..  #line
..  #error

.. _Compiler-Optionen:

Compiler-Optionen
-----------------

Der Standard-C-Compiler kann mit einer Vielzahl an Optionen aufgerufen werden,
mit denen der Compilier-Ablauf gesteuert werden kann. Möchte man beispielsweise
lediglich überprüfen, welche Ersetzungen vom Präprozessor vorgenommen wurden,
aber den Quellcode nicht kompilieren, so kann die Option ``-E`` verwendet
werden:

.. code-block:: bash

    gcc -E -o mycode.i mycode.c

In diesem Beispiel wird die Ausgabe, die der Präprozessor bei der Verarbeitung
der Datei ``mycode.c`` erzeugt, in die Datei ``mycode.i`` geschrieben. Mit der
Option ``-o`` ("output") wird bei ``gcc`` allgemein der Name der Ausgabedatei
angegeben.
    

.. _Verlinken von Bibliotheken:

Verlinken von Bibliotheken
--------------------------

Jeder Compiler bringt mehrere so genannte Bibliotheken ("Libraries") mit sich.
Diese enthalten fertige Funktionen in bereits compilierter Form, die von anderen
C-Programmen genutzt werden können. Der Linker sucht die benötigten Funktionen
aus den Bibliotheken heraus und fügt sie dem zu compilierenden Programm hinzu.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Zu beachten ist, dass bei der Definition eines Makros kein Leerzeichen
    zwischen dem Makronamen und der öffnenden runden Klammer der
    Argumentenliste vorkommen darf. Der Präprozessor würde ansonsten den
    Makronamen als Namen einer Konstanten interpretieren und den geamten Rest
    der Zeile als Wert dieser Konstanten interpretieren. 

.. [#] Zudem können mit dem zweiten möglichen Makro-Operator ``##`` die Namen
    von zwei oder mehreren übergebenen Argumenten zu einer neuen Bezeichnung
    verbunden werden. Dieser Operator wird allerdings nur sehr selten
    eingesetzt.

