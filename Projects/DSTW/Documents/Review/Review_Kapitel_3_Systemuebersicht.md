# Review – Kapitel 3 „Systemübersicht“

**Prüfgegenstand:** [RAM_DIL_3BU_17300_1209_DUAPCEd02PD01.docx](./RAM_DIL_3BU_17300_1209_DUAPCEd02PD01.docx)  
**Prüfumfang:** Kapitel 3, insbesondere Systembeschreibung und Abbildung 1  
**Ergebnis:** Die Grundarchitektur ist weiterhin plausibel und wird durch die verfügbaren Systemunterlagen gestützt. Die Beschreibung ist jedoch **nicht mehr vollständig synchron** mit den jüngeren DIL-Unterlagen. Vor allem Redundanzvarianten und die Beschreibung des ECMUX sollten aktualisiert bzw. eindeutig abgegrenzt werden.

## Befunde

| Thema | Aussage im RAM-Plan | Abgleich mit den verfügbaren Unterlagen | Bewertung / empfohlene Maßnahme |
| --- | --- | --- | --- |
| Cloud-Architektur und Verfügbarkeitszonen | Cloud-/Virtualisierungsinfrastruktur; Server an einem Standort in drei Availability Zones (AZ); Systemfunktion bleibt beim Ausfall einer AZ erhalten. | Das DIL-Sicherheitskonzept beschreibt ebenfalls drei AZ, hochverfügbare Netze und den Erhalt der Systemfunktion beim Ausfall einer AZ. Die SSS Data Center & Networks nennt eine Basisvariante mit einem und eine georedundante Variante mit zwei Rechenzentrumsstandorten. | **Im Grundsatz konsistent.** Ergänzen, dass die Darstellung mit einem Standort die Basisvariante beschreibt und eine georedundante Ausprägung mit zwei Standorten ebenfalls vorgesehen ist. Sonst kann die Ein-Standort-Aussage als vollständige Systemgrenze missverstanden werden. |
| ELEKTRA Core-Redundanz | „2x2oo2“ für ELEKTRA Core; keine Unterscheidung nach Geo-Redundanz. | Das Sicherheitskonzept und die SSS CU Part 1 unterscheiden eine nicht georedundante Basisvariante **2x2oo2** und eine georedundante Variante **4x2oo2**. Die Verteilung der VIL-Instanzen über drei AZ bleibt Teil des Konzepts. | **Unvollständig.** Beide Varianten aufnehmen und klarstellen, auf welche Variante sich die jeweilige Systembeschreibung bezieht. |
| ECMUX-Redundanz | „1oo2 for ECMUX“; das ECMUX wird zusammen mit der TAS Platform 2.6.x und IPS aufgeführt. | Das jüngere DIL-Sicherheitskonzept beschreibt für ECMUX das **J4S-Redundanzkonzept**: Die sicherheitsrelevante Java-Anwendung läuft je Instanz auf einer Hardwareinstanz; redundante ECMUX-Instanzen arbeiten Hot-Hot. Anzahl und Konfiguration hängen unter anderem von den Feldelementen ab. | **Präzisierung erforderlich.** „1oo2“ ist ohne Bezugsobjekt mehrdeutig und bildet die Instanz-/Hardwareebenen aus dem Sicherheitskonzept nicht ab. J4S, Ein-Hardwareinstanz je ECMUX-Instanz und Hot-Hot-Redundanz der ECMUX-Instanzen benennen; die konkrete Zuordnung mit der aktuellen Architektur abstimmen. |
| Feldelement-Subsysteme | Fünf EULYNX-Subsysteme auf Objektcontroller-Ebene: Weiche, Lichtsignal, Generic IO, Zugerkennung und Bahnübergang. | Dieselben fünf Subsysteme sind im DIL-Sicherheitskonzept aufgeführt. | **Konsistent.** Keine Änderung aus diesem Abgleich erforderlich. |
| X25 und Schnittstellenumsetzer | Unter „Schnittstellenkonverter“ stehen X25, IFC-ZG62 und IFC-Sbl60A. | Das Sicherheitskonzept beschreibt Block-IF ZG62 und Block-IF Sbl60A als Schnittstellenumsetzer zur Anbindung von Nachbarblöcken. Die Verbindungen des ELEKTRA Core zu diesen Umsetzern sowie zu RBC, NixL, SCWS und OMC erfolgen mittels X25-over-RaSTA. Die SSS CU Part 1 beschreibt für VIL-zu-VIL-Kommunikation X25 over RaSTA over TLS. | **Begriffe und Zuordnung präzisieren.** X25 selbst nicht als Umsetzer aufführen. Stattdessen die Block-IFs als Schnittstellenumsetzer und X25-over-RaSTA als Kommunikationsweg zu den genannten Komponenten beschreiben. X25 over RaSTA over TLS nur für den in der SSS CU beschriebenen VIL-zu-VIL-Verkehr nennen; keine Protokollvariante pauschal für alle Anschlüsse unterstellen. |
| TAS-Platform-Version | TAS Platform 2.6.x. | Das DIL-Sicherheitskonzept referenziert TAS Platform Core 2.6.0 (redundant bzw. nicht redundant). | **Konsistent auf Versionsfamilienebene.** Für eine belastbare Baseline ggf. die konkrete 2.6.0-Ausprägung und deren Geltungsbereich nennen; keine abweichende Plattformversion in den geprüften Quellen gefunden. |
| Abbildung 1 | Systemübersicht mit DIL-CU/VIL, ELEKTRA Core, ECMUX, IPS/ADM, IFCs, FES und externen Schnittstellen. | Die dargestellten Hauptbausteine und Schnittstellen sind mit der textlichen Beschreibung und den Systemunterlagen grundsätzlich vereinbar. X25-over-RaSTA/TLS erscheint in der Grafik als Kommunikation, nicht als eigenständiger Konverter. | **Kein grundsätzlicher Architekturwiderspruch erkennbar.** Bildunterschrift/-inhalt kann nach Aktualisierung des Begleittexts beibehalten werden; Bezeichnungen und Redundanzvarianten gegen die freigegebene Architekturzeichnung prüfen. |

