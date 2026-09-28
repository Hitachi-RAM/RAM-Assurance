# ELEKTRA SBB – Vergleich Angebot und SBB-Anforderungen

**Stand:** 28.09.2026  
**Projekt:** Anlagenbeobachtung ELEKTRA CH / SBB

## 1. Grundlage

Diese Zusammenfassung vergleicht das ursprüngliche Hitachi-Angebot zur erweiterten Anlagenbeobachtung mit der SBB-Rückmeldung vom 16.07.2025, die am 22.09.2026 weitergeleitet wurde.

Referenzen:

- [Hitachi-Angebot vom 22.07.2026](20260722_Angebot_Anlagenbeobachtung%20CH_Elektra.docx)
- [Hitachi-Angebot vom 24.07.2026](20260724_Angebot_Anlagenbeobachtung%20CH_Elektra.docx)
- [Hitachi-Angebot vom 17.08.2026 (unterzeichnet)](20260817_Angebot_Anlagenbeobachtung%20CH_Elektra_signed.pdf) ← **aktuellste Version mit finalen Preisen**
- [SBB-Rückmeldung / Weiterleitung](FW_%20Unser%20Angebot%20_Erweiterte%20Anlagebeobachtung%20ELEKTRA1_.msg)
- [SBB-Prüfliste kritischer Baugruppen](Anfrage%20Pr%C3%BCfung%20von%20Baugruppen%20aus%20AAL_2025-07-04_Ed1p03-AT.xlsx)

### Aktualisierung: Angebot vom 17.08.2026

Das neue, unterzeichnete Angebot vom 17.08.2026 konkretisiert die Preise und Termine definitiv:

| Element | Wert |
| --- | --- |
| **Initialaufwand** | 122.083,00 EUR |
| **Anlagenbeobachtung 3 Jahre** | 347.601,30 EUR |
| **Obsoleszenz Management 3 Jahre** | 84.966,00 EUR |
| **Gesamt für 3 Jahre** | **554.650,30 EUR** |
| **Bestellung** | Q4/2026 |
| **Start Beobachtung** | Q3/2027 |
| **1. Report** | Ende Q1/2028 |
| **Letzter Report (3-Jahre-Paket)** | Ende Q3/2030 |
| **Erste Kündigung möglich** | Ende Q4/2029 |
| **Jährliche Verlängerung danach** | 144.189,10 EUR/Jahr |
| **Gültig bis** | 30.10.2026 |

## 2. Vergleich

| Thema | Hitachi-Angebot (17.08.2026) | SBB-Erwartung | Status |
| --- | --- | --- | --- |
| Hauptziel | Halbjährliche Anlagenbeobachtung mit RAM-/Safety-Bewertung plus Obsoleszenzmanagement | Praxisnahe Bewertung der verbleibenden ELEKTRA-1-Lebensdauer | ⚠️ Eingrenzung offen |
| Fokus | ELEKTRA 1 als Zielsystem; ELEKTRA 2 zusätzlich als statistische Referenzbasis, weil 9 ELEKTRA-1-Anlagen allein zu wenig Daten liefern | Primär ELEKTRA 1 + obsolete/kritische Hardware | ✓ Begründet |
| Hardwareumfang | Schwerpunkt Interface-Leiterplatten + Relaisbeanspruchung | Zusätzlich Rechner-Hardware | ⚠️ Nicht explizit adressiert |
| Methodik | DGP-Auswertung, Relais-Schaltspiele, erwartete vs. tatsächliche Reparaturen | Ausfallstatistik, Fehlerbilder, Fehlercluster, Zuordnung zu Baugruppen | ⚠️ Unterschiedliche Ansätze |
| Altersbewertung | Im aktuellen CH-Angebot nicht ausdrücklich beschrieben | 5-Jahres-Scheinen allein nicht zielführend | ⚠️ Konkretisierung ausstehend |
| Prognose | Technische Einschätzung hauptsächlich bis nächster Bericht; **Hinweis:** "Zeitraum ausgewiesen, in dem nicht mit signifikantem Fehleranstieg zu rechnen ist" (aber keine ungebundene Lebensdauerprognose) | Aussage über restliche ELEKTRA-1-Lebensdauer gewünscht | ⚠️ Vorsichtlich formuliert |
| Maßnahmen | Empfehlungen bei Auffälligkeiten; Obsoleszenzmaßnahmen mit Bewertung | Konkrete Maßnahmen für Ziel-Lebensdauer (Bevorratung, Know-how-Sicherung) | ⚠️ Eher strategisch als konkret |
| ELEKTRA 2 | Statistische Referenzbasis wegen geringer Rechnerleiterplatten pro EL1-Anlage | Interface-Karten von EL2 separat im Obsoleszenzmanagement; statistische Nutzung noch abzugrenzen | ✓ Begründung plausibel |
| SBB-Datenlieferung | Zuarbeit über Service-Portal vorausgesetzt | Service-Portal nicht nutzbar; SBB arbeitet mit SIP 2.0 | ⚠️ Kritisch: Datenquelle klärt nicht |
| Preis | **554.650,30 EUR** für 3 Jahre (incl. Initialaufwand); danach **144.189,10 EUR/Jahr** | Keine Budgetvorgabe genannt | ✓ Nun konkret |
| Timeline | Start Q3/2027; 1. Report Ende Q1/2028; Letzter Report Ende Q3/2030 | Keine Timeline genannt | ✓ Nun konkret |
| Ergebnis | Halbjährliche firmeneigene Erklärung zur Gültigkeit des Sicherheitsnachweises | Fehler- und Baugruppenanalyse mit Abgleich gegen SBB-Obsoleszenzplan | ⚠️ Anderer Schwerpunkt |

