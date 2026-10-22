# Proposed RAM Plan Chapter — FRACAS: Required Input and Staged Implementation

**Primary document:** RAM Plan – Generische Anwendung – Digitales Stellwerk (ÖBB), 3BU 17300 1209 DUAPC, [Ed02 PD01](../Review/RAM_DIL_3BU_17300_1209_DUAPCEd02PD01.docx) (German). The German version of this chapter replaces its Section 5.2.7 "FRACAS" and extends Section 5.2.8 "RAM Reports".  
**Also to be included in:** the RAM Plans of GA DIL / VIL, IPS and DFE (English). The English version is used there; insertion points and plan-specific adaptations are given in the next section.  
**Status:** Draft for project review. The requirement statuses and the pilot timeline must be confirmed against the approved baselines before release.

## Target documents and insertion points

| RAM Plan | Edition reviewed | Language | Existing FRACAS text | Insertion point | Text version |
| --- | --- | --- | --- | --- | --- |
| **RAM_DIL** — Generische Anwendung DSTW, umbrella plan (3BU 17300 1209 DUAPC) | [Ed02 PD01](../Review/RAM_DIL_3BU_17300_1209_DUAPCEd02PD01.docx) | German | 5.2.7 FRACAS (two sentences: FRACAS per EN 50126-1, empirical failure rates); 5.2.8 RAM Reports (installed base, field diagnostics, repair data, workshops); 6.1 already lists "FRACAS" and "RAM Reports" | Replace 5.2.7 by 5.2.7.1 to 5.2.7.4; replace 5.2.8 by the extended text | German, complete, including the system-integrator role |
| **GA DIL / VIL** (3BU 17300 1209 DUAPA) | [Ed02 PD01](../Review/RAMP_GA_3BU_17300_1209_DUAPA_Ed02PD01.docx); Ed01 RL released | English | None. Section 3.2 calls "FRACAS monitoring" a system capability | New 5.2.6 "FRACAS" after 5.2.5 "Maintainability" (X = 5.2.6); add "FRACAS reports" to 6.1; reword the Section 3.2 sentence (FRACAS is a process, not a system function) | English, with the GA/VIL adaptations below |
| **IPS** (3BU 17300 2009 DUAPA) | [Ed02 PD01](../Review/RAMP_IPS_3BU_17300_2009_DUAPA_Ed02PD01.docx) | English | None | New 5.8 "FRACAS" after 5.7 "Maintainability" (X = 5.8); add "FRACAS reports" to 6.1 | English, with the IPS adaptations below |
| **DFE** (3BU 62800 0018 DUAPA) | [ED03 PD01](../Review/RAMP_DFE_3BU_62800_0018_DUAPA_ED03PD01.docx) | English | None | New 5.2.6 "FRACAS" after 5.2.5 "Maintenance" (X = 5.2.6); add "FRACAS reports" to 6.1 | English, with the DFE adaptations below |

All four plans keep the same structure and the same core text (purpose, required input, uniform data access, staged implementation, reporting), so that the FRACAS is described consistently. Only the scope, the data sources and the responsibility paragraph differ.

### Plan-specific adaptations for the English version

| Item | GA DIL / VIL | IPS | DFE |
| --- | --- | --- | --- |
| Scope sentence (add at the start of X.1) | "This FRACAS covers the VIL instances (ELEKTRA Core with CC, RCU and DGP, ECMUX) of the GA DIL." | "This FRACAS covers the IPS infrastructure of the DIL-CU: servers, storage, network components, virtualisation and cluster management, and ADM." | "This FRACAS covers the DFE equipment: Field Element Stations, Object Controllers (DCA, AzLM), block converters and, from their release, LCSI converters." |
| Responsibility paragraph in X.1 | Keep the system-integrator paragraph; add "The consolidation across all solution elements is described in [RAM_DIL], Section 5.2.7." | Replace the system-integrator paragraph by: "The consolidation across all solution elements is performed by the system integrator according to [RAM_DIL], Section 5.2.7. The IPS solution element provides its FRACAS data and analyses for this purpose and cooperates in coordination measures (EL4-DIL-SSS-REQ-00680)." | Same replacement as IPS, with "DFE solution element". Add: "Subsystems delivered by other suppliers (for example OC-AzLM, IFC-LCSI) provide their failure analyses and corrective actions through the DFE FRACAS." |
| Main diagnostic source (input 3) | ADM (VSTW monitoring) | ADM (infrastructure monitoring, ADM-INFRA) | SDI: PULSE in Stufe 1, DDSP from Stufe 2 |
| Availability requirements monitored | VIL instance 00587, 00569, 00570; DIL-CU 00406 to 00408 jointly with IPS | No own IPS requirement; contribution to DIL-CU 00406 to 00408; ADM 01481 | FES 00575, 00577, 00578; OC 00581 to 00583; block converters 01435; LCSI converters 01436 (later release) |
| SLA (00676, in negotiation) | 5 min | 5 min (as part of the DIL-CU, to confirm) | 30 min |
| Customer supplies to attribute separately (input 6) | SiDiNet, DDSP, data-centre infrastructure | Data-centre building, power supply and air conditioning, SiDiNet | Energy stations (EST), SiDiNet, track-side installations of the customer |
| Staged implementation (X.4) | Unchanged | Unchanged; IPS hardware data are available from ADM from stage A | Unchanged; field data depend on PULSE (stage A) and DDSP (from stage B) |

The allocation of the reliability requirements on server, PDU and UPS failures (EL4-DIL-SSS-REQ-00323 to -00325) to IPS shall be confirmed before they are listed in the IPS chapter.

## Why this chapter is needed

The RAM Plans of GA DIL / VIL, IPS and DFE do not describe a FRACAS, and the RAM_DIL plan only states the intention in two sentences. However, the SSS DIL RAMS contains accepted FRACAS requirements: the supplier must provide a FRACAS, monitor the availability of each DIL component and prove the availability values of DC, VIL, FES and OC within 5 years of the first VIL being put into operation (EL4-DIL-SSS-REQ-00671 to -00681).

