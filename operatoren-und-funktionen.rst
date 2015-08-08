.. _Operatoren und Funktionen:

Operatoren und Funktionen
=========================

.. index:: Operator
.. _Operatoren:

Operatoren
----------

Mit einem :ref:`Operator <gwm:Operationen>` werden üblicherweise zwei Aussagen
oder Variablen miteinander verknüpft. Ist die Anwendung des Operators für die
angegebenen Variablen erlaubt, so kann dieser -- je nach Operator -- einen
einzelnen Rückgabewert als Ergebnis liefern. Beispielsweise wird durch den
:ref:`Zuweisungsoperator <Zuweisungsoperator>` ``=`` das Ergebnis des Ausdrucks
auf der rechten Seite in der links vom Istgleich-Zeichen stehende Variablen
gespeichert.

In C existieren auch Operatoren, die nur auf eine einzelne Variable angewendet
werden, beispielsweise der :ref:`Adressoperator <Adressoperator>` ``&``, der die
Speicheradresse einer Variablen oder einer Funktion als Ergebnis liefert, oder
der :ref:`Inhaltsoperator <Inhaltsoperator>` ``*``, der den an einer
Speicherstelle abgelegten Wert ausgibt.

Die wichtigsten Operatoren werden in den folgenden Abschnitten kurz beschrieben.

.. _Mathematische Operatoren:

.. rubric:: Mathematische Operatoren

Die mathematischen Grundrechenarten Addition, Subtraktion, Multiplikation und
Division lassen sich in C erwartungsgemäß mittels der Operatoren ``+``, ``-``,
``*`` und ``/`` durchführen; dabei werden jeweils zwei numerische Variablen
oder Ausdrücke zu einem neuen Ergebnis verknüpft. Als Einziges ist die
Division durch Null nicht erlaubt, sie führt zu Fehlermeldungen beim
Compilieren oder kann das Abstürzen des Programms zur Folge haben.
Neben den vier Operatoren für die Grundrechenarten existiert zusätzlich der
Modulo-Operator ``%``, der den ganzzahligen Divisionsrest angibt; er liefert
somit stets einen Wert vom Typ ``int`` als Ergebnis.

.. list-table:: 
    :name: tab-mathematische-operatoren
    :widths: 20 50 

    * - Operator
      - Beschreibung
    * - ``+``
      - Addition zweier Zahlen
    * - ``-``
      - Subtraktion zweier Zahlen
    * - ``*``
      - Multiplikation zweier Zahlen
    * - ``/``
      - Division zweier Zahlen (Division durch Null nicht erlaubt!)
    * - ``%``
      - Ganzzahliger Rest bei der Division zweier Zahlen


.. _Inkrement und Dekrement:

Darüber hinaus existieren in C die beiden weiteren Operatoren ``++`` und ``--``,
die jeweils auf eine einzige ganzzahlige Variable angewendet werden. Der
Inkrement-Operator ``++`` erhöht den Wert der Variablen um ``1``, der
Dekrement-Operator ``--`` erniedrigt den Wert der Variablen um ``1``.
Beide Operatoren werden üblicherweise verwendet, um beispielsweise in
:ref:`Schleifen <Schleifen>` den Wert einer Zählvariablen schrittweise um Eins
zu erhöhen bzw. erniedrigen und dabei den Variablenwert mittels des
Zuweisungsoperators ``=`` einer anderen Variablen zuzuweisen: 

.. code-block:: c

    // Erhöht zunächst x um 1, weist anschließend y den Wert von x zu:
    y = ++x

    // Weist zunächst y den Wert von x zu, erhöht anschließend x um 1:
    y = x++

Wie das obige Beispiel zeigt, ist es bei der Anwendung der Operatoren ``++`` und
``--`` von Bedeutung, ob der Operator vor oder nach der jeweiligen Variablen
steht; im ersten Fall wird die Variable erst inkrementiert bzw. dekrementiert
und anschließend zugewiesen, im zweiten Fall ist es umgekehrt.

