# RAM DIL – Reviewvorschläge zu den Kapiteln 4.1, 4.2, 5.2 und 6.2

**Quelldokument:** `RAM_DIL_3BU_17300_1209_DUAPC.docx`  
**Status:** Konsolidierte Review-Fassung. Vorschläge sind durch die Dokumentverantwortlichen zu prüfen und zu übernehmen.

## Kapitel 5.2.3 – RAM HW-FMEA

**Schweregrad:** Hoch

### Zitierter Ausgangstext

> Es wird empfohlen, eine RAM Hardware-FMEA zu erstellen, die darauf abzielt, Verfügbarkeits- und Wartbarkeitsaspekte im Hinblick auf ausgefallene Hardwarekomponenten (LRU) oder Teilsysteme und deren betriebliche Auswirkungen zu analysieren.

### Review-Feststellung

Die Formulierung macht die RAM-HW-FMEA optional. Mindestumfang, Zuständigkeit, Fälligkeit, Review und Aktualisierungspflicht sind nicht festgelegt.

### Vorgeschlagene Neufassung

> Die Durchführung einer RAM-Hardware-FMEA ist für alle Hardware-Komponenten und Teilsysteme innerhalb des Geltungsbereichs verpflichtend; Systemgrenzen und Schnittstellen werden im jeweiligen projektspezifischen RAM-Plan festgelegt. Die Analyse umfasst mindestens die Funktionen, glaubhaften Hardware-Fehlermodi und -ursachen, lokalen und übergeordneten Auswirkungen bis zur betrieblichen Auswirkung, Erkennungs- und Diagnosemöglichkeiten sowie Auswirkungen auf Zuverlässigkeit, Verfügbarkeit und Wartbarkeit. Bestehende und empfohlene Maßnahmen sowie Nachweise und offene Punkte sind zu dokumentieren.
>
> Der RAM-AM koordiniert und moderiert die Aktivität und stellt die gelenkte Pflege sicher. Systemarchitekt und zuständige Komponenten- bzw. Subsystemverantwortliche liefern die technischen Eingaben, bewerten die Auswirkungen und bearbeiten zugewiesene Maßnahmen. Die FMEA ist für jedes Solution Element im RAM-Terminplan mit verantwortlicher Person und konkretem Meilenstein/Termin zu planen und spätestens vor Design-Freeze bzw. Freigabe der betroffenen Auslegung abzuschließen. Sie ist durch den RAM-AM und die zuständige Designverantwortung zu reviewen; Review-Ergebnisse und offene Maßnahmen sind zu dokumentieren und nachzuverfolgen.
>
> Bei relevanten Änderungen an Architektur, Hardware, Schnittstellen, Betriebsbedingungen, Diagnose- oder Wartungskonzept sowie bei neuen Felddaten mit Einfluss auf die Analyse ist die FMEA vor Freigabe der Änderung zu überprüfen, zu aktualisieren und erneut zu reviewen. Änderungen und Freigaben sind nachvollziehbar zu revisionieren.

## Kapitel 5.2.4 – Vorläufige Zuverlässigkeitsanalysen

**Schweregrad:** Hoch

### Zitierter Ausgangstext

> Nach Abschluss des RAM-Plans wird empfohlen, ein Dokument zur vorläufigen Zuverlässigkeitsanalyse zu erstellen. Dieses Dokument soll eine grobe Abschätzung der Verfügbarkeit und Zuverlässigkeit der in Kapitel 3 beschriebenen Teilsysteme liefern.

### Review-Feststellung

Die vorläufige Zuverlässigkeitsanalyse muss den in § 5.2.5 definierten Analyseumfang und die dort festgelegten System- und Verantwortungsgrenzen anwenden. Sie soll diese Grenzen nicht erst selbst festlegen; ihre Aufgabe ist eine frühe Abschätzung auf Basis der vorgegebenen Systemgrenze und die transparente Dokumentation vorläufiger Eingangsdaten, Annahmen und Lücken.