A FRACAS can only demonstrate availability if it receives complete operational data. Most of this data is generated and held by the customer: fault clearance records, operating times, operational impact and diagnostic data from the field. The chapter therefore states what input is needed, that it must be provided in a uniform way through the DDSP, and when a full FRACAS can realistically be provided.

---

## Proposed text for the RAM Plan (English, for GA DIL / VIL, IPS and DFE)

X is the section number of the FRACAS chapter in the respective plan (see the table above).

> ### X FRACAS
>
> #### X.1 Purpose and scope
>
> A Failure Reporting, Analysis and Corrective Action System (FRACAS) according to [EN 50126-1] is set up for the systems and subsystems delivered by Hitachi Rail (EL4-DIL-SSS-REQ-00671). The FRACAS records, classifies (defect classes FK1 to FK4) and analyses failures, faults and errors, tracks corrective and preventive actions, and monitors the achieved availability of the delivered systems against the requirements listed in Section 6.2 (EL4-DIL-SSS-REQ-00672 to -00675).
>
> The FRACAS is provided as a process with agreed reports and result data. The provision of internal Hitachi Rail IT tools or databases to the customer is not included unless explicitly agreed.
>
> As system integrator, Hitachi Rail consolidates the availability information of the connected subsystems on the basis of the data provided at the agreed interfaces (EL4-DIL-SSS-REQ-00678, -00679). The suppliers of subsystems remain responsible for the analysis and corrective actions within their scope and cooperate in the coordination (EL4-DIL-SSS-REQ-00680). Customer-supplied systems (for example SiDiNet, energy stations, data-centre infrastructure, DDSP) are not part of the availability of the Hitachi Rail delivery; events caused by them are recorded and attributed separately.
>
> #### X.2 Required input data
>
> The availability demonstration requires the following input. Data marked "customer" are generated or held by the customer and are provided from the MDM/DDSP, as stated in the SSS DIL RAMS, chapter "Monitoring System FRACAS".
>
> | No. | Input | Minimum content | Source / owner | Needed for |
> | --- | --- | --- | --- | --- |
> | 1 | Installed base and configuration | Unique identifier, type, serial number, HW and SW version, location (station, FES, data-centre site), commissioning date, configuration changes with date | Hitachi Rail (delivery, configuration management); customer (location changes) | Population and operating time per product type |
> | 2 | Operating time | Periods in which each unit was required to operate, including start and end of operation; planned outages and operational breaks | Customer | Denominator of every availability and failure-rate figure |
> | 3 | Failure and fault events | Unique event ID, affected unit, time of occurrence, time of detection, time of restoration, observed symptom, FK class, operational impact | Diagnostics: ADM (DSTW-ZE), SDI via DDSP (FES, OC); classification and impact: customer | Down time, failure rate, availability per class |
> | 4 | Fault clearance records | Time of notification, arrival on site, start and end of repair, replaced items (old and new serial number), actions taken, staff remarks | Customer (fault clearance process) | MDT and MTTR; verification of the SLA (EL4-DIL-SSS-REQ-00676, in negotiation) |
> | 5 | Returned-item analysis | Failure confirmed or no fault found, failure cause, failure mode | Hitachi Rail repair centre; subsystem suppliers | Root cause, corrective actions, failure-mode statistics |
> | 6 | External causes | Outages of SiDiNet, power supply, data-centre infrastructure, DDSP and other customer supplies with start and end times | Customer | Correct attribution of down time |
> | 7 | Changes and updates | Date and scope of SW updates, patches, configuration changes, HW replacements | Hitachi Rail; customer (activation) | Separation of planned from unplanned down time; reliability growth |
>
> **Outdoor equipment from other suppliers:** Where the outdoor equipment, in particular the Object Controllers, is not supplied by Hitachi Rail, the data required for the FRACAS (installed base, operating time, failure and fault events, fault clearance records and failure causes of these units) are requested from ÖBB. ÖBB obtains them from the responsible supplier and provides them in the same uniform way as described in Section X.3. These data are used for the monitoring of the overall system as system integrator; Hitachi Rail does not assume product responsibility for equipment of other suppliers.
>
> #### X.3 Uniform data access
>
> A meaningful availability evaluation is only possible if the input data are complete, consistent and comparable across all stations. The following conditions shall therefore be met and are agreed with the customer in a data-exchange specification:
>
> - **One access path:** The data of Section X.2 are made available to Hitachi Rail through a single agreed channel, the DDSP (or MDM), and not as separate local extracts per station.
> - **Uniform format:** Structured and machine-readable data with a fixed data model, mandatory fields and units, identical for all stations and all subsystems.
> - **Common identifiers:** The same unit identifiers in the installed base, the diagnostic data, the fault clearance records and the returned-item records, so that one event can be followed from detection to closure.
> - **Common time base:** Synchronised time stamps (for example UTC via NTP) for all sources, so that the start and end of an outage can be determined from different systems.
> - **Common classification:** The FK1 to FK4 classification and the attribution rules (supplier scope or customer supply) are applied identically by both parties; disputed classifications are resolved in the agreed review.
> - **Regular delivery:** A defined delivery interval and data cut-off date, aligned with the reporting cycle in Section X.5.
> - **Data quality:** The customer is responsible for the completeness and quality of the data it provides. Missing or inconsistent data are recorded as open points and limit the statement that can be made in the report.
>
> #### X.4 Staged implementation
>
> The continuous, cross-system collection of operational data requires the successful integration of the DDSP. In Stufe 1, the diagnosis of OC and FES is transferred to PULSE as a temporary counterpart, and the DSTW-ZE diagnosis is processed in ADM. The basic DDSP connection is planned with Stufe 2 and the full DDSP connection with Stufe 3. In addition, only a few stations are in operation during the pilot phases, so the population and operating time are too small for a statistically meaningful availability figure.
>
> The FRACAS is therefore introduced in stages:
>
> | Stage | Field configuration | Data basis | FRACAS scope |
> | --- | --- | --- | --- |
> | A — Pilot Stufe 1 | First pilot station | ADM (DSTW-ZE); PULSE (OC, FES); fault clearance records provided by the customer | Recording and analysis of individual events, root-cause analysis, corrective actions. No availability figures. |
> | B — Pilot Stufe 2 | Two further pilot stations | As stage A; DDSP data from the successful integration of the basic DDSP connection | As stage A, plus collection of DDSP data, trend analysis and first indicative availability values without demonstration claim. |
> | C — Further pilots | Further pilot projects with the full B-Vi and E-Geo scope | Full DDSP connection after successful integration | As stage B; verification of the data-exchange process, data quality and attribution rules. |
> | D — After the end of all pilot phases | Full rollout | Uniform DDSP data for all stations | Full FRACAS: availability monitoring per product population and availability class, regular reports (EL4-DIL-SSS-REQ-00673 to -00675), availability proof (EL4-DIL-SSS-REQ-00672). |
>
> A full FRACAS, including the statistical availability demonstration, can be provided after the end of all pilot phases, provided that the DDSP has been successfully integrated and the input of Section X.2 is available in the uniform way described in Section X.3. Before that, the FRACAS is limited to event-based failure analysis and corrective actions. Where the population of comparable units is statistically insufficient, the empirical result is supplemented by analytical assessments.
>
> #### X.5 Reporting
>
> Failure and repair data are reviewed in monthly internal Failure Review Board meetings. The customer receives a FRACAS report and a service workshop twice per year. The report shows, as far as the data allow, the availability per availability class and per product population down to module level, with the failure causes (EL4-DIL-SSS-REQ-00674, -00675). The report states for each figure the data basis, the observation period and the population used, and marks figures with insufficient data as indicative.

