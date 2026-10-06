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

> **Approval condition:** This plan is a project-specific working baseline. Project RAM targets, the applicable contractual requirement set, the RAM-AM appointment, and the complete system configuration have not been established by the inputs reviewed. These are controlled actions in Section 11. No numerical RAM target is created by this plan.

## 1. Purpose and Scope

This plan defines how RAM requirements will be identified, allocated, analysed, verified and reported for the ZIVD solution. It tailors the company Generic RAM Plan to the current project system definition and milestone strategy. It is to be read with the Solution Engineering and Management Plan (SEMP), requirements baseline, applicable customer/contract documents, Safety Plan, IV Plan, VQ Plan, Quality Management Plan and configuration management arrangements.

The scope is the ZIVD solution and its RAM-relevant interfaces as represented in the current PBS and system description. It includes the Interlocking (IXL) and ETCS Level 2 trackside solutions, the listed station/wayside and telecommunications elements, project-specific application/configuration data, integration and verification, field validation, Putting into Operation (PIO), the standby period, and transition to customer support to the extent these activities affect RAM evidence or assumptions.

The plan applies to new, existing and re-used elements where they contribute to the delivered function. It does not replace the SEMP, safety engineering, system design, IVVQ, maintenance, configuration or quality plans. RAM analyses are not safety analyses and do not establish a Safety Integrity Level. Safety-related conclusions and interfaces remain subject to the Safety Plan and the responsible safety authority.

## 2. Basis, References and Precedence

### 2.1 Project inputs reviewed

| Reference | Input and use in this plan |
| --- | --- |
| [SEMP ZIVD](../Input/SEMP_3BU_61914_0002_DPAPA_ED01PD01.docx) | Project scope, roles, plan register, tailoring and separate IXL/ETCS planned milestone chains. Proposal document; its target dates are planned. |
| [System Description - IXL](../Input/SD_IXL_3BU_61914_0016_PEAPQ_ED01PD02.pdf) | Preliminary IXL architecture drawing and communication/network notes. Drawing is not a complete RAM requirement or operational definition. |
| [BoM - ELEKTRA2 and AzLM](../Input/BoM_3BU_61914_2010_HAAPQ.xlsx) | Part quantities and equipment groups. The workbook title and content do not demonstrate that it is a complete BoM for all PBS elements. |
| [Project Breakdown Structure](../Input/Project_Breakdown_Structure_3BU_61914_0015_EDAPA.xlsm) | System decomposition, existing/new/re-used classification, make/team/buy assignments and maturity fields. Current reference is 100007442, dated 2026-09-23. |
| [SEMP RAM review](SEMP_RAM_Review.md) | RAM-focused review observations about RAM Plan identification, RAM-AM participation, CCB membership and required reconciliation with the SEMP. |

### 2.2 Governing method and example

1. Company RAM-Process and approved current methods govern execution and analysis tools.
2. Project contractual requirements, customer requirements, approved requirements baseline and project decisions govern project targets and acceptance criteria.
3. The Generic RAM Plan, 3BU 15000 1712 DUAPA, Edition 07, governs generic RAM process activities where applicable.
4. The DFE RAM Plan, 3BU 62800 0018 DUAPA, Edition 02, is used as an example of project-plan structure and RAM analysis topics only. Its project-specific targets, availability classes, environmental assumptions, methods and design rules are **not** transferred to ZIVD.
5. EN 50126-1:2017 applies as the generic railway RAMS lifecycle reference, subject to the project’s approved standards baseline and applicable national/customer requirements.

Where sources conflict, record the conflict, assess its impact, identify the controlling approved source, and raise a project decision/action. The CDRL is referenced in the SEMP as an external SharePoint item and was not available for this plan. No CDRL requirement has therefore been inferred.

## 3. Project System and RAM Boundary

### 3.1 PBS-based solution overview

The current PBS identifies the following principal branches. This is a RAM planning summary, not a substitute for the controlled PBS or design baseline.