## 3. Was SBB vermutlich beauftragen möchte

SBB möchte im Kern wissen:

> Welche kritischen ELEKTRA-1-Baugruppen fallen tatsächlich aus, wie entwickeln sich die Fehler, wie lange ist die Hardware voraussichtlich noch nutzbar und welche konkreten Maßnahmen sind erforderlich?

Das gewünschte Reporting soll voraussichtlich:

1. kritische Baugruppen aus SBB-Risikoanalyse und Hitachi-Einschätzung festlegen;
2. historische Ausfälle und Reparaturen auswerten;
3. Fehlerbilder möglichst detailliert erfassen;
4. Fehler zu Fehlerclustern zusammenfassen;
5. Häufigkeit und Trend je Fehlercluster bestimmen;
6. verantwortliche Baugruppen oder Bauteile identifizieren;
7. die Ergebnisse mit dem SBB-Obsoleszenzplan abgleichen;
8. Lücken zwischen Risikoanalyse, Ausfallstatistik und Obsoleszenzplan aufzeigen;
9. Maßnahmen für die Restlebensdauer ableiten, zum Beispiel Bevorratung, Know-how-Sicherung, Last-Time-Buy oder technische Ersatzlösungen.

Damit ist der SBB-Wunsch eher ein integriertes **Failure-, RAM- und Obsoleszenz-Reporting für ELEKTRA 1** als eine unveränderte Übernahme des AT-Anlagenbeobachtungsreports.

### Statistische Ausgangslage

Die ursprüngliche Hitachi-Annahme war, dass die neun verbleibenden ELEKTRA-1-Anlagen allein keine ausreichend große statistische Basis bilden. Zusätzlich ist pro ELEKTRA-1-Anlage nur eine begrenzte Anzahl von Rechnerleiterplatten verbaut. Deshalb sollten insbesondere vergleichbare Interface- und Rechnerleiterplatten aus ELEKTRA 2 in die statistische Betrachtung einbezogen werden.

Dabei müssen zwei Ebenen getrennt werden:

1. **Zielbewertung:** Aussagen über die kritischen Baugruppen und die Restlebensdauer der ELEKTRA-1-Anlagen.
2. **Statistische Referenzbasis:** Zusammengefasste oder vergleichbare ELEKTRA-2-Daten zur Erhöhung der Stichprobengröße, sofern Baugruppe, Belastung, Einsatzbedingungen und Ausfallmechanismus ausreichend vergleichbar sind.

Eine gemeinsame Datenbasis darf daher nicht automatisch als Aussage über ELEKTRA 1 interpretiert werden. Der Bericht sollte klar ausweisen, welche Ergebnisse ELEKTRA-1-spezifisch sind und welche nur durch die ELEKTRA-2-Referenzpopulation statistisch stabilisiert werden.

### Herkunft der 5-Jahres-Scheiben