---

## Background for the reviewer (not for the RAM Plan)

### Pilot timeline from the customer documents

| Ramp-up step (customer Leistungsbeschreibung V2.1, Ch. 6.2.2) | Latest commissioning after MS E01 | Stations in operation (cumulative) |
| --- | --- | --- |
| First pilot project, scope Stufe 1 B-Vi | 52 months | 1 |
| Two further pilot projects, scope Stufe 2 B-Vi | 54 months | 3 |
| Further pilot projects per supplier, full scope B-Vi and E-Geo | 64 months | 3 + further pilots; the Technical Concept (Ed07, server sizing) assumes 4 further stations, i.e. 7 |

The development stages in the same document: Stufe 2 includes the "basic DDSP connection", Stufe 3 the "full DDSP connection". The full rollout starts after the last pilot project.

### Why a statistical demonstration needs a larger population

A simple example shows that few stations cannot demonstrate the targets. For a VIL instance, the manual-correction scenario of EL4-DIL-SSS-REQ-00569 (99.9979 % at MTTR 6 h) corresponds to a mean up time of about 32.6 years (see [VIL_Availability_Requirements_Allocation.md](./VIL_Availability_Requirements_Allocation.md), section 3.2).

To demonstrate a mean time between failures $\mathrm{MTBF}$ with confidence $C$ when **no** failure occurs, the accumulated operating time must be at least

$$T_{\text{required}} = \frac{\chi^2_{C;\,2}}{2}\cdot \mathrm{MTBF} = -\ln(1-C)\cdot \mathrm{MTBF}$$

The factor $-\ln(1-C)$ is 0.92 for $C = 60\ \%$ and 2.30 for $C = 90\ \%$. Even at 60 % confidence and without a single failure:

$$T_{\text{required}} = 0.92 \cdot 32.6\ \text{years} \approx 30\ \text{instance-years}$$

| Stations in operation | Calendar time needed for 30 instance-years |
| --- | --- |
| 1 (pilot Stufe 1) | about 30 years |
| 3 (after pilot Stufe 2) | about 10 years |
| 7 (end of pilots, assumption from Technical Concept) | about 4.3 years |

One observed failure would increase the required time further. The FRACAS during the pilot phases can therefore detect and correct failures, but it cannot statistically demonstrate the availability targets. This calculation assumes a constant failure rate and is an illustration, not a contractual commitment.

### Risk: start of the 5-year period

EL4-DIL-SSS-REQ-00672 starts the 5-year proof period with the commissioning of the first VIL, which is the first pilot station. At that time, the DDSP is not yet fully integrated and only one station is in operation. Recommendation: agree with the customer that the observation period for the statistical proof starts when uniform DDSP data are available for a sufficient population (end of the pilot phases), or that pilot data are included only as indicative values.

### Requirement trace

| SSS DIL RAMS (Ed02PD01) | Customer PH | Status | Content | English section (RAM_DIL section) |
| --- | --- | --- | --- | --- |
| Chapter statement "Monitoring System FRACAS" | 5.8.0-8 (02_148) | Introductory text, no requirement ID | Customer provides the necessary MDM/DDSP data | X.2, X.3 (5.2.7.2, 5.2.7.3) |
| EL4-DIL-SSS-REQ-00671 | 02_141 | Accepted | FRACAS according to EN 50126-1 | X.1 (5.2.7.1) |
| EL4-DIL-SSS-REQ-00672 | 02_142 | Accepted | Proof of DC, VIL, FES, OC availability within 5 years of the first VIL | X.4 (5.2.7.4) |
| EL4-DIL-SSS-REQ-00673 | 02_143 | Accepted | Monitoring of each DIL component | X.4 (5.2.7.4) |
| EL4-DIL-SSS-REQ-00674 | 02_144 | Accepted | Regular reports | X.5 (5.2.8) |
| EL4-DIL-SSS-REQ-00675 | 02_145 | Accepted | Availability classes 1 to 3, module level, failure reason | X.5 (5.2.8) |
| EL4-DIL-SSS-REQ-00676 | 02_146 | In negotiation | SLA 5 min VIL, 30 min FES and OC | X.2, input 4 (5.2.7.2) |
| — | 5.8.0-7 (02_147) | Draft (PH) | Supplier monitors and proves the availability of the delivered systems; no separate SSS ID found | X.1 (5.2.7.1) |
| EL4-DIL-SSS-REQ-00678 to -00681 | 5.8.0-9 to -11 (02_149, 02_150, 02_257) | Accepted | Integrator monitoring, coordination, cooperation, responsibility | X.1 (5.2.7.1) |
| EL4-DIL-SSS-REQ-00321 | — | Accepted | Faults, errors and failures reported to the DDSP via SDI | X.2, input 3 (5.2.7.2) |
| EL4-DIL-SSS-REQ-00319 | — | In negotiation | Reporting to OMC via IF-61 | not used as FRACAS source until agreed |