## Empfohlene Textanpassungen

1. Die Aussage zur Drei-AZ-Architektur als **Basisvariante mit einem Standort** kennzeichnen und die georedundante Variante mit zwei Standorten erwähnen.
2. Für ELEKTRA Core die Varianten **2x2oo2 (Basis)** und **4x2oo2 (georedundant)** aufführen.
3. Die ECMUX-Aussage nicht isoliert als „1oo2“ stehen lassen. Stattdessen das J4S-Konzept und die Redundanz der Hot-Hot-ECMUX-Instanzen beschreiben; die konkrete Hardware-/Instanzzuordnung anhand der gültigen Systemarchitektur verifizieren.
4. Die Aufzählung der Schnittstellenumsetzer auf **Block-IF ZG62** und **Block-IF Sbl60A** begrenzen. X25-over-RaSTA als Kommunikationsweg des ELEKTRA Core zu diesen Umsetzern und den benannten Bestands-Umsystemen beschreiben. X25 over RaSTA over TLS nur für die in der SSS CU Part 1 beschriebene VIL-zu-VIL-Kommunikation anführen.

## Textvorschläge – Alt und Neu

Die folgenden Vorschläge ersetzen die entsprechenden Textabsätze aus **3.1 Systembeschreibung**. Die Absätze zu den fünf EULYNX-Subsystemen und zum projektspezifischen SEMP/RAM-Plan können unverändert bleiben.

### 1. Cloud-Architektur und Standortvarianten

| Alttext | Neuvorschlag |
|---|---|
| Die generische Lösung „Digitales Stellwerk“ (DSTW) basiert auf Cloud- und Virtualisierungstechnologien. Die Cloud-Infrastruktur erfordert ein hochverfügbares Netzwerk, Datenspeicher sowie Cloud- bzw. Virtualisierungssteuerungseinheiten. In der Basisarchitektur werden alle Server-Schränke an einem Standort in drei Verfügbarkeitszonen unterteilt, die über ein hochverfügbares Netzwerk miteinander verbunden sind. | Die generische Lösung „Digitales Stellwerk“ (DSTW) basiert auf Cloud- und Virtualisierungstechnologien. Die Cloud-Infrastruktur umfasst ein hochverfügbares Netzwerk, Datenspeicher sowie Cloud- bzw. Virtualisierungssteuerungseinheiten. In der Basisvariante sind die Serverschränke eines Rechenzentrums auf drei Verfügbarkeitszonen (Availability Zones, AZ) verteilt und über ein hochverfügbares Netzwerk miteinander verbunden. Die Systemarchitektur kann georedundant auf zwei Rechenzentrumsstandorte erweitert werden. |