Die Operatoren ``++`` und ``--`` haben für :ref:`Zeiger auf Felder <Zeiger auf
Felder>` eine eigene Bedeutung: Sie erhöhen den Wert des Zeigers nicht um
:math:`1`, sondern um die Länge des Datentyps, der in dem Array gespeichert
ist, also beispielsweise um ``size(int)`` für ein Array mit ``int``-Variablen. 
Somit können in Schleifen auch Felder mit dem Inkrement- bzw.
Dekrement-Operator durchlaufen werden.

.. _Zuweisungsoperatoren:

.. rubric:: Zuweisungsoperatoren

Der wichtigste Zuweisungsoperator ist das Istgleich-Zeichen ``=``: Es weist den
Wert des Ausdrucks, der rechts des Istgleich-Zeichnes steht, der links stehenden
Variablen zu.

.. list-table:: 
    :name: tab-zuweisungsoperatoren
    :widths: 20 50 

    * - Operator
      - Beschreibung
    * - ``=``
      - Wertzuweisung (von rechts nach links)
    * - ``+=``
      - Erhöhung einer Variablen (um Term auf der rechten Seite)
    * - ``-=``
      - Reduzierung einer Variablen  
    * - ``*=``
      - Vervielfachung einer Variablen
    * - ``/=``
      - Teilung einer Variablen (durch Term auf der rechten Seite)
    * - ``%=``
      - Ganzzahliger Rest bei Division (durch Term auf der rechten Seite)

Neben diesem einfachen Zuweisungsoperator existieren zusätzlich noch die
kombinierten Zuweisungsoperatoren ``+=``, ``-=``, ``*=``, ``/=`` und ``%=``. Sie
werten jeweils zunächst den Ausdruck auf der rechten Seite aus, führen
anschließend die jeweilige Operation mit der links stehenden Variablen aus, und
weisen schließlich das Ergebnis wieder der links stehenden Variablen zu. Somit
ist beispielsweise ``x -= 1`` eine Kurzschreibweise für ``x = x - 1``.

.. _Vergleichsoperatoren:

.. rubric:: Vergleichsoperatoren

Vergleichsoperatoren dienen zum Wertevergleich zweier Variablen oder Ausdrücke.
Ist der Vergleich wahr, so liefern sie "wahr" als Ergebnis zurück, in C also
einen von Null verschiedenen Wert. Ist im umgekehrten Fall der Vergleich nicht
wahr, so wird als Ergebnis "falsch" (also der Wert Null) zurück geliefert.

.. list-table:: 
    :name: tab-vergleichssoperatoren
    :widths: 20 50 

    * - Operator
      - Beschreibung
    * - ``==``
      - Test auf Wertgleichheit 
    * - ``!=``
      - Test auf Ungleichheit
    * - ``<``
      - Test, ob kleiner
    * - ``<=``
      - Test, ob kleiner oder gleich
    * - ``=>``
      - Test, ob größer oder gleich
    * - ``>``
      - Test, ob größer

Vergleichsoperatoren werden vor allem in Bedingungen von :ref:`if-Anweisungen
<Bedingte Anweisungen>` eingesetzt.

.. _Logische Operatoren:

.. rubric:: Logische Operatoren

Wie in der :ref:`Aussagenlogik <gwm:Logik>` der Mathematik lassen sich auch in C
mehrere Ausdrücke mittels logischer Operatoren zu einem Gesamt-Ausdruck
kombinieren. Die jeweiligen Symbole für die logischen Verknüpfungen Und, Oder
und Nicht sind in der folgenden Tabelle aufgelistet.

.. list-table:: 
    :name: tab-logische-operatoren
    :widths: 20 50 

    * - Operator
      - Beschreibung
    * - ``!``
      - Negation
    * - ``&&``
      - Logisches Und
    * - ``||``
      - Logisches Oder

Das ``!``-Zeichen als logisches Nicht bezieht sich auf den unmittelbar rechts
stehenden Ausdruck und kehrt dabei den Wahrheitswert des Ausdrucks um. Die
anderen beiden Operatoren ``&&`` und ``||`` verknüpfen den unmittelbar links
und den unmittelbar rechts stehenden Ausdruck zu einer Gesamtaussage. Eine
Und-Verknüpfung ist genau dann wahr, wenn beide Teil-Ausdrücke wahr sind, eine
Oder-Verknüpfung ist wahr, wenn mindestens einer der beiden Ausdrücke wahr
ist.