### Vorgeschlagene Neufassung

> Für jedes Solution Element ist nach Abschluss des zugehörigen RAM-Plans eine eigene vorläufige Zuverlässigkeitsanalyse zu erstellen. Sie liefert eine erste Abschätzung der Zuverlässigkeit und Verfügbarkeit des jeweiligen Solution Elements innerhalb seiner in § 5.2.5 festgelegten Analysegrenze. Abhängigkeiten zu anderen Solution Elements und externen Diensten sind entsprechend der dortigen Abgrenzung als Schnittstellen oder Randbedingungen zu berücksichtigen. Verfügbare Eingangsdaten, vorläufige Annahmen und Datenlücken sind mit Quelle und möglicher Auswirkung auf die Abschätzung zu dokumentieren. Ergebnisse und offene Punkte der vorläufigen Analyse sind als Eingaben für die detaillierte Zuverlässigkeitsanalyse desselben Solution Elements zu übergeben.

### Hinweis zur Abgrenzung

Die im Dokument dargestellten Solution Elements, darunter IPS und DFE, belegen für sich genommen noch keine konkrete AN-/AG-Verantwortungszuordnung. Diese ist anhand der gültigen Projektverantwortlichkeiten zu bestätigen. Außerhalb der jeweiligen Analysegrenze liegende Elemente, deren Verfügbarkeit oder Ausfall das Ergebnis beeinflussen kann, sind als Randbedingungen einschließlich Annahmen und Auswirkung zu dokumentieren.

## Kapitel 5.2.5 – Zuverlässigkeitsanalysen / System- und Verantwortungsgrenzen

**Schweregrad:** Hoch

### Zitierter Ausgangstext

> Die Zuverlässigkeitsanalyse ist ein zentrales Dokument mit Fokus auf hardwarebezogene Aspekte im operativen Betrieb. Sie beschreibt die Zuverlässigkeits-, Verfügbarkeits- und Wartbarkeitseigenschaften des technischen Produkts „Generic Application Digital Interlocking (GA DIL)“.

### Review-Kommentar

> Die RAM-Systemgrenzen und Verantwortungsgrenzen sind nicht definiert. Bitte je Nachweis festlegen, welche AN-Komponenten, AG-Beistellungen, Netzwerke, Stromversorgung, Zeitversorgung und externen Dienste einbezogen beziehungsweise als Randbedingungen behandelt werden. Das heißt: für welche Teile und für welche nicht?

### Review-Feststellung

Der Abschnitt beschreibt Zuverlässigkeitsanalysen, könnte aber so verstanden werden, als sei eine einzige Analyse für das gesamte GA DIL vorgesehen. Tatsächlich sind separate Zuverlässigkeitsanalysen für die einzelnen Solution Elements erforderlich. Der RAM-Plan muss deshalb festlegen, welche Analyse für welches Solution Element erstellt wird, was deren jeweilige Analysegrenze ist und wie Schnittstellenbeiträge in einer übergeordneten Systembetrachtung berücksichtigt werden, ohne eine gemeinsame Einzelanalyse oder doppelte Bilanzierung zu unterstellen.

### Vorgeschlagene Neufassung für den RAM-Plan

