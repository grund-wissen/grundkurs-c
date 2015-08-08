
.. _Kontrollstrukturen:

Kontrollstrukturen
==================

Im folgenden Abschnitt werden die grundlegenden Kontrollstrukturen vorgestellt,
mit denen sich der Ablauf eine C-Programms steuern lässt.

.. index:: if
.. _if:
.. _Bedingte Anweisungen:

``if``, ``elif`` und ``else`` -- Bedingte Anweisungen
-----------------------------------------------------

Mit Hilfe des Schlüsselworts ``if`` kann an einer beliebigen Stelle im Programm
eine Bedingung formuliert werden, so dass die Anweisung(en) im unmittelbar
folgenden Code-Block nur dann ausgeführt werden, sofern die Bedingung einen
wahren Wert (ungleich Null) ergibt. 

Eine ``if``-Anweisung ist also folgendermaßen aufgebaut:

.. code-block:: c

    if (Bedingung) 
    {
        Anweisungen
    }
    
In den runden Klammern können mittels der logischen Verknüpfungsoperatoren
``and`` beziehungsweise ``or`` mehrere Teilbedingungen zu einer einzigen
Bedingung zusammengefügt werden. Bei einer einzeiligen Anweisung können die
geschweiften Klammern weggelassen werden. Liefert die Bedingung den Wert Null,
so wird der Anweisungsblock übersprungen und das Programm fortgesetzt.

.. index:: else

Eine ``if``-Anweisung kann um den Zusatz ``else`` erweitert werden. Diese
Konstruktion wird immer dann verwendet, wenn man zwischen *genau* zwei
Alternativen auswählen möchte.

.. code-block:: c

    if (Bedingung) 
    {
        Anweisungen
    }
    else 
    {
        Anweisungen
    }
    
Der Vorteil einer ``if-else``-Bedingung gegenüber der Verwendung zweier
``if``-Anweisungen besteht darin, dass nur einmalig eine Bedingung getestet wird
und das Programm somit schneller ausgeführt werden kann. 

.. index:: else if

Soll neben der ``if``-Bedingungung eine (oder mehrere) weitere Bedingung
getestet werden, so kann dies mittels des kombinierten Schlüsselworts ``else
if`` geschehen. Die ``else if``-Anweisungen werden nur dann ausgeführt, wenn die
``if``-Bedingung falsch und die ``elif``-Bedingung wahr ist.

.. code-block:: c

    if (Bedingung_1) 
    {
        Anweisungen
    }
    else if (Bedingung_2)
    {
        Anweisungen
    }
    
Allgemein können in einer ``if``-Struktur mehrere ``else if``-Bedingungen, aber
nur ein ``else``-Block vorkommen. 


.. index:: switch, case, default
.. _case:
.. _Fallunterscheidungen:

``switch`` -- Fallunterscheidungen
----------------------------------

Mittels des Schlüsselworts ``switch`` kann in C eine Fallunterscheidung
eingeleitet werden. Hierbei wird der nach dem Schlüsselwort ``switch`` in runden
Klammern angegebene Ausdruck ausgewertet, und in Abhängigkeit des sich
ergebenden Werts einer der folgenden Fälle ausgewählt:

.. code-block:: c

    switch (Ausdruck)
    {
        case const_1:
            Anweisungen_1

        case const_2:
            Anweisungen_2

        ...

        default:
            Default-Anweisungen

    }

Bei den Konstanten, mit denen der Wert von ``Ausdruck`` verglichen wird, muss es
sich um ``int``- oder ``char``-Werte handeln, die nicht mehrfach vergeben werden
dürfen. Trifft kein ``case`` zu, so werden die unter ``default`` angegebenen
Anweisungen ausgeführt.

Trifft ein ``case`` zu, so werden die angegebenen Anweisungen ausgeführt,
anschließend wird der ``Ausdruck`` mit den übrigen ``case``-Konstanten
verglichen. Möchte man dies vermeiden, so kann man am Ende der
``case``-Anweisungen die Anweisung ``break;`` einfügen, die einen Abbruch der
Fallunterscheidung an dieser Stelle zur Folge hat.

In C ist es auch möglich Anweisungen für mehrere ``case``-Werte zu definieren.
Die Syntax dazu lautet:

.. code-block:: c

    switch (Ausdruck)
    {
        case const_1:
        case const_2:
        case const_3:
            Anweisungen

        ...
    } 

In diesem Fall werden die bei ``case const_3`` angegebenen Anweisungen auch
aufgerufen, wenn die Vergleiche ``case const_1`` oder ``case const_2``
zutreffen.


