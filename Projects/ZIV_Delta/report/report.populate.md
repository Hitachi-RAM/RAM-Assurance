---
name: "RAM Plan ZIV Delta"
title: "ZIV Delta Project RAM Plan"
subtitle: "Reliability, Availability and Maintainability Plan | Draft 0.1 for project review"
additional_resources: []
---

# ZIV Delta Project RAM Plan

| Document field | Value |
| --- | --- |
| Project | Zalaszentiván Delta (ZIVD) |
| Document title | Project-specific Reliability, Availability and Maintainability Plan |
| Document identifier | To be assigned by Document Control |
| Edition/status | Draft 0.1 - for project review; not approved for contractual use |
| Date | 2026-10-06 |
| RAM Assurance Manager (RAM-AM) | Appointment and independence to be confirmed |
| Prepared from | ZIVD SEMP proposal, system description, BoM and PBS listed in Section 2 |

> [!IMPORTANT]
> This is a project-specific working draft, not an approved contractual baseline. The available inputs do not establish project RAM targets, the complete contractual requirement set, the RAM-AM appointment, or the complete system configuration. The actions in Section 11 control these gaps; this plan introduces no numerical RAM target.

## 1. Purpose and Scope

This plan defines how RAM requirements will be identified, allocated, analysed, verified and reported for the ZIVD solution. It tailors the company Generic RAM Plan to the current project system definition and milestone strategy. It is to be read with the SEMP, requirements baseline, applicable contract/customer documents, Safety Plan, IV Plan, VQ Plan, Quality Management Plan and configuration-management arrangements.

The scope is the ZIVD solution and its RAM-relevant interfaces represented in the current Project Breakdown Structure (PBS) and system description. It includes the Interlocking (IXL) and ETCS Level 2 trackside solutions; listed station, wayside and telecommunications elements; application/configuration data; integration and verification; field validation; Putting into Operation (PIO); the standby period; and transition to customer support where these affect RAM evidence or assumptions. The SEMP identifies these solution branches and the project-specific validation, assessment and deployment sequence (SEMP, Sections 6.1, 6.2 and 15.1-15.2).

The plan applies to new, existing and re-used elements where they contribute to the delivered function. It does not replace system engineering, safety, IVVQ, maintenance, configuration or quality plans. RAM analyses are not safety analyses and do not establish a Safety Integrity Level. Safety-related conclusions remain subject to the Safety Plan and responsible safety authority.

## 2. Basis, References and Precedence

### 2.1 Project inputs reviewed

| Reference | Input and use in this plan |
| --- | --- |
| [SEMP ZIVD](../Input/SEMP_3BU_61914_0002_DPAPA_ED01PD01.docx) | Edition 01 proposal. Project scope, plan register, roles, tailoring and separate planned IXL/ETCS milestone chains. Relevant locators: Sections 6.1-6.2, 9, 12.1, 13.1.4, 13.12, 15.1-15.2 and 16.9. |
| [System Description - IXL](../Input/SD_IXL_3BU_61914_0016_PEAPQ_ED01PD02.pdf) | Preliminary IXL architecture drawing and communication/network notes; page 1. It does not define complete RAM requirements or operational conditions. |
| [BoM - ELEKTRA2 and AzLM](../Input/BoM_3BU_61914_2010_HAAPQ.xlsx) | The `Mengengerüst` worksheet lists part groups and project quantities for Zalaszentiván. Its title and content do not establish complete BoM coverage for all PBS branches. |
| [Project Breakdown Structure](../Input/Project_Breakdown_Structure_3BU_61914_0015_EDAPA.xlsm) | System decomposition, existing/new/re-used categories, make/team/buy assignments and maturity fields. `Arborescence` worksheet; reference 100007442, dated 2026-09-23. |
| [SEMP RAM review](../output/SEMP_RAM_Review.md) | RAM-focused review of the SEMP and Generic RAM Plan. Identifies RAM Plan, RAM-AM/CCB and participation alignment issues, with evidence and recommended actions. |

### 2.2 Governing method and example