| PBS branch | RAM-relevant items identified in the PBS |
| --- | --- |
| ETCS L2 trackside equipment, BL 2.3.0.d | RBC HW Release 3.1 and RBC HU SW baseline; HMI; maintenance/diagnostic workplace; GSM-R interface; DAKO; ELEKTRA 1 and ELEKTRA 2 interfaces; LEU; Eurobalises and balise drivers. |
| Interlocking equipment | ELEKTRA 2; cabinets and interfaces; existing/re-used station and block interfaces; AKF/operator and maintenance workplaces; AzLM axle counter system; power supply upgrade; station wayside signals, turnouts and related elements. |
| Telecommunications | Re-used Zalaszentiván station PIS, security, CCTV and data network; new Szentivánvölgyi stop telecommunications cabinet, PIS and data network; signalling cables. |

The current PBS records a mix of existing, new and re-used items and make, team and buy delivery routes. Supplier and partner inputs are therefore needed wherever design, failure, maintenance or field evidence is not held by the project team. Maturity labels in the PBS are planning data; they are not RAM evidence or acceptance results.

The supplied system description drawing depicts the interlocking architecture and shows operator/diagnostic workstations, axle counters, station level-crossing interfaces, RBC/DAKO and other IXL interfaces. It notes that Category 1 and 2 networks connect between locations and that the inter-station fibre-optic connection uses double-redundant rings on separated cable routes. This redundancy is a design statement to verify; no availability credit is taken until topology, route diversity, switching behaviour, common-cause exposure, failure modes and restoration arrangements are confirmed.

### 3.2 Boundary and external dependencies

The analysis boundary shall be confirmed against the contract and system requirements. It shall identify the delivered system, supplied equipment, reused equipment, customer-furnished equipment, interfaces, and external services. At minimum, the following dependencies shall be addressed in assumptions and models where they affect the service function:

- external power supplies and power distribution;
- GSM-R and other communication links, inter-station fibre routes and network interfaces;
- interfaces to existing IXL, block, station and wayside equipment;
- operator, maintenance and diagnostic facilities;
- environmental/site conditions, access, operating rules and maintenance resources;
- customer/operator response, spares, logistics, repair facilities and third-party service restoration.

No equipment or interface is excluded from RAM assessment solely because it is existing, re-used, purchased, or outside Hitachi Rail’s direct design responsibility. Such elements may be treated as external assumptions only when the boundary and supporting evidence are approved.

### 3.3 Configuration and BoM control

The BoM identifies ELEKTRA 2 and AzLM and includes 1,126 populated part rows, with project quantities in the Zalaszentiván column. Its stated scope does not on its own establish coverage of the ETCS, telecom and every other PBS element. Before quantitative analysis, the SEM, configuration manager and RAM-AM shall reconcile PBS, BoM, system architecture, equipment quantities, installed configuration, spares, variants and the maximum field-relevant configuration. Configuration changes affecting RAM assumptions or results shall be impact-assessed and controlled.

## 4. RAM Requirements and Acceptance Basis

### 4.1 Current status

The available SEMP contains no project RAM target values. It refers to the CDRL, but that contractual data source was not supplied. The BoM, PBS and system-description drawing define scope/configuration context; they do not define RAM acceptance criteria. Accordingly, reliability, availability, maintainability, service-affecting consequence classes, environmental limits, mission profiles and acceptance thresholds remain **to be confirmed**.

No target from the DFE example, another project, a generic standard, or an assumed availability class shall be applied to ZIVD without approved requirements and documented allocation rationale.

### 4.2 Requirements to identify and control

The Requirements Manager (RM), SEM and RAM-AM shall establish a traceable RAM requirements set from the contract, CDRL, customer/operator requirements, applicable specifications and approved project decisions. It shall cover, as applicable:

| RAM topic | Information to establish before analysis/acceptance |
| --- | --- |
| Reliability | Required function and configuration; covered failure population; operating profile and observation interval; treatment of random hardware failures, systematic/software faults and external causes; metric, target and confidence/evidence basis. |
| Availability | Service definition; availability type and boundary; service-affecting failure/consequence categories; required operating period; included/excluded downtime; target and reporting basis. |
| Maintainability | Fault detection, diagnosis, access, isolation, repair/replace, test and return-to-service requirements; required restoration times and conditions. |
| Maintenance and logistics | Preventive/corrective maintenance regime; access windows; staffing/skills; tools, spares, transport and repair arrangements; customer and supplier responsibilities. |
| Environment and use | Site/environmental conditions, power quality, installation constraints, duty cycle, operating and maintenance conditions, and evidence that equipment is suitable for them. |
| Verification and acceptance | Analysis/test/operational evidence, configurations, sample or operating period, pass/fail criteria, evidence owner, independent review and acceptance authority. |

Each requirement shall have a unique identifier, source, owner, allocated item(s), verification method, evidence reference, status and approved disposition. Conflicts, unverifiable statements and absent criteria shall be resolved through requirements management before they are treated as satisfied.

### 4.3 RAM performance definitions

For each approved metric, the project shall define the item boundary, mission/operating time, failure definition and data treatment before calculation. Where the assumptions are justified, the analysis may report failure rate (failures/hour and FIT), MTBF and reliability. FIT shall use $1\ \mathrm{FIT}=10^{-9}$ failures/hour. MTBF shall not be presented as a service-availability claim.

Availability calculations shall distinguish inherent, achieved or operational availability as required by the approved requirement. The model shall state treatment of active repair time, diagnosis, waiting for access, logistics, spares, planned maintenance and external delays. An operational availability calculation may use $A_o=\text{uptime}/(\text{uptime}+\text{downtime})$ only after the project has approved the time boundary and event definitions. No availability calculation is meaningful until its target, boundary, configuration and downtime assumptions are agreed.

## 5. RAM Organization and Responsibilities

The SEMP identifies a RAM-AM function, but its team roster labels an assigned role as “Project Manager (RAM-AM)”; the CCB membership table does not list the RAM-AM, and the milestone involvement tables show attendance on request for several RAM-relevant gates. The SEMP also states that subordinate plans are “Not applicable” while listing the Generic RAM Plan in its plan register. These inconsistencies shall be resolved by updating the controlled SEMP and project governance records.

| Role | RAM responsibility under this plan |
| --- | --- |
| Project Manager (PM) | Provide resources and schedule; resolve escalated project RAM issues; ensure approved RAM evidence is included in gate decisions. |
| System Engineering Manager (SEM) | Own system boundary and architecture; coordinate subsystem allocation, interface assumptions and technical inputs; ensure RAM requirements are addressed in design. |
| RAM Assurance Manager (RAM-AM) | Independently assure RAM requirements, methods, analyses, evidence, tailoring and status; participate in all essential RAM reviews; be a permanent CCB member; raise deviations and unresolved risks. The appointment, reporting line and functional independence from assessed design/implementation work shall be documented. |
| Requirements Manager (RM) | Maintain source-to-requirement traceability, allocation, verification method and status; control open or conflicting requirements. |
| Configuration Manager (CM) | Maintain the approved configuration and change records; support PBS/BoM/design reconciliation and analysis configuration control. |
| Design/work-package and supplier owners | Provide design, failure-rate, reliability, diagnostic, environmental, maintenance, repair and test evidence for allocated items; notify changes affecting assumptions or results. |
| IVVQ/Test Manager and Validator | Plan and execute RAM-related verification/validation evidence within approved test and validation plans; preserve configuration and failure records. |
| Quality Assurance Manager (QAM) | Assure compliance with the project quality and document-control processes and review records. |
| Operator/customer and maintenance stakeholders | Define service consequences, use and maintenance assumptions, operational data, access/logistics constraints and acceptance criteria. |

The RAM-AM shall be a permanent member of the CCB and have planned participation at RAM-relevant requirements, design, test-readiness, validation, PIO and qualification decisions. Attendance “on request” is not the default for a gate at which RAM requirements, architecture, assumptions, analysis results or acceptance evidence are decided. The SEMP responsibility matrix and CCB terms of reference shall be aligned with this requirement or an approved, justified tailoring decision.