> **Zuverlässigkeitsanalysen je Solution Element und Abgrenzung**
>
> Für jedes Solution Element wird eine eigene Zuverlässigkeitsanalyse erstellt. Die Analyse weist die RAM-Eigenschaften des jeweiligen Solution Elements innerhalb seiner in diesem RAM-Plan festgelegten technischen und funktionalen Systemgrenze nach. Die vorläufige Analyse und die detaillierte Analyse sind, soweit beide vorgesehen sind, je Solution Element zu erstellen bzw. fortzuschreiben; die vorläufige Analyse dokumentiert verfügbare Eingangsdaten, Annahmen und Datenlücken, die in der detaillierten Analyse zu bestätigen oder zu aktualisieren sind. Die Analysen der einzelnen Solution Elements bleiben eigenständige Nachweise und werden nicht durch eine einzige Zuverlässigkeitsanalyse für alle Solution Elements ersetzt.
>
> Die Analysegrenze wird für jedes Solution Element durch die zugehörige Systembeschreibung, die zugeordneten Funktionen und die in diesem RAM-Plan bzw. dem projektspezifischen RAM-Plan dokumentierte Liefer- und Verantwortungsgrenze festgelegt. Für die hier beschriebenen Solution Elements gelten folgende Nachweisgrenzen:
>
> | Solution Element / Abhängigkeit | Eigene Zuverlässigkeitsanalyse: Umfang und Grenze | Verantwortlichkeit und Schnittstellenbehandlung |
> | --- | --- | --- |
> | Generische Anwendung GA DIL | Eigener Nachweis für die dem GA DIL zugeordneten Funktionen und RAM-Anforderungen sowie die Integrations- und Systembeiträge innerhalb der GA-DIL-Grenze. Komponenten, die einem anderen Solution Element zugeordnet sind, werden nicht nochmals als GA-DIL-Komponenten bilanziert. | RAM-AM koordiniert den GA-DIL-Nachweis; Systemarchitekt und zuständige Komponentenverantwortliche liefern Architektur-, Anforderungs- und Integrationsdaten. Die Beiträge der Solution Elements werden über deren jeweilige Zuverlässigkeitsanalysen referenziert. |
> | Virtuelles Stellwerk VIL | Eigener Nachweis für VIL-Funktionen, VIL-Hardware und die dem VIL zugeordneten RAM-Anforderungen innerhalb der VIL-Grenze. Die für das VIL erforderlichen IPS-, DFE- und externen Dienste werden als Abhängigkeiten erfasst, nicht als VIL-eigene Komponenten doppelt bilanziert. | VIL-Verantwortliche liefern Konfiguration, Betriebsprofil und Ausfalldaten. Kennwerte abhängiger Solution Elements werden aus deren eigenen Nachweisen übernommen. |
> | IPS Solution | Eigener Nachweis für die der IPS Solution zugeordneten Plattformkomponenten, Server, Speicher, Cluster-Management und IPS-interne Netzwerke innerhalb der IPS-Grenze. | IPS-Verantwortliche erstellen den IPS-Nachweis und liefern Kennwerte sowie Schnittstellen- und Betriebsdaten an abhängige Solution Elements. |
> | Digital Field Elements (DFE) | Eigener Nachweis für die dem DFE zugeordneten Feldelementstationen, Objektcontroller und Schnittstellenumsetzer innerhalb der DFE-Grenze. | DFE-Verantwortliche erstellen den DFE-Nachweis und liefern Kennwerte sowie Schnittstellen- und Betriebsdaten an abhängige Solution Elements. |
> | AG-Beistellungen, Rechenzentrums-/Standortinfrastruktur, externe Netze, Stromversorgung, Klimatisierung und Zeitversorgung | Nicht Bestandteil der Komponenten-Ausfallraten eines Solution Elements, soweit diese Elemente außerhalb dessen festgelegter Liefer- und Produktgrenze liegen. Für jedes betroffene Solution Element sind sie als Randbedingungen in dessen Analyse zu berücksichtigen, sofern sie Funktion oder RAM-Anforderungen beeinflussen. | Der jeweilige Bereitsteller bzw. Betreiber liefert Spezifikationen, Verfügbarkeits- und Betriebsdaten. Die Zuordnung als AN-, AG- oder Drittverantwortung erfolgt gemäß Projekt-Liefer- und Verantwortungsmatrix. |
> | Externe Dienste und Schnittstellen, einschließlich RBC, NixL, SCWS und OMC | Dienste außerhalb der jeweiligen Solution-Element-Grenze werden nicht in dessen Hardware-Ausfallratenprognose einbezogen; ihre Auswirkungen sind in der betroffenen Solution-Element-Analyse als Randbedingung zu bewerten, soweit die Funktion davon abhängt. | Diensteigner bzw. Schnittstellenverantwortliche liefern die vereinbarten Schnittstellen-, Verfügbarkeits- und Betriebsdaten. |
>
> Für jedes Solution Element ist der zuständige RAM-Verantwortliche für Erstellung, Aktualisierung und fachliche Vollständigkeit der jeweiligen Zuverlässigkeitsanalyse verantwortlich. Der RAM-AM koordiniert die Analyseplanung, die einheitliche Anwendung der Abgrenzungen sowie den Austausch der Analyseergebnisse und offenen Punkte zwischen den Solution Elements. Der Systemarchitekt bestätigt die technische Architektur und die Schnittstellen zwischen den Solution Elements. Der PM bestätigt die Zuordnung der Komponenten und Dienste zu AN, AG oder Dritten anhand der geltenden Projekt- und Lieferverantwortlichkeiten. Bereitsteller bzw. Betreiber liefern die vereinbarten Eingabedaten für Randbedingungen.
>
> Eine übergeordnete GA-DIL-Systembetrachtung führt die Ergebnisse der eigenständigen Solution-Element-Analysen nur dann zusammen, wenn dies zum Nachweis einer zugeordneten Systemanforderung erforderlich ist. Sie übernimmt die Kennwerte und Annahmen aus den jeweiligen Elementnachweisen, weist Systemabhängigkeiten und gemeinsame Randbedingungen aus und vermeidet eine erneute Bilanzierung bereits berücksichtigter Komponenten. Sie ersetzt nicht die eigenständigen Zuverlässigkeitsanalysen der Solution Elements.
>
> Werden Komponenten, Netzwerke, Versorgungen oder Dienste in einer konkreten Solution-Element-Analyse als Randbedingung behandelt oder aus deren Berechnung ausgeschlossen, sind die betroffenen Elemente, die Begründung, die verwendeten Kennwerte und Annahmen sowie deren Quelle und Einfluss auf das Analyseergebnis in dieser Analyse anzugeben. Fehlende Daten oder ungeklärte Liefer- und Verantwortungszuordnungen sind als offene Punkte auszuweisen und durch den jeweils benannten Verantwortlichen zu klären. Eine Änderung der Systemkonfiguration, Schnittstellen, Projektverantwortlichkeiten oder Eingangsannahmen erfordert die Prüfung und gegebenenfalls Aktualisierung der betroffenen Solution-Element-Analysen.