### 2. VIL-Verteilung und Ausfall einer Verfügbarkeitszone

| Alttext | Neuvorschlag |
|---|---|
| Die virtuellen Stellwerke (VILs) werden redundant und gleichmäßig über die Verfügbarkeitszonen verteilt. Die internen VIL-Verbindungen sind über virtuelle Netzwerke innerhalb des hochverfügbaren Netzwerks isoliert. Auch externe Schnittstellen werden über dieses Netzwerk nach außen geführt. Die Architektur ist so ausgelegt, dass selbst bei Ausfall einer Verfügbarkeitszone die Funktion des Gesamtsystems erhalten bleibt und ausgefallene Einheiten aktualisiert und wieder integriert werden können. | Die virtuellen Stellwerke (VILs) werden redundant und gleichmäßig über die Verfügbarkeitszonen verteilt. Ihre interne Kommunikation erfolgt über virtuelle Netze, die auf dem hochverfügbaren Netzwerk aufsetzen und logisch voneinander getrennt sind. Externe Schnittstellen werden ebenfalls über die vorgesehene Netzwerkinfrastruktur angebunden. Die Basisarchitektur ist darauf ausgelegt, die Systemfunktion auch beim Ausfall einer Verfügbarkeitszone aufrechtzuerhalten. Ausgefallene Einheiten können nach Wiederherstellung aktualisiert und wieder in das Gesamtsystem integriert werden. |

### 3. ELEKTRA Core und ECMUX

| Alttext | Neuvorschlag |
|---|---|
| Das VIL-Kernsystem verwendet das Redundanzkonzept Platform Hot-Hot Redundancy 2x2oo2 for ELEKTRA Core and 1oo2 for ECMUX based on TAS Platform 2.6.x and IPS-Solution. Die Anwendungen des VIL-Kernsystems (CC, RCU und DGP) werden im synchronen Hot-Hot-Betrieb auf mehreren Servern in virtuellen Maschinen parallel ausgeführt, permanent synchronisiert und verglichen. Die zwei unterschiedlichen Softwarekanäle der ELEKTRA-Anwendung bleiben in diesem Konzept erhalten und laufen auf den beiden Hardware-Instanzen des 2oo2-Systems. Das 2oo2-System bzw. die beiden unterschiedlichen Kanäle erkennen zuverlässig Hardwarefehler. | Das VIL-Kernsystem basiert auf der TAS Platform und der IPS Solution. Für das ELEKTRA Core Subsystem ist in der Basisvariante eine 2x2oo2- und in der georedundanten Variante eine 4x2oo2-Konfiguration vorgesehen. Die Anwendungen des ELEKTRA Core Subsystems (CC, RCU und DGP) werden synchron im Hot-Hot-Betrieb auf mehreren Servern in virtuellen Maschinen ausgeführt, kontinuierlich synchronisiert und miteinander verglichen. Die beiden diversitären Softwarekanäle der ELEKTRA-Applikation bleiben erhalten und werden auf den Hardwareinstanzen des jeweiligen 2oo2-Systems betrieben. Für den ECMUX wird das J4S-Redundanzkonzept eingesetzt: Die sicherheitsrelevante Java-Applikation einer ECMUX-Instanz läuft innerhalb einer Virtual-TAS-Platform-VM auf einer Hardwareinstanz; die redundanten ECMUX-Instanzen arbeiten im Hot-Hot-Betrieb. Abhängig von der Anzahl der Feldelemente können ein oder mehrere ECMUX-Subsysteme konfiguriert werden. Die konkrete Konfiguration und Zuordnung der Instanzen ist gemäß der gültigen Systemarchitektur festzulegen. |