The PH responses quoted in this chapter (FRACAS as process and reports, population-based evaluation, dependence on DDSP/MDM, exclusion of customer supplies) have status Draft in the reviewed PH document.

### Open points

| No. | Open point | Proposed owner |
| --- | --- | --- |
| 1 | Data-exchange specification with the customer: data model, mandatory fields, interval, access, data quality | RAM-AM, Project Manager |
| 2 | Start of the 5-year observation period (EL4-DIL-SSS-REQ-00672) in relation to the pilot phases and DDSP integration | Project Manager, customer |
| 3 | Data supply during stages A and B, before the DDSP is available: format and responsibility for manual fault clearance records | RAM-AM, customer |
| 4 | Start and stop time stamps for the SLA and for down time (EL4-DIL-SSS-REQ-00676, in negotiation) | RAM-AM, customer |
| 5 | FK1 to FK4 assignment rules and attribution of customer supplies | RAM-AM, customer |
| 6 | FRACAS tool decision; the interim toolchain from the DSTW FRACAS summary is ProVIS with Excel/R | RAM-AM |
| 7 | Section 6.3 of all four RAM Plans is titled "Periodical RAM activities report" (RAM_DIL: "Regelmäßiger RAM-Aktivitäten Bericht") but describes RAM Plan revisions; align it with the reporting section (X.5, RAM_DIL 5.2.8) | RAM-AM |
| 8 | Overlap between RAM_DIL (DUAPC) and the GA DIL / VIL plan (DUAPA), which both cover the Generic Application: confirm that the system-integrator role and the overall consolidation are described only in RAM_DIL | RAM-AM |

---

## Deutsche Fassung

**Dokument:** RAM Plan – Generische Anwendung – Digitales Stellwerk (ÖBB), 3BU 17300 1209 DUAPC, [Ed02 PD01](../Review/RAM_DIL_3BU_17300_1209_DUAPCEd02PD01.docx)  
**Vorgeschlagene Position:** Der bestehende Abschnitt 5.2.7 „FRACAS“ wird durch die Abschnitte 5.2.7.1 bis 5.2.7.4 ersetzt, der bestehende Abschnitt 5.2.8 „RAM Reports“ durch den erweiterten Text unten. Abschnitt 6.1 führt „FRACAS“ und „RAM Reports“ bereits als Lieferdokumente und bleibt unverändert.  
**Weitere RAM-Pläne:** Das Kapitel wird mit gleicher Struktur auch in die RAM-Pläne GA DIL / VIL (neuer Abschnitt 5.2.6), IPS (neuer Abschnitt 5.8) und DFE (neuer Abschnitt 5.2.6) übernommen. Diese Pläne sind englisch; dort gilt die englische Fassung mit den Anpassungen aus der Tabelle „Plan-specific adaptations“ am Anfang dieses Dokuments.  
**Status:** Entwurf zur Projektprüfung. Anforderungsstatus und Pilotzeitplan sind vor der Freigabe gegen die freigegebenen Baselines zu bestätigen.

### Zieldokumente im Überblick

| RAM-Plan | Sprache | Vorhandener FRACAS-Text | Einfügestelle | Besonderheit |
| --- | --- | --- | --- | --- |
| RAM_DIL (DUAPC), Rahmenplan Generische Anwendung | Deutsch | 5.2.7 FRACAS (zwei Sätze), 5.2.8 RAM Reports | 5.2.7 und 5.2.8 ersetzen | Vollständiger Text einschließlich Rolle als Systemintegrator und Zusammenführung aller Solution Elements |
| GA DIL / VIL (DUAPA) | Englisch | Keiner; Abschnitt 3.2 nennt „FRACAS monitoring“ als Systemfunktion | Neuer 5.2.6 nach 5.2.5; 6.1 ergänzen; Satz in 3.2 umformulieren | Geltungsbereich VIL-Instanzen; Diagnosequelle ADM; SLA 5 min |
| IPS (DUAPA) | Englisch | Keiner | Neuer 5.8 nach 5.7; 6.1 ergänzen | Geltungsbereich Server, Speicher, Netzwerk, Cluster-Management, ADM; Verweis auf RAM_DIL für die Zusammenführung |
| DFE (DUAPA) | Englisch | Keiner | Neuer 5.2.6 nach 5.2.5; 6.1 ergänzen | Geltungsbereich FES, OC, Block- und LCSI-Umsetzer; Diagnose über PULSE, später DDSP; SLA 30 min |

### Warum dieses Kapitel erforderlich ist

Der RAM_DIL enthält in Abschnitt 5.2.7 nur die Absicht, ein FRACAS einzurichten; die RAM-Pläne von GA DIL / VIL, IPS und DFE beschreiben kein FRACAS. Die SSS DIL RAMS enthält jedoch akzeptierte FRACAS-Anforderungen: Der Lieferant muss ein FRACAS bereitstellen, die Verfügbarkeit jeder einzelnen DIL-Komponente überwachen und die Verfügbarkeitswerte von DC, VIL, FES und OC innerhalb von 5 Jahren nach Inbetriebnahme des ersten VIL nachweisen (EL4-DIL-SSS-REQ-00671 bis -00681).

Ein FRACAS kann die Verfügbarkeit nur nachweisen, wenn es vollständige Betriebsdaten erhält. Der Großteil dieser Daten entsteht beim Kunden und liegt bei ihm: Entstörprotokolle, Betriebszeiten, betriebliche Auswirkungen und Diagnosedaten aus dem Feld. Das Kapitel legt daher fest, welche Eingangsdaten erforderlich sind, dass sie einheitlich über die DDSP bereitgestellt werden müssen und ab wann ein vollständiges FRACAS realistisch bereitgestellt werden kann.