1. Company RAM-Process and approved current methods govern execution and analysis tools.
2. Project contractual/customer requirements, the approved requirements baseline and approved project decisions govern targets and acceptance criteria.
3. The [Generic RAM Plan](../../../Knowledge/Templates/RAM_Plan/RAM_Plan_Generic_3BU_15000_1712_DUAPA_ED07.docx), 3BU 15000 1712 DUAPA, Edition 07, governs applicable generic RAM process activities. Its relevant topics include the RAM-AM role, phase-related RAM activities, dependability requirements, RAM analysis and field failure reporting.
4. The [DFE RAM Plan](../../../Knowledge/Templates/RAM_Plan/RAM_Plan_DFE_3BU_62800_0018_DUAPA_ED02.docx), 3BU 62800 0018 DUAPA, Edition 02, is a structural and analytical example only. Its project targets, availability classes, environmental assumptions, methods and design rules are not transferred to ZIVD.
5. EN 50126-1:2017 is the generic railway RAMS lifecycle reference, subject to the approved project standards baseline and applicable national/customer requirements. This plan does not claim a complete standards-compliance assessment.

When sources conflict, record the conflict, assess its impact, identify the controlling approved source and raise a project decision/action. The SEMP refers to the CDRL as an external SharePoint source; it was not available for this plan. No CDRL requirement has therefore been inferred.

## 3. Project System and RAM Boundary

### 3.1 System description and subsystem breakdown

The ZIVD PBS defines three principal solution branches: ETCS L2 trackside equipment (1.1), interlocking equipment (1.2), and telecommunications (1.3). The following breakdown carries each branch to the subsystem and equipment-package level shown in the PBS. It describes the current project scope for RAM planning; it does not replace the controlled architecture or establish functions, interfaces, operating modes, or RAM performance not stated in the source documents (PBS, `Arborescence` worksheet, reference 100007442, dated 2026-09-23).

#### ETCS L2 trackside equipment (PBS 1.1)

The PBS identifies the following ETCS packages and lower-level elements:

- **RBC (1.1.1):** RBC hardware Release 3.1 and RBC HU software BL 1.2.1.A, with HIS operator interface, MCE/MOP maintenance server and diagnostic workplace, and GSM-R interface.
- **DAKO (1.1.2):** DAKO PV_01.02.02, including the ELEKTRA 1 interface (AHI, OLE, POK) and the new ELEKTRA 2 ZIV interface.
- **LEU (1.1.3):** LEU PV 3.5, with shelf, power distribution unit (PDU), PAB/RAB/SAB adaptation boards, PIO, balise driver (BD), and EMC materials.
- **Eurobalise (1.1.4):** existing and new Siemens S21 ERL6 balise installations, balise cable and balise driver. The PBS separately lists a BD under LEU and Eurobalise; the configuration owner shall resolve the PBS note that identifies a duplicated BD before quantities or reliability contributions are calculated.

These PBS entries identify equipment/configuration packages but do not fully define the ETCS functional architecture, interface allocation, operating modes, failure response, or RAM requirements. The approved ETCS design and requirements baseline shall provide those details before quantitative modelling.

#### Interlocking equipment (PBS 1.2)

The interlocking branch comprises the following packages:

- **ELEKTRA 2 (1.2.1):** PV INT 2.9.1A (INT_22.07), with EC/CC and IF cabinets; reused KOAX and SFA cabinets; ZG RIC at Nagykapornak and RIC at Egervár; A3 and Webride; station LCSI and its ETCS interface; RAD-PAD; and CU-modem (LTE, NTE).
- **AKF (1.2.2):** AKF PV akf-1.7.0 and application database app-akf-mav-hodos 1.5.0, with operator, Super AKF and maintenance workplaces.
- **AzLM (1.2.3):** AzLM PV 7.6, comprising AzLM cabinet and ZP 30K.
- **Power supply upgrade (1.2.4):** including the PQ upgrade.
- **MÁV block system toward Egervár (1.2.5):** including the AT 1420 update.
- **ZG Block (1.2.6):** including the ZG RIC connection toward Nagykapornak.
- **Station wayside equipment (1.2.7):** existing and new main signals, existing and new shunting signals, and existing and new turnouts.

The PBS marks elements across these packages as existing, new, or re-used and assigns make/team/buy routes. Treat these as configuration and supply-chain attributes, not evidence that an element is operationally independent or RAM-compliant. The current system description is an IXL architecture drawing; detailed subsystem functions, dependencies, interface behaviours and service consequences remain to be confirmed from controlled design and requirements evidence.

