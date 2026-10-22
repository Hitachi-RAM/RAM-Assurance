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

### Vorgeschlagene Antwort an den Reviewer

> Der Hinweis wird aufgenommen. Kapitel 5.2.5 wird um eine Abgrenzung je Zuverlässigkeitsnachweis ergänzt. Komponenten, die einem Solution Element zugeordnet sind, werden in dessen eigener Analyse innerhalb der technischen und funktionalen Systemgrenze bilanziert. Komponenten und Dienste außerhalb dieser Grenze – einschließlich AG-Beistellungen, externer Netze sowie externer Strom- und Zeitversorgung – werden nicht stillschweigend ausgeschlossen, sondern bei Einfluss auf die nachgewiesene Funktion als Randbedingungen mit Datenquelle, Annahmen und Auswirkung dokumentiert. Die vertragliche Zuordnung zu AN, AG oder Dritten wird separat anhand der gültigen Projekt-Liefer- und Verantwortungsmatrix bestätigt. Eine übergreifende Systembilanz erfolgt nur, soweit eine Systemanforderung dies verlangt, und ohne doppelte Bilanzierung.

### Review-Feststellung und erforderliche Änderung

Der Ausgangstext beschreibt eine Zuverlässigkeitsanalyse im Singular für das technische Produkt GA DIL und definiert weder Analysegrenzen noch die Behandlung gemeinsamer Infrastruktur und externer Abhängigkeiten. Dadurch bleibt offen, für welche Teile ein Nachweis geführt wird und ob fremdverantwortete oder beigestellte Einrichtungen in die Berechnung eingehen. Kapitel 5.2.5 sollte daher nicht nur auf die Systembeschreibung verweisen, sondern je Nachweis die technischen Ein- und Ausschlüsse sowie die Zuständigkeit für Analyse und Eingangsdaten festlegen.

Die verfügbaren Planangaben beschreiben eine Cloud-Infrastruktur mit Servern, Datenspeicher, Cloud-/Virtualisierungssteuerung, hochverfügbarem Netzwerk, Availability Zones, VIL-Anwendungen und EULYNX-Feldelementen. Sie belegen jedoch nicht abschließend die vertragliche AN-/AG-Zuordnung der einzelnen Komponenten oder der Strom- und Zeitversorgung. Diese Zuordnung darf nicht aus der technischen Architektur abgeleitet oder erfunden werden; sie ist gegen die gelenkte Liefer- und Verantwortungsmatrix zu bestätigen. Bis dahin ist sie als offener Punkt zu führen.

### Wo den RAM-Plan ändern?

1. **Kapitel 5.2.5, direkt nach dem einleitenden Absatz:** den folgenden Abgrenzungstext und die Matrix aufnehmen. Die bisherige Aussage zur GA-DIL-Zuverlässigkeitsanalyse im Singular ist durch die Aussage zu eigenständigen Analysen je Solution Element zu ersetzen.
2. **Kapitel 3/Systembeschreibung oder ein gelenkter Anhang:** die Komponenten- und Schnittstellenliste mit konkreten Bezeichnungen/IDs, Zuordnung zu Solution Elementen sowie AN-/AG-/Drittverantwortung ergänzen. Diese Liste bildet die überprüfbare Referenz für die Matrix in Kapitel 5.2.5.
3. **Jeder Zuverlässigkeitsnachweis:** die dort tatsächlich verwendete Konfiguration, einbezogenen Komponenten, Randbedingungen, Datenquellen, Annahmen und Ausschlüsse ausweisen. Änderungen an Konfiguration oder Verantwortlichkeiten lösen eine Aktualisierungsprüfung aus.

### Vorgeschlagene Neufassung für Kapitel 5.2.5