## Kapitel 4.1 – Zuverlässigkeitsanforderungen

**Schweregrad:** Mittel

### Zu korrigierender Wortlaut

> Die Anforderungen an Zuverlässigkeit, Verfügbarkeit und Wartbarkeit (RAM) werden in Kapitel 6.2 RAM Anforderungen identifiziert. Ihre Erfüllung wird anschließend in der Zuverlässigkeitsanalyse bewertet. Diese Analyse sollte außerdem eine angemessene Aufteilung und Verfeinerung dieser Anforderungen entsprechend dem Systemdesign enthalten.

### Review-Feststellung

Die Formulierung „in der Zuverlässigkeitsanalyse“ und „Diese Analyse“ verwendet den Singular und kann eine einzige Zuverlässigkeitsanalyse für alle Solution Elements nahelegen. Gemäß der in Kapitel 5.2.5 vorgesehenen Aufteilung wird jedoch für jedes Solution Element eine eigene Zuverlässigkeitsanalyse erstellt.

### Vorgeschlagene Neufassung

> Die verbindlichen Anforderungen an Zuverlässigkeit, Verfügbarkeit und Wartbarkeit (RAM) werden in Kapitel 6.2 identifiziert und referenziert. Ihre Erfüllung wird in den jeweiligen Zuverlässigkeitsanalysen der betroffenen Solution Elements bewertet. Soweit erforderlich, werden die Anforderungen dort entsprechend dem Systemdesign den Solution Elements und nachgeordneten Elementen zugeordnet, aufgeteilt und verfeinert; die Rückverfolgbarkeit zur Anforderung in Kapitel 6.2 bleibt erhalten.

