# NextGen_Bahnsignal – RAM-Anforderungsreview

**Datum der ursprünglichen Analyse:** 15.10.2026  
**Ergänzung zur Nachweisstrategie:** 16.10.2026  
**Deutsche Fassung:** 19.10.2026  
**Status:** Technischer Entwurf zur gemeinsamen Prüfung. Keine freigegebene Anforderungsbaseline und keine Konformitätserklärung.  
**Gegenstand:** Vergleich der Anforderungen aus dem Lastenheft Signalgeber mit der bisherigen Feature List Signal Element; Schwerpunkt LH-SIG-105.  
**Bezugsfassung:** [Englischer Bericht](./NextGen_Bahnsignal_RAM_Requirements_Review.md). Die Übersetzung stellt keine neue Prüfung der Quelldokumente dar.

## Inhaltsverzeichnis

- [1. Zusammenfassung](#1-zusammenfassung)
- [2. Angewendete Skills](#2-angewendete-skills)
- [3. Quellen und Prüfumfang](#3-quellen-und-prüfumfang)
  - [3.1 Umfang und Einschränkungen](#31-umfang-und-einschränkungen)
- [4. Befunde: RAM-Anforderungen und Vergleich mit der bisherigen FL](#4-befunde-ram-anforderungen-und-vergleich-mit-der-bisherigen-fl)
  - [4.1 Weitere RAM-relevante Anforderungen](#41-weitere-ram-relevante-anforderungen)
  - [4.2 Wichtige Abgrenzungen zur bisherigen FL](#42-wichtige-abgrenzungen-zur-bisherigen-fl)
- [5. LH-SIG-105: Interpretation](#5-lh-sig-105-interpretation)
  - [5.1 Kundenklärung](#51-kundenklärung)
  - [5.2 Eingangsgrößen](#52-eingangsgrößen)
  - [5.3 Annahmen](#53-annahmen)
  - [5.4 Formel und Berechnung](#54-formel-und-berechnung)
  - [5.5 Ergebnis](#55-ergebnis)
  - [5.6 Bedingte Interpretation je Schaltanforderung](#56-bedingte-interpretation-je-schaltanforderung)
- [6. Warum eine Hardware-MTBF-Prognose allein nicht ausreicht](#6-warum-eine-hardware-mtbf-prognose-allein-nicht-ausreicht)
- [7. Vorgeschlagene Projektanforderungen für LH-SIG-105](#7-vorgeschlagene-projektanforderungen-für-lh-sig-105)
  - [7.1 Leistungsanforderung unter Vorbehalt der Kundenfreigabe](#71-leistungsanforderung-unter-vorbehalt-der-kundenfreigabe)
  - [7.2 Unterstützende Anforderungen](#72-unterstützende-anforderungen)
- [8. Verifikation und statistischer Nachweis](#8-verifikation-und-statistischer-nachweis)
  - [8.1 Vorgeschlagene Nachweisstrategie](#81-vorgeschlagene-nachweisstrategie)
  - [8.2 Statistisches Beispiel ohne beobachtete Ereignisse](#82-statistisches-beispiel-ohne-beobachtete-ereignisse)
  - [8.3 Ratenziel gegenüber fester jährlicher Obergrenze](#83-ratenziel-gegenüber-fester-jährlicher-obergrenze)
- [9. Abgrenzung von Verfügbarkeit und Instandhaltbarkeit](#9-abgrenzung-von-verfügbarkeit-und-instandhaltbarkeit)
- [10. Annahmen und fehlende Informationen](#10-annahmen-und-fehlende-informationen)
- [11. Risiken](#11-risiken)
- [12. Empfehlungen](#12-empfehlungen)
- [13. Erforderliche Nachweise](#13-erforderliche-nachweise)
- [14. Maßnahmen](#14-maßnahmen)
- **[15. LH-SIG-105: Formulierung der Projektanforderung und Erfüllungsnachweis](#15-lh-sig-105-formulierung-der-projektanforderung-und-erfüllungsnachweis)**
  - [15.1 Vorgeschlagene Projektanforderung](#151-vorgeschlagene-projektanforderung)
  - [15.2 Zugehörige Ereignisdefinition](#152-zugehörige-ereignisdefinition)
  - [15.3 Drei Ebenen des Erfüllungsnachweises](#153-drei-ebenen-des-erfüllungsnachweises)
    - [15.3.1 Erforderliche Ereignis- und Expositionsdaten](#1531-erforderliche-ereignis--und-expositionsdaten)
  - [15.4 Beispiel für die quantitative Abnahme](#154-beispiel-für-die-quantitative-abnahme)
    - [15.4.1 Eingangsgrößen und Annahmen](#1541-eingangsgrößen-und-annahmen)
    - [15.4.2 Formel](#1542-formel)
    - [15.4.3 Berechnung](#1543-berechnung)
    - [15.4.4 Ergebnis](#1544-ergebnis)
  - [15.5 Praktische gestufte Nachweisstrategie](#155-praktische-gestufte-nachweisstrategie)
  - [15.6 Empfohlene Aussage zum aktuellen Erfüllungsstand](#156-empfohlene-aussage-zum-aktuellen-erfüllungsstand)
- [16. Prüfung der Review-Artefakte](#16-prüfung-der-review-artefakte)

## 1. Zusammenfassung

**LH-SIG-105 ist als Anforderung an die funktionale Störungshäufigkeit berechenbar. Ihre Erfüllung lässt sich jedoch nicht unmittelbar durch eine herkömmliche Hardware-MTBF-Berechnung nachweisen.**

Empfohlene Position:

> Der quantitative Zielwert ist definiert. Ereigniszählung, Expositionsbasis und Nachweiskriterien müssen jedoch vereinbart werden. Eine bauteilbasierte Zuverlässigkeitsprognose allein weist die Erfüllung nicht nach.

Die Projektunterlagen enthalten folgende Grundlagen:

- **LH-SIG-94:** Verfügbarkeit mindestens **0,9999**.
- **LH-SIG-95:** MTBF **100.000 h**.
- **LH-SIG-105:** eine Störung je **1.000 Signalgeber und Jahr**.
- Die bisherige FL behandelt LH-SIG-105 separat in **SE:FL:FEA:0806** und fordert höchstens **0,001 funktionale Störungen je Element und Jahr**.
- Die lokale Klärungs-E-Mail zitiert eine ÖBB-Antwort vom **12.12.2025**. Sie beschreibt einen **nicht sicherheitsrelevanten fehlerhaften Schaltvorgang**, beispielsweise einen grünen Lichtpunkt, der beim Einschalten dunkel bleibt.

**Die Störungsrate ist eine RAM-Kennzahl**, auch wenn sie weder die Verfügbarkeit beschreibt noch zwingend dieselbe Ereignispopulation wie die Hardware-MTBF verwendet.

Technische Nutzungsdauer, Hardware-Zuverlässigkeit, Verfügbarkeit, Instandhaltbarkeit und funktionale Störungshäufigkeit sind deshalb getrennt und rückverfolgbar in Projektanforderungen zu überführen.

## 2. Angewendete Skills

Folgende Repository-Skills wurden für die zugrunde liegende Analyse angewendet:

- [Railway-RAM](../../../Skills/Railway-RAM.md): RAM-Assurance und Lebenszyklusbewertung für Bahnanwendungen.
- [REQ-Review](../../../Skills/REQ-Review.md): Eindeutigkeit, Vollständigkeit, Rückverfolgbarkeit und Verifizierbarkeit.
- [RAM-Metrics](../../../Skills/RAM-Metrics.md): Kennzahlendefinitionen, Exposition, Ereigniszählung und Berichterstattung.
- [Reliability-Prediction](../../../Skills/Reliability-Prediction.md): Abgrenzung von prognostizierter Ausfallrate, beobachteter Störungshäufigkeit und Nutzungsdauernachweisen.

## 3. Quellen und Prüfumfang

Die Analyse verwendet Informationen aus folgenden Projektunterlagen:

| Referenz | Quelle | Verwendung |
| --- | --- | --- |
| S1 | [715 LH Signalgeber DSTW V1.1_Kom_SS_20250704.pdf](../715%20LH%20Signalgeber%20DSTW%20V1.1_Kom_SS_20250704.pdf) | Anforderungs-IDs, Verbindlichkeit und Variantengültigkeit; insbesondere S. 17–22. |
| S2 | [LH Signalgeber V2.0 signed.pdf](../LH%20Signalgeber%20V2.0%20signed.pdf) | Kundenanforderungen für konventionelle und SEA-Varianten; Freigabe vom 08.05.2024. |
| S3 | [FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx](../FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx) | Bisherige Produktfeatures; Dokument 3BU 62200 1001 FLAPQ, ED01, Änderungsverzeichnis vom 08.10.2025. |
| S4 | [RE_ Aufklärungen durch ÖBB bei LED Ausschreibung.msg](../RE_%20Aufkl%C3%A4rungen%20durch%20%C3%96BB%20bei%20LED%20Ausschreibung.msg) | Interner E-Mail-Verlauf vom 08.01.2026 mit zitierter Kundenantwort vom 12.12.2025. |
| S5 | [D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf](../D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf) | Zusätzliche Umwelt- und Gehäuselebensdaueranforderungen, soweit anwendbar. |
| S6 | [SSDD_iLED_01PD01.docx](../SSDD_iLED_01PD01.docx) | Architektur, Diagnoseverhalten und Verweis auf einen separaten RAM-Plan; kein quantitativer Erfüllungsnachweis. |

Zusätzlich wurden Unternehmensprozesse und Repository-Wissen berücksichtigt:

- [G-PRD_S06000_02_EN.pdf](../../../Knowledge/Process/RAM-Process/G-PRD_S06000_02_EN.pdf): Anforderungsanalyse, RAM-Planung, Durchführung und Überwachung; RAM-Nachweis- und FRACAS-Artefakte.
- [Requirements_Lessons.md](../../../Knowledge/Lessons_Learned/Requirements_Lessons.md): RL-011 zur Abgrenzung der Wiederherstellungszeit und RL-012 zur Klärung der Kundenintention vor Baseline-Freigabe. Dies sind freigegebene Beispiellehren, keine historischen Leistungsnachweise dieses Projekts.

### 3.1 Umfang und Einschränkungen

- Der Vergleich umfasst alle inhaltlichen Anforderungen des RAMS-Kapitels, LH-SIG-84 bis LH-SIG-116 sowie LH-SIG-139. Ergänzend werden ausgewählte Definitionen, funktionale Abnahmekriterien, Umweltbedingungen und Nachweisanforderungen behandelt.
- LH-SIG-83 und LH-SIG-117 sind Kapitelüberschriften, keine inhaltlichen Anforderungen.
- Dies ist keine vollständige Prüfung aller funktionalen, elektrischen, optischen, umweltbezogenen oder sicherheitstechnischen Anforderungen.
- Verbindlichkeit und Gültigkeit folgen **S1, DSTW-LH V1.1**. Die unterzeichnete V2.0 gehört zu einem anderen Dokumentenstrang. Versionsnummern allein bestimmen keine vertragliche Rangfolge.
- S4 verweist auf **LH 4.0**, das nicht im Projektordner vorliegt, und nennt die FL-Kennung FLAPC. Die bereitgestellte Vergleichsdatei trägt die Kennung FLAPQ. Vertragsbaseline und offizieller Klärungsnachweis sind zu bestätigen.
- Die nachfolgenden Beschreibungen sind technische Zusammenfassungen, keine wortgetreuen Abschriften.
- Vorgeschlagene Formulierungen und statistische Abnahmebeispiele benötigen eine Freigabe.
- Kundendokumentation muss LH-SIG-119 einschließlich der deutschen Dokumentationssprache erfüllen.

## 4. Befunde: RAM-Anforderungen und Vergleich mit der bisherigen FL

Die Featurenummern in der Tabelle stehen verkürzt für **SE:FL:FEA:xxxx**.

| LH-Anforderung | Kundenanforderung / Intention | Bisherige FL | Bewertung und Überführung ins Projekt |
| --- | --- | --- | --- |
| **84, 88** | Montage und Tausch von Teilsystemen mit handelsüblichem Werkzeug. | 1006; 0316/0317 | Inhaltlich abgedeckt. Freigegebene Werkzeuge und Bedingungen des Instandhaltbarkeitsnachweises festlegen. |
| **85** | Austausch defekter Frontoptik, Leuchtmittel oder Elektronik ohne Gehäusedemontage oder optische Neueinstellung. | 1005 | In V1.1 Info. LRU-Tausch ist nicht zwingend gleichbedeutend mit separatem Komponententausch. Umgang mit dem Ziel dokumentieren. |
| **86–87** | Vom Gehäuse unabhängig tauschbares Lichtpunkt- bzw. Anzeigerteilsystem ohne optische Neueinstellung. | 1005 | In V1.1 Soll. Die unterzeichnete V2.0 fordert das Lichtpunktteilsystem verbindlicher. Baseline und Umgang mit Soll-Zielen klären. |
| **89** | Tausch darf physikalische und funktionale Eigenschaften nicht verändern. | 1005 | In messbare Abnahmekriterien nach dem Tausch überführen. |
| **90** | Einbau oder Austausch maximal **10 min**, bezeichnet als MRT. | 0811; 1005 | 0811 schwächt das Maximum zu einer mittleren Reparaturzeit ab und schließt Vorbereitung aus. 1005 fordert weniger als 10 min. **Maximal 600 s je definierter Tätigkeit** mit vereinbartem Start/Ende festlegen. |
| **91** | Sichtbarkeit bleibt trotz Degradation, Temperatureinfluss und Teilausfällen über die Nutzungsdauer erhalten. | 0219; 0810 | Explizite optische Nutzungsdaueranforderung und Nachweise erforderlich. Zulässige Teilausfälle dürfen die Sichtbarkeit nicht abschwächen. |
| **92** | Der geforderte Achslichtstärkebereich darf während der Nutzungsdauer nicht unterschritten werden. | 0808/0810 | 0808 referenziert diese ID, fordert im verbindlichen Text aber Verfügbarkeit und MTBF. Explizite optische Nutzungsdaueranforderung ergänzen. |
| **93** | Technische Nutzungsdauer mindestens **130.000 Betriebsstunden**. | 0810; Kommentare zu 0808 | **15 Kalenderjahre** sind bei intermittierender Nutzung nicht allgemein gleichwertig. Betriebsstundenziel beibehalten und Kalenderalterung separat behandeln. |
| **94** | Verfügbarkeit mindestens **0,9999** über die Lebensdauer. | 0808 | Zahlenwert stimmt überein. Verfügbarkeitsart, Systemgrenze, Ausfallzeitanteile und Beobachtungsbasis fehlen. |
| **95** | MTBF **100.000 h**. | 0808: mindestens **200.000 h** | Bisheriges Ziel ist bei gleicher Systemgrenze und gleichem Einsatzprofil strenger. Mindestwertinterpretation und fortbestehende Produktzusagen bestätigen. |
| **96** | Schaltungstechnische Maßnahmen zur Erreichung der Nutzungsdauer sind freigestellt. | Entwurfsprinzipien | Info bzw. Gestaltungsfreiheit, kein zusätzliches quantitatives Ziel. |
| **97** | Betriebsstunden lokal speichern. | 0407 | Feature mit Status Accepted zählt Zeit unter Spannung einschließlich Dunkelzeit. V1.1 gilt für SEA. Genauigkeit, Erhalt der Werte und Verhalten beim Tausch festlegen. |
| **98** | Nutzungsanzeige am Signalstandort ohne Demontage oder zusätzliche Systeme sichtbar. | 0633 | Lücke: Feature ist Descoped, obwohl V1.1 eine Muss-Anforderung für konventionelle/SEA-Varianten enthält. |
| **99** | Grün bis 68 % der Nutzungsdauer; gelb 68,1–81,1 %; rot ab 81,2 %. | 0634 | Lücke: Feature ist Descoped. Quantisierung und Rundung zur Schließung der Intervalllücken vereinbaren. |
| **100** | Position des Indikators mit dem Kunden abstimmen. | 0633 | Ein ausgeplantes Feature belegt keine abgestimmte Einbauposition. |
| **101** | Betriebsstunden nach Demontage kabelgebunden auslesen. | 0643 | Akzeptiertes CAN-Auslesen unterstützt digitale Varianten. Konventionelle Varianten und Auslesekonfiguration prüfen. |
| **102** | Drahtloses Auslesen ohne Demontage. | 0644 | In V1.1 Soll, in der FL Descoped. Formelle Entscheidung erforderlich. |
| **103** | Nutzungsdauergrenze umfasst alle notwendigen Teile ab kabelseitiger Klemmleiste einschließlich des vollständigen Steckers. | 0810 | Inhaltlich abgedeckt. Nicht nur die Elektronikbaugruppe bewerten. |
| **104** | Typisch 300 Einschaltungen/Tag, 100 Blinkanschaltungen/Tag zu je 2 min; Extreme von Dauerbetrieb bis einmal in zwei Jahren. | 0810/0812/0813 | Widersprüchliche bisherige Profile: 300 × 2 min bzw. 100 × 1 min. Variantenbezogene Profile vereinbaren; typische Mittelwerte sind keine allgemeinen Maximalwerte. |
| **105** | Eine Störung je **1.000 Signalgeber und Jahr**. | 0806 | Zahlenziel zugeordnet. Ereignisumfang, Zählregeln, Exposition und Nachweiskriterien sind unvollständig. |
| **106** | Bei Störung hochohmige Stellwerksschnittstelle für konventionelle Varianten. | 0805 | Impedanzkriterien und Reaktionszeiten festlegen. |
| **107** | Störung an der Stellwerksschnittstelle offenbaren, für DSTW/SEA. | 0805; 0406 | Diagnosemeldungen, Abdeckung, Latenz und Verhalten bei Kommunikationsausfall festlegen. |
| **108–109** | Keine erforderliche periodische Wartung während der Nutzungsdauer, ausgenommen definierte äußere Reinigung. | 1001 | Weitgehend abgedeckt. Korrektive Eingriffe gegenüber Reparatur nach zufälligem Ausfall abgrenzen. |
| **110** | Falls erforderlich: Instandhaltungs-/Inspektionsintervall mindestens **2 Jahre**. | 1004 | Das bisherige Ideal „keine wiederkehrende Prüfung“ enthält die explizite Untergrenze nicht. |
| **111** | Intervall von mindestens **4 Jahren** als Ziel. | 1004 | Kein explizites Vierjahresziel identifiziert. Erfüllung oder freigegebene Abweichung dokumentieren. |
| **112** | Sicherheitsnachweis/Anwendungsbedingungen dürfen keine Stellwerksansteuerung oder Zustandswechsel für Inspektion/Instandhaltung verlangen. | 1003 | Bisherige Formulierung schwächer. Explizites Verbot erhalten und Diagnoseannahmen bei seltenem Betrieb prüfen. |
| **113** | Signaltechnische Sicherheit SIL4 im Zulassungssicherheitsnachweis dokumentieren. | 0801/0807 | Sicherheitsbezogene Anforderung, kein Ersatz für RAM-Nachweise. |
| **114–116** | Anwendbare THR-Matrizen für kleine/große Lichtpunkte und Signalgeber. | 0801 | Kontrollierte Matrizen beschaffen. Ein allgemeiner THR-Einzelwert ersetzt keine gefährdungsspezifischen Zuweisungen. |
| **139** | Leuchtdauer bei konventionellen Varianten lokal speichern. | 0407 | Lücke: Zeit unter Spannung einschließlich Dunkelzeit ist nicht gleich Leuchtdauer. |

### 4.1 Weitere RAM-relevante Anforderungen

| LH-Anforderung | RAM-Bezug | Vergleich / Maßnahme |
| --- | --- | --- |
| **5–9** | Signalgebertypen und Gesamtsystemgrenzen. | Gelieferte Optik, Schnittstelle, Stecker, Befestigung, Gehäuse und thermische Einrichtungen entsprechend berücksichtigen. |
| **10–11** | Störungsdefinition und nicht spezifiziertes optisches Verhalten. | LH-SIG-10 umfasst Funktionsverlust, optische Abweichungen, Schnittstellenabweichungen und Flackern. Mit der engeren Schaltvorgangsklärung abstimmen. |
| **12–13** | Störungsreaktion und dunkler/hochohmiger Zustand. | 0805 behandelt nicht behebbare Fehler. Weitere Verhaltensabweichungen und digitale Schnittstellen prüfen. |
| **18** | Anzuwendende Normen einschließlich EN 50126-1. | Ausgaben und Anwendbarkeit in der Normenbaseline festlegen. |
| **33, 35–36** | Erhalt der Justierung, Tausch ohne Neueinstellung und Masse. | 0317/1005 decken Tauschintention ab. Variantenbezogene Masseforderungen teilweise strenger. Messbare Kriterien festlegen. |
| **40–48** | Umweltbeständigkeit, Schnee, Temperatur, EMV, Transport/Lagerung, IP und Druck-/Sogbelastung. | Vollständiges freigegebenes Umweltprofil und Qualifikationsnachweise verwenden. IP65 übertrifft IP54, ist aber allein kein Nutzungsdauernachweis. |
| **54–57, 63, 65** | Sichtbarkeit, Einblickwinkel, Lichtverteilung und Erhalt der Lichtstärke. | Kriterien zur funktionalen Störungsklassifikation und optischen Nutzungsdauer, keine MTBF-Zielwerte. |
| **67–69** | Farbstabilität bei Temperatur, Alterung, Spannungsänderungen und Phantomlicht. | 0220 deckt Intention ab. Informelle Farbtoleranzabweichungen benötigen eine Kundenfreigabe. |
| **71, 74, 81–82** | Störungsoffenbarung, Serienschaltung, Spannungsverhalten und kein Flackern bei einpoliger Abschaltung. | In Störungs- und Schnittstellenverifikation aufnehmen. 0317 referenziert LH-SIG-82 fälschlich für Befestigung. |
| **76–77** | Blinken mit 1 Hz, Tastverhältnis 1:1 und Toleranzen. | 0502 ist enger toleriert. Festlegen, ob jede Blinkflanke eine Schaltanforderung ist. |
| **118** | RAM-Nachweise. | Installationsunterlagen allein gewährleisten kein vollständiges RAM-Nachweispaket. |
| **119–120** | Deutsche Dokumentation sowie veränderbare/unveränderbare digitale Formate. | Englische generische Produktunterlagen allein erfüllen die Kundenlieferpflicht nicht. |
| **121–123** | Handbuch, Diagnose, Ersatzteile, Messverfahren und freigegebene Werkzeuge. | Vollständigkeit prüfen und Werkzeugabweichungen schriftlich freigeben lassen. |
| **124–126** | Kennzeichnung und maschinenlesbare Daten für Anlagen- und FRACAS-Rückverfolgbarkeit. | Identität, Konfiguration, Exposition und Störungsdaten verknüpfen. |
| **135** | Lichtstärke kleiner Lichtpunkte. | 0619 passt zum Nennbereich. **0624 erlaubt nachts mindestens 21 cd statt geforderter 40 cd**. Variantengültigkeit und Alterungsreserve klären. |
| **136–138** | Anzeigerlichtstärke, Sichtwinkel und Symbolerkennbarkeit. | Erkennbarkeit bei zulässigen Teilausfällen prüfen. Pixel-Ausfallgrenzen anderer Kunden nicht automatisch für ÖBB übernehmen. |

### 4.2 Wichtige Abgrenzungen zur bisherigen FL

- **Der Feature-Status Accepted ist kein Nachweis der Kundenkonformität.**
- **30 Jahre Produktunterstützung/Produktlebensdauer** nach 0809 sind von **130.000 Betriebsstunden technischer Nutzungsdauer** und ausfallfreiem Betrieb zu trennen.
- S5 fordert gegebenenfalls **30 Jahre UV-Beständigkeit der Gehäuse**; diese Anforderung ist separat zuzuweisen.
- Umgebungstemperatur, äußere Gehäusetemperatur und innere Bauteiltemperatur dürfen nicht gleichgesetzt werden.
- S5 fordert gegebenenfalls **−40 bis +70 °C Umgebungstemperatur im Gleisbereich**. LH-SIG-42/43 beziehen sich dagegen auf äußere Gehäusetemperaturen.
- Eine bisherige Rechenannahme von **20 °C** bildet kein vollständiges Einsatzprofil ab.

## 5. LH-SIG-105: Interpretation

### 5.1 Kundenklärung

S4 unterstützt die Einordnung von LH-SIG-105 als Anforderung an **fehlerhafte Schaltvorgänge**, statt lediglich die Hardware-Ausfallrate aus LH-SIG-95 anzuwenden.

Dabei bleiben folgende Punkte offen:

1. Die zitierte Antwort bezeichnet LH-SIG-95 als „Verfügbarkeit“. Technisch wird dort **MTBF** gefordert; LH-SIG-94 ist die separate Verfügbarkeitsanforderung.
2. Der Verlauf verweist auf das nicht bereitgestellte **LH 4.0**. Seine Anwendbarkeit ist zu bestätigen.
3. Ein fehlerhafter Schaltvorgang kann eine Hardwareursache haben. **Hardwarebedingte Schaltfehler und störende sichere Dunkelschaltungen nicht ohne Kundenvereinbarung ausschließen.**
4. V1.1 ordnet LH-SIG-105 **konventionellen und SEA-Varianten**, nicht DSTW zu. Eine Erweiterung muss explizit erfolgen.
5. Jährliche Störungsgrenze, Schaltbeispiel und breite Definition nach LH-SIG-10 benötigen einen abgestimmten Ereigniskatalog.
6. **Ein Ereignis** und **ein betroffenes Gerät** sind unterschiedliche Kennzahlen, wenn dasselbe Gerät wiederholt gestört ist.

### 5.2 Eingangsgrößen

| Parameter | Wert | Quelle / Status |
| --- | --- | --- |
| Zulässige Störungshäufigkeit | Eine Störung je 1.000 Signalgeberjahre | LH-SIG-105; Interpretation als Ereignisrate noch abzustimmen. |
| Hardware-MTBF | 100.000 h | LH-SIG-95; Interpretation als Mindestwert bestätigen. |
| Verfügbarkeit | Mindestens 0,9999 | LH-SIG-94; Verfügbarkeitsart und Ausfallzeitgrenze offen. |
| Typische Einschaltzahl für das Beispiel | 300 Einschaltungen/Tag | LH-SIG-104; kein allgemeines Maximum und keine vollständige Definition der Schaltanforderung. |

### 5.3 Annahmen

Nur für die entsprechend gekennzeichneten Berechnungen gelten:

- Ein Jahr wird mit **365 Tagen** angesetzt.
- Kontinuierliche Exposition entspricht **8.760 h/Jahr**.
- Der Kehrwert als mittlerer Ereignisabstand setzt einen stationären Ereignisprozess voraus.
- Die Umrechnung je Schaltanforderung setzt voraus, dass ausschließlich diese Anforderungen die betrachteten Ereignisse verursachen.
- Statistische Beispiele setzen unabhängige seltene Ereignisse, homogene repräsentative Exposition, konstante Ereignisrate und vollständige Beobachtung voraus.
- Keine dieser Annahmen ist damit ein kundenfreigegebenes Abnahmekriterium.

### 5.4 Formel und Berechnung

Gemessene Störungshäufigkeit:

$$
r_D = \frac{K_D}{E}
$$

- $K_D$: Anzahl der nach vereinbarter Definition zählbaren Störungsereignisse.
- $E$: kumulierte anrechenbare Exposition in Signalgeberjahren.

Vorgeschlagene quantitative Interpretation:

$$
r_D \leq \frac{1}{1000}
= 0{,}001\ \text{Störungen/(Signalgeberjahr)}
$$

Die Größe ist aus Ereignis- und Expositionsdaten unmittelbar berechenbar.

Bei kontinuierlicher Exposition:

$$
\nu_D = \frac{0{,}001}{8760}
= 1{,}142 \times 10^{-7}\ \text{Ereignisse/h}
$$

$$
\text{Äquivalent in FIT-Einheiten}
= \nu_D \times 10^9
= 114{,}2
$$

$$
\text{Mittlerer Ereignisabstand}
= \frac{1}{\nu_D}
= 8.760.000\ \text{h}
$$

### 5.5 Ergebnis

| Bedingtes Ergebnis | Wert | Bedeutung |
| --- | --- | --- |
| Zielwert der Störungshäufigkeit | 0,001 Ereignisse/Signalgeberjahr | Vorgeschlagene jährliche Rateninterpretation. |
| Zeitnormierte Störungshäufigkeit | $1{,}142 \times 10^{-7}$ Ereignisse/h | Nur unter Annahme kontinuierlicher Exposition. |
| Äquivalent in FIT-Einheiten | 114,2 FIT | Einheitenumrechnung, keine Hardwareprognose. |
| Kehrwert als mittlerer Ereignisabstand | 8.760.000 h | Nicht automatisch die Hardware-MTBF nach LH-SIG-95. |

Wenn beide Anforderungen genau dieselben Ereignisse erfassen, ist LH-SIG-105 wesentlich strenger:

$$
\frac{8.760.000}{100.000} = 87{,}6
$$

Das ist nicht zwingend ein logischer Widerspruch zu einer Mindest-MTBF. Es ist aber ein erheblicher Machbarkeits- und Nachweispunkt.

### 5.6 Bedingte Interpretation je Schaltanforderung

Bei 300 Einschaltanforderungen pro Tag und ausschließlicher Verursachung der gezählten Störungen durch diese Anforderungen:

$$
D = 300 \times 365 = 109.500\ \text{Anforderungen/(Signalgeberjahr)}
$$

$$
p_D = \frac{0{,}001}{109.500}
= 9{,}13 \times 10^{-9}\ \text{Fehler/Anforderung}
$$

Dies ist ein Rechenbeispiel, **keine kundenseitig spezifizierte Anforderung je Schaltvorgang**. Tatsächliche Schaltprofile, Blinkflanken und lange Ruhezeiten müssen vor Verwendung einer solchen Umrechnung festgelegt werden.

## 6. Warum eine Hardware-MTBF-Prognose allein nicht ausreicht

Eine bauteilbasierte Prognose quantifiziert üblicherweise nicht vollständig:

- sporadisches Einschaltversagen;
- Software-, Zeitverhaltens- und Schnittstellenfehler;
- vorübergehende Störfestigkeitsprobleme;
- unerwünschte Diagnoseabschaltungen;
- zeitweilige optische Grenzwertverletzungen;
- wiederholte fehlgeschlagene Anforderungen und Wiederanlaufverhalten.

Für LH-SIG-95 ist die unternehmensseitig freigegebene Zuverlässigkeitsmethode anzuwenden. Für LH-SIG-105 sind eine **eigene Störungsbewertung, funktionale Verifikation und Betriebsnachweise** erforderlich.

In diesem Review wurde keine Prognose nach FIDES, IEC 61709 oder MIL-HDBK-217 durchgeführt. Die Berechnungen sind Einheitenumrechnungen und beispielhafte Ereignisratenanalysen.

Die Zweikanalarchitektur aus S6 rechtfertigt ohne Analyse keine Unabhängigkeitsannahme. Gemeinsame Ursachen in Versorgung, Umwelt, Kommunikation oder systematischem Verhalten können mehrere Störungen auslösen und ein einfaches Zusammenfassen statistischer Daten unzulässig machen.

## 7. Vorgeschlagene Projektanforderungen für LH-SIG-105

### 7.1 Leistungsanforderung unter Vorbehalt der Kundenfreigabe

> **NGB-RAM-DST-105-01:** Die Häufigkeit der gemäß dem freigegebenen Störungskatalog als LH-SIG-105-Ereignisse klassifizierten Störungen darf unter dem freigegebenen Einsatzprofil **0,001 Ereignisse je Signalgeberjahr** nicht überschreiten. Die Exposition ist gemäß der freigegebenen Expositionsdefinition zu bestimmen.

Die Formulierung erhält das jährliche Ratenziel, ohne es stillschweigend durch Hardware-MTBF oder Fehlerwahrscheinlichkeit je Schaltanforderung zu ersetzen.

### 7.2 Unterstützende Anforderungen

Die folgenden Punkte sind **vorgeschlagene abgeleitete Verifikations- und Nachweisanforderungen**, keine zusätzlich zitierten Kundenanforderungen.

| Entwurfs-ID | Vorgeschlagene Anforderung | Verifikation / Freigabe |
| --- | --- | --- |
| **NGB-RAM-DST-105-02** | Der freigegebene Ereigniskatalog muss die von der Kundenklärung erfassten nicht sicherheitsrelevanten fehlerhaften Schaltvorgänge und ihre Beziehung zur breiteren Definition nach LH-SIG-10 festlegen. | Gemeinsame Klassifikationsprüfung; Anwendbarkeit der zitierten LH4.0-Klärung bestätigen. |
| **NGB-RAM-DST-105-03** | Die Zählspezifikation muss getrennte Ereignisse, wiederholte fehlerhafte Befehle, Dauerstörungen, Wiederherstellung, Neustarts, Blinkflanken und Zuordnung zur vereinbarten Systemgrenze festlegen. | Prüfung repräsentativer Szenarien; kein pauschaler Ausschluss hardwarebedingter oder sicher-dunkler Ereignisse. |
| **NGB-RAM-DST-105-04** | Die Expositionsspezifikation muss die Akkumulation anrechenbarer Signalgeberjahre einschließlich Einbau, Ausbau, Zeit unter Spannung, Leuchtdauer, Ruhezeiten und Beobachtungslücken festlegen. | Zeitbasis und Behandlung von Ausfallzeiten freigeben. |
| **NGB-RAM-DST-105-05** | Das Nachweissystem muss Störungen mit Geräteidentität, Konfiguration, Ereigniszeit, Sollzustand, Istzustand, Wiederherstellung und zugehöriger Exposition aufzeichnen. | Datenqualität und Protokollierung prüfen; Quellen zwischen Gerät, Stellwerk, Werkzeugen und FRACAS zuweisen. |
| **NGB-RAM-DST-105-06** | Der RAM-Nachweisplan muss statistisches Modell, Konfidenzniveau, Stichprobenexposition, Behandlung gemeinsamer Ursachen und Abnahmeregel vor einer Erfüllungsaussage festlegen. | Kundenfreigabe des Nachweisplans. |
| **NGB-RAM-DST-105-07** | Die Verifikation muss Schaltfolgen unter freigegebenen elektrischen, umweltbezogenen, zeitlichen und einsatzbezogenen Bedingungen einschließlich Start, Neustart, seltenem Betrieb und gegebenenfalls Blinken prüfen. | Robustheits- und Schnittstellenprüfungen; allein kein quantitativer Jahresratennachweis. |
| **NGB-RAM-DST-105-08** | Die RAM-Erfüllungsmatrix muss MTBF, Verfügbarkeit und Störungshäufigkeit nach LH-SIG-105 mit freigegebenen Ereignisklassen und Grenzen getrennt ausweisen. | Rückverfolgbarkeitsprüfung; ein Ereignis kann mehrere Kennzahlen beeinflussen. |

## 8. Verifikation und statistischer Nachweis

### 8.1 Vorgeschlagene Nachweisstrategie

1. Ereigniskatalog, Zählregeln und Expositionsdefinition freigeben.
2. Relevante Fehlerarten und Entwurfsbeiträge einschließlich transienter und systematischer Ursachen analysieren.
3. Funktionale Robustheit unter freigegebenen Einsatz- und Umweltprofilen verifizieren.
4. Übertragbarkeit historischer Flottendaten auf neue Hardware, Software, Schnittstellen und Umwelt bewerten.
5. Feldnachweis und FRACAS-Berichterstattung vereinbaren.
6. Erfüllungsnachweis bis zum Vorliegen ausreichender vereinbarter Evidenz offenhalten.

### 8.2 Statistisches Beispiel ohne beobachtete Ereignisse

**Nur Beispielannahmen:** homogene unabhängige Poisson-Ereignisse, vollständige Beobachtung und **einseitiges Konfidenzniveau von 95 %**. Dies ist kein kundenseitig festgelegtes Abnahmekriterium.

Bei null beobachteten Ereignissen:

$$
r_{D,U} = \frac{-\ln(0{,}05)}{E}
$$

Für $r_{D,U} \leq 0{,}001$:

$$
E \geq \frac{-\ln(0{,}05)}{0{,}001}
= 2995{,}7\ \text{Signalgeberjahre}
$$

| Beobachtung / Beispielkriterium | Ergebnis |
| --- | --- |
| Null Ereignisse in 1.000 Signalgeberjahren | Obere Rate etwa 0,002996 Ereignisse/Signalgeberjahr; für das Beispielkriterium nicht ausreichend. |
| Null Ereignisse und obere Rate höchstens 0,001 | Aufgerundet etwa **2.996 volle Signalgeberjahre** erforderlich. |
| Ein Ereignis und obere Rate höchstens 0,001 | Aufgerundet etwa **4.744 volle Signalgeberjahre** erforderlich. |

Bei einem Ereignis wird der obere Poisson-Erwartungswert aus folgender Gleichung ermittelt:

$$
e^{-\mu_U}(1+\mu_U) = 0{,}05
$$

$$
\mu_U = 4{,}7438645,\qquad
E \geq \frac{\mu_U}{0{,}001} = 4743{,}9\ \text{Signalgeberjahre}
$$

Gemeinsame Ursachen, Alterung, Beobachtungslücken und Konfigurationsunterschiede können ein einfaches Zusammenfassen der Daten unzulässig machen.

### 8.3 Ratenziel gegenüber fester jährlicher Obergrenze

Ein statistisches Ratenziel ist nicht gleichbedeutend mit einer festen Grenze von einem Ereignis in jedem Flottenjahr.

Bei einem Poisson-Erwartungswert von einem Ereignis:

$$
P(K \geq 2) = 1-e^{-1}(1+1) = 0{,}2642
$$

Auch bei einem Erwartungswert von eins beträgt die Wahrscheinlichkeit für mindestens zwei Ereignisse somit **26,4 %**. Der Kunde muss die beabsichtigte Abnahmelogik bestätigen.

## 9. Abgrenzung von Verfügbarkeit und Instandhaltbarkeit

Die Austauschzeit nach LH-SIG-90 ist nicht automatisch die Ausfallzeit für LH-SIG-94.

Für ein vereinfachtes Modell aus Betriebs- und Ausfallzeiten gilt:

$$
A = \frac{\text{MTBF}}{\text{MTBF}+\text{MDT}}
$$

Mit MTBF = 100.000 h und $A = 0{,}9999$:

$$
\text{MDT} \leq 100.000
\left(\frac{1}{0{,}9999}-1\right)
= 10{,}001\ \text{h}
$$

Dies gilt nur unter der vereinbarten Verfügbarkeitsdefinition und dem vereinfachten Erneuerungsmodell. Es ist kein freigegebenes Ausfallzeitbudget.

Bei ausschließlicher Berücksichtigung einer aktiven Austauschzeit von 10 min:

$$
A = \frac{100.000}{100.000+10/60}
= 0{,}99999833
$$

Erkennung, Mobilisierung, Zugang, Ersatzteillogistik, Prüfung und Wiederinbetriebnahme sind darin nicht enthalten. Dies ist **kein Nachweis der betrieblichen Verfügbarkeit**.

## 10. Annahmen und fehlende Informationen

| Punkt | Status / Auswirkung |
| --- | --- |
| Vertragliche Dokumentenrangfolge | Nicht bestätigt. LH-Dokumentenstränge und zitierte LH4.0-Klärung abstimmen. |
| Ereigniskatalog LH-SIG-105 | Nicht freigegeben. Schaltbeispiele und breite Störungsdefinition abgleichen. |
| Expositionsnenner | Nicht definiert. Kalenderzeit, Zeit unter Spannung, Leuchtdauer und Betriebsbereitschaft sind nicht austauschbar. |
| Zählung wiederholter Ereignisse | Nicht definiert. Anzahl betroffener Geräte ist nicht gleich Ereigniszahl. |
| Statistische Abnahme | Konfidenz, Stichprobe, Zeitraum und feste Jahresgrenze nicht vereinbart. |
| Stückliste und Zuverlässigkeitsdaten | Für eine quantitative Hardwareprognose nicht bereitgestellt. |
| Einsatz- und Temperaturprofile | Nicht freigegeben. Dauer-, intermittierenden, Blink- und seltenen Betrieb gesondert behandeln. |
| Feldstörungs- und Expositionsdaten | Nicht bereitgestellt. Ist-Rate und Erfüllung nicht feststellbar. |
| Instandhaltbarkeitsnachweis | Nicht bereitgestellt. Maximale Tätigkeitsdauer und vollständige Wiederherstellungsgrenze offen. |
| RAM-Plan und quantitative Analysen | S6 verweist auf einen separaten RAM-Plan; vollständige Nachweise liegen nicht vor. |
| THR-Matrizen | Kontrollierte Werte und Zuweisungen beschaffen; hier keine Werte abgeleitet. |
| Informelle PDF-Kommentare | Eine Aussage über aktuell mehr als 400.000 h MTBF enthält keine zugehörige Rechnung und wird nicht als Leistungsnachweis verwendet. |

## 11. Risiken

| Risiko | Technische Folge | Empfohlene Beherrschung |
| --- | --- | --- |
| LH-SIG-105 als nicht berechenbar behandeln | Quantitatives Kundenziel geht bei der Anforderungsüberführung verloren. | Ratenziel erhalten und offene Nachweisbedingungen ausweisen. |
| Erfüllung aus Status Accepted von FL0806 ableiten | Featurezuordnung wird mit Umsetzung und Leistung verwechselt. | Separate Erfüllungsbewertung mit Nachweisreferenz. |
| LH-SIG-105 ohne Ereignisvereinbarung als Hardware-MTBF behandeln | Unbelegte Umrechnung verfälscht die Entwurfsverpflichtung. | Ereignispopulation vereinbaren und Kennzahlnachweise trennen. |
| Sicher-dunkle oder hardwarebedingte Ereignisse ohne Freigabe ausschließen | Zu geringe Ereigniszählung und irreführende Erfüllungsberichte. | Ursache, Sicherheitsstatus und Kennzahlzugehörigkeit separat erfassen. |
| Gemeinsame Ursachen ignorieren | Mehrere Geräte können gleichzeitig gestört werden; Unabhängigkeit gilt nicht. | Umwelt-, Versorgungs-, Kommunikations- und systematische Ursachen bewerten. |
| Maximale Austauschzeit als mittlere Reparaturzeit übernehmen | Instandhaltbarkeitsanforderung wird abgeschwächt. | Maximaldauer und freigegebenes Nachweisverfahren festlegen. |
| 15 Kalenderjahre mit 130.000 Betriebsstunden gleichsetzen | Intermittierender Betrieb und Kalenderalterung nicht ausreichend erfasst. | Betriebsstundennutzungsdauer, Kalenderalterung und Produktunterstützung trennen. |
| Bisheriges Descoping als Kundenverzicht behandeln | Verbindliche Anzeigen oder Zähler könnten fehlen. | Kontrollierte Kundenentscheidung oder Umsetzung. |
| Uneinheitliche Blink- und Temperaturprofile verwenden | Prognose und Nutzungsdauerbeleg repräsentieren den Einsatz nicht. | Rückverfolgbares Profil je anwendbarer Variante freigeben. |
| Nachtlichtstärke kleiner Lichtpunkte unter Kundengrenze | Optische Nichtkonformität und gegebenenfalls Störungsereignis. | 21-cd-/40-cd-Abweichung und Alterungsreserve klären. |

## 12. Empfehlungen

**LH-SIG-105 nicht als „nicht berechenbar“ einstufen und nicht allein aufgrund des Status Accepted von FL0806 als erfüllt erklären.**

Empfohlener Status:

> **Quantitativer Zielwert verstanden; Ereignisklassifikation, Expositionsdefinition und Nachweiskriterien offen; Erfüllung noch nicht nachgewiesen.**

Getrennte Projektanforderungen und Nachweise vorsehen für:

1. Technische Nutzungsdauer und optische Degradation.
2. Hardware-MTBF.
3. Verfügbarkeit.
4. Instandhaltbarkeit und Wiederherstellung.
5. Funktionale Störungshäufigkeit.
6. Sicherheit und Fehlerreaktion.

LH-SIG-105 erst nach Vereinbarung von Interpretation, Gültigkeit und Ereignispopulation in die freigegebene Baseline übernehmen. Quantitative Erfüllung erst nach Vorliegen der vereinbarten Evidenz erklären.

## 13. Erforderliche Nachweise

- Kontrollierte Vertragsbaseline und offizielle Kundenklärung.
- Freigegebene Variantengültigkeit und RAM-Systemgrenze.
- Freigegebener Störungskatalog sowie Zähl- und Expositionsspezifikation.
- Freigegebene Einsatz- und Umweltprofile einschließlich thermischer Modellierung.
- RAM-Plan und kundenfreigegebener RAM-Nachweisplan.
- Hardwareprognose nach Unternehmensmethode mit Datenquellen und Fehlerartenzuordnung.
- Nachweise zu optischer Degradation, Nutzungsdauer und mechanischer Beständigkeit.
- Verfügbarkeitsmodell mit vereinbarten Ausfallzeitanteilen.
- Zeitgemessener Instandhaltbarkeitsnachweis.
- Robustheits- und Schnittstellenprüfberichte.
- FRACAS-Daten, konfigurationskontrollierte Exposition und repräsentative Felderfahrung.
- Sicherheitsnachweis und kontrollierte THR-Zuweisungen.
- Deutsche RAM- und Instandhaltungsdokumentation mit vollständiger bidirektionaler Rückverfolgbarkeit.

## 14. Maßnahmen

| Priorität | Maßnahme | Verantwortliche Rollen | Abschlussnachweis |
| --- | --- | --- | --- |
| 1 | Vertragsbaseline und Anwendbarkeit der zitierten ÖBB-Klärung bestätigen. | Projekt / Anforderungsmanagement / Kunde | Kontrollierte Baseline und Klärungsnachweis. |
| 1 | Störungskatalog, Zählregeln und Expositionsbasis freigeben. | RAM / Systemtechnik / Sicherheit / Kunde | Spezifikationen mit repräsentativen Szenarien. |
| 1 | Abnahmelogik, realisierbare Beobachtungsexposition und Evidenzstrategie vereinbaren. | RAM / V&V / Kunde | Freigegebener RAM-Nachweisplan. |
| 2 | Nutzungsdauer, MTBF, Verfügbarkeit und Störungsrate getrennt spezifizieren. | RAM / Anforderungsmanagement | Geprüfte Anforderungs- und Nachweismatrix. |
| 2 | Mindest-MTBF-Interpretation und fortbestehende Produktzusage von 200.000 h bestätigen. | Produktmanagement / RAM / Anforderungsmanagement | Freigegebene Zielzuweisung. |
| 2 | Descoping von Zählern/Indikatoren und Schwellenrundung klären. | Produktmanagement / Systemtechnik / Kunde | Umsetzungsplan oder schriftliche Kundenentscheidung. |
| 2 | Maximal 600 s je Austauschtätigkeit und vollständige Wiederherstellungsgrenze definieren. | Instandhaltung / V&V / Kunde | Freigegebenes Nachweisverfahren. |
| 2 | Blink- und Umweltprofile abstimmen. | Entwicklung / RAM / Kunde | Freigegebene Variantenprofile. |
| 2 | Nachtlichtstärkeabweichung 21 cd gegenüber 40 cd klären. | Produktmanagement / Optik / Anforderungsmanagement | Optische Spezifikation und Qualifikationsnachweise. |
| 2 | Wartungsfreiheit und Sicherheitsannahmen bei seltenem Betrieb prüfen. | Instandhaltung / Sicherheit / RAM | Instandhaltungskonzept und Sicherheitsannahmen. |
| 2 | THR-Matrizen beschaffen und RAM-Nachweise vollständig zuweisen. | Sicherheit / RAM / V&V | Kontrollierte Zuweisungen und Nachweismatrix. |
| 3 | Fehlende LH-SIG-94-Herkunftsreferenz in 0808 und fehlerhafte Befestigungsreferenz LH-SIG-82 korrigieren. | Anforderungsmanagement / Produktmanagement | Geprüfte bidirektionale Rückverfolgbarkeit. |
| 3 | Vereinbarte Störungstaxonomie, Zählregeln und Nachweisstrategie für künftige Reviews und RAM-Vorlagen wiederverwenden. | RAM-Prozessverantwortlicher | Nach Kundenvereinbarung geprüfte wiederverwendbare Anleitung. |

## 15. LH-SIG-105: Formulierung der Projektanforderung und Erfüllungsnachweis

**Ergänzt am 16.10.2026.** Dieses Kapitel bündelt die vorgeschlagene Anforderung und den praktischen Erfüllungsnachweis. Es ergänzt die vorherige Analyse; es stellt weder eine Kundenfreigabe noch nachgewiesene Erfüllung dar.

Empfohlen wird eine **quantitative Anforderung an funktionale Störungen** mit abgestimmter Nachweisspezifikation, nicht eine weitere Hardware-MTBF-Anforderung.

> Die Anforderung legt die zulässige Störungshäufigkeit fest. Die Nachweisspezifikation definiert, was gezählt wird, wie die Exposition bestimmt wird und wann die Evidenz ausreicht.

### 15.1 Vorgeschlagene Projektanforderung

> **NGB-RAM-DST-105-01 – Zulässige funktionale Störungsrate**  
> Die funktionale Störungsrate des Signalgebers darf unter dem freigegebenen Einsatz- und Umgebungsprofil **0,001 Störungsereignisse je Signalgeberjahr** nicht überschreiten. Als Störungsereignisse gelten die im freigegebenen Störungskatalog für LH-SIG-105 definierten Ereignisse. Die Ermittlung der Exposition erfolgt gemäß der freigegebenen Nachweisspezifikation.

**Rückverfolgbarkeit:** LH-SIG-105 → SE:FL:FEA:0806 → NGB-RAM-DST-105-01.

Diese Formulierung präzisiert denselben Entwurf wie in Kapitel 7 und ist keine zweite unabhängige Anforderung. Sie ist eine **vorgeschlagene Ereignisrateninterpretation**, keine vereinbarte Vertragsklärung. Eine Anzahl betroffener Geräte darf nicht stillschweigend durch eine Ereigniszahl ersetzt werden, wenn der Kunde Ersteres meint.

### 15.2 Zugehörige Ereignisdefinition

Ausgehend von der in S4 zitierten Klärung wird folgende Definition zur Freigabe vorgeschlagen:

> Ein LH-SIG-105-Störungsereignis liegt vor, wenn ein gültiger Schaltauftrag unter spezifizierten Betriebsbedingungen nicht zum geforderten funktionalen Verhalten des Signalgebers führt und das Ereignis dem vereinbarten, nicht-sicherheitsrelevanten Ereignisumfang zugeordnet ist.

**Beispiel:** Ein gültiger Einschaltbefehl wird ausgegeben, der grüne Lichtpunkt bleibt jedoch über die spezifizierte Reaktionszeit hinaus dunkel.

Die Reaktionszeit ist aus der anwendbaren Funktions-/Schnittstellenspezifikation zu übernehmen. Die Definition führt keinen neuen Zeitgrenzwert ein.

| Thema | Vor Baseline-Freigabe erforderliche Entscheidung |
| --- | --- |
| Ereignisumfang | Nur fehlerhafte Schaltvorgänge oder auch Flackern, zeitweilige Lichtstärkeabweichungen und andere LH-SIG-10-Störungen? |
| Wiederholung | Zählt ein dauerhafter Dunkelzustand einmal oder jeder erfolglose Befehl? |
| Wiederherstellung | Ab wann kann ein wiederhergestelltes Gerät ein neues Ereignis erzeugen? |
| Exposition | Kalenderzeit im Einsatz, Zeit unter Spannung oder andere vereinbarte Basis? |
| Zuordnung | Wie werden externe Versorgungs-/Schnittstellenstörungen und hardwarebedingte Schaltfehler behandelt? |
| Gültigkeit | Gilt die zitierte LH4.0-Klärung für das Projekt? V1.1 gilt für konventionelle/SEA-Varianten, nicht DSTW. |

Eine Störung nicht allein deshalb ausschließen, weil sie sicher, selbstbehebend oder hardwarebedingt ist.

### 15.3 Drei Ebenen des Erfüllungsnachweises

| Nachweisebene | Methode | Aussage |
| --- | --- | --- |
| **Entwurfsabsicherung** | Fehlerartenanalyse, Schnittstellen-/Zeitverhaltensprüfung, Diagnosebewertung und Analyse gemeinsamer Ursachen. | Relevante Störungsmechanismen wurden identifiziert und behandelt. |
| **Funktionale Verifikation** | Schalten, Start/Neustart, Blinken, seltener Betrieb, Versorgungsbereich, Temperatur und EMV. | Das geforderte Verhalten wird unter den geprüften Bedingungen erreicht. |
| **Quantitativer Nachweis** | Repräsentative Felddaten oder begründete gleichwertige Evidenz mit vollständiger Expositionsbilanz. | Ob das quantitative Ziel der Störungshäufigkeit nachgewiesen ist. |

**Bestandene Funktionstests allein belegen keine Rate von 0,001 je Signalgeberjahr.** Eine Hardware-MTBF-Berechnung deckt ebenfalls nicht alle intermittierenden, Software-, Zeitverhaltens- und Schnittstellenstörungen ab.

#### 15.3.1 Erforderliche Ereignis- und Expositionsdaten

Je Ereignis erfassen:

- Geräteidentität und Hardware-/Softwarekonfiguration.
- Befehl, erwartete und beobachtete Reaktion.
- Zeitstempel und Betriebsbedingungen.
- Dauer, Wiederherstellung und Korrekturmaßnahme.
- Klassifikation und Zuordnung.

Für den Nenner die anrechenbaren Beobachtungszeiten jedes Geräts einschließlich Einbau/Ausbau und Überwachungslücken erfassen.

Die Datenerfassung zwischen Signalgeber, Stellwerk, Servicewerkzeugen und FRACAS zuweisen. Nicht die gesamte Aufzeichnung muss im Signalgeber implementiert sein.

### 15.4 Beispiel für die quantitative Abnahme

#### 15.4.1 Eingangsgrößen und Annahmen

- Ziel: $r_D \leq 0{,}001$ Ereignisse/Signalgeberjahr.
- Beispielkriterium: **95 % einseitige Konfidenz**, keine Vertragsforderung.
- Homogener Poisson-Prozess, repräsentative Exposition und vollständige Beobachtung.
- Unabhängigkeit und konstante Rate begründen; gemeinsame Ursachen gesondert behandeln.

#### 15.4.2 Formel

Beobachtete Rate:

$$
\hat r_D = \frac{K}{E}
$$

$K$ ist die Anzahl zählbarer Ereignisse, $E$ die anrechenbare Exposition in Signalgeberjahren.

Bei null beobachteten Ereignissen ergibt sich die obere Konfidenzgrenze:

$$
r_{D,U} = \frac{-\ln(0{,}05)}{E}
$$

#### 15.4.3 Berechnung

$$
E \geq \frac{-\ln(0{,}05)}{0{,}001}
= 2995{,}7\ \text{Signalgeberjahre}
$$

#### 15.4.4 Ergebnis

| Beobachtung | Obere Ratengrenze, Ereignisse/Signalgeberjahr | Interpretation unter dem Beispielkriterium |
| --- | --- | --- |
| Null Ereignisse in 100 Signalgeberjahren | Etwa 0,02996 | Positiver Hinweis, aber unzureichende Evidenz. |
| Null Ereignisse in 1.000 Signalgeberjahren | Etwa 0,002996 | Quantitatives Ziel nicht nachgewiesen. |
| Null Ereignisse in 3.000 Signalgeberjahren | Etwa 0,000999 | Quantitatives Ziel nachgewiesen, sofern die Annahmen gelten. |

Der Kunde muss festlegen, ob die Abnahme eine Konfidenzgrenze, eine beobachtete Rate oder eine feste jährliche Ereignisobergrenze verwendet. Diese Kriterien sind nicht gleichwertig.

### 15.5 Praktische gestufte Nachweisstrategie

| Stufe | Erforderliche Tätigkeit | Ergebnis / zulässige Aussage |
| --- | --- | --- |
| **Vor Entwurfsbaseline** | Ereignisdefinition, Exposition, Gültigkeit und Abnahmemethode freigeben. | Anforderung und Nachweisbasis vereinbart. |
| **Vor Produktfreigabe** | Entwurfsabsicherung und Robustheitstests abschließen; übertragbare Evidenz bisheriger Produkte bewerten. | Entwurf und geprüftes Verhalten abgesichert; quantitative Erfüllung nur bei ausreichender vereinbarter Evidenz. |
| **Im Pilot-/Regelbetrieb** | Repräsentative Exposition sammeln und vereinbarten statistischen Nachweis führen. | Quantitative Erfüllung gemäß freigegebener Abnahmeregel bewertet. |

Daten bestehender Produkte können den Nachweisaufwand nur reduzieren, wenn die Übertragbarkeit auf neue Hardware, Software, Schnittstellen, Einsatzprofil und Erfassungsvollständigkeit belegt ist. Ähnliche Produktnamen oder eine gemeinsame Architektur allein reichen nicht aus.

Wenn vor Lieferung nicht genügend Exposition erreichbar ist, eine **gestufte Abnahme mit dem Kunden vereinbaren**. „Tests bestanden“ nicht ohne diese Vereinbarung anstelle des quantitativen Erfüllungsnachweises verwenden.

### 15.6 Empfohlene Aussage zum aktuellen Erfüllungsstand

Die folgende Formulierung ist nur zu verwenden, wenn die genannten unterstützenden Aktivitäten tatsächlich vorgesehen bzw. eingerichtet sind. Sie behauptet nicht, dass diese bereits abgeschlossen wurden:

> Die Anforderung ist spezifiziert und wird durch konstruktive Maßnahmen sowie Funktions- und Robustheitsprüfungen unterstützt. Der quantitative Nachweis der zulässigen Störungsrate erfolgt gemäß dem mit dem AG abgestimmten RAM-Nachweisplan. Bis zum Vorliegen ausreichender repräsentativer Nachweisdaten bleibt der quantitative Erfüllungsnachweis offen.

**Fazit:** Die Anforderung kann spezifiziert und der Entwurf gegen relevante Störungsmechanismen verifiziert werden. Vollständige quantitative Erfüllung benötigt eine vereinbarte Nachweismethode und ausreichende repräsentative Evidenz.

## 16. Prüfung der Review-Artefakte

Das zugehörige Review-Register und die Berechnungsarbeitsmappe wurden während der ursprünglichen Analyse erzeugt und erneut geöffnet. Geprüft wurden:

- 84 Quelleinträge und vollständige Abdeckung der inhaltlichen RAMS-Kapitelanforderungen.
- Acht separat abgeleitete LH-SIG-105-Anforderungen.
- Zwanzig Klärungs-/Maßnahmeneinträge.
- CSV-Struktur und Existenz vollständig qualifizierter bisheriger Feature-IDs.
- Berechnungen zu Rate, Exposition und vereinfachter Verfügbarkeit.

Diese Prüfungen betreffen die Review-Artefakte und Berechnungen, **nicht die tatsächliche Produktkonformität**. Die Quelldokumente wurden nicht verändert.

Für die deutsche Fassung bleiben Kennungen, Werte, Nachweisannahmen und Kapitelstruktur der englischen Bezugsfassung erhalten. Die englische Fassung bleibt unverändert verfügbar.