#### Telecommunications (PBS 1.3)

The telecommunications branch covers two location packages:

- **Zalaszentiván station (1.3.1):** PIS including Schauer IRCS cabinets; station-building security system; camera system monitoring centre (NVR); data transmission network including fibre-optic splicing assemblies and ODF; and open-line signalling cables Fv24/Fv96.
- **Szentivánvölgyi train-stop platform (1.3.2):** outdoor telecommunications cabinet containing IRCS, UPS, MOXA Remote I/O, fire and intrusion sensors; PIS with audio-visual equipment and clock; and data transmission network.

The PBS identifies these packages and equipment but does not define the telecommunications service boundary, network topology or all interfaces. Confirm those from the controlled telecom design before assigning RAM dependencies or redundancy credit.

The IXL system-description drawing shows operator/diagnostic workstations, axle counters, station level-crossing interfaces, RBC/DAKO and other IXL interfaces. It notes that Category 1 and 2 networks connect between locations and that inter-station fibre-optic links use double-redundant rings on separated cable routes. This is a design statement to verify, not an availability result. Do not credit redundancy until topology, route diversity, switching/recovery, common-cause exposure and restoration arrangements are confirmed (System Description - IXL, page 1).

Across all three branches, the PBS records a mix of existing, new and re-used items and make, team and buy routes. These classifications identify where supplier and partner evidence may be needed; they are not RAM evidence or acceptance results. PBS descriptions are a scope breakdown, not a complete functional system description. Reconcile this breakdown against approved requirements, interface specifications, detailed architecture and final configuration before analysis.

### 3.2 Boundary and external dependencies

The analysis boundary shall be confirmed against the contract and approved system requirements. It shall identify the delivered system, supplied and reused equipment, customer-furnished equipment, interfaces and external services. Where they affect the service function, the assumptions and models shall address:

- external power supplies and power distribution;
- GSM-R and other communication links, inter-station fibre routes and network interfaces;
- interfaces to existing IXL, block, station and wayside equipment;
- operator, maintenance and diagnostic facilities;
- environmental/site conditions, access, operating rules and maintenance resources;
- customer/operator response, spares, logistics, repair facilities and third-party restoration.

No equipment or interface is excluded from RAM assessment solely because it is existing, re-used, purchased or outside Hitachi Rail's direct design responsibility. An item may be treated as an external assumption only when its boundary and supporting evidence are approved.

### 3.3 Configuration and BoM control

The BoM is titled for ELEKTRA2 and AzLM. Its `Mengengerüst` worksheet contains 1,126 populated part rows and a Zalaszentiván project-quantity column. This does not demonstrate coverage of ETCS, telecommunications or every other PBS element (BoM, `Mengengerüst` worksheet). Before quantitative analysis, the SEM, configuration manager and RAM-AM shall reconcile the PBS, BoM, architecture, quantities, installed configuration, spares, variants and maximum field-relevant configuration. Configuration changes affecting RAM assumptions or results shall be impact-assessed and controlled.

## 4. RAM Requirements and Acceptance Basis

### 4.1 Current status

The reviewed SEMP contains no project RAM target values and refers to the CDRL as an external source that was not provided. The BoM, PBS and system-description drawing define configuration context, not RAM acceptance criteria. Reliability, availability, maintainability, service-affecting consequence classes, environmental limits, mission profiles and acceptance thresholds are therefore **not established in the reviewed sources**. The separate SEMP RAM review records this evidence limitation and recommends confirming the CDRL and project requirements before baselining the plan (SEMP, Sections 9, 12.1 and 16.9; SEMP RAM Review, Review Comment RAM-01).

No target from the DFE example, another project, a generic standard or an assumed availability class shall be applied to ZIVD without approved requirements and documented allocation rationale.

### 4.2 Requirements to identify and control

The Requirements Manager (RM), SEM and RAM-AM shall establish a traceable RAM requirements set from the contract, CDRL, customer/operator requirements, applicable specifications and approved project decisions. At minimum, clarify:

| RAM topic | Information to establish before analysis or acceptance |
| --- | --- |
| Reliability | Required function/configuration; covered failure population; operating profile and observation interval; treatment of random hardware failures, systematic/software faults and external causes; metric, target and evidence/confidence basis. |
| Availability | Service definition; availability type and boundary; service-affecting failure/consequence categories; operating period; included/excluded downtime; target and reporting basis. |
| Maintainability | Fault detection, diagnosis, access, isolation, repair/replace, test and return-to-service requirements; required restoration times and conditions. |
| Maintenance and logistics | Preventive/corrective maintenance regime; access windows; staffing/skills; tools, spares, transport and repair arrangements; customer and supplier responsibilities. |
| Environment and use | Site/environmental conditions, power quality, installation constraints, duty cycle, operating and maintenance conditions, and evidence of suitability. |
| Verification and acceptance | Analysis/test/operational evidence; configuration and exposure period; pass/fail criteria; evidence owner; independent review and acceptance authority. |

Each requirement shall have a unique identifier, source, owner, allocation, verification method, evidence reference, status and approved disposition. Conflicts, unverifiable statements and absent criteria shall be resolved through requirements management before they are reported as satisfied.

### 4.3 RAM performance definitions

For each approved metric, define the item boundary, mission/operating time, failure definition and data treatment before calculation. Where assumptions are justified, analysis may report failure rate in failures/hour and FIT, MTBF and reliability. Use $1\ \mathrm{FIT}=10^{-9}$ failures/hour. MTBF shall not be presented as a service-availability claim.

Availability calculations shall distinguish inherent, achieved or operational availability as required by the approved requirement. State the treatment of active repair, diagnosis, access waiting time, logistics, spares, planned maintenance and external delays. The expression $A_o=\text{uptime}/(\text{uptime}+\text{downtime})$ is usable only after the project approves the time boundary and event definitions. No availability result is meaningful until its target, boundary, configuration and downtime assumptions are agreed.

## 5. RAM Organization and Responsibilities

The SEMP identifies a RAM-AM function, but the roster labels an assigned role “Project Manager (RAM-AM)”; its CCB membership table does not list the RAM-AM, and its milestone involvement tables show attendance on request at several RAM-relevant gates. The SEMP also states that subordinate plans are “Not applicable” while listing the Generic RAM Plan in its plan register. These statements are documented in the SEMP RAM review (SEMP, Sections 9, 12.1, 13.1.1, 13.1.4, 13.12 and 16.9; SEMP RAM Review, Review Comments RAM-01 and RAM-02). The controlled SEMP and governance records shall be aligned.

| Role | RAM responsibility under this plan |
| --- | --- |
| Project Manager (PM) | Provide resources and schedule; resolve escalated project RAM issues; ensure RAM evidence is considered at gates. |
| System Engineering Manager (SEM) | Own system boundary and architecture; coordinate allocation, interfaces and technical inputs; ensure RAM requirements are addressed in design. |
| RAM Assurance Manager (RAM-AM) | Independently assure RAM requirements, methods, analyses, evidence, tailoring and status; participate in essential RAM reviews; be a permanent CCB member; raise deviations and unresolved risks. Appointment, reporting line and independence from assessed design/implementation work shall be documented. |
| Requirements Manager (RM) | Maintain source-to-requirement traceability, allocation, verification method and status; control open/conflicting requirements. |
| Configuration Manager (CM) | Maintain approved configuration and change records; support PBS/BoM/design reconciliation and analysis configuration control. |
| Design/work-package and supplier owners | Provide design, failure-rate, reliability, diagnostic, environmental, maintenance, repair and test evidence; report changes affecting assumptions/results. |
| IVVQ/Test Manager and Validator | Plan and execute RAM-related verification/validation evidence within approved plans; preserve configuration and failure records. |
| Quality Assurance Manager (QAM) | Assure compliance with project quality and document-control processes and review records. |
| Operator/customer and maintenance stakeholders | Define service consequences, use/maintenance assumptions, operational data, access/logistics constraints and acceptance criteria. |

The Generic RAM Plan requires a nominated RAM-AM to participate in essential meetings/reviews and be a permanent CCB member; it also requires functional independence from design and implementation activities subject to RAM assessment (Generic RAM Plan, “RAM Assurance Manager”). Accordingly, the RAM-AM shall have planned participation at RAM-relevant requirements, design, test-readiness, validation, PIO and qualification decisions. “Attend on request” is not the default at a gate where RAM requirements, architecture, assumptions, analysis or acceptance evidence are decided. Align the SEMP responsibility matrix and CCB terms of reference, or record an approved and justified tailoring decision.

