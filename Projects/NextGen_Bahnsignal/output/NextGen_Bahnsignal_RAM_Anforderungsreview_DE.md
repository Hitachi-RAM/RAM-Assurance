# NextGen_Bahnsignal – RAM-Anforderungsreview

**Datum der ursprünglichen Analyse:** 15.10.2026

**Überarbeitet:** 19.10.2026 – Beschränkung auf bestehende Anforderungen und dokumentierte Klärungen.

**Status:** Quellenbezogene technische Analyse. Keine neue Anforderungsspezifikation, keine Abnahmevorschrift und keine Konformitätserklärung.

**Gegenstand:** Vergleich des Lastenhefts Signalgeber mit der bisherigen Feature List Signal Element; Schwerpunkt LH-SIG-105.

**Parallelfassung:** [Englischer Bericht](./NextGen_Bahnsignal_RAM_Requirements_Review.md).

**Korrektur gegenüber der bisherigen Fassung:** Eigene Requirement-Entwürfe, zusätzliche Nachweispflichten und statistische Abnahmekriterien wurden entfernt. Sie waren nicht durch die zitierten Kundenanforderungen vorgegeben. Die Rücknahme ist in Kapitel 16 dokumentiert. Die übrigen Projektquellen wurden nicht verändert.

## Inhaltsverzeichnis