Zur besseren Lesbarkeit sowie zur Vermeidung von Fehlern ist es empfehlenswert,
die durch logische Ausdrücke verknüpften Aussagen stets in runde Klammern zu
setzen, also beispielsweise ``(ausdruck_1 && ausdruck_2)`` zu schreiben.

.. _Der Bedingungsoperator:

.. rubric:: Der Bedingungsoperator

Der Bedingungsoperator ist der einzige Operator in C, der drei Ausdrücke
miteinander verbindet. Er hat folgenden Aufbau:

.. code-block:: c

    bedingung ? anweisung1 : anweisung2

Wenn der Bedingungs-Ausdruck wahr ist, also einen Wert ungleich Null als
Ergebnis liefert, so wird ``anweisung1`` ausgeführt, ist der
Bedingungs-Ausdruck falsch, so wird ``anweisung2`` ausgeführt. Beim
Bedingungsoperator handelt es sich somit um eine sehr kurze Schreibform einer
:ref:`if-else-Anweisung <Bedingte Anweisungen>`. Er kann unter anderem bei der
Zuweisung von Werten eingesetzt werden, um beispielsweise einer neuen Variablen
den größeren Wert zweier anderer Variablen zuzuweisen:

.. code-block:: c

    // Die größere der beiden Variabeln var_1 und var_2 in my_var abspeichern:
    my_var = ( var_1 > var_2 ) ? var_1 : var_2;

.. index:: Cast-Operator
.. _Cast-Operator:

.. rubric:: Der Cast-Operator

Mittels des so genannten Cast-Operators kann eine Variable mit einem bestimmten
Datentyp manuell in einen anderen Datentyp umgewandelt werden.

Von C werden auch automatisch derartige Umwandlungen vorgenommen, beispielsweise
wenn ein ``int``-Wert mit einem ``float``-Wert multipliziert werden soll;
hierbei wird der ``int``-Wert zunächst in einen ``float``-Wert gewandelt, damit
der Operator auf zwei syntaktisch gleichwertige Objekte angewendet wird.
Ebenso werden :ref:`enum <Aufzählungen>`-Konstanten automatisch nach ``int``
konvertiert.

..  char -> short -> long -> float -> double -> long double

Während eine automatische Konvertierung in den jeweils nächst "größeren" Datentyp
ohne Probleme möglich ist (beispielsweise ``float -> double`` oder ``double ->
long double``), so ist eine Konvertierung in einen kleineren Datentyp oftmals
mit Verlusten behaftet; beispielsweise kann der ``float``-Wert :math:`3.14` nur
gerundet als ``int``-Wert dargestellt werden. Eine solche derartige Umwandlung
erfolgt in C dadurch, dass man bei der Zuweisung vor den Ausdruck auf der
rechten Seite den gewünschten Datentyp in runden Klammern angibt:

.. code-block:: c

    int n;
    float pi=3.14;

    n = (int) pi;

Die runde Klammer mit dem darin enthaltenen Ziel-Datentyp wird hierbei als
Cast-Operator bezeichnet. Am häufigsten werden Casts wohl beim :ref:`dynamischen
Reservieren von Speicherplatz <Dynamische Speicherreservierung>` verwendet:
Hierbei wird zunächst ein unbestimmter Zeiger auf den reservierten Speicherplatz
erzeugt, der dann in einen Zeiger des gewünschten Typs umgewandelt wird.

.. index:: sizeof()
.. _Der Sizeof-Operator:

.. rubric:: Der ``sizeof``-Operator

Der ``sizeof``-Operator gibt die Größe des anschließend angegebenen Datentyps
an; der Datentyp kann dabei wahlweise mit oder ohne Klammern angegeben werden.
Beispielsweise würden ``sizeof float;`` oder ``sizeof(float);``, je nach
Betriebsystem, beispielsweise den Wert ``4`` liefern.