### Textvorschlag für den RAM_DIL

> #### 5.2.7 FRACAS (Fehlererfassung, Analyse und Korrekturmaßnahmen)
>
> ##### 5.2.7.1 Zweck und Geltungsbereich
>
> Für die von Hitachi Rail gelieferten Systeme und Teilsysteme wird ein Failure Reporting, Analysis and Corrective Action System (FRACAS) gemäß [EN 50126-1] eingerichtet (EL4-DIL-SSS-REQ-00671). Das FRACAS erfasst Ausfälle, Störungen und Fehler, klassifiziert sie (Fehlerklassen FK1 bis FK4) und analysiert sie, verfolgt Korrektur- und Vorbeugemaßnahmen und überwacht die erreichte Verfügbarkeit der gelieferten Systeme gegenüber den in Abschnitt 6.2 aufgeführten Anforderungen (EL4-DIL-SSS-REQ-00672 bis -00675).
>
> Das FRACAS wird als Prozess mit vereinbarten Berichten und Ergebnisdaten bereitgestellt. Die Überlassung interner IT-Werkzeuge oder Datenbanken von Hitachi Rail an den Kunden ist nicht enthalten, sofern dies nicht ausdrücklich vereinbart wird.
>
> Als Systemintegrator führt Hitachi Rail die Verfügbarkeitsinformationen der angebundenen Teilsysteme auf Basis der an den vereinbarten Schnittstellen bereitgestellten Daten zusammen (EL4-DIL-SSS-REQ-00678, -00679). Die Lieferanten der Teilsysteme bleiben für Analyse und Korrekturmaßnahmen in ihrem Lieferumfang verantwortlich und wirken an der Abstimmung mit (EL4-DIL-SSS-REQ-00680). Vom Kunden beigestellte Systeme (z. B. SiDiNet, Energiestationen, Rechenzentrumsinfrastruktur, DDSP) sind nicht Teil der Verfügbarkeit des Hitachi-Rail-Lieferumfangs; dadurch verursachte Ereignisse werden erfasst und gesondert zugeordnet.
>
> Jedes Solution Element (VIL, IPS, DFE) beschreibt in seinem RAM-Plan [RAM_Plan_SE] den FRACAS-Geltungsbereich, die Diagnosequellen und die überwachten Verfügbarkeitsanforderungen seines Lieferumfangs und stellt seine FRACAS-Daten und Analysen für die Zusammenführung bereit.
>
> ##### 5.2.7.2 Erforderliche Eingangsdaten
>
> Für den Verfügbarkeitsnachweis sind die folgenden Eingangsdaten erforderlich. Mit „Kunde“ gekennzeichnete Daten entstehen beim Kunden oder liegen bei ihm vor und werden aus der MDM/DDSP bereitgestellt, wie in der SSS DIL RAMS, Kapitel „Monitoring System FRACAS“, festgelegt.
>
> | Nr. | Eingangsdaten | Mindestinhalt | Quelle / verantwortlich | Benötigt für |
> | --- | --- | --- | --- | --- |
> | 1 | Installierte Basis und Konfiguration | Eindeutige Kennung, Typ, Seriennummer, HW- und SW-Version, Einbauort (Bahnhof, FES, Rechenzentrumsstandort), Inbetriebnahmedatum, Konfigurationsänderungen mit Datum | Hitachi Rail (Lieferung, Konfigurationsmanagement); Kunde (Standortänderungen) | Population und Betriebszeit je Produkttyp |
> | 2 | Betriebszeit | Zeiträume, in denen jede Einheit in Betrieb sein musste, einschließlich Beginn und Ende des Betriebs; geplante Abschaltungen und Betriebspausen | Kunde | Bezugsgröße jeder Verfügbarkeits- und Ausfallratenkennzahl |
> | 3 | Ausfall- und Störungsereignisse | Eindeutige Ereignis-ID, betroffene Einheit, Zeitpunkt des Auftretens, der Erkennung und der Wiederherstellung, beobachtetes Fehlerbild, Fehlerklasse FK, betriebliche Auswirkung | Diagnose: ADM (DSTW-ZE), SDI über DDSP (FES, OC); Klassifizierung und Auswirkung: Kunde | Ausfallzeit, Ausfallrate, Verfügbarkeit je Klasse |
> | 4 | Entstörprotokolle | Zeitpunkt der Meldung, Eintreffen vor Ort, Beginn und Ende der Instandsetzung, getauschte Teile (alte und neue Seriennummer), durchgeführte Maßnahmen, Anmerkungen des Personals | Kunde (Entstörprozess) | MDT und MTTR; Nachweis der SLA (EL4-DIL-SSS-REQ-00676, in Verhandlung) |
> | 5 | Befundung rückgelieferter Teile | Fehler bestätigt oder ohne Befund, Fehlerursache, Fehlermodus | Hitachi-Rail-Reparaturzentrum; Teilsystemlieferanten | Grundursache, Korrekturmaßnahmen, Fehlermodenstatistik |
> | 6 | Externe Ursachen | Ausfälle von SiDiNet, Stromversorgung, Rechenzentrumsinfrastruktur, DDSP und anderen Kundenbeistellungen mit Beginn und Ende | Kunde | Korrekte Zuordnung der Ausfallzeit |
> | 7 | Änderungen und Updates | Datum und Umfang von SW-Updates, Patches, Konfigurationsänderungen, HW-Tausch | Hitachi Rail; Kunde (Aktivierung) | Trennung geplanter von ungeplanter Ausfallzeit; Zuverlässigkeitswachstum |
>
> **Außenanlage anderer Lieferanten:** Wird die Außenanlage, insbesondere die Object Controller, nicht von Hitachi Rail geliefert, werden die für das FRACAS erforderlichen Daten (installierte Basis, Betriebszeit, Ausfall- und Störungsereignisse, Entstörprotokolle und Ausfallursachen dieser Einheiten) bei der ÖBB eingefordert. Die ÖBB beschafft sie beim zuständigen Lieferanten und stellt sie in derselben einheitlichen Form bereit, wie in Abschnitt 5.2.7.3 beschrieben. Diese Daten werden für die Überwachung des Gesamtsystems als Systemintegrator verwendet; Hitachi Rail übernimmt keine Produktverantwortung für Einrichtungen anderer Lieferanten.
>
> ##### 5.2.7.3 Einheitlicher Datenzugang
>
> Eine aussagekräftige Verfügbarkeitsbewertung ist nur möglich, wenn die Eingangsdaten vollständig, konsistent und über alle Bahnhöfe vergleichbar sind. Die folgenden Bedingungen sind daher einzuhalten und werden mit dem Kunden in einer Datenaustauschspezifikation vereinbart:
>
> - **Ein Zugangsweg:** Die Daten aus Abschnitt 5.2.7.2 werden Hitachi Rail über einen einzigen vereinbarten Kanal, die DDSP (oder MDM), bereitgestellt und nicht als getrennte lokale Auszüge je Bahnhof.
> - **Einheitliches Format:** Strukturierte und maschinenlesbare Daten mit festem Datenmodell, Pflichtfeldern und Einheiten, identisch für alle Bahnhöfe und alle Teilsysteme.
> - **Gemeinsame Kennungen:** Dieselben Einheitenkennungen in installierter Basis, Diagnosedaten, Entstörprotokollen und Befundungen, sodass ein Ereignis von der Erkennung bis zum Abschluss verfolgt werden kann.
> - **Gemeinsame Zeitbasis:** Synchronisierte Zeitstempel (z. B. UTC über NTP) für alle Quellen, sodass Beginn und Ende eines Ausfalls aus verschiedenen Systemen bestimmt werden können.
> - **Gemeinsame Klassifizierung:** Die Fehlerklassifizierung FK1 bis FK4 und die Zuordnungsregeln (Lieferumfang oder Kundenbeistellung) werden von beiden Parteien gleich angewendet; strittige Einstufungen werden im vereinbarten Review geklärt.
> - **Regelmäßige Lieferung:** Ein festgelegtes Lieferintervall und ein Datenstichtag, abgestimmt auf den Berichtszyklus in Abschnitt 5.2.8.
> - **Datenqualität:** Der Kunde ist für Vollständigkeit und Qualität der von ihm bereitgestellten Daten verantwortlich. Fehlende oder inkonsistente Daten werden als offene Punkte geführt und schränken die im Bericht möglichen Aussagen ein.
>
> ##### 5.2.7.4 Gestufte Einführung
>
> Die kontinuierliche, systemübergreifende Erfassung von Betriebsdaten setzt die erfolgreiche Integration der DDSP voraus. In Stufe 1 wird die Diagnose von OC und FES an PULSE als temporäre Gegenstelle übertragen, die Diagnose der DSTW-ZE wird in der ADM verarbeitet. Die Basis-Anbindung der DDSP ist mit Stufe 2 geplant, die vollumfängliche Anbindung mit Stufe 3. Zudem sind während der Pilotphasen nur wenige Bahnhöfe in Betrieb, sodass Population und Betriebszeit für eine statistisch belastbare Verfügbarkeitskennzahl nicht ausreichen.
>
> Das FRACAS wird daher stufenweise eingeführt:
>
> | Stufe | Feldkonfiguration | Datenbasis | Umfang FRACAS |
> | --- | --- | --- | --- |
> | A — Pilot Stufe 1 | Erster Pilotbahnhof | ADM (DSTW-ZE); PULSE (OC, FES); vom Kunden bereitgestellte Entstörprotokolle | Erfassung und Analyse einzelner Ereignisse, Ursachenanalyse, Korrekturmaßnahmen. Keine Verfügbarkeitskennzahlen. |
> | B — Pilot Stufe 2 | Zwei weitere Pilotbahnhöfe | Wie Stufe A; DDSP-Daten ab erfolgreicher Integration der Basis-Anbindung | Wie Stufe A, zusätzlich Erfassung der DDSP-Daten, Trendanalyse und erste indikative Verfügbarkeitswerte ohne Nachweisanspruch. |
> | C — Weitere Pilotprojekte | Weitere Pilotprojekte mit vollem Umfang B-Vi und E-Geo | Vollumfängliche DDSP-Anbindung nach erfolgreicher Integration | Wie Stufe B; Verifikation des Datenaustauschprozesses, der Datenqualität und der Zuordnungsregeln. |
> | D — Nach Abschluss aller Pilotphasen | Vollumfänglicher Rollout | Einheitliche DDSP-Daten für alle Bahnhöfe | Vollständiges FRACAS: Verfügbarkeitsüberwachung je Produktpopulation und Verfügbarkeitsklasse, regelmäßige Berichte (EL4-DIL-SSS-REQ-00673 bis -00675), Verfügbarkeitsnachweis (EL4-DIL-SSS-REQ-00672). |
>
> Ein vollständiges FRACAS einschließlich des statistischen Verfügbarkeitsnachweises kann nach Abschluss aller Pilotphasen bereitgestellt werden, sofern die DDSP erfolgreich integriert ist und die Eingangsdaten aus Abschnitt 5.2.7.2 in der in Abschnitt 5.2.7.3 beschriebenen einheitlichen Form vorliegen. Davor beschränkt sich das FRACAS auf die ereignisbezogene Fehleranalyse und Korrekturmaßnahmen. Ist die Population vergleichbarer Einheiten statistisch unzureichend, wird das empirische Ergebnis durch analytische Bewertungen ergänzt.
>
> #### 5.2.8 RAM Reports
>
> Die regelmäßigen Reports basieren auf den Informationen aus dem FRACAS. Wie bei den bereits etablierten Reports zur Anlagenbeobachtung von ELEKTRA 1 und ELEKTRA 2 dienen Installationsbasis, Felddiagnosen und Reparaturdaten als Grundlage; ergänzend werden die Eingangsdaten aus Abschnitt 5.2.7.2 verwendet.
>
> Ausfall- und Instandsetzungsdaten werden in monatlichen internen Sitzungen des Failure Review Board ausgewertet. Der Kunde erhält zweimal jährlich einen FRACAS-Bericht, der im Rahmen eines Service-Workshops präsentiert und zur Verfügung gestellt wird. Der Bericht zeigt, soweit die Daten dies zulassen, die Verfügbarkeit je Verfügbarkeitsklasse und je Produktpopulation bis auf Modulebene mit den Ausfallursachen (EL4-DIL-SSS-REQ-00674, -00675). Für jede Kennzahl werden Datenbasis, Beobachtungszeitraum und verwendete Population angegeben; Kennzahlen mit unzureichender Datenbasis werden als indikativ gekennzeichnet.

