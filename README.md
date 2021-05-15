# 14105 go-eCharger

## Beschreibung 

Der Baustein dient zur Kommunikation mit einer [go-e](https://go-e.co/) Ladestation / Wallbox, s. [API](https://github.com/goecharger/go-eCharger-API-v1)

## Eingänge

| Nr. | Name | Initialisierung | Beschreibung |
| --- | --- | --- | --- |
| 1 | IP | | IP der Wallbox |
| 2 | Port | 0 | Port der Wallbox |
| 3 | Intervall | 0 | Bei einem Wert <> 0 werden die Daten go-e Wallbox zyklisch mit dem angegebenen Intervall in Sekunden abgerufen. |
| 4 | Trigger | 0 | Bei einem Wert <> 0 werden die Daten go-e Wallbox abgerufen. |
| 5ff | ... | ... | Für die weiteren Parameter, s. [go-eCharger API](https://github.com/goecharger/go-eCharger-API-v1). *Von der API abweichende Einheiten sind am jew. Ein- Ausgang des Bausteins angegeben.* |

## Ausgänge

| Nr. | Name | Initialisierung | Beschreibung |
| --- | --- | --- | --- |
| 1 | Online 1 | 0 | 1, wenn Wallbox erreichbar; 0, wenn nicht |
| 2ff | ... | ... | Für die weiteren Parameter, s. [go-eCharger API](https://github.com/goecharger/go-eCharger-API-v1). *Von der API abweichende Einheiten sind am jew. Ein- Ausgang des Bausteins angegeben.* |
| | nrg / Json | | Werte des Strom und Spannungssensor als Json Array, z.B. "{'V N': 1, 'P% L2': 0, 'P% L3': 0, 'P% L1': 0, 'V L2': 220, 'V L3': 219, 'kW L1': 0.0, 'V L1': 218, 'kW N': 0.0, 'P% N': 0, 'kW L3': 0.0, 'kW Sum': 0.0, 'kW L2': 0.0, 'A L3': 0.0, 'A L2': 0.0, 'A L1': 0.0}"

## Beispielwerte

| Eingang | Ausgang |
| --- | --- |
| - | - |


## Other

- Neuberechnug beim Start: Nein
- Baustein ist remanent: nein
- Interne Bezeichnung: 11083
- Kategorie: Datenaustausch

### Change Log

 - v0.6
     - Refactoring
 - v0.5
     - Fix: Ausgang TME liefert Zeit unformatiert
	 - Ausgang aktueller Stromfluss auf L1+L2+L3 ergänzt
 - v0.2
     - Referenzen auf API in Hilfe ergänzt
	 - Ein-/Ausgänge gem. API benannt
 - v0.1
     - Initial


### Open Issues / Know Bugs

- keine

### Support

Please use [github issue feature](https://github.com/En3rGy/14108_tibber/issues) to report bugs or rise feature requests.
Questions can be addressed as new threads at the [knx-user-forum.de](https://knx-user-forum.de) also. There might be discussions and solutions already.


### Code

Der Code des Bausteins befindet sich in der hslz Datei oder auf [github](https://github.com/En3rGy/14105_go-eCharger).

### Devleopment Environment

- [Python 2.7.18](https://www.python.org/download/releases/2.7/)
    - Install python markdown module (for generating the documentation) `python -m pip install markdown`
- Python editor [PyCharm](https://www.jetbrains.com/pycharm/)
- [Gira Homeserver Interface Information](http://www.hs-help.net/hshelp/gira/other_documentation/Schnittstelleninformationen.zip)


## Requirements
-

## Software Design Description


## Validation & Verification
- Unit tests are performed.

## Licence

Copyright 2021 T. Paul

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
