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
| Fokus | ELEKTRA 1 und teilweise ELEKTRA 2 als statistische Basis | Primär ELEKTRA 1 und obsolete bzw. kritische Hardware |
| Hardwareumfang | Schwerpunkt Interface-Leiterplatten und Relaisbeanspruchung | Zusätzlich Rechner-Hardware |
| Methodik | DGP-Auswertung, Relais-Schaltspiele, erwartete vs. tatsächliche Reparaturen, Altersklassen | Ausfallstatistik, detaillierte Fehlerbilder, Fehlercluster und Zuordnung zu Baugruppen |
| Altersbewertung | Klassifizierung in 5-Jahres-Scheiben | 5-Jahres-Scheiben allein werden nicht als zielführend angesehen |
| Prognose | Technische Einschätzung hauptsächlich bis zum nächsten Bericht | Aussage über die restliche ELEKTRA-1-Lebensdauer gewünscht |
| Maßnahmen | Empfehlungen bei Auffälligkeiten; Obsoleszenzmaßnahmen separat | Konkrete Maßnahmen für die Ziel-Lebensdauer, z. B. Bevorratung und Know-how-Sicherung |
| ELEKTRA 2 | Teilweise statistische Datengrundlage | Interface-Karten von ELEKTRA 2 separat im Obsoleszenzmanagement betrachten |
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

Eine uneingeschränkte Prognose bis zum Ende der Restlebensdauer sollte nicht zugesagt werden. Fachlich belastbarer ist eine trendbasierte Risikoabschätzung mit Szenarien, Datenqualitätsbewertung und klar dokumentierten Annahmen.