## 6. RAM Activities and Project Milestones

The SEMP plans separate IXL and ETCS milestone dates. Dates below are planned (P) and shall be updated from the controlled project schedule. RAM evidence is reviewed at the relevant gate for each solution branch; a shared project RAM Plan does not imply identical maturity dates.

| Gate | IXL plan | ETCS plan | RAM focus / expected decision evidence |
| --- | --- | --- | --- |
| SOR - Solution Orientation Review | 10/2026 | 11/2026 | Confirm boundary, stakeholders, RAM-AM appointment, applicable sources, major assumptions, RAM work packages and open requirement sources. |
| SRR - Solution Requirements Review | 11/2026 | 12/2026 | Establish approved RAM requirements and verification approach; resolve service definition, targets, consequences, environment and acceptance evidence or record approved open actions. |
| SFR - Solution Functional Review | 11/2026 | 12/2026 | Review functional architecture and preliminary RAM allocation; identify single points, interfaces, dependencies and data needed for preliminary analysis. |
| PDR - Preliminary Design Review | 12/2026 | 02/2027 | Review preliminary RAM model, failure/repair assumptions, design constraints, initial RAM design rules and maintenance concept; confirm operator assumptions and requirement allocation. |
| CDR - Critical Design Review | 01/2027 | 02/2027 | Review detailed configuration and complete BoM/PBS reconciliation; confirm analysis inputs, RAM FMEA/other failure analysis, supplier evidence, maintainability and test coverage. |
| TRR1-LAB - Start Laboratory IVVQ | 02/2027 | 05/2027 | Confirm RAM-relevant laboratory configuration, test objectives, fault/diagnostic recording, entry criteria and defect/FRACAS workflow. |
| TRR1-FIELD - Start Field IVVQ | 02/2027 | 05/2027 | Confirm approved field configuration, installation/operational assumptions, field test evidence collection and failure-reporting readiness. |
| TQR1 / TRR2 | 06/2027 | 09/2027 | Review integration and verification results, requirement compliance status, deviations, analysis updates and readiness for operational validation. |
| TQR2-1 - Initial Validation / Assessment Handover | 07/2027 | 10/2027 | Provide the RAM evidence set and open-item status for validation and assessment handover; identify limitations and outstanding operational evidence. |
| FQR-1 - Start Dark Operation and PIO | 08/2027 | 12/2027 | Confirm RAM-related operational prerequisites, baseline, monitoring/reporting, maintenance readiness and approved residual assumptions before PIO. |
| TQR2-2 - Finished PIO / Standby Period | 08/2027 | 12/2027 | Review operation/standby-period failure and maintenance records, update analyses, close or justify remaining deviations and confirm final validation evidence. |
| FQR-2 - Final Qualification Review | 08/2027 | 12/2027 | Present final RAM compliance/evidence status, unresolved limitations, accepted deviations and transition-to-support arrangements for customer acceptance. |

At each gate, the RAM-AM shall provide a concise status covering requirements, evidence, assumptions, open actions, risks, deviations and decisions needed. A gate shall not imply RAM compliance merely because a deliverable exists; the evidence shall be configuration-specific and checked against approved acceptance criteria.

## 7. RAM Methods, Analyses and Controls

### 7.1 Analysis strategy

Analysis depth shall be proportionate to the requirement, system boundary, design maturity, risk, field consequences and available data. Tailoring shall be justified and recorded. The approved company RAM process and current analysis tools shall be used. Analysis inputs, tool/version, assumptions, units, configuration, data source, uncertainty and independent checks shall be retained for reproducibility.

### 7.2 Reliability and availability analysis

The reliability analysis shall include the maximum field-relevant delivered configuration and an auditable mapping from requirements through PBS/configuration items to model elements. It shall:

- identify functional paths, operating modes, dependencies and interfaces;
- identify failure-rate data provenance, component conditions and treatment of reused/vendor items;
- model relevant series, redundant and shared-support elements where supported by architecture evidence;
- assess common-cause, shared power, communication, environmental and maintenance dependencies;
- calculate only the approved metrics and compare like-for-like with approved targets;
- include sensitivity/uncertainty and identify dominant contributors;
- state exclusions and quantify or bound their potential impact where practicable.

Company-approved failure-rate methods and data shall be selected under the current RAM-Process. Manufacturer data and relevant field data may be used when their configuration, operating conditions, confidence and derivation are sufficiently documented. A prediction standard or environmental class shall not be selected by default: the project shall justify it against hardware type, supplier evidence and approved site conditions. Do not combine systematic software faults with random hardware rates without an approved model and explicit rationale. Systematic faults shall be addressed through the applicable lifecycle, verification, validation, change and FRACAS processes.

The separated-route fibre rings shown in the system description shall not be modelled as independent redundant channels until the actual topology, shared nodes/power, route separation, automatic/manual recovery, switchover and common-cause failure behaviour are verified. Similar evidence is required before crediting any other redundancy.

### 7.3 RAM failure analysis

A RAM hardware FMEA/FMECA or equivalent structured failure analysis shall be performed where needed to support the requirements and system model. It shall consider one failure mode per row and capture, as applicable, item/function, failure mode and cause, local and higher-level effects, service consequence, detection/diagnostics, restoration/maintenance response, evidence and action. Interfaces with hazard and safety analyses shall be coordinated; RAM analysis does not replace them. Analysis of software/systematic failure shall use the project’s applicable assurance methods and shall not be represented as random hardware prediction.

### 7.4 Maintainability, maintenance and logistics

The maintainability assessment shall trace approved restoration requirements to fault detection, diagnosis, access, isolation, replacement/repair, testing and return to service. It shall account for staff availability, competency, safe access, possessions, tools, spares, transport, repair turnaround and third-party response where these contribute to downtime. Installation, operation and maintenance instructions, diagnostics and maintenance data shall be reviewed as evidence. Where times are not available, they shall remain explicit data gaps, not assumed zero.

### 7.5 Environment, installation and operation

Design and supplier evidence shall be checked against approved site and operating conditions, including indoor/outdoor installation, temperature, humidity, vibration/shock, EMC, power, ingress, cabling and maintenance exposure as applicable. The SEMP, SD, PBS and BoM do not establish a complete environmental profile or all operating/maintenance conditions. Applicable requirements and verification evidence shall be taken from the approved project/environmental baseline.

## 8. Verification, Validation and Operational Evidence

RAM requirements shall be verified by the method and acceptance criterion allocated in the requirements baseline. Evidence may include analysis, inspection, review, test, supplier evidence and operational demonstration, as appropriate. The IV Plan and VQ Plan shall identify test/validation steps, configuration, responsible parties, entry/exit criteria, data capture, pass/fail criteria and evidence records. The SEMP identifies the IV and VQ plans but the ZIVD-specific versions were not reviewed here.

Tests and field/operational monitoring shall capture failures, defects, intermittent events, false alarms, repair/restore times, unavailable service time, operating exposure, configuration, environmental/operating context, corrective action and recurrence. Data shall be sufficient to distinguish hardware faults, systematic/design faults, external causes, maintenance-induced events and non-failure interruptions. Data quality and censoring/zero-failure treatment shall be stated before statistical claims are made.

At TQR2-1, FQR-1, TQR2-2 and FQR-2, RAM evidence shall be reviewed alongside validation, DeBo/assessment, safety, quality, customer and operational evidence as applicable. Acceptance remains with the authority identified in the contract and project governance; this plan does not assign customer acceptance authority.

## 9. FRACAS and RAM Reporting

The project shall use the approved project failure-reporting and corrective-action process. A FRACAS shall be established or the project’s approved equivalent identified before laboratory/field IVVQ begins. The process shall define event criteria, reporting responsibility, severity/service impact, configuration and exposure data, investigation, root cause, corrective/preventive actions, verification of effectiveness, closure authority, trend analysis and escalation.

