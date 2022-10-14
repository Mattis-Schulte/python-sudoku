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

## Klassenentwurf
![sudoku-class-diagram](https://user-images.githubusercontent.com/34488470/194714669-16bd8696-7729-4407-8fd9-a086b98e4bd0.png)

## Beschreibung der Lösung

### Algorithmen:
Zum Generieren des Sudoku-Boards haben wir uns verschiedene Lösungsansätze überlegt, welche sich grundsätzlich in drei Kategorien einteilen lassen:
- **Mathematisch** (wie zum Beispiel durch die Verwendung von [Konvolution](https://de.wikipedia.org/wiki/Faltung_(Mathematik)), was wir nicht näher verfolgt haben, aber eventuelle möglich ist)
- **Backtracking** (entweder rekursionsbasiert oder nicht-rekursionsbasiert)
- **Vertauschen** (entweder durch das Vertauschen einer einzelnen Zeile, Spalte, 3x3 Abschnitt oder durch das Vertauschen eines kompletten Boards)  

**Rekursionsbasierter Backtracking-Algorithmus (1,3 ms):**  
Diese Art von Lösung war, nachdem mathematischen Ansatz die Zweite, die uns in den Sinn kam und die Erste, die wir dann auch tatsächlich ausprogrammiert haben. Sie ist rekursionsbasiert und füllt ein Feld nach dem anderen auf, wodurch wir uns eine sehr gute Performance und gute Lesbarkeit versprochen haben. Dies hat sich auch in der Realität bewahrheitet, auch wenn die Verwendung von Rekursion zugunsten der Performance einiges an Lesbarkeit kostet. 

Jedoch haben wir später festgestellt, dass es noch andere Lösungsansätze gibt, die weitaus performanter und lesbarer sind. Allerdings haben wir uns aufgrund der Zuverlässigkeit und Möglichkeit, alle möglichen Sudoku-Boards zu generieren sowie der immer noch mehr als akzeptabler Performance und Lesbarkeit dazu entschieden, diese Lösung weiterhin zu verwenden.

**Vertauschen eines schon fertigen Board (0,2 ms):**  
Unser nächster Lösungsansatz war das Vertauschen von Zeilen, Spalten und 3x3 Quadraten eines schon hinterlegten Boards. Da durch würde jegliche Form von Überprüfung unnötig und auch Zufall sollte keinerlei Rolle mehr in der Laufzeit spielt, womit eine lineare Zeitkomplexität erreicht werden würde. 

Nach etwas Suchen im Internet haben wir dann [diese Lösung](https://stackoverflow.com/a/61442050/12278623) gefunden und den Code von Java in Python übersetzt, um ihn mit unserer Backtracking-Lösung zu vergleichen (wie genau der Code funktioniert ist auch in dem StackOverflow-Post beschrieben). Das Ergebnis hat uns tatsächlich etwas überrascht, da wir einen größeren Performance-Unterschied erwartet haben. Bei weiterer Überlegung macht das Ergebnis aber mehr Sinn und bestätigt uns nur in der Annahme, das unser Backtracking-Algorithmus sehr gut ist. Der Nachteil dieser Lösung ist, dass der Code nur schwer verständlich ist.

**Vertauschen eines einzigen 3x3 Quadrat bzw. Zeile (0,008 ms):**  
> Unsere tatsächliche Lösung weicht hiervon leicht ab, folgt dabei aber weiterhin denselbem Prinzip.  

Eine Weitere Lösungsmöglichkeit die uns eingefallen ist, ist ein einziges 3x3 Quadrat wie unten in der Abbildung zu vertauschen. Unser Ziel dabei war es, die Lösung mit der kürzesten Laufzeit und der geringsten Länge an Code zu finden, ohne dabei auf andere Dinge Rücksicht zu nehmen. Was wir unserer Meinung nach auch erreicht haben. Hierbei entsteht jedoch der Nachteil, das deutliche Muster zu erkennen sind. Des Weiteren ist die Anzahl der verschiedenen Sudoku-Boards die mit dieser Methode erstellt werden können, auf ```9!``` (362880) begrenzt.

![sudoku-permutation-2](https://user-images.githubusercontent.com/34488470/194714718-c8806d87-225f-4e02-8502-6066fabe5022.png)

### Ausgabe und Spieldesign:
Bei der Ausgabe haben wir uns zunächst auf ein Spiel in der Konsolenebene geeinigt und dies implementiert. Später wollten wir dann aus Gründen der Übersichtlichkeit und Benutzererfahrung stattdessen eine GUI verwenden. Für das Spieldesign wollten wir das Spiel so unkompliziert wie möglich gestalten, daher lassen wir den User beispielsweise keine falschen Zahlen eingeben, sondern weisen ihn sofort auf seinen Fehler hin.

Bei den Schwierigkeitsstufen haben wir uns auf folgende drei geeinigt:
- Einfach (56 Felder)
- Mittel (46 Felder)
- Schwierig (36 Felder)

**Terminal:**  
```
  1 2 3   4 5 6   7 8 9
A   2   |   3   | 8 7 9
B     9 | 7   1 |   3 4
C 3 6 7 | 9 8   |      
  ------+-------+------
D     3 |       |   2 7
E     2 |     8 | 5   1
F       |     7 |   8 3
  ------+-------+------
G 2 1 6 | 4 7   |   9  
H     8 |       |   4  
I     4 |     3 |   1  
```
**Grafische Benutzeroberfläche:**  


## Besonderheiten
- Sehr schnell
- Mehrere Lösungsansätzte
- Simpler Code
## Fazit und Selbstreflexion
Das Projekt war sehr interessant und hat viel Spaß gemacht, da wir selbst Sudoku spielen. Der Basiscode stand sehr schnell, daher haben wir die meißte Zeit daran gearbeitet, ihn zu verbessern. Dadurch haben wir es geschafft, sehr schnelle, sehr gute Sudoku-Bretter erstellen zu können, weshalb wir mit dem Ergebnis zufrieden sind. Die GUI (ist nicht fertig geworden, da wir uns zu sehr auf den Code konzentriert haben und zu spät die Aufgaben aufgeteilt haben / ist gut gelungen und bereitet dem Nutzer ein gutes Spiel-Erlebnis.) Am Anfang haben wir alles zusammen bearbeitet, was dazu geführt hat, dass meist nur 1-2 Personen aktiv am Code gearbeitet haben. Deshalb haben wir uns aufgeteilt, haben die Dokumentation, die GUI und den Algorithmus untereinander aufgeteilt, wodurch am Ende jeder eine Aufgabe hat. 
