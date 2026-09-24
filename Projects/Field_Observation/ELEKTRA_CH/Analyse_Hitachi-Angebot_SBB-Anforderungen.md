# ELEKTRA SBB – Vergleich Angebot und SBB-Anforderungen

**Stand:** 24.09.2026  
**Projekt:** Anlagenbeobachtung ELEKTRA CH / SBB

## 1. Grundlage

Diese Zusammenfassung vergleicht das ursprüngliche Hitachi-Angebot zur erweiterten Anlagenbeobachtung mit der SBB-Rückmeldung vom 16.07.2025, die am 22.09.2026 weitergeleitet wurde.

Referenzen:

- [Hitachi-Angebot vom 22.07.2026](20260722_Angebot_Anlagenbeobachtung%20CH_Elektra.docx)
- [Hitachi-Angebot vom 24.07.2026](20260724_Angebot_Anlagenbeobachtung%20CH_Elektra.docx)
- [SBB-Rückmeldung / Weiterleitung](FW_%20Unser%20Angebot%20_Erweiterte%20Anlagebeobachtung%20ELEKTRA1_.msg)
- [SBB-Prüfliste kritischer Baugruppen](Anfrage%20Pr%C3%BCfung%20von%20Baugruppen%20aus%20AAL_2025-07-04_Ed1p03-AT.xlsx)

## 2. Vergleich

| Thema | Hitachi-Angebot | SBB-Erwartung |
| --- | --- | --- |
| Hauptziel | Halbjährliche Anlagenbeobachtung mit RAM-/Safety-Bewertung plus Obsoleszenzmanagement | Praxisnahe Bewertung der verbleibenden ELEKTRA-1-Lebensdauer |
| Fokus | ELEKTRA 1 als Zielsystem; ELEKTRA 2 zusätzlich als statistische Referenzbasis, weil neun ELEKTRA-1-Anlagen allein zu wenig Daten liefern | Primär ELEKTRA 1 und obsolete bzw. kritische Hardware |
| Hardwareumfang | Schwerpunkt Interface-Leiterplatten und Relaisbeanspruchung | Zusätzlich Rechner-Hardware |
| Methodik | DGP-Auswertung, Relais-Schaltspiele, erwartete vs. tatsächliche Reparaturen, Altersklassen | Ausfallstatistik, detaillierte Fehlerbilder, Fehlercluster und Zuordnung zu Baugruppen |
| Altersbewertung | Im aktuellen CH-Angebot nicht ausdrücklich beschrieben; 5-Jahres-Scheiben stammen aus dem früheren Angebotsansatz | 5-Jahres-Scheiben allein werden nicht als zielführend angesehen |
| Prognose | Technische Einschätzung hauptsächlich bis zum nächsten Bericht | Aussage über die restliche ELEKTRA-1-Lebensdauer gewünscht |
| Maßnahmen | Empfehlungen bei Auffälligkeiten; Obsoleszenzmaßnahmen separat | Konkrete Maßnahmen für die Ziel-Lebensdauer, z. B. Bevorratung und Know-how-Sicherung |
| ELEKTRA 2 | Zusätzliche statistische Population, insbesondere wegen der geringen Anzahl von Rechnerleiterplatten je ELEKTRA-1-Anlage | Interface-Karten von ELEKTRA 2 separat im Obsoleszenzmanagement betrachten; die statistische Nutzung als Referenzbasis ist damit noch abzugrenzen |
| SBB-Datenlieferung | Teilweise Zuarbeit über das Service-Portal vorausgesetzt | Service-Portal ist für SBB nicht nutzbar; SBB arbeitet mit SIP 2.0 |
| Ergebnis | Halbjährlicher RAM-/Safety-Bericht | Fehler- und Baugruppenanalyse mit Abgleich gegen den SBB-Obsoleszenzplan |

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

## 7. Fachliche Schlussfolgerung

SBB möchte kein reines Obsoleszenz-Reporting und auch nicht ausschließlich den bisherigen AT-Ansatz. Gewünscht ist ein baugruppenbezogenes, ausfallstatistisches Lebensdauer-Reporting für ELEKTRA 1, das mit dem SBB-Obsoleszenzplan abgeglichen wird und konkrete Maßnahmen für den Weiterbetrieb ableitet.

Die ursprüngliche Hitachi-Annahme bleibt fachlich maßgeblich: Die neun verbleibenden ELEKTRA-1-Anlagen und die geringe Anzahl von Rechnerleiterplatten je Anlage reichen allein voraussichtlich nicht aus, um für einzelne Baugruppentypen robuste statistische Aussagen zu treffen. ELEKTRA 2 wurde deshalb als zusätzliche statistische Referenzbasis vorgesehen. Das ist kein Widerspruch zum SBB-Fokus auf ELEKTRA 1, erfordert aber eine klare methodische Trennung:

- **ELEKTRA 1:** Zielsystem der Bewertung und Grundlage für die konkrete Weiterbetriebsempfehlung.
- **ELEKTRA 2:** statistische Referenzpopulation zur Erhöhung der Stichprobengröße, sofern die Baugruppen und Ausfallmechanismen vergleichbar sind.
- **Bericht:** getrennte Darstellung von ELEKTRA-1-Daten, ELEKTRA-2-Referenzdaten und daraus abgeleiteten gemeinsamen Aussagen.

Die geeignete Lösung ist daher ein zweistufiges Reporting: eine ELEKTRA-1-spezifische Bewertung der kritischen Baugruppen sowie eine ausdrücklich gekennzeichnete Referenzanalyse mit ELEKTRA-2-Daten. Die Vergleichbarkeit und die Grenzen der Übertragbarkeit müssen je Baugruppentyp dokumentiert werden.

Eine uneingeschränkte Prognose bis zum Ende der Restlebensdauer sollte trotzdem nicht zugesagt werden. Fachlich belastbarer ist eine trendbasierte Risikoabschätzung mit Szenarien, Datenqualitätsbewertung und klar dokumentierten Annahmen. Die Aussage zur Restlebensdauer sollte als technische Einschätzung unter definierten Voraussetzungen formuliert werden, nicht als statistisch uneingeschränkter Nachweis.

**Abschließende Festlegung zur Auswertung:** Die ELEKTRA-1- und ELEKTRA-2-Daten sind zunächst getrennt zu analysieren. ELEKTRA 1 ist das Zielsystem der SBB-Bewertung. ELEKTRA 2 darf nur als zusätzliche Referenzbasis herangezogen werden, wenn die Vergleichbarkeit der betrachteten Baugruppen, Betriebsbedingungen und Ausfallmechanismen nachgewiesen oder begründet wurde. Gemeinsame statistische Aussagen sind entsprechend zu kennzeichnen und dürfen nicht unmittelbar als ELEKTRA-1-spezifischer Nachweis interpretiert werden.