### 4. Feldelemente und Schnittstellenumsetzer

| Alttext | Neuvorschlag |
|---|---|
| Die Schnittstelle zu den Feldelementen wird nach dem EULYNX-Konzept realisiert. Die EULYNX-Systemdefinition beschreibt fünf verschiedene Subsysteme auf Ebene der Objektcontroller: Subsystem – Weiche; Subsystem – Lichtsignal; Subsystem – Generische IO; Subsystem – Zugerkennungssystem; Subsystem – Bahnübergang (LX). Zusätzlich zu den Objektcontroller-Subsystemen gibt es die Schnittstellenkonverter: X25; IFC-ZG62; IFC-Sbl60A. | Die Anbindung der Feldelemente erfolgt auf Basis des EULYNX-Konzepts. Die EULYNX-Systemdefinition unterscheidet auf Ebene der Objektcontroller die folgenden Subsysteme: Subsystem Weiche (Point); Subsystem Lichtsignal (Light Signal); Subsystem Generic IO; Subsystem Zugdetektion (Train Detection System); Subsystem Bahnübergang (Level Crossing, LX). Zusätzlich zu den Objektcontroller-Subsystemen werden Schnittstellenumsetzer für Block-IF ZG62 und Block-IF Sbl60A eingesetzt. Sie dienen der Anbindung von Nachbarblöcken. Die Verbindungen des ELEKTRA Core zu diesen Schnittstellenumsetzern sowie zu den externen Komponenten RBC, NixL, SCWS und OMC erfolgen mittels X25-over-RaSTA. Für die Kommunikation zwischen benachbarten VILs ist gemäß SSS CU Part 1 X25 over RaSTA over TLS vorgesehen. |

**Hinweis zur Freigabe:** Der Neuvorschlag trennt die Redundanzbeschreibung nach ELEKTRA Core und ECMUX, ersetzt aber nicht die notwendige Bestätigung der konkreten Systemkonfiguration. Insbesondere Anzahl und Zuordnung der ECMUX-Instanzen sowie die für dieses RAM-Plan-Release geltende Geo-Redundanzvariante sind mit der verantwortlichen Systemarchitektur abzugleichen, bevor der Text in das Dokument übernommen wird.

## Geprüfte Vergleichsunterlagen

- [SafetyConcept_DIL_3BU_17300_1280_DUAPC_Ed01_Pd01.docx](../SafetyConcept_DIL_3BU_17300_1280_DUAPC_Ed01_Pd01.docx) – insbesondere Systemübersicht und Redundanzbeschreibung.
- [SSS_CU_Part1_3BU_17300_1255_DTAPA_Ed02PD01.docx](../SSS_CU_Part1_3BU_17300_1255_DTAPA_Ed02PD01.docx) – insbesondere VIL-Redundanzkonzept, Geo-Redundanz und X25-over-RaSTA.
- [SSS_DataCenter_Networks_3BU_17300_1258_DTAPA_Ed02PD01.docx](../SSS_DataCenter_Networks_3BU_17300_1258_DTAPA_Ed02PD01.docx) – Basis- und georedundante Rechenzentrumsvarianten.
- [SSS_Field_Element_Controller_and_Stations_3BU_17300_1256_DTAPA_Ed02PD01.docx](../SSS_Field_Element_Controller_and_Stations_3BU_17300_1256_DTAPA_Ed02PD01.docx) – Feldelement-/Objektcontroller-Kontext.
- [RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf) – ältere Projekt-RAM-Plan-Fassung; enthält noch die verkürzte Formulierung „2x2oo2 … and 1oo2 for EC-MUX“.

## Einschränkungen

Der Abgleich basiert auf den im lokalen Ordner `Projects/DSTW/Documents` verfügbaren Fassungen. Der Freigabe- bzw. Gültigkeitsstatus und mögliche neuere Ablageversionen wurden nicht unabhängig verifiziert. Die in Abbildung 1 dargestellten Elemente wurden visuell geprüft; die technische Richtigkeit einzelner Signal-/Schnittstellenbezeichnungen ist anhand der jeweils freigegebenen Architekturzeichnung zu bestätigen.