Mit dem ``sizeof``-Operator kann auch die Größe von :ref:`Feldern <Felder>` oder
:ref:`Zusammengesetzten Datentypen <Strukturen>` ermittelt werden; sie
entspricht der Summe der Größen aller darin vorkommenden Elemente.

Das Ergebnis von ``sizeof()`` hat als Datentyp ``size_t``, was gleichbedeutend
mit ``unsigned int`` ist.

.. _Der Kommaoperator:

.. rubric:: Der Kommaoperator

In C wird das Komma meist als Trennungszeichen für Funktionsargumente oder bei
der Deklaration von Variablen verwendet. Es kann allerdings auch als Operator
genutzt werden, wenn es zwischen zwei Ausdrücken steht. Hierbei wird zunächst
der links vom Komma stehende Ausdruck ausgewertet, anschließend der rechte. Als
Ergebnis wird der Wert des rechten Ausdrucks zurückgegeben.

Am häufigsten wird der Komma-Operator in :ref:`for-Schleifen <Schleifen>`
eingesetzt.

.. _Rangfolge der Operatoren:

.. rubric:: Rangfolge der Operatoren

In der folgenden :ref:`Tabelle <tab-rangfolge-operatoren>` ist aufgelistet,
welche Operatoren mit welcher Priorität ausgewertet werden (ebenso wie "Punkt
vor Strich" in der Mathematik). Operatoren mit einem hohen Rang, die weiter oben
in der Tabelle stehen, werden vor Operatoren mit einem niedrigen Rang
ausgewertet. Haben zwei Operatoren den gleichen Rang, so entscheidet die so
genannte Assoziativität, in welcher Reihenfolge ein Ausdruck auszuwerten ist: 

* Bei der Assoziativität "von links nach rechts" wird der Ausdruck der
  Reihe nach abgearbeitet, genau so, wie man den Code liest. 
  
* Bei der Assoziativität "von rechts nach links" wird zunächst der Ausdruck
  auf der rechten Seite des Operators ausgewertet, und erst anschließend der
  Operator auf den sich ergebenden Ausdruck angewendet.


.. list-table:: 
    :name: tab-rangfolge-operatoren
    :widths: 10 60 20

    * - Rang
      - Operator
      - Assoziativität
    * - 1
      - Funktionsaufruf ``()``, Array-Operator ``[]``, Strukturzugriff ``.`` und
        ``->``
      - von links nach rechts 
    * - 2
      - Adress-Operator ``&``, Inhalts-Operator ``*``, Vorzeichen-Operator ``+``
        und ``-``, Negation ``!``, Inkrement ``++`` und Dekrement ``--``,
        Einerkomplement ``~``, ``sizeof``, ``(cast)`` 
      - von rechts nach links
    * - 3
      - Multiplikation ``*``, Division ``/``, Modulo ``%``
      - von links nach rechts
    * - 4
      - Addition ``+``, Subtraktion ``-`` 
      - von links nach rechts
    * - 5
      - Bitweises Schieben ``>>`` und ``<<`` 
      - von links nach rechts
    * - 6
      - Werte-Vergleich ``>`` ``<`` ``>=`` ``<=`` 
      - von links nach rechts
    * - 7
      - Werte-Vergleich ``==`` und ``!=`` 
      - von links nach rechts
    * - 8
      - Binäres Und ``&`` 
      - Von links nach rechts
    * - 9
      - Binäres Entweder-Oder ``^``
      - von links nach rechts
    * - 10
      - Binäres Oder ``|`` 
      - von links nach rechts
    * - 11
      - Logisches Und ``&&`` 
      - von links nach rechts
    * - 12
      - Logisches Oder ``||`` 
      - von links nach rechts
    * - 13
      - Bedingungsoperator ``?:``
      - Von rechts nach links
    * - 14
      - Zuweisungsoperator ``=`` ``*=`` ``/=`` ``%=`` ``+=`` ``-=`` ``^=``
        ``|=`` ``&=`` ``<<=`` ``>>=``
      - von rechts nach links
    * - 15
      - Sequenzoperator ``,``
      - von links nach rechts

Enthält ein Ausdruck mehrere Operatoren mit gleicher Priorität, so werden die
meisten Operatoren von links nach rechts ausgewertet. Beispielsweise haben im
Ausdruck ``3 * 4 % 5 / 2`` alle Operatoren die gleiche Priorität, sie werden
gemäß ihrer Assoziativität von links nach rechts ausgewertet, so dass der
Ausdruck formal mit ``((3 * 4) % 5) / 2`` identisch ist; somit ist das Ergebnis
gleich ``(12 % 5) / 2 = 2 / 2 = 1``.

Zur besseren Lesbarkeit können Teilaussagen die durch einen Operator mit höherer
Priorität verbunden sind jederzeit, auch wenn es nicht notwendig ist, in runde
Klammern gesetzt werden, ohne den Wert der Aussage zu verändern.


.. index:: Funktion, Block
.. _Funktionen:

Funktionen
----------

Funktionen werden verwendet, um einzelne, durch geschweifte Klammern begrenzte
Code-Blöcke mit einem Namen zu versehen. Damit können Funktionen an beliebigen
anderen Stellen im Programm aufgerufen werden.  

Eine Funktion kann somit als "Unterprogramm" angesehen werden, dem
gegebenenfalls ein oder auch mehrere Werte als so genannte "Argumente" übergeben
werden können und das je nach Definition einen Wert als Ergebnis zurück gibt. 

Die Definition einer Funktion hat folgenden Aufbau:

.. code-block:: c

    // Definition einer Funktion:
    rueckgabe_typ funktionsname( arg1, arg2, ... )
    {
        Anweisungen
    }

Der Rückgabe-Typ gibt den Datentyp an, den die Funktion zurück gibt,
beispielsweise ``int`` für ein ganzzahliges Ergebnis oder ``char *`` für eine
Zeichenkette. Liefert die Funktion keinen Wert zurück, wird ``void`` als
Rückgabe-Typ geschrieben. Die Argumentenliste der Funktion kann entweder leer
sein oder eine beliebige Anzahl an zu übergebenden Argumenten beinhalten, wobei
jedes Argument aus einem Argument-Typ und einem Argument-Namen besteht. 
Beim Aufruf der Funktion müssen die Datentypen der übergebenen Werte mit denen
der bei der Deklaration angegebenen Argumentliste übereinstimmen. [#]_

Bezüglich der Anweisungen innerhalb eines Funktionsblocks bestehen kaum
Einschränkungen, außer dass es nicht möglich ist, innerhalb einer Funktion
weitere Funktionen zu definieren. Neue Variablen, deren Gültigkeit auf die
jeweilige Funktion beschränkt ist, müssen stets zu Beginn des Funktionsblocks
definiert werden. Am Ende der Funktion verlieren diese "lokalen" Variablen
standardmäßig wieder ihre Gültigkeit; soll eine Variable ihren Wert jedoch
bis zum nächsten Aufruf der Funktion behalten, muss bei der Definition der
Variablen das Schlüsselwort :ref:`static <static>` verwendet werden.

.. index:: return

Soll eine Funktion einen Wert als Ergebnis zurückzugeben, so muss innerhalb der
Funktion das Schlüsselwort ``return`` gesetzt werden, gefolgt von einem
C-Ausdruck. Wenn die Funktion an einer ``return``-Anweisung ankommt, wird der
Ausdruck ausgewertet und das Ergebnis an die aufrufende Stelle im Programm
zurück gegeben. Zu beachten ist lediglich, dass der von ``return`` zurück
gelieferte Wert mit dem in der Funktionsdefinition angegebenen Datentyp
übereinstimmt, damit der Compiler keine Fehlermeldung ausgibt.

Nach der Definition der Funktion kann diese an beliebigen Stellen im Code
genutzt werden, sie kann also auch von anderen Funktionen aufgerufen werden. Um
eine Funktion allerdings bereits aufrufen zu können, wenn ihre Definition erst
an einer späteren Stelle der Datei erfolgt, muss am Dateianfang -- wie bei
Variablen -- zunächst der Prototyp der Funktion deklariert werden: [#]_

.. code-block:: c

    // Deklaration des Funktions-Prototyps:
    rueckgabe_typ funktionsname( arg1, arg2, ... );

Bei C-Programmen, die nur aus einer einzigen Datei bestehen, werden die
Funktions-Prototypen üblicherweise gemeinsam mit der Deklaration von Variablen
an den Anfang der Datei geschrieben. Die konkrete Definition der Funktionen
erfolgt dann üblicherweise nach der Definition der Funktion ``main()``.

..  Es bleibt noch die Frage zu klären, wo man die Funktionsprototypen im Quellcode
..  unterbringen soll. Am sinnvollsten ist es, sie vor main zu stellen oder vor die
..  Definition der ersten Funktion. Der guten Lesbarkeit halber ist es zu empfehlen,
..  alle Prototypen an einer Stelle anzugeben.


Um eine Funktion aufzurufen, wird der Name der Funktion in Kombination mit 
einer Argumentliste in runden Klammern angegeben:

.. code-block:: c

    //  Aufruf einer Funktion:
    funktionsname( arg1, arg2, ... );

Beim Aufruf einer Funktion müssen die Anzahl der übergebenen Argumente und ihre
Datentypen mit der Funktions-Definition übereinstimmen.

C-Programme bestehen letztlich aus einer Vielzahl an Funktionen, die jeweils
möglichst eine einzige, klar definierte Teilaufgabe übernehmen; entsprechend
sollte der Funktionsname auf den Zweck der Funktion hinweisen. Eine Funktion
Funktion sollte ebenfalls nicht allzu umfangreich sein, nur wenige Funktionen
bestehen aus mehr als 30 Zeilen Code. [#]_ Auf diese Weise lassen sich einerseits
einzelne Code-Teile leichter wieder verwerten, andererseits kann dadurch beim Suchen
nach Fehlern der zu hinterfragende Code-Bereich schneller eingegrenzt werden.

.. Strukturierte Programmierung

.. index:: Call by Value
.. _Call by Value und Call by Reference:

.. rubric:: Call by Value und Call by Reference

In C werden alle Argumente standardmäßig "by Value" übergeben, das heißt, dass
die übergebenen Werte beim Funktionsaufruf kopiert werden, und innerhalb der
Funktion mit lokalen Kopien der Werte gearbeitet wird. Eine Funktion kann
hierbei die Originalvariablen nicht verändern. 

.. index:: Call by Reference

Wenn eine Funktion übergebene Variablen jedoch verändern soll, so müssen
anstelle der Variablenwerte die Adressen der jeweiligen Variablen übergeben
werden. Eine derartige Übergabe wird als "Call by Reference" bezeichnet:
Anstelle der Variablen wird ein :ref:`Zeiger <Zeiger>` auf die Variable als
Argument übergeben. Ändert die Funktion den Wert der Speicherstelle, auf die der
Pointer zeigt, so wird, wenn der Variablenwert erneut abgerufen wird, die
Veränderung auch im restlichen Programmteil festgestellt. 

Komplexe Datentypen, beispielsweise :ref:`Strukturen <Strukturen>`, werden fast
nie direkt, sondern meistens mittels eines Zeigers an eine Funktion übergeben;
dadurch muss nicht die ganze Struktur, sondern nur die Speicheradresse (ein
``unsigned int``-Wert) kopiert werden. Wird ein :ref:`Array <Felder>` mittels
eines Pointers an eine Funktion übergeben, so wird häufig dessen maximale Anzahl
an Elementen (ein ``int``-Wert) als zusätzliches Argument an die Funktion
übergeben.

.. _Lokale Variablen:

.. rubric:: Lokale Variablen

Innerhalb einer Funktion können, ebenso wie am Anfang einer Quellcode-Datei,
neue Variablen deklariert werden. Die in der Funktionsdefinition angegebenen
Parameter-Namen werden automatisch als neue Variablen deklariert. Beim Aufruf
einer Funktion werden den Parameter-Namen dann die entsprechenden Argumente als
Werte zugewiesen.

Die so genannten "lokalen" Variablen, die innerhalb einer Funktion definiert
werden, sind völlig unabhängig von den Variablen, die außerhalb der Funktion
existieren. Variablen des Programms können nur als Argumente an die Funktion
übergeben werden, und Variablenwerte der Funktion können nur über die
``return``-Anweisung an das Programm zurückgegeben werden.

Gibt es in einem Programm eine Variable ``var_1``, so kann innerhalb einer
Funktion also dennoch eine gleichnamige Variable ``var_1`` definiert werden. Die
lokale Variable "überdeckt" in diesem Fall die Programmvariable, bis die
Funktion abgearbeitet ist. Mit dem Funktionsende erlischt eine lokale Variable
wieder, es sei denn, sie wurde als :ref:`static <static>` deklariert. In diesem
Fall hat die lokale Variable beim nächsten Funktionsaufruf den Wert, den sie
beim Beenden des vorhergehenden Funktionsaufrufs hatte.


.. _Rekursion:

.. rubric:: Rekursion

Ruft eine Funktion in ihrem Anweisungsblock sich selbst auf, so spricht man von
Rekursion. Das wohl bekannteste Beispiel einer rekursiven Funktion ist die so
genannte Fakultät :math:`x!`:

.. math::
    
    x! = x \cdot (x - 1)  \cdot (x-2) \cdot \ldots \cdot 2 \cdot 1 

Diese mathematische Funktion, die für positive ganzzahlige Werte definiert ist,
kann mittels einer C-Funktion für jeden beliebigen Wert :math:`x` rekursiv
mittels :math:`x! = x \cdot (x-1)!` berechnet werden: 

.. code-block:: c

    unsigned int fakultaet(unsigned int x)
    {
        if (a == 1)
        {
            return 1;
        }
        else
        {
            x *= fakultaet(x-1);
            return x;
        }
    }

Bei diesem Beispiel wird die Funktion ``fakultaet`` so lange von sich selbst
aufgerufen, bis das Argument ``x`` gleich ``1`` ist. Die zurückgegebenen Werte
werden dabei jeweils mit Hilfe des Zuweisungsoperators ``*=`` mit dem als
Argument übergebenen Wert von ``x`` multipliziert, das Ergebnis wird an die
aufrufende Funktion zurückgegeben.

Rekursive Funktionen sollten, sofern möglich, vermieden werden. Der Grund liegt
darin, dass der Computer bei jedem neuen Funktionsaufruf unter anderem
Variablenwerte kopieren und neue Variablen initiieren muss, was zu einer
Verlangsamung des Programms führt. Die Fakultäts-Funktion kann beispielsweise
auch geschickter mittels einer :ref:`for <Schleifen>`-Schleife implementiert
werden, dank der insbesondere bereits berechnete Teilergebnisse nicht erneut
berechnet werden müssen:

.. code-block:: c

    unsigned int fakultaet(unsigned int n)
    {
        int i;
        int result = 1;

        for (i=1; i<=n; i++) 
        {
            ergebnis *= i;
        }

        return result;
    }

In manchen Fällen, beispielsweise beim "Merge-Sort"-Verfahren, ist Rekursion
hingegen unvermeidbar; aufgrund der effizienteren Vorgehensweise ist dieses
Sortierverfahren dem klassischen "Bubble-Sort"-Verfahren, das ohne Rekursion
auskommt, bei großen Datenmengen weit überlegen.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Streng genommen werden die Argumente bei der Definition als "formale
    Parameter" bezeichnet, die beim Aufruf übergebenen Werte hingegen werden
    "aktuelle Parameter" oder schlicht Argumente genannt.  

.. [#] Deklarationen von Funktionen sind für das Compilieren des Programms
    unerlässlich, da für jeden Funktionsaufruf geprüft wird, ob die Art und
    Anzahl der übergebenen Argumente korrekt ist. 

.. [#] Eine Funktion sollte maximal 100 Zeilen umfassen. Die Hauptfunktion
    ``main()`` sollte nur Unterfunktionen aufrufen, um möglichst übersichtlich
    zu sein.