## Kapitel 4.2 – Verfügbarkeitsanforderungen

**Schweregrad:** Mittel

### Zitierter Ausgangstext

> Zur Sicherstellung eines angemessenen Systemverhaltens in Bezug auf die Verfügbarkeit ist eine umfassende Systemanalyse durchzuführen. Ziel dieser Analyse ist die Ermittlung der Verfügbarkeitskennzahlen einzelner Komponenten und Teilsysteme. Die Ergebnisse fließen in die übergeordnete Zuverlässigkeitsanalyse ein.

### Review-Kommentar

> Bezieht sich „übergeordnete Zuverlässigkeitsanalyse“ auf eine End-to-End-Analyse?

### Review-Feststellung

Die Formulierung im Singular kann eine einzige, übergeordnete End-to-End-Zuverlässigkeitsanalyse für das gesamte GA DIL nahelegen. Gemäß der in § 5.2.5 vorgesehenen Aufteilung werden jedoch eigenständige Zuverlässigkeitsanalysen je Solution Element erstellt. Der Absatz sollte daher festlegen, dass Verfügbarkeitskennzahlen je Solution Element ermittelt und in dessen eigener Zuverlässigkeitsanalyse bewertet werden. Eine übergreifende Zusammenführung ist damit nicht automatisch zugesagt.

### Vorgeschlagene Neufassung

> Zur Bewertung der Verfügbarkeit ist für jedes Solution Element eine Analyse der relevanten Komponenten und Teilsysteme innerhalb der dafür festgelegten Systemgrenze durchzuführen. Dabei sind die für das jeweilige Solution Element maßgeblichen Verfügbarkeitskennzahlen unter Berücksichtigung der vereinbarten Betriebs-, Installations- und Wartungsbedingungen zu ermitteln. Die Ergebnisse fließen in die jeweilige Zuverlässigkeitsanalyse des betreffenden Solution Elements ein und dienen dort der Bewertung der zugeordneten Verfügbarkeitsanforderungen. Abhängigkeiten zu anderen Solution Elements und externen Diensten sind gemäß den in § 5.2.5 festgelegten Analysegrenzen und Randbedingungen zu berücksichtigen. Eine End-to-End- oder übergeordnete Systemanalyse ist nur dann durchzuführen, wenn sie als eigener Nachweis für eine Systemanforderung festgelegt ist; sie ersetzt nicht die Zuverlässigkeitsanalysen der einzelnen Solution Elements.

## Kapitel 6.2 – RAM-Anforderungen

**Schweregrad:** Hoch

### Zitierter Ausgangstext

> Die RAM-bezogenen Kundenanforderungen, siehe [LH_OBB] und [PH_DSTW], müssen in den verschiedenen Entwicklungsphasen überprüft, bei Bedarf geklärt und entsprechend verfeinert werden. Falls zusätzliche RAM-Aspekte berücksichtigt werden müssen, um die RAM-bezogenen Kundenanforderungen zu erfüllen, sollten diese mit den entsprechenden Normen, insbesondere [EN 50126-1], übereinstimmen.  
> Die Erfüllung der RAM Anforderungen muss in den entsprechenden Zuverlässigkeitsanalysen der jeweiligen Solution Elemente nachgewiesen werden.

### Review-Feststellung

Kapitel 6.2 verweist auf Lastenheft und Pflichtenheft, weist die daraus geltenden RAM-Anforderungen aber nicht einzeln aus. Ohne eine Anforderungstabelle ist nicht nachvollziehbar, welche Anforderungen verbindlich sind, welchen Solution Elements sie gelten und wo ihre Erfüllung nachzuweisen ist. Anforderungen mit Status „Accepted“, „Draft“ oder „In negotiation“ müssen dabei unterscheidbar bleiben; nicht abgestimmte Entwürfe dürfen nicht als verbindliche Ziele erscheinen.