## 6. RAM Activities and Project Milestones

The SEMP plans distinct IXL and ETCS milestone dates; the dates below are planned (P), not confirmed actuals. RAM evidence shall be reviewed at the relevant gate for each solution branch. The planned milestone sequences and objectives are in SEMP Sections 6.1-6.2 (milestone tables) and 15.1-15.2.

| Gate | IXL plan | ETCS plan | RAM focus / expected decision evidence |
| --- | --- | --- | --- |
| SOR - Solution Orientation Review | 10/2026 | 11/2026 | Confirm boundary, stakeholders, RAM-AM appointment, applicable sources, assumptions, RAM work packages and open requirement sources. |
| SRR - Solution Requirements Review | 11/2026 | 12/2026 | Establish approved RAM requirements and verification approach; resolve service definition, targets, consequences, environment and acceptance evidence, or record approved actions. |
| SFR - Solution Functional Review | 11/2026 | 12/2026 | Review functional architecture and preliminary RAM allocation; identify single points, interfaces, dependencies and data needs. |
| PDR - Preliminary Design Review | 12/2026 | 02/2027 | Review preliminary RAM model, failure/repair assumptions, design constraints, initial RAM design rules and maintenance concept; confirm operator assumptions and allocation. |
| CDR - Critical Design Review | 01/2027 | 02/2027 | Review detailed configuration and PBS/BoM reconciliation; confirm analysis inputs, RAM FMEA or equivalent, supplier evidence, maintainability and test coverage. |
| TRR1-LAB - Start Laboratory IVVQ | 02/2027 | 05/2027 | Confirm RAM-relevant lab configuration, test objectives, fault/diagnostic recording, entry criteria and FRACAS workflow. |
| TRR1-FIELD - Start Field IVVQ | 02/2027 | 05/2027 | Confirm approved field configuration, installation/operational assumptions, evidence collection and failure-reporting readiness. |
| TQR1 / TRR2 | 06/2027 | 09/2027 | Review integration/verification results, requirement status, deviations, analysis updates and readiness for operational validation. |
| TQR2-1 - Initial Validation / Assessment Handover | 07/2027 | 10/2027 | Provide RAM evidence and open-item status for validation/assessment handover; identify limitations and outstanding operational evidence. |
| FQR-1 - Start Dark Operation and PIO | 08/2027 | 12/2027 | Confirm RAM-related operational prerequisites, baseline, monitoring/reporting, maintenance readiness and approved residual assumptions. |
| TQR2-2 - Finished PIO / Standby Period | 08/2027 | 12/2027 | Review operational/standby failure and maintenance records; update analyses; close or justify remaining deviations. |
| FQR-2 - Final Qualification Review | 08/2027 | 12/2027 | Present final RAM compliance/evidence status, limitations, accepted deviations and transition-to-support arrangements for customer acceptance. |

At each gate, the RAM-AM shall provide status of requirements, evidence, assumptions, open actions, risks, deviations and decisions needed. A deliverable's existence does not establish compliance; evidence shall be configuration-specific and assessed against approved acceptance criteria.

## 7. RAM Methods, Analyses and Controls

### 7.1 Analysis strategy

Analysis depth shall be proportionate to requirements, boundary, design maturity, risk, field consequences and available data. Tailoring shall be justified and recorded. Use approved company RAM processes and current tools. Retain analysis inputs, tool/version, assumptions, units, configuration, data sources, uncertainty and independent checks for reproducibility. This follows the Generic RAM Plan's lifecycle tailoring and RAM analysis guidance (sections “Phase related RAM activities” and “RAM analysis”).

### 7.2 Reliability and availability analysis

The reliability analysis shall cover the maximum field-relevant delivered configuration and map requirements through PBS/configuration items to model elements. It shall:

- identify functional paths, operating modes, dependencies and interfaces;
- identify failure-rate data provenance, component conditions and treatment of reused/vendor items;
- model relevant series, redundant and shared-support elements where supported by architecture evidence;
- assess common-cause, shared power, communication, environmental and maintenance dependencies;
- calculate only approved metrics and compare them with approved targets on a like-for-like basis;
- include sensitivity/uncertainty and identify dominant contributors;
- state exclusions and quantify or bound their potential impact where practicable.