### Hintergrund für den Reviewer (nicht für den RAM-Plan)

#### Pilotzeitplan aus den Kundendokumenten

| Ramp-up-Stufe (Leistungsbeschreibung V2.1 des Kunden, Kap. 6.2.2) | Inbetriebnahme spätestens nach MS E01 | Bahnhöfe in Betrieb (kumuliert) |
| --- | --- | --- |
| Erstes Pilotprojekt, Funktionsumfang Stufe 1 B-Vi | 52 Monate | 1 |
| Zwei weitere Pilotprojekte, Funktionsumfang Stufe 2 B-Vi | 54 Monate | 3 |
| Weitere Pilotprojekte je AN, voller Umfang B-Vi und E-Geo | 64 Monate | 3 + weitere Pilotprojekte; das Technische Konzept (Ed07, Serverdimensionierung) geht von 4 weiteren Stellwerken aus, also 7 |

Die Entwicklungsstufen im selben Dokument: Stufe 2 enthält die „Basic DDSP-Anbindung“, Stufe 3 die „vollumfängliche Anbindung der DDSP“. Der vollumfängliche Rollout beginnt nach dem letzten Pilotprojekt.

#### Warum ein statistischer Nachweis eine größere Population erfordert

Ein einfaches Beispiel zeigt, dass wenige Bahnhöfe die Ziele nicht nachweisen können. Für eine VIL-Instanz entspricht das Szenario manuelle Behebung aus EL4-DIL-SSS-REQ-00569 (99,9979 % bei MTTR 6 h) einer mittleren Betriebszeit von etwa 32,6 Jahren (siehe [VIL_Availability_Requirements_Allocation.md](./VIL_Availability_Requirements_Allocation.md), Abschnitt 3.2).

