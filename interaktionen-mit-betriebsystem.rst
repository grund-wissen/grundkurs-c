.. _Interaktionen mit dem Betriebsystem:

Interaktionen mit dem Betriebsystem
===================================

.. getopt
.. argv, argc

.. envp -- Umgebungsinformationen
.. environment pointer

.. index:: system()
.. _System-Interaktion:

``system()`` -- Externe Programme aufrufen
------------------------------------------

Mittels der Funktion ``system()`` aus der Standard-Bibliothek :ref:`stdlib.h
<stdlib.h>` können Programme des Betriebsystems, beispielsweise
:ref:`Shell-Programme <gwl:Standard-Programme>`, aus einem C-Programm heraus
aufgerufen werden. Als Argument wird der Funktion dabei eine Zeichenkette
übergeben, die den Namen des aufzurüfenden Programms mitsamt aller Argumente
und Optionen enthält, beispielsweise ``"ls -lh"``: 

.. code-block:: c

    #include <stdlib.h> 

    // ...

    system("ls -lh");

    // ...

Wenn das externe Programm beendet ist, wird das C-Programm weiter ausgeführt.


.. index:: exit(), atexit()
.. _exit() und atexit():

``exit()`` und ``atexit()`` -- Programme ordentlich beenden
-----------------------------------------------------------

Mittels der Funktion ``exit()`` kann ein Programm in geordneter Weise beendet
werden. Als Argument wird beim Aufruf der Funktion ein ``int``-Wert angegeben,
der als Rückgabewert an das System dient. Der Wert ``0`` gilt dabei für ein
normales Programmende, der Wert ``1`` wird üblicherweise im Falle eines Fehlers
zurück gegeben. 

Trifft das Programm auf eine ``exit()``-Funktion, so werden automatisch alle
noch nicht geschriebenen Ausgabe-Streams geschrieben, alle offenen Dateien
geschlossen sowie alle mittels ``tmpfile()`` angelegten temporären Dateien
gelöscht.

Zusätzlich können im vorangehenden Teil des Codes, häufig in der Funktion
``main()``, mittels ``atexit()`` Pointer auf Funktionen angegeben werden, die
bei einem Aufruf von ``exit()`` ausgeführt werden, bevor das Programm beendet
wird. Das Besondere dabei ist, dass die Funktionen von hinten nach vorne
durchlaufen werden, d.h. die zuletzt angegebene ``atexit()``-Funktion wird als
erstes aufgerufen, die als erstes angegebene ``atexit()``-Funktion zuletzt. 