Die 5-Jahres-Scheiben stehen **nicht** im aktuellen CH-Angebot vom 22.07.2026 oder 24.07.2026. SBB erwähnt sie in der Rückmeldung vom 16.07.2025 zum früheren Hitachi-Angebot vom 14.04.2025 und lehnt diese Unterteilung als alleinige Methode ab. Der AT-Referenzreport verwendet Altersklassen ebenfalls als ergänzende Auswertung der installierten Basis.

## 4. Daten, die SBB voraussichtlich bereitstellen kann

### 4.1 Bereits konkret genannt

| Daten/Information | Mögliche Verwendung |
| --- | --- |
| SIP-2.0-Tickets | Störungen, Fehlerbilder und Fehlerhistorie |
| Wöchentliche SIP-Auszüge | Regelmäßige Aktualisierung der Statistik |
| SBB-Risikoanalyse | Auswahl kritischer Baugruppen |
| SBB-Obsoleszenzplan / OMP | Abgleich mit empirischer Ausfallanalyse |
| Historische Ausfallstatistik | Trend- und Häufigkeitsanalyse |
| Fehlerbeschreibungen | Bildung von Fehlerclustern, abhängig von der Datenqualität |
| Lagerdaten Zürich | Bestands- und Versorgungsbewertung |
| Anlagen- und Baugruppenlisten | Definition von Scope und installierter Basis |

### 4.2 Für die Auswertung anzufordernde Felder

- Ticket-ID
- Anlage und Betriebsstelle
- ELEKTRA-Version
- Baugruppe, LRU, Leiterplattentyp und Materialnummer
- Fehlerdatum und Meldedatum
- Fehlerbild und Fehlercode
- Auswirkung auf den Betrieb
- Austausch oder Reparatur
- Rücksende-/Reparaturdatum
- Reparaturergebnis
- Wiederholungsfehler
- Ausfall- oder Stillstandszeit
- Einbauort bzw. Schrank
- Seriennummer, soweit verfügbar
- Zuordnung zu Risiko- oder Sicherheitsklasse

## 5. Daten, die Hitachi ergänzen müsste

Für ein belastbares Reporting müssten von Hitachi zusätzlich bereitgestellt oder erstellt werden:

- Reparaturdaten aus Qualitäts- und Reparatursystemen;
- erwartete Fehlerraten oder Referenzwerte;
- installierte Hardwarebasis je Anlage;
- DGP-Daten, sofern für ELEKTRA 1 verfügbar;
- Zuordnung von Fehlern zu Baugruppen und Bauteilen;
- Reparierbarkeit und technischer Obsoleszenzstatus;
- Lagerbestände bei HR-AUT;
- Last-Time-Buy-Informationen;
- bekannte systematische Fehler und Reparaturmaßnahmen;
- gegebenenfalls Referenzdaten aus ELEKTRA 2 oder Österreich.

## 6. Kritische Datenlücken und Klärpunkte

Vor einer Beauftragung müssen mindestens folgende Punkte geklärt werden:

- Sind die SIP-Tickets vollständig genug, um Fehlerbilder zu clustern?
- Sind Reparaturen eindeutig Anlage und Baugruppe zugeordnet?
- Sind mindestens drei Jahre historische Daten verfügbar?
- Gibt es belastbare DGP-Daten für ELEKTRA 1?
- Ist die Rechner-Hardware vollständig in der installierten Basis erfasst?
- Sind Ausfall- und Reparaturdatum getrennt verfügbar?
- Dürfen Daten aus Österreich nur qualitativ oder auch quantitativ verwendet werden?
- Welche Aussage zur Restlebensdauer ist fachlich und haftungsrechtlich zulässig?
- Soll das Ergebnis ein halbjährlicher Report, ein einmaliger Lebensdauerbericht oder beides sein?

### 6.1 Update: Angebot 17.08.2026 — Welche Fragen beantwortet sind

Das neue, unterzeichnete Angebot vom 17.08.2026 konkretisiert folgende Punkte:

| Frage | Status | Erkenntnis aus August-Angebot |
| --- | --- | --- |
| Daten-Zuordnung | ✓ Adressiert | "Zuordnung der einzelnen Reparaturen zu den Betriebsstellen" wird gefordert (optimal rückwirkend 3 Jahre, minimum 6 Monate); danach monatliche Lieferung |
| Installierte Hardware | ✓ Adressiert | "Vollständige Aufstellung ∑ Summe der eingesetzten Interface-Leiterplatten pro Betriebsstelle" wird gefordert; auch Umbauten müssen erfasst sein |
| Rohdaten-Frequenz | ✓ Adressiert | "Die entsprechenden Rohdaten werden monatlich zur Verfügung gestellt" |
| Reporting-Rhythmus | ✓ Konkret | Halbjährliche Reports; 1. Report Ende Q1/2028; letzte Report Ende Q3/2030 |
| Scope of Work | ✓ Konkret | Fokus: Relais-Alterung, Interface-Board-Beanspruchung, erwartete vs. empirische Fehlerraten; firmeneigene Sicherheitserklärung halbjährlich |
| Restlebensdauer-Aussage | ⚠️ Vorsichtig | "Zeitraum ausgewiesen, in dem im Rahmen der technischen Möglichkeiten nicht mit einem signifikanten Anstieg der Fehlerrate zu rechnen ist" — aber keine ungebundene Prognose zugesagt |
| Timeline | ✓ Konkret | Q4/2026 Bestellung; Q3/2027 Start; Q1/2028–Q3/2030 Reports |
| Preis | ✓ Konkret | 554.650,30 EUR über 3 Jahre (incl. Initialaufwand); danach 144.189,10 EUR/Jahr |
| ELEKTRA 2 | ✓ Begründet | Explizite Erwähnung: "Mit den oben genannten ELEKTRA 1.0 Anlagen ist es jedoch nicht möglich, diverse statistische Aussagen zu treffen. Um hier entsprechende Aussagen treffen zu können, wurde gemeinsam mit Hitachi Rail Schweiz vereinbart, ebenfalls die ELEKTRA 2.0 Anlagen mit zu betrachten." |
| Service-Portal | ⚠️ Nicht gelöst | Angebot spricht noch von "monatliche Zuordnung", nicht von SIP-2.0-Schnittstelle oder Datenquelle |

## 7. Fachliche Schlussfolgerung (aktualisiert 28.09.2026)

### 7.1 Fortschritt durch das Angebot vom 17.08.2026

Das unterzeichnete Angebot vom 17.08.2026 konkretisiert die Leistungsdefinition erheblich:

1. **Datenfluss geklärt:** SBB muss Reparaturdaten mit Betriebsstelle-Zuordnung **monatlich** liefern (optimal rückwirkend 3 Jahre, minimum 6 Monate).
2. **Installierte Basis:** Hitachi fordert explizit eine vollständige Aufstellung der eingesetzten Interface-Leiterplatten je Betriebsstelle, incl. Umbauten.
3. **ELEKTRA-2-Begründung schriftlich fixiert:** Das Angebot erklärt klar, warum ELEKTRA 2 hinzugezogen wird: neun ELEKTRA-1-Anlagen allein ermöglichen "diverse statistische Aussagen" nicht. Das ist eine legitime methodische Begründung, erfordert aber eine klare Trennung der Ergebnisse.
4. **Timeline konkret:** Bestellung Q4/2026, Start Q3/2027, regelmäßige halbjährliche Reports von Q1/2028 bis Q3/2030.
5. **Preis transparent:** 554.650,30 EUR für 3 Jahre, danach 144.189,10 EUR/Jahr für Verlängerungen.
6. **Sicherheitsnachweis-Erklärung:** Hitachi wird halbjährlich firmeneigene Erklärung zur Gültigkeit des Sicherheitsnachweises ausstellen (nicht Gutachten).
7. **Vorsichtige Restlebensdauer-Aussage:** "Zeitraum ausgewiesen, in dem nicht mit signifikantem Fehleranstieg zu rechnen ist" — fachlich defensibel, da szenariogebunden.

### 7.2 Noch offene methodische Punkte

Folgende Aspekte sind im August-Angebot nicht vollständig adressiert:

1. **SIP-2.0-Schnittstelle:** Das Angebot spricht von "monatlich zu stellende Daten", nicht von einer direkten SIP-2.0-Integration. SBB muss klären, wie die Datenlieferung praktisch erfolgt (Export, API, manuell).
2. **Fehlercluster-Methodik:** Das Angebot nennt "Identifizierung von Ausfallverhalten" und "Relais-Schaltspiele", erwähnt aber nicht explizit die Fehlercluster-Gruppierung, die SBB als Kernmethode fordert.
3. **Rechner-Hardware-Scope:** Der Fokus liegt auf Interface-Leiterplatten und Relais. Ob Rechner-Hardware (CPU, Speicher) gleich behandelt wird, ist nicht explizit geklärt.
4. **Abgrenzung ELEKTRA 1 / ELEKTRA 2 im Report:** Das Angebot sagt nicht, wie die Ergebnisse getrennt oder zusammengefasst werden. Wird es einen Bericht geben, der "ELEKTRA-1-Daten" und "ELEKTRA-2-Referenzen" klar unterscheidet?