> **Zuverlässigkeitsanalysen je Solution Element und Abgrenzung**
>
> Für jedes Solution Element ist eine eigene Zuverlässigkeitsanalyse zu erstellen. Jede Analyse bewertet die dem Solution Element zugeordneten RAM-Anforderungen innerhalb der nachfolgend festgelegten technischen und funktionalen Analysegrenze. Zufällige Hardwareausfälle werden innerhalb der jeweiligen Grenze bilanziert. Die Analysegrenze richtet sich nach Funktionen, Architektur und Komponenten-/Schnittstellenzuordnung; sie ist nicht automatisch identisch mit der vertraglichen Liefer- oder Verantwortungsgrenze. Die Zuverlässigkeitsanalysen der Solution Elements bleiben eigenständige Nachweise.
>
> Die folgende Tabelle legt die grundsätzliche Behandlung der Systemelemente fest. Die konkreten Komponenten, Schnittstellen, Lieferverantwortlichen und Betreiber sind in der gelenkten Komponenten- und Verantwortungsmatrix des Projekts mit Bezeichnung bzw. ID einzutragen und je Analyseversion zu referenzieren.
>
> | Nachweis / Element | In der jeweiligen Analyse zu bilanzieren | Außerhalb der Komponentenbilanz: als Randbedingung zu behandeln |
> | --- | --- | --- |
> | GA DIL / Systemintegration | Die dem GA DIL-Nachweis ausdrücklich zugeordneten Funktionen und Systemanforderungen. Beiträge von VIL, IPS und DFE sind über deren eigene Analysen und Schnittstellenkennwerte zu übernehmen; ihre Komponenten-Ausfallraten werden nicht ein zweites Mal berechnet. | Gemeinsame Infrastruktur und externe Dienste, soweit sie außerhalb der GA-DIL-Komponentengrenze liegen. Nur wenn ein Systemnachweis dafür gefordert ist, werden ihre Beiträge in einer separaten Systembilanz zusammengeführt. |
> | VIL | Die gemäß Komponenten-/Verantwortungsmatrix dem VIL zugeordneten VIL-Anwendungen, VIL-Instanzen und VIL-eigenen Komponenten innerhalb der VIL-Grenze. | IPS-Hostplattform, physische Infrastruktur und Netzwerke, DFE sowie externe Dienste, sofern sie nicht dem VIL zugeordnet sind. Ihre Verfügbarkeit und Ausfallwirkung sind aus den verantwortlichen Nachweisen bzw. Eingangsdaten als Abhängigkeit anzusetzen. |
> | IPS Solution | Die der IPS Solution zugeordneten Server, Speicher, Virtualisierungs-/Cloud-Steuerung und internen Plattformnetzwerke, soweit diese Komponenten laut gelenkter System- und Verantwortungsmatrix Bestandteil der IPS-Grenze sind. Jede Komponente wird nur in einem Nachweis mit ihrer Ausfallrate bilanziert. | VIL- und DFE-Anwendungen sowie Standort- und Rechenzentrumsinfrastruktur, die außerhalb der IPS-Grenze liegen. Abhängigkeiten und gemeinsame Ausfallursachen sind mit den jeweiligen Betreibern zu klären und als Randbedingungen zu dokumentieren. |
> | DFE | Die dem DFE zugeordneten Feldelementstationen, Objektcontroller und Schnittstellenumsetzer gemäß System-/Komponentenliste. Abweichende Anforderungsgrenzen – beispielsweise eine Anforderung, die die Verfügbarkeit von Objektcontrollern ausdrücklich ausnimmt – sind für den jeweiligen Nachweis gesondert einzuhalten. | Externe streckenseitige Einrichtungen, Übertragungswege oder Dienste, soweit sie außerhalb der DFE-Grenze liegen; ihre funktionalen Auswirkungen werden als Abhängigkeit betrachtet. |
> | AN-Komponenten | In den Nachweis des Solution Elements aufnehmen, dem die Komponente technisch zugeordnet ist; für diese Komponente sind Konfiguration, Mengenansatz, Ausfalldaten und Wartungs-/Wiederherstellungsdaten anzugeben. AN-Zuständigkeit allein begründet keine doppelte Erfassung in mehreren Analysen. | Komponenten des AN, die außerhalb der jeweiligen Nachweisgrenze liegen, werden wie andere externe Abhängigkeiten behandelt und nur bei Bedarf in einer Systembilanz berücksichtigt. |
> | AG-Beistellungen / Drittkomponenten | Nur dann in eine Komponentenbilanz aufnehmen, wenn sie innerhalb der festgelegten Systemgrenze des konkreten Nachweises liegen und belastbare Eingangsdaten verfügbar sind. | Liegen sie außerhalb der Nachweisgrenze, sind sie mit Betreiber, Verfügbarkeit/Ausfalldaten, Betriebsbedingungen und Einfluss auf das Ergebnis als Randbedingungen zu dokumentieren; andernfalls sind Datenlücken als offene Punkte auszuweisen. |
> | Netzwerke und Kommunikationsverbindungen | Interne physische oder logische Netze werden genau dem Solution Element zugeordnet, das sie gemäß gelenkter Architektur-/Verantwortungsmatrix bereitstellt und für das ein Nachweis geführt wird. Redundante Pfade und gemeinsame Komponenten sind dort entsprechend der tatsächlichen Topologie abzubilden. | Externe/AG-Netze, Übergabestrecken und Kommunikationsdienste außerhalb dieser Zuordnung werden als Randbedingungen erfasst. Auswirkungen von Netzausfällen auf die nachgewiesene Funktion dürfen nicht durch den Ausschluss der Netzkomponente verborgen werden. |
> | Stromversorgung | Geräteinterne Netzteile und Versorgungskomponenten innerhalb der Produkt-/Komponentengrenze werden in der zugeordneten Komponentenbilanz berücksichtigt. | Standortversorgung, Gebäudeinstallation, USV/Notstrom und kundenseitige Einspeisung werden als Randbedingung behandelt, sofern sie nicht ausdrücklich Bestandteil eines Solution Elements oder des konkreten Systemnachweises sind. Quelle, Redundanz, Überbrückungszeit und Betreiber sind anzugeben, sofern für die RAM-Bewertung relevant. |
> | Zeitversorgung | Interne Zeitverteilungskomponenten werden dem Solution Element zugeordnet, das sie bereitstellt und betreibt, und dort bilanziert. | Externe Zeitquelle und kundenseitiger Zeitdienst werden außerhalb der Komponentenbilanz als Randbedingung behandelt. Quelle, Schnittstelle, Verfügbarkeit und Verhalten bei Zeitverlust sind für abhängige Funktionen zu dokumentieren. |
> | Externe Dienste und Schnittstellen | In die Analyse gehen die dem Solution Element zugeordneten Schnittstellenkomponenten und die aus Anforderungen resultierenden Funktionsfolgen eines Dienstausfalls ein. | Dienste außerhalb der Systemgrenze werden nicht als eigene Hardware-Ausfallraten des Solution Elements bilanziert. Ihre Verfügbarkeit, Wiederherstellungsannahmen und Auswirkungen sind als Randbedingungen anzusetzen. Die im Projekt-Schnittstellenverzeichnis tatsächlich relevanten Dienste sind dort namentlich zu führen. |
>
> Die Verantwortlichkeiten für Analyse und Datenlieferung sind je Solution Element wie folgt festzulegen: Der RAM-Verantwortliche des Solution Elements erstellt und pflegt dessen Analyse; der Systemarchitekt bestätigt technische Systemgrenzen, Komponentenallokation und Schnittstellen; der PM bzw. die vertraglich benannte Stelle bestätigt AN-/AG-/Drittverantwortung anhand der gültigen Liefer- und Verantwortungsmatrix. Komponentenverantwortliche, Betreiber und Diensteigner liefern Konfiguration, Betriebsprofil, Ausfall-/Verfügbarkeitsdaten sowie Wartungs- und Wiederherstellungsdaten für die von ihnen verantworteten Elemente. Der RAM-AM koordiniert die Analysegrenzen, Nachweisplanung und Nachverfolgung offener Punkte.
>
> In jedem Nachweis sind die analysierte Konfiguration und die Systemgrenze, einbezogene Komponenten, als Randbedingungen behandelte oder ausgeschlossene Elemente, Zuordnungsbegründung, verwendete Daten und Quellen sowie der Einfluss wesentlicher Annahmen auf das Ergebnis anzugeben. Fehlende oder nicht bestätigte Daten und Verantwortlichkeiten sind als offene Punkte mit Verantwortlichem und Klärungstermin zu dokumentieren. Wenn eine Systemanforderung die Verfügbarkeit über mehrere Solution Elements oder externe Abhängigkeiten verlangt, ist hierfür bei Bedarf eine gesonderte Systembilanz aus den jeweiligen Nachweisen zu erstellen. Bereits in einem Elementnachweis bilanzierte Komponenten werden nicht erneut angesetzt. Bei Änderungen der Architektur, Konfiguration, Schnittstellen, Liefer-/Betriebsverantwortung oder Eingangsannahmen sind die betroffenen Analysen zu überprüfen und erforderlichenfalls zu aktualisieren.

### Zu bestätigende Nachweise vor Freigabe

- Gültige Komponenten-/Stücklisten und Konfigurationsstände je Solution Element einschließlich Server, Speicher, Cloud-/Virtualisierungssteuerung, physische und logische Netzwerke sowie Feldelemente.
- Gültige Projekt-Liefer- und Verantwortungsmatrix mit benanntem AN, AG bzw. Drittbetreiber je Komponente, Netzwerk, Strom-/Zeitversorgung und externem Dienst.
- Schnittstellen- und Betriebsdaten für externe Netze/Dienste sowie Versorgungsdaten für Strom und Zeit; fehlende Werte sind als Annahmen bzw. offene Punkte auszuweisen.
- Bestätigung, welche RAM-Anforderungen einen reinen Solution-Element-Nachweis und welche einen übergreifenden Systemnachweis verlangen.

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
