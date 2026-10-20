# RAM-Review – Safety Concept DFE, Kapitel 3.4 „Zuverlässigkeitskonzept“

**Prüfgegenstand:** [Safety Concept DFE, Ed01 Pd01 Work](../SafetyConcept/SafetyConcept_DFE_3BU_62800_1001_DUAPC_Ed01_Pd01_Work.docx)  
**Prüfumfang:** Kapitel 3.4 im Zusammenhang mit der DFE-Systembeschreibung und den verfügbaren DFE-RAM-Unterlagen  
**Ergebnis:** Das Kapitel beschreibt nützliche Architekturprinzipien, formuliert deren Wirkung jedoch teilweise absolut und lässt Randbedingungen, RAM-Eingaben und die konkrete Nachweisreferenz offen. Besonders die Zusagen zur Fehlerisolation und zur permanenten Überwachung aller Kommunikationsverbindungen sollten auf die tatsächlich spezifizierten Konfigurationen und nachgewiesenen Funktionen begrenzt werden.

## Executive Summary

Kapitel 3.4 sollte Zuverlässigkeit, Verfügbarkeit und Instandhaltbarkeit kurz voneinander abgrenzen und klarstellen, dass die beschriebenen Architekturprinzipien den RAM-Nachweis unterstützen, ihn aber nicht ersetzen. Die Aussagen zu Fehlerisolation, Modularität und Kommunikationsüberwachung benötigen überprüfbare Geltungsgrenzen. Für Lieferantenkomponenten sollten RAM-Eingabedaten getrennt von den Sicherheitsnachweisen bewertet werden. Schließlich sollte der gültige DFE-RAM-Plan einschließlich Edition und Geltungsbereich eindeutig referenziert werden.

## Findings

| ID / Priorität | Originaltext | Befund und empfohlene Ergänzung |
|---|---|---|
| RAM-01 / Mittel – RAM-Ziel und Abgrenzung | „Die DFE-Lösung ist als verteiltes feldseitiges System konzipiert. Das Zuverlässigkeitskonzept basiert auf modularen Komponenten, standardisierten Schnittstellen sowie einer konsequenten Trennung der einzelnen Funktionen. Ziel ist es, die Auswirkungen von Fehlern auf den jeweils betroffenen Anlagenteil zu begrenzen und einen wartungsfreundlichen Betrieb zu ermöglichen.“ | Der Absatz nennt Architekturprinzipien, grenzt Zuverlässigkeit, Verfügbarkeit und Instandhaltbarkeit aber nicht voneinander ab. Verdeutlichen, dass diese Prinzipien die RAM-Leistung unterstützen, jedoch keinen quantitativen Nachweis darstellen. Auf die geltenden DFE-RAM-Ziele und -Nachweise verweisen; keine zusätzlichen Kennzahlen im Safety Concept einführen. |
| RAM-02 / Hoch – Fehlerisolation und gemeinsame Abhängigkeiten | „Die Architektur der DFE folgt dem Grundsatz, dass Ausfälle einzelner Komponenten möglichst lokal begrenzt bleiben. Ein Ausfall eines DFE-Subsystems darf nicht zu einer Beeinträchtigung unabhängiger DFE-Subsysteme führen. Hierzu werden die verschiedenen Funktionen auf getrennte Object Controller und Interface Converter verteilt und über definierte Schnittstellen miteinander verbunden.“ | „Darf nicht“ ist eine absolute Zusage; „unabhängige DFE-Subsysteme“ und Systemgrenze sind nicht definiert. Die Aussage auf freigegebene Anforderungen und Konfigurationen begrenzen. Gemeinsame FES-Versorgung, Netzwerk und sonstige Infrastruktur als mögliche gemeinsame Fehlerursachen berücksichtigen. Die Wirksamkeit der Fehlerisolation ist nachzuweisen. Die RAM-Designregeln enthalten hierzu konkretere Anforderungen, insbesondere zur Isolation eines OC-Ausfalls gegenüber anderen OCs derselben FES. |
| RAM-03 / Mittel – Austausch und Erweiterung | „Die Field Element Stations (FES) stellen die physische Infrastruktur für den Betrieb der DFE-Komponenten bereit. Durch den modularen Aufbau können Komponenten ausgetauscht oder erweitert werden, ohne grundlegende Änderungen an der Gesamtarchitektur durchführen zu müssen. Die verschiedenen Baugrößen der FES ermöglichen eine an den jeweiligen Anwendungsfall angepasste Skalierung.“ | Die Austausch- und Erweiterungsaussage enthält keine Betriebsbedingungen oder Kriterien für die Wiederinbetriebnahme. Auf definierte austauschbare Einheiten, freigegebene FES-Konfigurationen und RAM-Designregeln begrenzen sowie auf Installations- und Instandhaltungsanweisungen verweisen. Nach Austausch oder Erweiterung können Konfigurations-, Funktions- oder Integrationsprüfungen erforderlich sein. |
| RAM-04 / Hoch – Kommunikationsschnittstellen und Überwachung | „Die Kommunikation zwischen den DFE-Komponenten erfolgt über standardisierte digitale Schnittstellen. Kommunikationsverbindungen werden permanent überwacht. Fehler in der Kommunikation werden erkannt und führen zu definierten Fehlerreaktionen der betroffenen Teilsysteme.“ | Die pauschale Aussage passt nicht auf alle im Dokument beschriebenen Pfade, darunter die parallele Schnittstelle des IFC-LCSI zu Bestands-EKSA. Umfang der Überwachung, Fehlererkennung und Fehlerreaktion sind schnittstellen- und subsystemabhängig. Kommunikationspfade unterscheiden und auf die zugehörigen Schnittstellenspezifikationen bzw. Supplier Safety Cases verweisen. Nur belegte Überwachungs- und Reaktionsfunktionen behaupten. |
| RAM-05 / Mittel – Lieferantennachweise | „Die im Rahmen von Intercompany Orders bzw. durch externe Lieferanten bereitgestellten Subsysteme OC-DCA3, OC-AzLM und IFC-LCSI verfügen über eigenständige Entwicklungs-, Verifikations- und Nachweisprozesse. Die zugehörigen Zuverlässigkeits- und Sicherheitsnachweise werden durch die jeweiligen Lieferorganisationen bereitgestellt und als Eingangsdokumente für die DFE-Integrationsbewertungen verwendet.“ | RAM- und Sicherheitsnachweise nicht gleichsetzen. Für die konkrete Konfiguration sind die relevanten Zuverlässigkeits-/Verfügbarkeitsdaten, Einsatz- und Umgebungsbedingungen, Annahmen, Diagnose- und Instandhaltungsdaten sowie gültigen HW-/SW-Stände gesondert als RAM-Eingaben zu identifizieren und auf Vollständigkeit und Anwendbarkeit zu prüfen. Offene Annahmen und Abweichungen in der Integrationsbewertung nachverfolgen. |
| RAM-06 / Mittel – Ziele, Baseline und Nachweis | „Die detaillierten Zuverlässigkeitskennwerte, Verfügbarkeitsziele und Nachweise werden im RAM Plan sowie in den zugehörigen Sicherheits- und Zuverlässigkeitsnachweisen der einzelnen Subsysteme spezifiziert.“ | Die Referenz ist nicht eindeutig und trennt RAM- und Sicherheitsnachweise nicht klar. Den für die Freigabe gültigen DFE-RAM-Plan mit Edition und Geltungsbereich angeben. Der verfügbare DFE-RAM-Plan Ed02 nennt unter anderem FES-Verfügbarkeit K2 ≥ 99,995 % (Anforderung 02_124), FES für manuelle Fehlerbehebung K2 ≥ 99,9979 % (02_127) und OC für automatische Fehlerbehebung innerhalb von 2 min K3 ≥ 99,9996 % (02_138). Diese Ziele gelten jeweils nur im definierten Scope und dürfen nicht pauschal jeder DFE-Komponente oder dem Safety Case zugeordnet werden. Prüfen, ob diese Edition der gültigen Freigabebaseline entspricht. |