### 7.3 Empfehlung für die nächste Phase

Das Angebot ist nun konkret genug für eine verhandelte Konkretisierung. SBB sollte in einer Kick-off-Abstimmung folgende Punkte klären:

| Punkt | Empfohlener Klärungsvorschlag |
| --- | --- |
| Datenquelle | Vereinbarung einer SIP-2.0-Export-Schnittstelle oder eines wöchentlichen Exports (mit Feldern gemäß Abschnitt 4.2 oben) |
| Fehlercluster | Explizite Aufnahme einer Fehler-Clusteranalyse in den Scope; Definition von Fehler-Kategorien (HW-Ausfälle, Kontaktprobleme, Umwelteinflüsse, Verschleiß, etc.) |
| Rechner-Hardware | Klarstellung, ob Rechner-Hardware (z. B. CPU, Speicher aus ELEKTRA-1-Anlagen) in gleicher Tiefe wie Interface-Leiterplatten analysiert wird |
| EL1/EL2-Reporting | Vereinbarung, dass der Bericht explizit zwischen ELEKTRA-1-Daten und ELEKTRA-2-Referenzdaten unterscheidet |
| Maßnahmen-Ableitung | Klärung, in welchen Szenarien Hitachi konkrete Maßnahmen (Bevorratung, Alternative, Migration) vorschlägt oder nur Risiken aufzeigt |

### 7.4 Fachliche Bewertung der Statistischen Ausgangslage

Die ursprüngliche Hitachi-Annahme bleibt fachlich maßgeblich: Die neun verbleibenden ELEKTRA-1-Anlagen und die geringe Anzahl von Rechnerleiterplatten je Anlage reichen allein voraussichtlich nicht aus, um für einzelne Baugruppentypen robuste statistische Aussagen zu treffen. ELEKTRA 2 wurde deshalb als zusätzliche statistische Referenzbasis vorgesehen. Das ist kein Widerspruch zum SBB-Fokus auf ELEKTRA 1, erfordert aber eine klare methodische Trennung:

- **ELEKTRA 1:** Zielsystem der Bewertung und Grundlage für die konkrete Weiterbetriebsempfehlung.
- **ELEKTRA 2:** statistische Referenzpopulation zur Erhöhung der Stichprobengröße, sofern die Baugruppen und Ausfallmechanismen vergleichbar sind.
- **Bericht:** getrennte Darstellung von ELEKTRA-1-Daten, ELEKTRA-2-Referenzdaten und daraus abgeleiteten gemeinsamen Aussagen.

Die geeignete Lösung ist daher ein zweistufiges Reporting: eine ELEKTRA-1-spezifische Bewertung der kritischen Baugruppen sowie eine ausdrücklich gekennzeichnete Referenzanalyse mit ELEKTRA-2-Daten. Die Vergleichbarkeit und die Grenzen der Übertragbarkeit müssen je Baugruppentyp dokumentiert werden.

Eine uneingeschränkte Prognose bis zum Ende der Restlebensdauer sollte trotzdem nicht zugesagt werden. Fachlich belastbarer ist eine trendbasierte Risikoabschätzung mit Szenarien, Datenqualitätsbewertung und klar dokumentierten Annahmen. Die Aussage zur Restlebensdauer sollte als technische Einschätzung unter definierten Voraussetzungen formuliert werden, nicht als statistisch uneingeschränkter Nachweis.

**Abschließende Festlegung zur Auswertung:** Die ELEKTRA-1- und ELEKTRA-2-Daten sind zunächst getrennt zu analysieren. ELEKTRA 1 ist das Zielsystem der SBB-Bewertung. ELEKTRA 2 darf nur als zusätzliche Referenzbasis herangezogen werden, wenn die Vergleichbarkeit der betrachteten Baugruppen, Betriebsbedingungen und Ausfallmechanismen nachgewiesen oder begründet wurde. Gemeinsame statistische Aussagen sind entsprechend zu kennzeichnen und dürfen nicht unmittelbar als ELEKTRA-1-spezifischer Nachweis interpretiert werden.