Select company-approved failure-rate methods and data under the current RAM-Process. Manufacturer and field data may be used when configuration, conditions, confidence and derivation are documented. Select and justify a prediction method/environmental class against hardware type, supplier evidence and approved site conditions; do not transfer the DFE example's assumptions. Do not combine systematic software faults with random hardware rates without an approved model and explicit rationale. Address systematic faults through applicable lifecycle, verification, validation, change and FRACAS processes (Generic RAM Plan, “RAM analysis,” “Software errors” and “Field statistics”).

The system-description drawing states that inter-station fibre links use double-redundant rings on separated routes (page 1). Do not model them as independent redundant channels until topology, shared nodes/power, physical route separation, recovery, switchover and common-cause behaviour are verified. Apply the same evidence threshold before crediting other redundancy.

### 7.3 RAM failure analysis

Perform a RAM hardware FMEA/FMECA or equivalent structured failure analysis where required to support requirements and the system model. Use one failure mode per row and capture item/function, failure mode/cause, local and higher-level effects, service consequence, detection/diagnostics, restoration/maintenance response, evidence and action. Coordinate interfaces with hazard and safety analyses; RAM analysis does not replace them. Assess software/systematic failures using applicable project assurance methods, not as random hardware prediction. The DFE plan is an example of these analysis topics, not a source of ZIVD targets or design rules (DFE RAM Plan, Sections 5.2.2-5.2.4).

### 7.4 Maintainability, maintenance and logistics

Trace approved restoration requirements to fault detection, diagnosis, access, isolation, replacement/repair, testing and return to service. Account for staffing, competency, safe access, possessions, tools, spares, transport, repair turnaround and third-party response when these affect downtime. Review installation, operation and maintenance instructions, diagnostics and maintenance data as evidence. Where time data are absent, record a data gap rather than assuming zero. These activities follow the Generic RAM Plan's phase-related RAM and field-statistics guidance.

### 7.5 Environment, installation and operation

Check design and supplier evidence against approved site and operating conditions, including indoor/outdoor installation, temperature, humidity, vibration/shock, EMC, power, ingress, cabling and maintenance exposure as applicable. The reviewed SEMP, system description, PBS and BoM do not establish a complete environmental profile or all operating/maintenance conditions. Use the approved project/environmental baseline; do not infer DFE's Ground Benign/Ground Fixed assumptions for ZIVD.

## 8. Verification, Validation and Operational Evidence

Verify RAM requirements by the method and acceptance criterion allocated in the requirements baseline. Evidence may include analysis, inspection, review, test, supplier evidence and operational demonstration, as appropriate. The SEMP identifies IV and VQ plans, but their ZIVD-specific versions were not among the reviewed inputs (SEMP, plan register, Section 9). Those plans shall identify RAM-related steps, configuration, responsible parties, entry/exit criteria, data capture, pass/fail criteria and evidence records.

Tests and field/operational monitoring shall capture failures, defects, intermittent events, false alarms, repair/restore times, unavailable service time, operating exposure, configuration, environmental/operating context, corrective action and recurrence. Data shall distinguish hardware faults, systematic/design faults, external causes, maintenance-induced events and non-failure interruptions. State data quality and censoring/zero-failure treatment before making statistical claims. The Generic RAM Plan calls for failure reporting and analysis of field data (sections “Field statistics” and “Failure reporting”).

At TQR2-1, FQR-1, TQR2-2 and FQR-2, review RAM evidence with validation, DeBo/assessment, safety, quality, customer and operational evidence as applicable. Acceptance remains with the authority identified in the contract and project governance; this plan does not assign customer acceptance authority.

## 9. FRACAS and RAM Reporting

Use the approved project failure-reporting and corrective-action process. Establish a FRACAS or identify the approved equivalent before laboratory/field IVVQ begins. Define event criteria, reporting responsibility, severity/service impact, configuration/exposure data, investigation, root cause, corrective/preventive actions, effectiveness verification, closure authority, trend analysis and escalation. The Generic RAM Plan calls for a failure reporting and corrective action system for failures and software errors during operation and for recording corrective measures (section “Failure reporting”). The SEMP's specific FRACAS arrangements and deliverable obligations remain to be confirmed against the CDRL and applicable project process.