Failures and defects found in laboratory tests, installation, field IVVQ, PIO, standby and operation shall be recorded and screened for RAM impact. Safety-significant events shall also be managed through the Safety Plan and applicable reporting process. FRACAS closure does not by itself close a RAM requirement or approve a model change; affected requirements, analyses and evidence shall be updated under configuration/change control.

RAM status shall be reported at project milestone reviews and periodically at the frequency agreed with the PM and RAM-AM. Each report shall summarize requirement status, analysis maturity/results, data gaps, field performance, FRACAS trends, risk, deviations, actions, decisions required and changes since the previous baseline.

## 10. RAM Deliverables

The project-specific deliverable register shall be aligned with the CDRL, SEMP deliverables tables and controlled document plan. The table below defines the RAM planning baseline; contractual deliverable IDs, editions, owners and submission dates remain to be confirmed.

| Deliverable / record | Applicability and purpose | Planned timing / control |
| --- | --- | --- |
| Project RAM Plan | Required project-specific definition of RAM requirements process, activities, roles, evidence and tailoring. | Approve/update at SRR and maintain through FQR-2; identify in SEMP and document plan. |
| RAM requirements and traceability register | Required source, allocation, verification, evidence and compliance status for each approved RAM requirement. | Establish for SRR; baseline and update at each requirements/configuration gate. |
| RAM assumptions, boundary and configuration record | Required model/configuration basis, interfaces, exclusions, data sources and approved operational assumptions. | Initial at SOR/SFR; baseline at PDR/CDR; update with changes. |
| Preliminary reliability/availability assessment | Recommended by the Generic RAM Plan; identifies early architecture gaps, dominant dependencies and data needs. | Target SFR/PDR; update as design matures. |
| RAM FMEA/FMECA or justified equivalent | Perform where required by the approved RAM requirements and analysis strategy; supports failure consequences, diagnosis and maintenance. | Develop with design maturity; review by CDR and update for design changes. |
| Reliability and availability analysis | Required RAM analysis deliverable under the Generic RAM Plan; configuration-specific demonstration against approved targets. | Inputs baselined by CDR; issue/update for TQR1/TRR2, TQR2-1 and FQR-2 as evidence matures. |
| Maintainability / maintenance evidence | Demonstrates restoration process, repair/diagnosis assumptions, resources, instructions and applicable time criteria. | Review by CDR; verify before PIO/FQR-1 and close at FQR-2. |
| RAM verification and validation evidence | Results, deviations and traceability from tests, inspections, reviews, supplier evidence and operational validation. | Produced at applicable TRR/TQR/FQR gates in IV/VQ and milestone records. |
| FRACAS records and trend/status reports | Required if specified by contract/process; establish the reporting system for test/field events and corrective actions. | Ready before TRR1-LAB; maintain through PIO, standby and transition to support. |
| RAM milestone/status reports and final compliance summary | Summarize current evidence, residual gaps, decisions, accepted deviations and final RAM status. | At agreed milestone reviews; final at FQR-2. |

“Required” in this table describes the RAM process baseline, not a confirmed CDRL submission obligation. Contractual status and delivery format shall be reconciled with the project CDRL and approved SEMP.

## 11. Assumptions, Uncertainties and Actions

### 11.1 Assumptions and limitations

- The SEMP is an Edition 01 proposal and its dates are planned, not confirmed actual dates.
- The reviewed CDRL is not available locally; no numerical RAM target, customer acceptance criterion or submission obligation is confirmed.
- The supplied SD is a preliminary IXL architecture drawing. It does not define all ETCS, telecommunications, operational, environmental or maintenance details needed for final RAM models.
- The PBS is the current project breakdown reference, but configuration and quantities require confirmation against controlled design and as-built records.
- The BoM titled ELEKTRA2 and AzLM may not cover all PBS branches; completeness and revision alignment are unconfirmed.
- Supplier, operator and maintenance data have not been provided. Predictions and operational availability claims cannot yet be substantiated.
- Fibre ring route diversity is stated in the SD drawing but has not been independently verified; no redundancy benefit is credited in this plan.
- Confidence in project RAM targets and numerical RAM performance is presently low because the governing requirements, boundary, configuration and data are incomplete. This is a planning assessment, not a conclusion that the solution fails RAM requirements.