- [1. Zusammenfassung](#1-zusammenfassung)
- [2. Angewendete Skills](#2-angewendete-skills)
- [3. Quellen und Prüfumfang](#3-quellen-und-prüfumfang)
  - [3.1 Umfang und Einschränkungen](#31-umfang-und-einschränkungen)
- [4. Befunde: RAM-Anforderungen und Vergleich mit der bisherigen FL](#4-befunde-ram-anforderungen-und-vergleich-mit-der-bisherigen-fl)
  - [4.1 Weitere RAM-relevante Anforderungen](#41-weitere-ram-relevante-anforderungen)
  - [4.2 Wichtige Abgrenzungen](#42-wichtige-abgrenzungen)
- [5. LH-SIG-105: Quellenlage und Interpretation](#5-lh-sig-105-quellenlage-und-interpretation)
  - [5.1 Lastenheft](#51-lastenheft)
  - [5.2 Feature List](#52-feature-list)
  - [5.3 Dokumentierte Kundenklärung](#53-dokumentierte-kundenklärung)
  - [5.4 Jahresbezug und offene Interpretation](#54-jahresbezug-und-offene-interpretation)
- [6. Abgrenzung zur Hardware-MTBF](#6-abgrenzung-zur-hardware-mtbf)
- [7. Bestehende Anforderung statt neuer Requirements](#7-bestehende-anforderung-statt-neuer-requirements)
- [8. Nachweisfrage ohne zusätzliche Abnahmekriterien](#8-nachweisfrage-ohne-zusätzliche-abnahmekriterien)
- [9. Abgrenzung von Verfügbarkeit und Instandhaltbarkeit](#9-abgrenzung-von-verfügbarkeit-und-instandhaltbarkeit)
- [10. Offene Informationen](#10-offene-informationen)
- [11. Risiken der Interpretation](#11-risiken-der-interpretation)
- [12. Ergebnis der Anforderungsanalyse](#12-ergebnis-der-anforderungsanalyse)
- [13. Dokumentierte Nachweisanforderungen und vorliegende Evidenz](#13-dokumentierte-nachweisanforderungen-und-vorliegende-evidenz)
- [14. Offene Klärungsfragen](#14-offene-klärungsfragen)
- **[15. LH-SIG-105: Jahresbezogene Bewertung der bestehenden Forderung](#15-lh-sig-105-jahresbezogene-bewertung-der-bestehenden-forderung)**
  - [15.1 Bezugsanforderung](#151-bezugsanforderung)
  - [15.2 Ereignisumfang](#152-ereignisumfang)
  - [15.3 Aussagekraft von Prüfungen](#153-aussagekraft-von-prüfungen)
  - [15.4 Lesbares Rechenbeispiel für ein Jahr](#154-lesbares-rechenbeispiel-für-ein-jahr)
    - [15.4.1 Eingangsgrößen des Beispiels](#1541-eingangsgrößen-des-beispiels)
    - [15.4.2 Rechenregel](#1542-rechenregel)
    - [15.4.3 Berechnung](#1543-berechnung)
    - [15.4.4 Aussage und Grenze des Beispiels](#1544-aussage-und-grenze-des-beispiels)
  - [15.5 Nicht aus der Quelle ableitbare Festlegungen](#155-nicht-aus-der-quelle-ableitbare-festlegungen)
  - [15.6 Aktueller Erfüllungsstand](#156-aktueller-erfüllungsstand)
- [16. Korrekturregister und Dokumentprüfung](#16-korrekturregister-und-dokumentprüfung)

## 1. Zusammenfassung

**LH-SIG-105 enthält eine quantitative, jahresbezogene Störungsforderung. Sie ist nicht allein deshalb unberechenbar, weil sie weder MTBF noch Verfügbarkeit nennt.**

Die Quellen unterscheiden:

- **LH-SIG-94:** Verfügbarkeit mindestens **0,9999**.
- **LH-SIG-95:** MTBF **100.000 h**.
- **LH-SIG-105:** „Pro Jahr darf bei einem von 1000 Signalgebern eine Störung erfolgen.“
- **SE:FL:FEA:0806:** höchstens **0,001 Funktionsstörungen je Element und Jahr**.

Die in S4 zitierte ÖBB-Klärung beschreibt einen nicht sicherheitsrelevanten fehlerhaften Schaltvorgang, beispielsweise einen grünen Lichtpunkt, der beim Einschalten dunkel bleibt. Ihre Anwendbarkeit auf die Projektbaseline ist nicht belegt, da der E-Mail-Verlauf auf ein nicht vorliegendes LH 4.0 verweist.

**Der Jahresbezug bleibt erhalten.** Die Analyse ersetzt ihn weder durch einen mehrjährigen Beobachtungszeitraum noch durch einen statistischen Mittelwert über mehrere Jahre. LH-SIG-105 und FL0806 legen jedoch nicht allein fest, wie eine konkrete Abnahmeprüfung auszuführen ist.

Eine beobachtete Jahresrate lässt sich aus passenden Daten berechnen. Ein Feature-Status Accepted oder eine Hardware-MTBF-Berechnung allein belegt nicht die beobachtete jährliche Störungsrate. Ein tatsächlicher Erfüllungsnachweis liegt in den bereitgestellten Unterlagen nicht vor.

## 2. Angewendete Skills

Für die technische Analyse wurden folgende Repository-Methodiken berücksichtigt:

- [Railway-RAM](../../../Skills/Railway-RAM.md): Abgrenzung der RAM-Größen und Prüfung der Projektquellen.
- [REQ-Review](../../../Skills/REQ-Review.md): Trennung von Anforderung, Interpretation und fehlender Information.
- [RAM-Metrics](../../../Skills/RAM-Metrics.md): Einheit und Berechnung einer beobachteten Störungsrate.
- [Reliability-Prediction](../../../Skills/Reliability-Prediction.md): Grenzen des Vergleichs mit Hardware-MTBF.

Diese Methodiken begründen keine zusätzlichen Kundenanforderungen. Ein statistisches Konfidenzniveau wird daraus nicht als Projektforderung übernommen.

## 3. Quellen und Prüfumfang

| Referenz | Quelle | Verwendung |
| --- | --- | --- |
| S1 | [715 LH Signalgeber DSTW V1.1_Kom_SS_20250704.pdf](../715%20LH%20Signalgeber%20DSTW%20V1.1_Kom_SS_20250704.pdf) | Lastenheftanforderungen, IDs, Verbindlichkeit und Gültigkeit; insbesondere S. 5 und S. 17–22. |
| S2 | [LH Signalgeber V2.0 signed.pdf](../LH%20Signalgeber%20V2.0%20signed.pdf) | Kundenanforderungen für konventionelle und SEA-Varianten; Freigabe vom 08.05.2024. |
| S3 | [FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx](../FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx) | Bisherige Produktfeatures; 3BU 62200 1001 FLAPQ, ED01, Änderungsverzeichnis vom 08.10.2025. |
| S4 | [RE_ Aufklärungen durch ÖBB bei LED Ausschreibung.msg](../RE_%20Aufkl%C3%A4rungen%20durch%20%C3%96BB%20bei%20LED%20Ausschreibung.msg) | Interner Verlauf vom 08.01.2026 mit zitierter Kundenantwort vom 12.12.2025; kein separat vorliegender offizieller Antwortnachweis. |
| S5 | [D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf](../D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf) | Zusätzliche Umwelt- und Gehäuseanforderungen, soweit anwendbar. |
| S6 | [SSDD_iLED_01PD01.docx](../SSDD_iLED_01PD01.docx) | Architektur und Diagnoseverhalten; verweist auf einen separaten RAM-Plan, enthält aber keinen quantitativen Nachweis zu LH-SIG-105. |

Als Prozess- und Review-Kontext wurden außerdem [G-PRD_S06000_02_EN.pdf](../../../Knowledge/Process/RAM-Process/G-PRD_S06000_02_EN.pdf) und [Requirements_Lessons.md](../../../Knowledge/Lessons_Learned/Requirements_Lessons.md) betrachtet. Prozesshinweise und Beispiellehren sind keine projektbezogenen Kundenforderungen oder Felddaten.

### 3.1 Umfang und Einschränkungen

- Der Vergleich umfasst LH-SIG-84 bis LH-SIG-116 und LH-SIG-139 sowie ausgewählte RAM-relevante Anforderungen außerhalb des RAMS-Kapitels. LH-SIG-83 und LH-SIG-117 sind Überschriften.
- Die Tabellen geben technische Zusammenfassungen wieder, keine vollständigen wortgetreuen Abschriften. Nur ausdrücklich gekennzeichnete Zitate sind Quellwortlaut.
- Verbindlichkeit und Gültigkeit beziehen sich auf S1. S2 gehört zu einem anderen Dokumentenstrang; Versionsnummern allein bestimmen keine vertragliche Rangfolge.
- S4 nennt LH 4.0 und die FL-Kennung FLAPC. Vorhanden sind die oben aufgeführten LH-Fassungen und FLAPQ. Die Abweichung bleibt offen.
- Ein eigenständiges, freigegebenes Projekt-Pflichtenheft mit einer verbindlichen Nachweismethode zu LH-SIG-105 wurde unter den sechs bereitgestellten Projektdateien nicht identifiziert. S6 ist eine Systementwurfsbeschreibung.
- Es werden keine neuen Requirement-IDs, Grenzwerte, Testumfänge, Aufzeichnungsfunktionen oder Abnahmeverfahren festgelegt.
- Angaben als Info oder Soll werden nicht zu Muss-Anforderungen hochgestuft.
- Es handelt sich nicht um einen vollständigen Review aller funktionalen, elektrischen, optischen oder sicherheitstechnischen Anforderungen.

## 4. Befunde: RAM-Anforderungen und Vergleich mit der bisherigen FL

Featurenummern stehen verkürzt für **SE:FL:FEA:xxxx**. Die letzte Spalte enthält Quellenvergleiche und offene Punkte, keine zusätzlichen Projektanforderungen.

| LH-Anforderung | Inhalt der bestehenden Quelle | Bisherige FL | Vergleich / offener Punkt |
| --- | --- | --- | --- |
| **84, 88** | Montage und Tausch mit handelsüblichem Werkzeug. | 1006; 0316/0317 | Inhaltliche Entsprechung. Konkrete Nachweisbedingungen sind durch diesen Vergleich nicht festgelegt. |
| **85** | Austausch von Frontoptik, Leuchtmittel oder Elektronik ohne Gehäusedemontage bzw. optische Neueinstellung. | 1005 | In V1.1 Info. LRU-Tausch entspricht nicht zwingend separatem Komponententausch. |
| **86–87** | Gehäuseunabhängiger Tausch von Lichtpunkt-/Anzeigerteilsystem ohne optische Neueinstellung. | 1005 | In V1.1 Soll; S2 verwendet für das Lichtpunktteilsystem verbindlichere Formulierungen. Gültigkeit für 87 in S1 nicht befüllt. |
| **89** | Tausch ohne Änderung physikalischer und funktionaler Eigenschaften. | 1005 | Inhaltliche Entsprechung; konkrete Umsetzung nicht nachgewiesen. |
| **90** | Einbau/Austausch maximal 10 min, als MRT bezeichnet. | 0811; 1005 | 0811 verwendet eine mittlere Reparaturzeit und schließt Vor-/Nachbereitung aus; 1005 fordert weniger als 10 min. Maximum und Mittelwert sind nicht gleichbedeutend. 10 min entsprechen 600 s, ohne neue Zeitvorgabe. |
| **91** | Sichtbarkeit trotz Degradation, Temperatur und Teilausfällen während der Nutzungsdauer erhalten. | 0219; 0810 | Teilweise optische Nutzungsdauerabdeckung; kein vollständiger Nachweis durch die Featuretexte. |
| **92** | Achslichtstärkebereich während der Nutzungsdauer nicht unterschreiten. | 0808/0810 | 0808 referenziert die ID, fordert im verbindlichen Text aber Verfügbarkeit/MTBF statt einer expliziten optischen Grenze. |
| **93** | Technische Nutzungsdauer mindestens 130.000 Betriebsstunden. | 0810; Kommentare zu 0808 | 15 Kalenderjahre sind bei intermittierender Nutzung nicht gleich 130.000 Betriebsstunden. |
| **94** | Verfügbarkeit mindestens 0,9999 über die Lebensdauer. | 0808 | Zahlenwert entspricht 99,99 %. Verfügbarkeitsart und Ausfallzeitumfang sind in diesem Wortlaut nicht definiert. |
| **95** | „Ein Signalgeber muss eine MTBF von 100.000h aufweisen.“ | 0808: mindestens 200.000 h | FL nennt ausdrücklich einen Mindestwert; LH-Wortlaut nicht. Vergleich hängt auch von Systemgrenze, Fehlerdefinition und Profil ab. |
| **96** | Schaltungstechnische Maßnahmen zur Nutzungsdauererreichung freigestellt. | Entwurfsprinzipien | Info/Gestaltungsfreiheit, kein eigenes Zahlenziel. |
| **97** | Betriebsstunden lokal speichern; Gültigkeit SEA. | 0407 | Zählt Zeit unter Spannung einschließlich Dunkelzeit. |
| **98** | Nutzungsanzeige ohne Demontage/Zusatzsystem am Standort sichtbar. | 0633 | Feature Descoped trotz Muss in S1 für konventionelle/SEA-Varianten; keine Kundenbefreiung belegt. |
| **99** | Grün bis 68 %, gelb 68,1–81,1 %, rot ab 81,2 % der Nutzungsdauer. | 0634 | Feature Descoped. Umgang mit Werten zwischen den genannten Grenzen im Wortlaut nicht erläutert. |
| **100** | Position des Indikators mit dem AG abstimmen. | 0633 | Kundenabstimmung aus dem Featurestatus nicht belegbar. |
| **101** | Kabelgebundenes Auslesen nach Demontage. | 0643 | CAN-Auslesen beschrieben; Anwendbarkeit auf konventionelle Varianten offen. |
| **102** | Drahtloses Auslesen ohne Demontage. | 0644 | Soll in S1, Descoped in FL. Descope ist keine dokumentierte Kundenbefreiung. |
| **103** | Nutzungsdauer umfasst Gesamtsystem ab kabelseitiger Klemmleiste einschließlich vollständigem Stecker. | 0810 | Inhaltliche Entsprechung. Aussage betrifft ausdrücklich die Nutzungsdauergrenze. |
| **104** | Durchschnittlich 300 Einschaltungen/Tag bzw. 100 Blinkanschaltungen/Tag zu je 2 min; kontinuierlicher bis sehr seltener Betrieb. | 0810/0812/0813 | Unterschiedliche FL-Profile: unter anderem 300 × 2 min und 100 × 1 min. S1 kennzeichnet die Angabe als Info; Durchschnitt ist kein universeller Maximalwert. |
| **105** | Pro Jahr darf bei einem von 1.000 Signalgebern eine Störung erfolgen. | 0806 | Jährliche Normierung 0,001 Funktionsstörungen je Element und Jahr vorhanden. Ereigniszählung und konkrete Nachweismethode nicht vollständig beschrieben. |
| **106** | Bei Störung hochohmige Stellwerksschnittstelle, konventionell. | 0805 | Verwandte analoge Fehlerreaktion; keine neue Impedanz-/Zeitgrenze aus diesem Review. |
| **107** | Störungsoffenbarung an der Schnittstelle, DSTW/SEA. | 0805; 0406 | Diagnoseverhalten beschrieben; numerische Erfüllung nicht aus Featuretext ableitbar. |
| **108–109** | Keine erforderliche vorgeschriebene/periodische Wartung; Ausnahme äußere Reinigung. | 1001 | Inhaltlich ähnlich. Wortlaut zu korrektiven Eingriffen und Reparatur nach zufälligem Ausfall auslegungsbedürftig. |
| **110** | Falls erforderlich: Instandhaltungs-/Inspektionsintervall mindestens 2 Jahre. | 1004 | „Im Idealfall keine wiederkehrende Prüfung“ übernimmt die Zweijahresgrenze nicht ausdrücklich. |
| **111** | Mindestens 4 Jahre als Intervallziel, Soll. | 1004 | Keine explizite Vierjahresangabe identifiziert. |
| **112** | Keine vorgeschriebene Stellwerksansteuerung/Zustandswechsel für Instandhaltungszwecke über Sicherheitsnachweis/Anwendungsbedingungen. | 1003 | „Sicherheit oder Anwendungsbedingungen nicht beeinflussen“ ist nicht dasselbe wie das Verbot einer geforderten Ansteuerung. |
| **113** | SIL4-Sicherheit im Zulassungsnachweis dokumentieren. | 0801/0807 | Sicherheit ist von Störungsrate und Verfügbarkeit zu unterscheiden. |
| **114–116** | THR-Matrizen für kleine/große Lichtpunkte und Signalgeber. | 0801 | Allgemeiner FL-THR-Wert ersetzt nicht ohne Zuordnung die referenzierten Matrizen. |
| **139** | Leuchtdauer lokal speichern; konventionelle Varianten. | 0407 | Betriebsstunden einschließlich Dunkelzeit sind nicht dieselbe Größe wie Leuchtdauer. |

### 4.1 Weitere RAM-relevante Anforderungen

| LH-Anforderung | Quelleninhalt / RAM-Bezug | Vergleich / offener Punkt |
| --- | --- | --- |
| **5–9** | Signalgebertypen und Gesamtsystemdefinitionen. | Optik, Schnittstelle, Stecker, Befestigung und Gehäuse gehören entsprechend der jeweiligen Definition zum System. |
| **10–11** | Störungsdefinition und nicht spezifiziertes optisches Verhalten. | Breiter als das Schaltbeispiel in S4; Verhältnis zur Klärung offen. |
| **12–13** | Störungszustand, dunkel/hochohmig. | 0805 behandelt nicht behebbare Fehler; vollständige Deckung und digitale Anwendbarkeit nicht belegt. |
| **18** | Normen einschließlich EN 50126-1. | 0108/0701/0807 enthalten Bezüge; Vertragsausgaben sind damit nicht abschließend bestimmt. |
| **33, 35–36** | Erhalt der Justierung, Tausch ohne Neujustierung, Massegrenzen. | 0317/1005 sowie Massefeatures haben Entsprechungen, teilweise strengere Produktwerte. |
| **40–48** | Umwelt, Schnee, Temperatur, EMV, Transport/Lagerung, IP, Druck/Sog. | 0703/0706/0707/0314/0803/0301 behandeln diese Themen. IP65 in FL gegenüber IP54 im LH; Temperaturbezüge und Profile nicht durchgehend gleich. |
| **54–57, 63, 65** | Sichtbarkeit, Winkel, Verteilung und Erhalt der Lichtstärke. | Funktionale Kriterien für Störungen und Nutzungsdauer, keine zusätzlichen MTBF-Ziele. |
| **67–69** | Farbstabilität bei Alterung, Temperatur, Spannung und Phantomlicht. | 0220 mit entsprechender Intention; informelle Farbabweichungen belegen keine Kundenfreigabe. |
| **71, 74, 81–82** | Fehleroffenbarung, Serienschaltung, Spannungsverhalten, kein Flackern bei einpoliger Abschaltung. | Schnittstellenbezug zur Störungsdefinition. 0317 referenziert LH-SIG-82 fälschlich für Befestigung. |
| **76–77** | 1 Hz, Tastverhältnis 1:1, Toleranzen. | 0502 enthält engere Toleranz; daraus folgt keine LH-SIG-105-Zählregel für Blinkflanken. |
| **118–120** | RAM-Nachweise, deutsche Sprache, digitale veränderbare/unveränderbare Formate. | 0904/0905/0807 teilweise passend; englische generische Unterlagen allein entsprechen nicht der deutschen Lieferforderung. |
| **121–123** | Handbuch, Diagnose, Ersatzteile, Messverfahren und Werkzeuge. | 0904/0905/1006 mit Entsprechungen; vollständige Lieferung nicht belegt. |
| **124–126** | Kennzeichnung und maschinenlesbare Angaben. | 0903; daraus folgt nicht automatisch eine zusätzliche Ereignisprotokollierungsfunktion. |
| **135** | Kleine Lichtpunkte: nachts 40–300 cd im genannten Bereich. | 0619 passt nominal; 0624 nennt mindestens 21 cd statt 40 cd. Variantenbezogene Diskrepanz. |
| **136–138** | Anzeigerlichtstärke, Winkel und Erkennbarkeit. | 0218/0601/0602 haben Entsprechungen. Pixel-Ausfallgrenzen anderer Kunden sind nicht automatisch ÖBB-Grenzen. |

### 4.2 Wichtige Abgrenzungen

- Accepted bedeutet Featureannahme, nicht nachgewiesene Umsetzung oder Kundenkonformität.
- Descoped bedeutet Produktentscheidung, nicht nachgewiesenen Kundenverzicht.
- 30 Jahre Produktunterstützung/Produktlebensdauer nach 0809 sind nicht identisch mit 130.000 Betriebsstunden technischer Nutzungsdauer.
- Die gegebenenfalls anwendbare 30-jährige UV-Beständigkeit aus S5 betrifft Gehäuse, nicht automatisch sämtliche Bauteile.
- Umgebungstemperatur, äußere Gehäusetemperatur und innere Bauteiltemperatur sind unterschiedliche Größen. S5 nennt gegebenenfalls −40 bis +70 °C im Gleisbereich; LH-SIG-42/43 beziehen sich auf das Gehäuse.
- Eine FL-Annahme von 20 °C ist nicht mit allen Umweltforderungen gleichzusetzen.

## 5. LH-SIG-105: Quellenlage und Interpretation

### 5.1 Lastenheft

**Wortlaut S1, LH-SIG-105, S. 19:**

> Die zulässige Störungsrate ist wie folgt definiert und darf nicht überschritten werden:
>
> Pro Jahr darf bei einem von 1000 Signalgebern eine Störung erfolgen.

Verbindlichkeit: **Muss**. Gültigkeit: **Konventionell, SEA**. DSTW ist für diese Zeile nicht genannt.

### 5.2 Feature List

**Wortlaut S3, SE:FL:FEA:0806:**

> Die Störungsrate (Anzahl von Störungen je Element und Jahr) für Funktionsstörungen (fallweise Einschaltversagen, fallweise Toleranzüberschreitungen, etc.) eines Signalelements darf nicht mehr als 0.001 betragen.

Die FL nennt als Ursprung LH-SIG105 und den Status Accepted. Sie macht die Normierung auf Element und Jahr explizit und nennt Beispiele funktionaler Störungen.

### 5.3 Dokumentierte Kundenklärung

Die in S4 zitierte Antwort vom 12.12.2025 beschreibt, dass unter 1.000 Signalgebern ein Schaltvorgang im nicht sicherheitsrelevanten Fall fehlerhaft sein darf; Beispiel: grüner Lichtpunkt bleibt beim Einschalten dunkel.

Die Antwort bezeichnet LH-SIG-95 als Verfügbarkeit. Der Lastenheftwortlaut fordert dort jedoch MTBF; Verfügbarkeit steht separat in LH-SIG-94. Diese Terminologieabweichung ändert nicht automatisch die Anforderungstexte.

Die Antwort liegt als Zitat in einem internen E-Mail-Verlauf vor. Ob und mit welcher Rangfolge sie die vorliegenden LH-Fassungen präzisiert, ist nicht abschließend belegt.

### 5.4 Jahresbezug und offene Interpretation

Belegt sind **„pro Jahr“** im LH und **„je Element und Jahr“** in der FL. Es werden keine längere Beobachtungsdauer und keine Mittelung über mehrere Jahre daraus abgeleitet.

Nicht abschließend erklärt sind wiederholte Störungen desselben Geräts, feste oder gleitende Jahresgrenzen sowie der Umgang mit wechselnder Flotte und Erfassungslücken. Das sind offene Analysefragen, keine hier festgelegten Zusatzbedingungen.

## 6. Abgrenzung zur Hardware-MTBF

LH-SIG-95 nennt eine Zeitgröße in Stunden. LH-SIG-105/FL0806 betreffen die Anzahl funktionaler Störungen je Element und Jahr. Die Ereignisumfänge sind nicht als identisch belegt.

Eine Hardwareprognose allein liefert keine beobachtete jährliche Anzahl sporadischer Einschaltfehler oder Toleranzüberschreitungen. Umgekehrt ist ein beobachteter Schaltfehler nicht automatisch frei von Hardwareursachen.

Aus LH-SIG-105 werden hier **weder ein Hardware-MTBF-Ziel noch ein FIT-Ziel oder eine zulässige Fehlerwahrscheinlichkeit je Schaltvorgang** abgeleitet. Die früheren entsprechenden Umrechnungen wurden aus der geltenden Analyse entfernt, da sie zusätzliche Expositions- und Ereignisannahmen benötigten.

Eine tatsächliche Prognose nach FIDES, IEC 61709 oder MIL-HDBK-217 ist nicht Gegenstand dieses Reviews.

## 7. Bestehende Anforderung statt neuer Requirements

Die vorhandene Zuordnung lautet:

```text
LH-SIG-105 → SE:FL:FEA:0806
```

Es werden keine zusätzlichen Projekt-Requirement-IDs und keine erweiterten Muss-Texte eingeführt.

Die zuvor formulierten Pflichten zu freigegebenem Ereigniskatalog, Expositionsspezifikation, Logging, statistischem Nachweisplan und Testszenarien waren Vorschläge des Assistenten. Sie sind keine aus LH-SIG-105 nachgewiesenen Vertragsforderungen und wurden als Requirement-Entwürfe zurückgenommen.

Offene Begriffe dürfen als Klärungsbedarf beschrieben werden. Daraus folgt nicht automatisch, dass der Kunde jeweils ein zusätzliches Dokument oder eine Gerätefunktion verlangt.

## 8. Nachweisfrage ohne zusätzliche Abnahmekriterien

LH-SIG-105 und FL0806 enthalten den Jahresbezug und das Zahlenziel. Ihr zitierter Wortlaut schreibt keine konkrete Gerätezahl für einen Versuch, kein Konfidenzniveau und keine vollständige Abnahmeprozedur vor.

**Bewertung von Prüfungen, keine zusätzliche Prüfforderung:**

| Vorhandene oder denkbare Evidenz | Mögliche Aussage | Was daraus allein nicht folgt |
| --- | --- | --- |
| Featuretext mit Status Accepted | Forderung ist in der FL aufgenommen. | Tatsächliche jährliche Störungsrate ist eingehalten. |
| Funktionstest | Verhalten unter den protokollierten Bedingungen wurde geprüft. | Quantitative Jahresrate, wenn die Ergebnisse keinen nachvollziehbaren Jahresbezug haben. |
| Schalt-/Dauerbetriebsversuch | Kann Ereigniszahlen und Prüfzeit bzw. Schaltzahlen liefern. | Automatische Gleichsetzung von Schaltzahlen oder Laborstunden mit einem Betriebsjahr. |
| Jahresbezogene Betriebsaufzeichnung | Kann eine beobachtete Rate für den betrachteten Gerätebestand und das betrachtete Jahr liefern. | Garantie für andere Jahre oder automatisch eine formelle Kundenabnahme. |
| Hardware-MTBF-Prognose | Aussage zur jeweils modellierten Hardware-Zuverlässigkeit. | Vollständiger Nachweis aller Funktionsstörungen nach FL0806. |

Die Aussage „Bestandene Funktionstests allein belegen keine Rate von 0,001 je Signalgeberjahr“ ist somit eine **Grenze der Aussagekraft**, keine Forderung nach einem bestimmten Zusatztest oder einer statistischen Konfidenz.

Welches Nachweisverfahren im Projekt tatsächlich gilt, ist aus den vorliegenden Dokumenten nicht abschließend feststellbar. Es wird hier nicht erfunden.

## 9. Abgrenzung von Verfügbarkeit und Instandhaltbarkeit

- LH-SIG-94 fordert Verfügbarkeit mindestens 0,9999.
- LH-SIG-90 nennt maximal 10 min für Einbau/Austausch.
- FL0811 bezeichnet eine mittlere Reparaturzeit und schließt Vor-/Nachbereitung aus.

Eine maximale Austauschtätigkeit ist nicht dieselbe Größe wie mittlere vollständige Ausfallzeit. Der Quellenvergleich zeigt diese Unterscheidung, legt aber keine zusätzlichen Ausfallzeitanteile oder Budgets fest.

Die früher berechneten beispielhaften MDT-Grenzen und Verfügbarkeitswerte wurden entfernt. Sie waren modellabhängige Zusatzrechnungen, keine bestehenden Anforderungen.

## 10. Offene Informationen

| Punkt | Befund |
| --- | --- |
| Vertragsrangfolge | Verhältnis von S1, S2 und zitierter LH4.0-Klärung offen. |
| Störungsumfang | Breite LH-SIG-10-Definition, FL-Beispiele und Schaltklärung nicht abschließend abgegrenzt. |
| Wiederholungen | Ereigniszahl gegenüber Anzahl betroffener Geräte bei Wiederholstörungen nicht vollständig erklärt. |
| Jahresabgrenzung | Fester oder gleitender Jahreszeitraum nicht ausdrücklich festgelegt. |
| Wechselnde Gerätepopulation | Behandlung von Teiljahren, Tausch und Erfassungslücken nicht aus dem Wortlaut bestimmt. |
| Nachweismethode | Keine vollständige projektspezifische Abnahmeregel in den bereitgestellten Unterlagen identifiziert. |
| Erfüllungsdaten | Keine jährlichen Störungsaufzeichnungen oder zugeordneten Prüfergebnisse für die konkrete Bewertung bereitgestellt. |
| Weitere RAM-Nachweise | Vollständiger separater RAM-Plan, Berechnungen, Instandhaltbarkeitsnachweis und kontrollierte THR-Zuordnungen liegen in der betrachteten Dateiauswahl nicht vor. |

Diese Lücken belegen fehlende Information in der Review-Grundlage, nicht automatisch fehlende Aktivitäten oder Nichtkonformität im Projekt.

## 11. Risiken der Interpretation

| Risiko | Mögliche Fehlbewertung |
| --- | --- |
| Eigene statistische Regeln ergänzen | Zusätzliche Verpflichtungen werden als Kundenforderung dargestellt. |
| Jahresbezug durch Mehrjahresmittel ersetzen | Eine auffällige Jahresrate könnte durch andere Jahre verdeckt werden; die Quelle belegt diese Mittelung nicht. |
| Normierung mit Testumfang verwechseln | „Je 1.000“ wird ohne Quelle zu zwingend 1.000 Prüflingen erklärt. |
| Ereigniszählung eigenmächtig festlegen | Wiederholstörungen werden ohne Grundlage ausgeschlossen oder mehrfach gezählt. |
| Sichere Dunkelschaltung pauschal ausnehmen | Nicht sicherheitsrelevante Funktionsstörungen könnten unberechtigt entfallen. |
| Accepted oder Descoped als Kundenentscheidung lesen | Erfüllung oder Verzicht wird ohne Nachweis angenommen. |
| MTBF, Nutzungsdauer und Störungsrate gleichsetzen | Unterschiedliche Kenngrößen und Ereignisumfänge werden vermischt. |
| Vorhandene FL-Abweichungen übergehen | Maximum/Mittelwert, Zählerarten, Wartungsintervalle und optische Grenzwerte bleiben unzutreffend zugeordnet. |

## 12. Ergebnis der Anforderungsanalyse

**Quellenbezogenes Ergebnis:**

> LH-SIG-105 enthält eine jahresbezogene Störungsforderung. FL0806 bildet sie mit höchstens 0,001 Funktionsstörungen je Element und Jahr ab. Die konkrete Zähl- und Nachweisauslegung ist in den vorliegenden Unterlagen nicht vollständig beschrieben. Die tatsächliche Erfüllung ist mit den bereitgestellten Daten nicht bewertbar.

Die Forderung ist nicht pauschal „unberechenbar“. Unvollständig sind die Grundlage für eine konkrete Auswertung und der Nachweis, nicht der vorhandene Zahlenwert.

Es gibt in dieser Fassung keine neuen Anforderungsentwürfe oder verbindlichen Abnahmeformulierungen.

## 13. Dokumentierte Nachweisanforderungen und vorliegende Evidenz

| Quellenbezug | Dokumentierte Forderung / vorhandene Aussage | Stand der Review-Grundlage |
| --- | --- | --- |
| LH-SIG-118 | Lieferdokumentation umfasst unter anderem RAM-Nachweise. | Kein daraus ableitbares spezifisches Konfidenzniveau oder Prüfprogramm für LH-SIG-105. |
| LH-SIG-119 | Kundendokumentation auf Deutsch. | Bestehende Lieferforderung, keine Ergänzung des Reviews. |
| LH-SIG-120 | Digitale veränderbare und unveränderbare Dokumentation. | Bestehende Formatforderung. |
| LH-SIG-121–123 | Handbuch, Mess-/Prüfunterlagen bei erforderlichen Messungen und definierte Werkzeuge. | Anforderungen gemäß jeweiliger Anwendbarkeit; keine pauschale zusätzliche Testpflicht aus LH-SIG-105. |
| S6 | Verweis auf einen separaten RAM-Plan. | Verweis ist kein vorliegender quantitativer Erfüllungsbeleg. |
| S3, FL0806 | Forderung mit Status Accepted. | Belegt Aufnahme in die FL, nicht die Ist-Rate. |

Die frühere pauschale Liste „Erforderliche Nachweise“ wurde durch diese Quellenzuordnung ersetzt. Weitere aus RAM-Sicht mögliche Analysen werden nicht als zusätzliche Kundenlieferpflicht deklariert.

## 14. Offene Klärungsfragen

Dies sind **Fragen zur Auslegung vorhandener Anforderungen**, keine zugewiesenen neuen Arbeitspakete oder Requirements.

| Quellenbezug | Offene Frage |
| --- | --- |
| S1/S2/S4 | Welche Dokumentfassung und welche Kundenklärung gelten verbindlich für NextGen_Bahnsignal? |
| LH-SIG-10 / LH-SIG-105 / FL0806 | Wie ist der breite Störungsbegriff gegenüber den Schalt- und Toleranzbeispielen abgegrenzt? |
| LH-SIG-105 | Wie werden wiederholte Störungen desselben Geräts gezählt? |
| LH-SIG-105 / FL0806 | Welches Jahr und welcher Gerätebestand sind für die konkrete Auswertung maßgeblich? |
| LH-SIG-118 / S6 | Gibt es bereits eine verbindliche Nachweismethode in nicht bereitgestellten Projektunterlagen? |
| LH-SIG-90 / FL0811 | Ist die unterschiedliche Interpretation von maximaler Austauschzeit und mittlerer Reparaturzeit geklärt? |
| LH-SIG-93 / FL0810 | Wie ist der Unterschied zwischen Betriebsstunden und Kalenderjahren im konkreten Einsatz berücksichtigt? |
| LH-SIG-98–102 / FL0633/0634/0644 | Gibt es dokumentierte Entscheidungen zu den ausgeplanten Anzeigen und Ausleseoptionen? |
| LH-SIG-104 / FL0812/0813 | Welches der unterschiedlichen Einsatzprofile gilt für die jeweilige Variante? |
| LH-SIG-135 / FL0624 | Wie ist die Abweichung 21 cd gegenüber 40 cd für die betroffene Variante aufgelöst? |

## 15. LH-SIG-105: Jahresbezogene Bewertung der bestehenden Forderung

Dieses Kapitel ersetzt die früheren eigenen Requirement- und Abnahmeentwürfe. Es erläutert nur die vorhandene Forderung und ihre rechnerische Normierung.

### 15.1 Bezugsanforderung

Maßgebliche Texte sind LH-SIG-105 und SE:FL:FEA:0806 aus Kapitel 5. Es wird kein zusätzlicher Muss-Text erstellt.

```text
Lastenheft: Pro Jahr darf bei einem von 1000 Signalgebern eine Störung erfolgen.
FL0806:     Höchstens 0,001 Funktionsstörungen je Element und Jahr.
```

Die FL-Zeile ist hier zusammengefasst; der vollständige Quellwortlaut steht in Abschnitt 5.2.

### 15.2 Ereignisumfang

LH-SIG-10 nennt den Verlust der vollen Funktionsfähigkeit, etwa unzulässige optische Eigenschaften, Schnittstellenverhalten und Flackern. FL0806 nennt fallweises Einschaltversagen und Toleranzüberschreitungen. S4 beschreibt einen nicht sicherheitsrelevanten fehlerhaften Schaltvorgang.

Eine neue Definition mit zusätzlicher Reaktionszeit, Rücksetzbedingung oder Ursachenbefreiung wird daraus nicht formuliert. Die Beziehung der Aussagen bleibt ein Interpretationspunkt.

### 15.3 Aussagekraft von Prüfungen

Ein Funktionstest belegt das protokollierte Verhalten unter seinen Prüfbedingungen. Ob er auch den Jahreswert belegt, hängt vom vorhandenen Nachweisinhalt und seinem Bezug zur Jahresforderung ab.

Weder die Forderung nach statistischer Absicherung noch ein bestimmter Dauer-, Schalt-, Feld- oder beschleunigter Versuch ist im zitierten Wortlaut von LH-SIG-105/FL0806 festgelegt. Solche Methoden werden hier nicht als Pflicht eingeführt.

### 15.4 Lesbares Rechenbeispiel für ein Jahr

#### 15.4.1 Eingangsgrößen des Beispiels

- Betrachtet wird **ein Jahr**, entsprechend dem Jahresbezug der Quelle.
- **1.000 Signalgeber** dienen zur anschaulichen Darstellung der Normierung.
- Beispielhaft sind alle 1.000 Geräte für dieses Jahr im betrachteten Bestand und die gezählten Störungen bekannt.
- Dies sind Rechenannahmen, keine vorgeschriebene Stichprobengröße oder Abnahmeprozedur.

#### 15.4.2 Rechenregel

```text
Für denselben Gerätebestand über ein Jahr:

Beobachtete jährliche Störungsrate =
Anzahl gezählter Funktionsstörungen im Jahr ÷ Anzahl betrachteter Signalgeber

Einheit: Störungen je Signalgeber und Jahr
Quellgrenze FL0806: höchstens 0,001
```

#### 15.4.3 Berechnung

```text
0 Störungen bei 1.000 Signalgebern in einem Jahr:
0 ÷ 1.000 = 0

1 Störung bei 1.000 Signalgebern in einem Jahr:
1 ÷ 1.000 = 0,001

2 Störungen bei 1.000 Signalgebern in einem Jahr:
2 ÷ 1.000 = 0,002
```

Es werden keine drei Beobachtungsjahre benötigt, um diese Jahreswerte auszurechnen. Die frühere Berechnung einer mehrjährigen statistischen Exposition war kein Bestandteil der Kundenforderung und wurde entfernt.

#### 15.4.4 Aussage und Grenze des Beispiels

| Jahresbeobachtung im Beispiel | Vergleich mit dem Zahlenwert aus FL0806 |
| --- | --- |
| 0 Störungen bei 1.000 Signalgebern | Beobachteter Wert liegt unter 0,001. |
| 1 Störung bei 1.000 Signalgebern | Beobachteter Wert entspricht 0,001. |
| 2 Störungen bei 1.000 Signalgebern | Beobachteter Wert liegt über 0,001. |

Das ist ein Zahlenvergleich für das betrachtete Jahr und den angenommenen Ereignisumfang. Er ersetzt keine noch ungeklärte vertragliche Abnahmeregel und garantiert keine Rate für künftige Jahre.

Bei wechselndem Bestand, Teiljahren oder unklarer Ereigniszählung wird hier keine eigene Umrechnungsregel festgelegt.

### 15.5 Nicht aus der Quelle ableitbare Festlegungen

Aus dem zitierten Wortlaut allein folgen nicht:

- eine zwingende Prüfung von genau 1.000 Geräten;
- ein statistisches Konfidenzniveau oder ein Poisson-Modell;
- eine mehrjährige fehlerfreie Beobachtung;
- eine bestimmte Anzahl Laborstunden oder Schaltzyklen;
- eine Pflicht zu zusätzlichem Logging im Signalgeber;
- eine gestufte Kundenabnahme;
- ein eigenes Hardware-MTBF-/FIT-Ziel oder eine Fehlerwahrscheinlichkeit je Schaltung.

Der jährliche Bezug ist vorhanden. Die konkrete Ausführung des Nachweises darf damit nicht verwechselt werden.

### 15.6 Aktueller Erfüllungsstand

**Aus den bereitgestellten Unterlagen feststellbar:** Die Forderung ist im Lastenheft und als FL0806 dokumentiert.

**Nicht feststellbar:** Welche Ist-Rate die projektbezogenen Signalgeber im maßgeblichen Jahr hatten oder ob ein vorhandener Prüfbericht die Forderung verbindlich nachweist.

Es wird nicht behauptet, dass ein abgestimmter Nachweisplan, laufende Tests oder ein Pilotprogramm bereits existieren.

## 16. Korrekturregister und Dokumentprüfung

### Rückgenommene Ergänzungen

Die folgenden Zitate stammen aus der bisherigen Berichtsfassung, nicht aus dem Lastenheft. Sie kennzeichnen konkrete korrigierte Stellen.

| Bisherige Stelle / wörtlicher Auszug | Befund | Korrektur |
| --- | --- | --- |
| Kapitel 7: „Der RAM-Nachweisplan muss statistisches Modell, Konfidenzniveau, Stichprobenexposition, Behandlung gemeinsamer Ursachen und Abnahmeregel vor einer Erfüllungsaussage festlegen.“ | Eigene abgeleitete Muss-Anforderung, nicht Quellwortlaut. | Entwurf und eigene Requirement-IDs entfernt; offene Fragen ohne neue Dokumentpflicht. |
| Kapitel 15.4.1: „Beispielkriterium: **95 % einseitige Konfidenz**, keine Vertragsforderung.“ | Trotz Vorbehalt als Nachweisbasis ausgearbeitet und mit dem Kundenauftrag verwechselt. | Statistisches Abnahmebeispiel entfernt. |
| Kapitel 15.4.4: „Quantitatives Ziel nicht nachgewiesen.“ | Bewertung bezog sich auf das hinzugefügte Konfidenzkriterium, nicht allein auf die Jahresforderung. | Durch reinen Vergleich des beobachteten Jahreswerts mit FL0806 ersetzt. |
| Kapitel 15.5: „Wenn vor Lieferung nicht genügend Exposition erreichbar ist, eine **gestufte Abnahme mit dem Kunden vereinbaren**.“ | Nicht belegte zusätzliche Abnahmegestaltung. | Als Vorgabe entfernt. |
| Kapitel 15.6: „Der quantitative Nachweis der zulässigen Störungsrate erfolgt gemäß dem mit dem AG abgestimmten RAM-Nachweisplan.“ | Existenz eines abgestimmten Plans und vorgesehener Tätigkeiten nicht belegt. | Durch quellenbezogenen Informationsstand ersetzt. |
| Kapitel 13: „Freigegebener Störungskatalog sowie Zähl- und Expositionsspezifikation.“ | Eigene Dokumentliste unter „Erforderliche Nachweise“, nicht aus LH-SIG-105 belegt. | Nachweisanforderungen nur mit Quellenbezug in Kapitel 13. |

Auch die ergänzten Stunden-/FIT-/Schaltwahrscheinlichkeitsumrechnungen, modellabhängigen Verfügbarkeitsbeispiele und pauschalen Test-/Aufzeichnungspflichten wurden entfernt. Formeln werden in lesbarer Textform dargestellt.

### Umfang der Korrektur

- Beide projektbezogenen Markdown-Berichte wurden inhaltlich angeglichen.
- Die nummerierte Struktur und das Inhaltsverzeichnis bleiben erhalten.
- Die Tabellen zum Quellenvergleich bleiben bestehen; ihre Bewertungen sind keine neuen Requirements.
- Lastenhefte, FL und sonstige Quelldokumente wurden nicht geändert.
- Früher erzeugte CSV-/Excel-Artefakte außerhalb dieser Markdown-Berichte wurden mit dieser Korrektur nicht überarbeitet. Die dort enthaltenen eigenen Anforderungsentwürfe und statistischen Kriterien sind ebenfalls keine Kundenanforderungen und dürfen nicht als solche verwendet werden.

Die Dokumentprüfung bestätigt keine Produktkonformität. Sie korrigiert die Abgrenzung zwischen Quelleninhalt, Analyse und unbelegten Ergänzungen.