### Vorgeschlagene Ergänzung

> Die für den Geltungsbereich dieses RAM-Plans anwendbaren Anforderungen an Zuverlässigkeit, Verfügbarkeit und Wartbarkeit sind in Tabelle X einzeln aufgeführt. Die Tabelle wird aus den gültigen, freigegebenen Anforderungsbaselines [LH_OBB] und [PH_DSTW] erstellt und bei Änderungen dieser Baselines aktualisiert. Jede Anforderung ist einer oder mehreren Solution Elements zugeordnet. Für jede Zuordnung sind der erforderliche Nachweis und dessen Fundstelle in der jeweiligen Zuverlässigkeitsanalyse bzw. den zugehörigen RAM-Nachweisen anzugeben. Nicht freigegebene oder noch in Klärung befindliche Anforderungen werden mit ihrem jeweiligen Status als offene Punkte geführt und nicht als verbindliche RAM-Ziele behandelt.
>
> Für die vier Bezugsobjekte DSTW/DIL-CU, VIL, FES und OC bildet die folgende Tabelle den Verfügbarkeitsanteil ab. Sie enthält die in der eingesehenen SSS-Baseline mit Verfügbarkeit verknüpften Ziel-, Verteilungs-, Betriebs- und Überwachungsanforderungen. Die Quellenallokation ist wiedergegeben und ersetzt nicht die verbindliche Zuordnung zu den Solution Elements im RAM-Plan.
>
> | RAM-ID | Bezugsobjekt | Verfügbarkeitsanforderung / Kriterium | Status in der eingesehenen Quelle | Quellenallokation |
> | --- | --- | --- | --- | --- |
> | EL4-DIL-SSS-REQ-00406 | DSTW-ZE / DIL-CU | Gesamtverfügbarkeit Klasse 1: mindestens 99,999 %. | Accepted; Mandatory | DIL, VIL, IPS |
> | EL4-DIL-SSS-REQ-00407 | DSTW-ZE / DIL-CU | Verteilung Klasse 1: mindestens 99,9998 % bei MTTR 6 h; 99,9996 % bei MTTR 10 min; 99,9996 % bei MTTR 2 min. | Accepted; Mandatory | DIL, VIL, IPS |
> | EL4-DIL-SSS-REQ-00408 | DSTW-ZE / DIL-CU | Verfügbarkeit bei Ausfällen ohne betriebliche Auswirkungen: mindestens 99,7154 %. | Accepted; Mandatory | DIL, VIL, IPS |
> | EL4-DIL-SSS-REQ-00567 | DIL-CU / DSTW | Der Lieferant stellt Betriebssystem und operative Software bereit, die zur Erfüllung der Verfügbarkeitsklassen der DIL-CU erforderlich sind. | Accepted; Mandatory | DIL, VIL, IPS, ADM |
> | EL4-DIL-SSS-REQ-00587 | VIL-Instance | Gesamtverfügbarkeit Klasse 2: mindestens 99,995 %. | Accepted; Mandatory | DIL, VIL |
> | EL4-DIL-SSS-REQ-00569 | VIL-Instance | Verteilung Klasse 2: mindestens 99,9979 % bei MTTR 6 h; 99,999 % bei MTTR 10 min; 99,9996 % bei MTTR 2 min. | Accepted; Mandatory | DIL, VIL |
> | EL4-DIL-SSS-REQ-00570 | VIL-Instance | Verfügbarkeit bei Ausfällen ohne betriebliche Auswirkungen: mindestens 99,7154 %. | Accepted; Mandatory | DIL, VIL |
> | EL4-DIL-SSS-REQ-00573 | VIL | Kleinere Änderungen an Software (Patches) oder Hardware ohne betriebliche Einschränkungen durchführen. | Accepted; Mandatory | DIL, VIL, IPS |
> | EL4-DIL-SSS-REQ-00818 | VIL | Größere Software- oder Hardwareänderungen während Betriebspausen durchführen. | Accepted; Mandatory | DIL, VIL, IPS |
> | EL4-DIL-SSS-REQ-00574 | VIL | Betriebliche Ausfallzeit höchstens so lang wie Wiederanlauf des betroffenen Elements und dessen Wiederintegration in das Gesamtsystem. | Accepted; Mandatory | DIL, VIL, IPS |
> | EL4-DIL-SSS-REQ-00575 | FES | Gesamtverfügbarkeit Klasse 2: mindestens 99,995 %; die Verfügbarkeit der OC ist dabei ausdrücklich nicht einzurechnen. | Accepted; Mandatory | DIL, DFE |
> | EL4-DIL-SSS-REQ-00577 | FES | Verteilung Klasse 2: mindestens 99,9979 % bei MTTR 0,5 h; 99,999 % bei MTTR 10 min; 99,9996 % bei MTTR 2 min. | Accepted; Mandatory | DIL, DFE |
> | EL4-DIL-SSS-REQ-00578 | FES | Verfügbarkeit bei Ausfällen ohne betriebliche Auswirkungen: mindestens 99,7154 %. | Accepted; Mandatory | DIL, DFE |
> | EL4-DIL-SSS-REQ-00581 | OC | Gesamtverfügbarkeit Klasse 3: mindestens 99,99 %. | Accepted; Mandatory | DIL, DFE |
> | EL4-DIL-SSS-REQ-00582 | OC | Verteilung laut Anforderung Klasse 2: mindestens 99,9957 % bei MTTR 0,5 h; 99,999 % bei MTTR 10 min; 99,9996 % bei MTTR 2 min. | Accepted; Mandatory | DIL, DFE |
> | EL4-DIL-SSS-REQ-00583 | OC | Verfügbarkeit bei Ausfällen ohne betriebliche Auswirkungen: mindestens 99,7154 %. | Accepted; Mandatory | DIL, DFE |
> | EL4-DIL-SSS-REQ-00586 | OC, Block- und LCSI-Konverter | Softwareerweiterungen und -änderungen während Betriebspausen durchführen, um eine Unterschreitung der zulässigen Verfügbarkeit zu vermeiden. | In negotiation; nicht als verbindliches Ziel ansetzen | DIL, DFE |
> | EL4-DIL-SSS-REQ-00678 | Gesamtsystem einschließlich Teilsystemen | Verfügbarkeit überwachen, dokumentieren und analysieren sowie Ergebnisse dem Kunden mitteilen. | Accepted; Mandatory | DIL, VIL, IPS, ADM, DFE |
>
>
> **Hinweise zur Anwendung:** Die Statusangaben und Quellenallokationen entsprechen der eingesehenen *SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01*; sie sind vor Übernahme als verbindliche Projektanforderungen gegen die freigegebenen Lastenheft- und Pflichtenheftbaselines zu prüfen. Die SSS führt die Anforderungen 00406–00408 im Kontext der DIL-CU; die referenzierten Lastenhefttexte sprechen teilweise von der DSTW-ZE. Diese Bezugsobjekte sind im RAM-Plan eindeutig abzugleichen. Die Anforderungen 00581 und 00582 weisen zudem eine Klärungsbedürftigkeit auf: Für die OC wird eine Gesamtverfügbarkeit der Klasse 3 gefordert, während die Verteilung in 00582 ausdrücklich Klasse 2 zugeordnet ist. Die Anforderungen 00574 und 00573 enthalten keine vollständigen quantitativen Abnahmekriterien für Wiederanlauf/Wiederintegration bzw. „ohne betriebliche Einschränkungen“. Die Tabelle deckt die Verfügbarkeitsanforderungen der vier genannten Bezugsobjekte im eingesehenen SSS-Stand ab; sie ersetzt nicht die separate vollständige Ermittlung der Zuverlässigkeits- und Wartbarkeitsanforderungen. Weitere Anforderungsquellen sind im Dokumentenverzeichnis zu referenzieren.
