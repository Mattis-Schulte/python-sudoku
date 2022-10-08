# Sudoku (Backtracking-Algorithmus)
## Gruppenmitglieder
- Enno Rockmann: Algorithmus, Qualitätskontrolle, Dokumentation
- Sajan Sivapatham: UI-Design/-Programmierung, Spiel-Design, Dokumentation
- Mattis Schulte: Programmierung, Projektleiter, Dokumentation

## Zeitplanung
- 13.09.2022: Grundstruktur und erste Ideen
- 16.09.2022: Erster Algorithmus
- 27.09.2022: Geschwingsoptiemrungen und Vergleich mit anderen Algorithmen
- 30.09.2022: Terminal-Ausgabe
- 04.10.2022: Simples Menu und Spielmodis
- 11.10.2022: Grafische Benutzeroberfläche
- 14.10.2022: Dokumentation und Qualitätskontrolle


## Aufgabenbeschreibung
Es soll ein Algorithmus in Python objektorientiert programmiert werden. Es müssen mindestens die Klassen SudokuBoard und SudokuGame existieren. Ein Sudoku-Board „straight forward“ aufzubauen dauert sehr lange, deshalb wird dies zum Beispiel über ein Backtracking-Algorithmus gelöst.  
  
**Backtracking**
> Ein Verfahren, das darauf beruht ein oder mehrere Schritte zurückzugehen falls keine Lösung gefunden wird. Es kann zu einer oder auch keiner Lösung führen und unter Umständen auch sehr lange Laufzeiten haben.

**Die Aufgabe erfordert:**
- die Umsetzung des Spiels in Python unter Berücksichtigung der obigen Vorgaben (es kann auch Alternativen geben, andere Form des Backtrackings z.B.) inkl. Kommentierung des Codes
- ein Userinterface auf Consolen-Ebene, so dass ein Nutzer das Spiel bedienen kann inkl. der Einführung von Schwierigkeitsgraden (leicht, mittel, schwer) – der User wählt über das Menü den Schwierigkeitsgrad aus und erhält sein Board mit Lücken inkl. Kommentierung des Codes
- eine Dokumentation/Bericht bestehend aus:
  - der Aufgabenbeschreibung
  - dem Klassenentwurf
  - Beschreibung der Lösung und Besonderheiten
  - Fazit und Selbstreflexion

## Klassenentwurf (Enno)
![sudoku-class-diagram](https://user-images.githubusercontent.com/34488470/194714669-16bd8696-7729-4407-8fd9-a086b98e4bd0.png)

## Beschreibung der Lösung (Mattis / Sajan)

### Algorithmen:
Zum Generieren des Sudoku-Boards haben wir uns verschiedene Lösungsansätze überlegt, welche sich grundsätzlich in drei Kategorien einteilen lassen:
- **Mathematisch** (wie zum Beispiel durch die Verwendung von [Konvolution](https://de.wikipedia.org/wiki/Faltung_(Mathematik)), was wir nicht näher verfolgt haben, aber theoretisch möglich sein sollte)
- **Backtracking** (entweder rekursionsbasiert oder nicht-rekursionsbasiert)
- **Vertauschen** (entweder durch das Vertauschen einer einzelnen Zeile, Spalte, 3x3 Abschnitt oder durch das Vertauschen eines kompletten Boards)  
#### Rekursionsbasierter Backtracking-Algorithmus (1,3 ms):
Diese Art von Lösung war, nachdem mathematischen Ansatz die Zweite, die uns in den Sinn kam und die Erste, die wir dann auch tatsächlich ausprogrammiert haben. Sie ist rekursionsbasiert und füllt ein Feld nach dem anderen auf, wodurch wir uns eine sehr gute Performance und gute Lesbarkeit versprochen haben. Dies hat sich auch in der Realität bewahrheitet, auch wenn die Verwendung von Rekursion zugunsten der Performance einiges an Lesbarkeit kostet. 

Jedoch haben wir später festgestellt, dass es noch andere Lösungsansätze gibt, die weitaus performanter und lesbarer sind. Allerdings haben wir uns aufgrund der Zuverlässigkeit und Möglichkeit, alle möglichen Sudoku-Boards zu generieren sowie der immer noch mehr als akzeptabler Performance und Lesbarkeit dazu entschieden, diese Lösung weiterhin zu verwenden.

#### Vertauschen eines schon fertigen Board (0,2 ms):
Unser nächster Lösungsansatz war das Vertauschen von Zeilen, Spalten und 3x3 Quadraten eines schon hinterlegten Boards. Da durch würde jegliche Form von Überprüfung unnötig und auch Zufall sollte keinerlei Rolle mehr in der Laufzeit spielt, womit eine lineare Zeitkomplexität erreicht werden würde. 

Nach etwas Suchen im Internet haben wir dann [diese Lösung](https://stackoverflow.com/a/61442050/12278623) gefunden und den Code von Java in Python übersetzt, um ihn mit unserer Backtracking-Lösung zu vergleichen (wie genau der Code funktioniert ist auch in dem StackOverflow-Post beschrieben). Das Ergebnis hat uns tatsächlich etwas überrascht, da wir einen größeren Performance-Unterschied erwartet haben. Bei weiterer Überlegung macht das Ergebnis aber mehr Sinn und bestätigt uns nur in der Annahme, das unser Backtracking-Algorithmus sehr gut ist. Der Nachteil dieser Lösung ist, dass der Code nur schwer verständlich ist.

#### Vertauschen eines einzigen 3x3 Quadrat bzw. Zeile (0,008 ms):
![sudoku-permutation-2](https://user-images.githubusercontent.com/34488470/194714718-c8806d87-225f-4e02-8502-6066fabe5022.png)

### Ausgabe und Spieldesign:
#### Terminal:
#### Grafische Benutzeroberfläche:

## Besonderheiten

## Fazit und Selbstreflexion