Record and screen failures/defects found during laboratory tests, installation, field IVVQ, PIO, standby and operation for RAM impact. Manage safety-significant events through the Safety Plan and applicable reporting process as well. FRACAS closure does not by itself close a RAM requirement or approve a model change; update affected requirements, analyses and evidence under configuration/change control.

Report RAM status at milestone reviews and at a frequency agreed with the PM and RAM-AM. Each report shall summarize requirement status, analysis maturity/results, data gaps, field performance, FRACAS trends, risks, deviations, actions, required decisions and changes since the previous baseline.

## 10. RAM Deliverables

The deliverable register shall be aligned with the CDRL, SEMP deliverables tables and controlled document plan. The Generic RAM Plan identifies reliability analysis outputs and recommends preliminary reliability analysis and FRACAS where appropriate/required; this project register tailors that baseline to ZIVD. Contractual IDs, editions, owners and submission dates remain unconfirmed because the CDRL was not reviewed.

| Deliverable / record | Applicability and purpose | Planned timing / control |
| --- | --- | --- |
| Project RAM Plan | Project-specific definition of requirements, activities, roles, evidence and tailoring. | Approve/update at SRR; maintain through FQR-2; identify in SEMP and document plan. |
| RAM requirements and traceability register | Source, allocation, verification, evidence and compliance status for each approved RAM requirement. | Establish for SRR; baseline/update at requirements and configuration gates. |
| RAM assumptions, boundary and configuration record | Model/configuration basis, interfaces, exclusions, data sources and approved operational assumptions. | Initial at SOR/SFR; baseline at PDR/CDR; update with changes. |
| Preliminary reliability/availability assessment | Recommended early assessment of architecture gaps, contributors and data needs. | Target SFR/PDR; update as design matures. |
| RAM FMEA/FMECA or justified equivalent | Failure consequences, diagnosis and maintenance evidence where required by approved requirements/analysis strategy. | Develop with design maturity; review by CDR and update for changes. |
| Reliability and availability analysis | Configuration-specific demonstration against approved targets; generic plan reliability-analysis deliverable. | Baseline inputs by CDR; issue/update for TQR1/TRR2, TQR2-1 and FQR-2. |
| Maintainability / maintenance evidence | Restoration process, repair/diagnosis assumptions, resources, instructions and applicable time criteria. | Review by CDR; verify before PIO/FQR-1; close at FQR-2. |
| RAM verification and validation evidence | Results, deviations and traceability from tests, inspections, reviews, supplier data and operational validation. | Produce at applicable TRR/TQR/FQR gates in IV/VQ and milestone records. |
| FRACAS records and trend/status reports | Event and corrective-action records for applicable testing/field use, under approved process and CDRL. | Ready before TRR1-LAB; maintain through PIO, standby and support transition. |
| RAM milestone/status reports and final compliance summary | Evidence status, residual gaps, decisions, accepted deviations and final RAM position. | At agreed reviews; final at FQR-2. |

The word “required” in this plan describes the RAM process baseline, not a confirmed CDRL submission obligation. Confirm contractual status and delivery format against the CDRL and approved SEMP.

## 11. Assumptions, Uncertainties and Actions

### 11.1 Assumptions and limitations

- The SEMP is an Edition 01 proposal; the milestone dates are planned, not confirmed actual dates (SEMP, Sections 6.1-6.2 and 15.1-15.2).
- The CDRL is not available locally; no numerical RAM target, customer acceptance criterion or submission obligation is confirmed (SEMP, Sections 9 and 12.1; SEMP RAM Review, RAM-01).
- The supplied SD is a preliminary IXL architecture drawing. It does not define all ETCS, telecommunications, operational, environmental or maintenance details needed for final RAM models.
- The PBS is the current project breakdown reference, but configuration and quantities require confirmation against controlled design and as-built records.
- The ELEKTRA2/AzLM BoM may not cover all PBS branches; completeness and revision alignment are unconfirmed.
- Supplier, operator and maintenance data have not been provided. Predictions and operational availability claims cannot yet be substantiated.
- The drawing states that fibre-ring routes are separated, but this has not been independently verified; no redundancy benefit is credited.
- Confidence in numerical project RAM performance is low because requirements, boundary, configuration and data are incomplete. This is a planning limitation, not a conclusion that the solution fails RAM requirements.

### 11.2 Action list