## Risiken

- Die Formulierung einer uneingeschränkten Fehlerisolation könnte eine nicht nachgewiesene Verfügbarkeit einzelner DFE-Bereiche nahelegen.
- Gemeinsame FES-, Versorgungs- oder Netzabhängigkeiten können mehrere Komponenten gleichzeitig beeinträchtigen und so die erwartete Fehlerbegrenzung aufheben.
- Eine pauschale Zusage permanenter Kommunikationsüberwachung kann einen höheren Überwachungsumfang suggerieren, als einzelne Schnittstellen tatsächlich bereitstellen.
- Ohne eindeutig referenzierte RAM-Baseline sind Zielwerte und Verifikationsnachweise nicht sicher auf die freizugebende DFE-Konfiguration rückführbar.

## Empfehlungen und Maßnahmen

1. RAM-, Verfügbarkeits- und Instandhaltbarkeitsaussagen in Kapitel 3.4 als Konzeptbeschreibung kennzeichnen und auf den quantitativen RAM-Nachweis verweisen.
2. Die absolute Fehlerisolationsaussage auf konkrete RAM-Designregeln und freigegebene Konfigurationen begrenzen; gemeinsame Infrastrukturabhängigkeiten berücksichtigen.
3. Die Austausch-/Erweiterungsaussage durch Randbedingungen und Verweise auf Betriebs- und Instandhaltungsanweisungen absichern.
4. Kommunikationsüberwachung und Fehlerreaktionen je Schnittstellenpfad beschreiben oder auf die jeweilige Spezifikation bzw. den Supplier Safety Case verweisen.
5. Für Lieferantenkomponenten die RAM-Eingaben explizit von Sicherheitsnachweisen trennen und auf Anwendbarkeit für die DFE-Konfiguration prüfen.
6. Den gültigen DFE-RAM-Plan mit kontrollierter Ausgabe und Geltungsbereich referenzieren und die Requirement-IDs mit der Freigabebaseline abgleichen.

## Quellen und Grenzen der Prüfung

- Safety Concept DFE, Ed01 Pd01 Work – Kapitel 3.4 und DFE-System-/Schnittstellenbeschreibung.
- Project Specific RAM Plan DFE, Ed02 – RAM Design Rules und Verfügbarkeitsanforderungen.
- SSS Field Element Controller and Stations, Ed02 Pd01 – Architektur- und Schnittstellenkontext.
- Review des DFE-RAM-Plans Ed03 Pd01 – zur Einordnung des vorhandenen RAM-Planungsstands.

Die verfügbaren Projektunterlagen belegen nicht abschließend, ob der RAM-Plan Ed02 weiterhin die freigegebene Baseline ist. Die Zahlen und Requirement-IDs sind deshalb vor Übernahme in ein freigegebenes Safety Concept gegen die aktuelle Konfigurations- und Anforderungsbaseline zu prüfen. Dies ist eine RAM-Fachprüfung, keine vollständige Normkonformitätsbewertung.

## Applied Skills

Document Review, Railway-RAM und RAM-Metrics.