### 11.2 Action list

| ID | Action / closure evidence | Suggested owner | Required by |
| --- | --- | --- | --- |
| ZD-RAM-01 | Obtain and review the CDRL and all contractual/customer RAM requirements; create source-linked RAM requirements and acceptance criteria. | PM / RM / RAM-AM | Before SRR approval |
| ZD-RAM-02 | Confirm RAM-AM appointment, role label, reporting line and functional independence; add the RAM-AM as permanent CCB member and define mandatory gate participation. | PM / SEM / RAM-AM | SOR; implement before SRR |
| ZD-RAM-03 | Update the SEMP plan register to identify this controlled project RAM Plan and reconcile “Subordinate Plans: Not applicable”; align deliverable and responsibility tables. | SEM / Document Manager / RAM-AM | Before SRR approval |
| ZD-RAM-04 | Confirm system boundary, operational service definition, maximum field-relevant configuration, external dependencies and applicable acceptance authority. | SEM / PM / Operator / RAM-AM | SOR/SRR |
| ZD-RAM-05 | Reconcile PBS, BoM, SD, requirements baseline, variants and supplier scope; confirm coverage of ETCS and telecom elements and configuration quantities. | CM / SEM / Work-package owners | Before preliminary analysis; baseline by CDR |
| ZD-RAM-06 | Obtain failure-rate, reliability, diagnostic, environmental, maintainability, maintenance and field-history evidence for new, existing and re-used elements; document data quality. | Work-package owners / suppliers / RAM-AM | SFR through CDR |
| ZD-RAM-07 | Agree analysis method, software/systematic-failure treatment, service consequences, downtime definitions, environment and operating/maintenance assumptions. | RAM-AM / SEM / RM / Operator | Before analysis baseline at PDR |
| ZD-RAM-08 | Verify ring topology, physical route separation, shared dependencies, failover/recovery behaviour and restoration strategy before assigning availability credit. | Telecom/design owner / SEM / RAM-AM | PDR/CDR |
| ZD-RAM-09 | Align RAM test/validation criteria, configuration records, event data capture and FRACAS workflow with controlled IV/VQ plans. | IVM / Validator / RAM-AM | Before TRR1-LAB |
| ZD-RAM-10 | Confirm RAM deliverable IDs, editions, owners, submission dates and customer acceptance evidence against the CDRL and document plan. | Document Manager / PM / RAM-AM | Before SRR; maintain to FQR-2 |

## 12. Document Review and Approval

This draft shall be reviewed by the SEM, RM, CM, IVVQ/Test Manager, QAM, RAM-AM and project/customer representatives as required by project governance. Approval shall be recorded in the controlled document system. Changes shall be managed under document and configuration control; revisions shall identify affected requirements, analysis assumptions, models, results, deliverables and open actions.

## 13. References

1. Hitachi Rail, *RAM Plan Generic*, 3BU 15000 1712 DUAPA, Edition 07.
2. Hitachi Rail, *RAM Plan DFE*, 3BU 62800 0018 DUAPA, Edition 02 (example only).
3. EN 50126-1:2017, *Railway applications - The Specification and Demonstration of Reliability, Availability, Maintainability and Safety (RAMS) - Part 1: Generic RAMS Process*.
4. ZIVD SEMP, 3BU_61914_0002_DPAPA_ED01PD01, Edition 01 proposal.
5. ZIVD system description drawing, 3BU 61914 0016 PEAPQ, ED 01PD02, dated 2026-08-17.
6. ZIVD BoM, 3BU_61914_2010_HAAPQ, *Bill of Material / Mengengeruest / Anyaglista - ELEKTRA2 and AzLM*.
7. ZIVD Product Breakdown Structure, 3BU_61914_0015_EDAPA, reference 100007442, dated 2026-09-23.
8. ZIVD *SEMP RAM Review*, 2026-10-06.