| ID | Action / closure evidence | Suggested owner | Required by |
| --- | --- | --- | --- |
| ZD-RAM-01 | Obtain/review the CDRL and contractual/customer RAM requirements; create source-linked RAM requirements and acceptance criteria. | PM / RM / RAM-AM | Before SRR approval |
| ZD-RAM-02 | Confirm RAM-AM appointment, role label, reporting line and independence; add the RAM-AM as permanent CCB member and define required gate participation. | PM / SEM / RAM-AM | SOR; implement before SRR |
| ZD-RAM-03 | Identify this controlled project RAM Plan in the SEMP and reconcile “Subordinate Plans: Not applicable”; align plan/deliverable and responsibility tables. | SEM / Document Manager / RAM-AM | Before SRR approval |
| ZD-RAM-04 | Confirm boundary, service definition, maximum field-relevant configuration, external dependencies and acceptance authority. | SEM / PM / Operator / RAM-AM | SOR/SRR |
| ZD-RAM-05 | Reconcile PBS, BoM, SD, requirements baseline, variants and supplier scope; confirm ETCS/telecom coverage and quantities. | CM / SEM / Work-package owners | Before preliminary analysis; baseline by CDR |
| ZD-RAM-06 | Obtain failure-rate, reliability, diagnostic, environmental, maintainability, maintenance and field-history evidence for new/existing/re-used elements; document data quality. | Work-package owners / suppliers / RAM-AM | SFR through CDR |
| ZD-RAM-07 | Agree analysis method, software/systematic-failure treatment, service consequences, downtime definitions, environment and operating/maintenance assumptions. | RAM-AM / SEM / RM / Operator | Before analysis baseline at PDR |
| ZD-RAM-08 | Verify ring topology, physical route separation, shared dependencies, failover/recovery and restoration before assigning availability credit. | Telecom/design owner / SEM / RAM-AM | PDR/CDR |
| ZD-RAM-09 | Align RAM test/validation criteria, configuration records, event data capture and FRACAS workflow with controlled IV/VQ plans. | IVM / Validator / RAM-AM | Before TRR1-LAB |
| ZD-RAM-10 | Confirm RAM deliverable IDs, editions, owners, submission dates and customer acceptance evidence against the CDRL and document plan. | Document Manager / PM / RAM-AM | Before SRR; maintain to FQR-2 |

## 12. Document Review and Approval

Review this draft by the SEM, RM, CM, IVVQ/Test Manager, QAM, RAM-AM and project/customer representatives required by project governance. Record approval in the controlled document system. Manage changes under document/configuration control and identify affected requirements, assumptions, models, results, deliverables and actions.

## 13. References

1. Hitachi Rail, [*RAM Plan Generic*, 3BU 15000 1712 DUAPA, Edition 07](../../../Knowledge/Templates/RAM_Plan/RAM_Plan_Generic_3BU_15000_1712_DUAPA_ED07.docx).
2. Hitachi Rail, [*RAM Plan DFE*, 3BU 62800 0018 DUAPA, Edition 02](../../../Knowledge/Templates/RAM_Plan/RAM_Plan_DFE_3BU_62800_0018_DUAPA_ED02.docx), example only.
3. EN 50126-1:2017, *Railway applications - The Specification and Demonstration of Reliability, Availability, Maintainability and Safety (RAMS) - Part 1: Generic RAMS Process*.
4. ZIVD SEMP, [3BU_61914_0002_DPAPA_ED01PD01](../Input/SEMP_3BU_61914_0002_DPAPA_ED01PD01.docx), Edition 01 proposal.
5. ZIVD system description drawing, [3BU 61914 0016 PEAPQ](../Input/SD_IXL_3BU_61914_0016_PEAPQ_ED01PD02.pdf), ED 01PD02, dated 2026-08-17.
6. ZIVD BoM, [3BU_61914_2010_HAAPQ](../Input/BoM_3BU_61914_2010_HAAPQ.xlsx), *Bill of Material / Mengengerüst / Anyaglista - ELEKTRA2 and AzLM*.
7. ZIVD Product Breakdown Structure, [3BU_61914_0015_EDAPA](../Input/Project_Breakdown_Structure_3BU_61914_0015_EDAPA.xlsm), reference 100007442, dated 2026-09-23.
8. ZIVD [SEMP RAM Review](../output/SEMP_RAM_Review.md), 2026-10-06.