.. index:: for
.. _for:
.. _Schleifen:

``for`` und ``while`` -- Schleifen
----------------------------------

Eine ``for``-Schleife ist folgendermaßen aufgebaut:

.. code-block:: c

    for ( Initialisierung; Bedingung; Inkrementierung )
    {
        Anweisungen
    }

Gelangt das Programm zu einer ``for``-Schleife, so werden nacheinander folgende
Schritte ausgeführt:

* Zunächst wird der Initialisierungs-Ausdruck ausgewertet. Dieser ist
  üblicherweise eine Zuweisung, die eine Zählvariable auf einen bestimmten Wert
  setzt.

* Als nächstes wird der Bedingungs-Ausdruck wird ausgewertet. Dieser ist
  normalerweise ein relationaler Ausdruck (Vergleich).

  Wenn die Bedingung falsch ist, so wird die ``for``-Schleife beendet, und das
  Programm springt zur nächsten Anweisung außerhalb der Schleife. 

  Wenn die Bedingung wahr ist, so werden die im folgenden
  Block angegebenen Anweisung(en) ausgeführt.

* Nach der Ausführung der Anweisungen wird der Inkrementierungs-Ausdruck
  ausgewertet; hierbei wird beispielsweise die Zählvariable oder der Index eines
  Arrays mit jedem Schleifendurchlauf um :math:`1` erhöht. Anschließend wird
  wiederum der Bedingungs-Ausdruck geprüft und gegebenenfalls die Ausführung der
  Schleifenanweisungen fortgesetzt.

Innerhalb einer ``for``-Anweisung können weitere ``for``-Anweisungen auftreten,
so dass auch über mehrere Zählvariablen iteriert werden kann. Bei einer nur
einzeiligen Anweisung können die geschweiften Klammern weggelassen werden.

.. index:: break, continue
.. _break:
.. _continue:

Soll eine Schleife vorzeitig beendet werden, so kann dies mittels des
Schlüsselworts ``break`` erreicht werden: Trifft das Programm auf diese
Anweisung, so wird die Schleife unmittelbar beendet. [# ] Möchte man die
Schleife nicht beenden, sondern nur den aktuellen Schleifendurchgang
überspringen, so kann man das Schlüsselwort ``continue`` verwenden. Trifft das
Programm auf diese Anweisung, so wird der aktuelle Schleifendurchgang beendet,
und das Programm fährt mit dem nächsten Schleifendurchgang fort.

Üblicherweise werden ``for``-Schleifen verwendet, um mittels der Zählvariablen
für eine bestimmte Anzahl von Durchläufen zu sorgen. Ist zu Beginn der Schleife
nicht bekannt, wie häufig der folgende Anweisungsblock durchlaufen werden soll,
wird hingegen meist eine ``while``-Schleife eingesetzt.

.. index:: while
.. _while:

Eine ``while``-Schleife ist folgendermaßen aufgebaut:

.. code-block:: c

    while ( Bedingung )
    {
        Anweisungen
    }

Eine ``while``-Schleife führt einen Anweisungsblock aus, solange die angegebene
Bedingung wahr (nicht Null) ist. Das Programm wertet dabei zunächst den als
Bedingung angegebenen Ausdruck aus, und nur falls dieser einen von Null
verschiedenen Wert liefert, wird der Anweisungsblock ausgeführt. Ergibt der als
Bedingung angegebene Ausdruck bereits bei der ersten Auswertung den Wert Null,
so wird die ``while``-Schleife übersprungen, ohne dass der Anweisungsblock
ausgeführt wird.

Häufig werden ``while``-Schleifen als Endlos-Schleifen verwendet, die einen
(zunächst) wahren Ausdruck als Bedingung verwenden. Unter einer bestimmten
Voraussetzung wird dann mittels einer ``if``-Anweisung innerhalb des
Schleifenkörpers entweder der Bedingungsaustruck auf den Wert Null gesetzt oder
die Schleife mittels ``break`` beendet.  

.. _do-while:
    
Soll eine gewöhnliche ``while``-Schleife, unabhängig von ihrer Bedingung,
mindestens einmal ausgeführt werden, so wird in selteneren Fällen
eine ``do-while``-Schleife eingesetzt. Eines solche Schleife ist folgendermaßen
aufgebaut:
    
.. code-block:: c

    do
    {
        Anweisungen
    } while ( Bedingung )

Da es stets möglich ist, eine ``do-while``-Schleife auch mittels einer
``while``-Schleife zu schreiben, werden letztere wegen ihrer besseren
Lesbarkeit meist bevorzugt.