Um eine mittlere Betriebsdauer zwischen Ausfällen $\mathrm{MTBF}$ mit der Aussagewahrscheinlichkeit $C$ nachzuweisen, wenn **kein** Ausfall auftritt, muss die kumulierte Betriebszeit mindestens betragen:

$$T_{\text{erforderlich}} = \frac{\chi^2_{C;\,2}}{2}\cdot \mathrm{MTBF} = -\ln(1-C)\cdot \mathrm{MTBF}$$

Der Faktor $-\ln(1-C)$ beträgt 0,92 für $C = 60\ \%$ und 2,30 für $C = 90\ \%$. Selbst bei 60 % Aussagewahrscheinlichkeit und ohne einen einzigen Ausfall gilt:

$$T_{\text{erforderlich}} = 0{,}92 \cdot 32{,}6\ \text{Jahre} \approx 30\ \text{Instanzjahre}$$

| Bahnhöfe in Betrieb | Erforderliche Kalenderzeit für 30 Instanzjahre |
| --- | --- |
| 1 (Pilot Stufe 1) | etwa 30 Jahre |
| 3 (nach Pilot Stufe 2) | etwa 10 Jahre |
| 7 (Ende der Pilotphasen, Annahme aus dem Technischen Konzept) | etwa 4,3 Jahre |

Ein einziger beobachteter Ausfall würde die erforderliche Zeit weiter erhöhen. Das FRACAS kann in den Pilotphasen daher Ausfälle erkennen und beheben, die Verfügbarkeitsziele aber nicht statistisch nachweisen. Die Rechnung setzt eine konstante Ausfallrate voraus und dient der Veranschaulichung, nicht als vertragliche Zusage.

#### Risiko: Beginn des 5-Jahres-Zeitraums

EL4-DIL-SSS-REQ-00672 lässt den 5-jährigen Nachweiszeitraum mit der Inbetriebnahme des ersten VIL beginnen, also mit dem ersten Pilotbahnhof. Zu diesem Zeitpunkt ist die DDSP noch nicht vollständig integriert und nur ein Bahnhof in Betrieb. Empfehlung: Mit dem Kunden vereinbaren, dass der Beobachtungszeitraum für den statistischen Nachweis beginnt, sobald einheitliche DDSP-Daten für eine ausreichende Population vorliegen (Ende der Pilotphasen), oder dass Pilotdaten nur als indikative Werte einfließen.

#### Anforderungsverfolgung

| SSS DIL RAMS (Ed02PD01) | PH des Kunden | Status | Inhalt | Abschnitt RAM_DIL |
| --- | --- | --- | --- | --- |
| Kapiteleinleitung „Monitoring System FRACAS“ | 5.8.0-8 (02_148) | Einleitungstext, keine Anforderungs-ID | Kunde stellt die erforderlichen MDM/DDSP-Daten bereit | 5.2.7.2, 5.2.7.3 |
| EL4-DIL-SSS-REQ-00671 | 02_141 | Accepted | FRACAS gemäß EN 50126-1 | 5.2.7.1 |
| EL4-DIL-SSS-REQ-00672 | 02_142 | Accepted | Nachweis der Verfügbarkeit von DC, VIL, FES, OC innerhalb von 5 Jahren nach dem ersten VIL | 5.2.7.4 |
| EL4-DIL-SSS-REQ-00673 | 02_143 | Accepted | Überwachung jeder DIL-Komponente | 5.2.7.4 |
| EL4-DIL-SSS-REQ-00674 | 02_144 | Accepted | Regelmäßige Berichte | 5.2.8 |
| EL4-DIL-SSS-REQ-00675 | 02_145 | Accepted | Verfügbarkeitsklassen 1 bis 3, Modulebene, Ausfallgrund | 5.2.8 |
| EL4-DIL-SSS-REQ-00676 | 02_146 | In negotiation | SLA 5 min VIL, 30 min FES und OC | 5.2.7.2 (Eingangsdaten 4) |
| — | 5.8.0-7 (02_147) | Draft (PH) | Lieferant überwacht die Verfügbarkeit der gelieferten Systeme und weist sie nach; keine eigene SSS-ID gefunden | 5.2.7.1 |
| EL4-DIL-SSS-REQ-00678 bis -00681 | 5.8.0-9 bis -11 (02_149, 02_150, 02_257) | Accepted | Überwachung durch den Integrator, Abstimmung, Mitwirkung, Verantwortung | 5.2.7.1 |
| EL4-DIL-SSS-REQ-00321 | — | Accepted | Störungen, Fehler und Ausfälle werden über SDI an die DDSP gemeldet | 5.2.7.2 (Eingangsdaten 3) |
| EL4-DIL-SSS-REQ-00319 | — | In negotiation | Meldung an OMC über IF-61 | bis zur Einigung nicht als FRACAS-Quelle verwendet |

Die in diesem Kapitel zitierten PH-Antworten (FRACAS als Prozess und Berichtswesen, populationsbezogene Auswertung, Abhängigkeit von DDSP/MDM, Ausschluss von Kundenbeistellungen) haben im geprüften PH-Dokument den Status Draft.

#### Offene Punkte

| Nr. | Offener Punkt | Vorgeschlagene Verantwortung |
| --- | --- | --- |
| 1 | Datenaustauschspezifikation mit dem Kunden: Datenmodell, Pflichtfelder, Intervall, Zugang, Datenqualität | RAM-AM, Projektleiter |
| 2 | Beginn des 5-jährigen Beobachtungszeitraums (EL4-DIL-SSS-REQ-00672) im Verhältnis zu Pilotphasen und DDSP-Integration | Projektleiter, Kunde |
| 3 | Datenbereitstellung in den Stufen A und B, bevor die DDSP verfügbar ist: Format und Verantwortung für manuelle Entstörprotokolle | RAM-AM, Kunde |
| 4 | Start- und Endzeitstempel für SLA und Ausfallzeit (EL4-DIL-SSS-REQ-00676, in Verhandlung) | RAM-AM, Kunde |
| 5 | Zuordnungsregeln FK1 bis FK4 und Zuordnung von Kundenbeistellungen | RAM-AM, Kunde |
| 6 | Entscheidung zum FRACAS-Werkzeug; die Übergangslösung laut DSTW-FRACAS-Zusammenfassung ist ProVIS mit Excel/R | RAM-AM |
| 7 | Abschnitt 6.3 aller vier RAM-Pläne heißt „Regelmäßiger RAM-Aktivitäten Bericht“ bzw. „Periodical RAM activities report“, beschreibt aber Revisionen des RAM-Plans; mit dem Abschnitt zum Berichtswesen (RAM_DIL 5.2.8) abstimmen | RAM-AM |
| 8 | Überschneidung zwischen RAM_DIL (DUAPC) und dem RAM-Plan GA DIL / VIL (DUAPA), die beide die Generische Anwendung behandeln: bestätigen, dass die Rolle als Systemintegrator und die Gesamtzusammenführung nur im RAM_DIL beschrieben werden | RAM-AM |

## Applied Skills

- `FRACAS` — failure reporting, root cause, corrective actions and data requirements.
- `Railway-RAM` — requirement traceability, responsibility boundaries and RAM Plan structure.
- `RAM-Metrics` — availability demonstration, population and statistical confidence.

## Repository information used

- [RAM_DIL, DUAPC Ed02 PD01](../Review/RAM_DIL_3BU_17300_1209_DUAPCEd02PD01.docx), [GA DIL / VIL Ed02 PD01](../Review/RAMP_GA_3BU_17300_1209_DUAPA_Ed02PD01.docx), [IPS Ed02 PD01](../Review/RAMP_IPS_3BU_17300_2009_DUAPA_Ed02PD01.docx), [DFE ED03 PD01](../Review/RAMP_DFE_3BU_62800_0018_DUAPA_ED03PD01.docx) — chapter structure, existing FRACAS and report sections, insertion points.
- [DIL Technische Konzepte, Ed07](../DIL_Technische_Konzepte_3BU_17300_0010_DSAPC_Ed07.docx) also used for the ADM monitoring services (ADM-VSTW, ADM-INFRA).
- [SSS DIL RAMS, Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx) — FRACAS requirements 00671 to 00681, 00319, 00321 and the MDM/DDSP data statement.
- [Customer PH, D2.2 RAMS, chapter 5.8](../EL4_PH_PleaseReview_Clean.docx) — requirements 5.8.0-1 to 5.8.0-11 with the proposed responses; PULSE and DDSP staging.
- [Leistungsbeschreibung V2.1](../2026-03-27_OBB_RA-DSTW-D1_Leistungsbeschreibung_V2.1.pdf) — Chapter 6.2: development stages and pilot ramp-up.
- [DIL Technische Konzepte, Ed07](../DIL_Technische_Konzepte_3BU_17300_0010_DSAPC_Ed07.docx) — station numbers per stage, DDSP integration preconditions, fault classes and service workshops.
- [DSTW FRACAS Project Summary](../../DSTW_FRACAS_Project_Summary.md) — reporting cadence, interim toolchain and open points.
- [FRACAS Lessons Learned](../../../../Knowledge/Lessons_Learned/FRACAS_Lessons.md) — minimum event data and bounded problem statements.
- [VIL availability requirements analysis](./VIL_Availability_Requirements_Allocation.md) — required mean up time for the manual-correction scenario.
