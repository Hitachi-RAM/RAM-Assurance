# L03000 DDQS Process - RAM Review

## Scope and basis

This review compares `G-PRD_L03000_00d09_EN_for_final_review_cleaned.docx` with `06.1 DDQ - Design  Develop and Qualify the Solution.pdf` (release L.2.2.0), with focus on reliability, availability, maintainability and lifecycle RAM control.

The comparison is based on the process text, its named activities, references, transition/KPI pointers, and R.A.C.I./input-output sections available in the two files. It does not verify the content of documents that are only referenced by the processes.

## Executive conclusion

L03000 is structurally broader and more integrated than the former DDQ process. It explicitly includes RAM in requirements capture and concept/architecture decisions, calls out reliability engineering and prediction in qualification, and strengthens lifecycle topics such as obsolescence, component availability and maintainability. It also improves generic traceability from requirements through verification evidence.

However, RAM is still mainly mentioned as a discipline or design consideration. The process does not establish a complete, auditable RAM management chain from targets to allocation, analysis, design decisions, verification, acceptance, operation and feedback. The former process at least named the RAMT Instruction and required engineering plans to include RAMT; L03000 currently contains no assigned RAM reference document and no explicit RAM role or RAM deliverable set.

**Recommendation:** accept the integrated L03000 structure only after adding a mandatory RAM control block, minimum RAM outputs, RAM ownership in the R.A.C.I., and RAM-specific transition/KPI criteria. These additions can remain generic enough for project tailoring while preventing RAM activities from being silently omitted.

## Main changes with RAM relevance

| Topic | Former 06.1 DDQ | New L03000 | RAM assessment |
| --- | --- | --- | --- |
| Requirements | Requirements were formalised through SRR and subsequent design reviews; RAMT was referenced in engineering planning material. | RAM is explicitly listed among functional, non-functional, safety, quality, cybersecurity, environmental and regulatory requirements. | **Improved visibility**, but no explicit RAM target hierarchy, allocation, assumptions or acceptance-criteria control is stated. |
| Architecture and design | Architecture, design, PDR and CDR provided formal review points. | Concept trade-offs, high-level architecture, interfaces, design justification and LCC considerations are integrated across the lifecycle. | **Improved integration**, but RAM trade-offs and required RAM analysis evidence are not defined. |
| Reliability | Qualification included reliability engineering and prediction as an industrialisation interface. | Reliability engineering and prediction are explicitly included in product qualification coordination. | **Retained/improved**, but method, data source, prediction baseline, confidence level and acceptance use are unspecified. |
| Maintainability and availability | No strong standalone RAM work-product chain is visible in the extracted process; process gates provided control points. | Obsolescence addresses maintainability, component availability and long-term availability; sustainability includes repairability and modularity. | **Partly improved**, but maintainability demonstration, restoration/repair assumptions and availability model are absent. |
| Verification and qualification | TRR, TQR and FQR created explicit readiness, qualification and acceptance gates. | Integration, verification, validation and qualification are continuous and evidence is consolidated through traceability. | **More flexible**, but RAM-specific entry/exit criteria and evidence are no longer explicit. |
| Lifecycle feedback | The former process included engineering-discipline/value-creation controls and named RAMT instruction material. | L03000 is lifecycle-oriented and points to L03001 KPIs, but no explicit FRACAS or operational RAM feedback loop is stated. | **Potential regression** unless the feedback/data loop is added or clearly delegated. |
| Roles and references | RAMT appears in engineering plans and a RAMT Instruction is listed. | Generic Project Engineer/Solution Development Team responsibilities are defined; activity references are repeatedly marked `to be assigned`. | **Gap**: RAM authority, competence, independence and reference documents are not controlled. |
| Tailoring | The former gated process made the applicable reviews and activities visible. | Tailoring may reduce/combine activities and merge deliverables while preserving traceability, verification and safety principles. | **Risk**: RAM minimum activities are not protected from inappropriate tailoring. |

## Findings and required improvements

### RAM-01 - Missing RAM management and planning baseline

Priority: **High**

L03000 requires RAM requirements to be identified and discipline-specific plans to be maintained, but does not require a RAM plan or define its minimum content. This leaves targets, assumptions, lifecycle profile, responsibilities, methods, data sources, analyses, reviews and acceptance evidence dependent on project interpretation.

**Add a requirement such as:**

> For each Solution where RAM requirements or RAM-related risks apply, establish and maintain a RAM plan, or an approved integrated plan section, covering the RAM targets, lifecycle and operating assumptions, allocation approach, analysis methods, data sources, responsibilities, milestones, verification and acceptance evidence, and management of deviations and residual risks.

### RAM-02 - No explicit RAM allocation and flow-down

Priority: **High**

The requirements activity does not state that system RAM targets shall be decomposed and allocated to Solution Items, interfaces, operating modes or maintainability resources. A generic RTM alone does not demonstrate that a top-level RAM target is achievable.

**Add a requirement such as:**

> RAM requirements and targets shall be flowed down and allocated to the applicable Solution Items, functions, interfaces and operational scenarios. Allocation assumptions, margins, dependencies and residual gaps shall be recorded and controlled through the requirements and configuration baselines.

### RAM-03 - RAM analysis methods and minimum work products are unspecified

Priority: **High**

The new process names reliability prediction but does not identify when RAM analyses are required. There is no explicit reference to reliability prediction, FMEA/FMECA, fault-tree or reliability block analysis where applicable, maintainability analysis, availability modelling, common-cause/dependency treatment, or criticality analysis.

**Add a minimum, applicability-based output list:**

- reliability prediction or other justified reliability assessment;
- FMEA/FMECA and criticality assessment where relevant;
- maintainability analysis, including maintenance concept, restoration assumptions and support resources;
- availability model or equivalent quantitative assessment where an availability target applies;
- RAM risk, assumption and action log;
- controlled RAM conclusions and design trade-off records.

The process should state that the selected method, model boundary, assumptions, data quality, confidence/uncertainty and exclusions are documented and approved.

### RAM-04 - RAM verification and acceptance criteria are not explicit

Priority: **High**

L03000 requires verification evidence generally, and it mentions reliability qualification, but it does not require each RAM requirement to have a defined verification method, sample/population basis, test duration, calculation rule, confidence level or acceptance threshold. The removal of explicit TQR/FQR RAM checkpoints increases the need for clear RAM entry/exit criteria.

**Add a requirement such as:**

> Each RAM requirement shall have an approved verification method and acceptance criterion. RAM verification shall use analysis, inspection, demonstration, test, operational evidence or a justified combination. The evidence shall identify the configuration, data period, sample/population, calculation method, confidence/uncertainty, deviations and residual risk.

Add RAM-specific readiness and completion checks to the applicable lifecycle milestone or to the L03000 transition rules, including review of open RAM actions and target compliance.

### RAM-05 - Maintainability and availability are only implicit

Priority: **High**

Obsolescence and sustainability text refers to maintainability, repairability and component availability, but this is not equivalent to controlling maintainability or operational availability. The process does not explicitly cover maintainability targets, maintenance intervals, access/replaceability, diagnostic coverage, spares, repair time, logistic delays, degraded modes, restoration strategy or availability allocation.

**Improve the design and qualification activity** to require these topics when applicable, with explicit links to the maintenance concept, support solution, LCC and operational scenarios.

### RAM-06 - No FRACAS and lifecycle RAM feedback loop

Priority: **High**

The extracted L03000 text does not explicitly require failure reporting, analysis and corrective action, nor the use of historical/field data to update predictions, FMEA/FMECA, RAM models, requirements, obsolescence risk or acceptance evidence. This is a material lifecycle-control gap for a process titled Design, Develop and Qualify the Solution.

**Add a requirement such as:**

> Establish and maintain a controlled RAM problem-reporting and corrective-action feedback loop. Relevant failure, test, supplier, maintenance and operational data shall be classified, analysed for trends and recurrent causes, and used to update RAM analyses, requirements, design actions, predictions, verification evidence and lessons learned.

The process should identify the interface with the corporate FRACAS process and define the handover point from development into service/maintenance activities.

### RAM-07 - RAM responsibility and competence are not visible in the R.A.C.I

Priority: **High**

The new process identifies the Project Engineer, Solution Development Team and Heads of Engineering Disciplines, but the extracted R.A.C.I. does not visibly identify a RAM authority or RAM engineering role. Generic accountability can result in RAM tasks being assigned without the required competence or independence.

**Improve the R.A.C.I.** by naming the RAM Engineer/RAM Manager (or approved equivalent) and assigning responsibility or accountability for RAM planning, requirements, allocation, analyses, reviews, verification evidence, deviations and lifecycle feedback. Define required competence and the independence of RAM assessment where contractual or safety rules require it.

### RAM-08 - References and transition rules are incomplete

Priority: **High**

The new document repeatedly contains `Reference L2 docs: to be assigned`. The former process at least listed the RAMT Instruction. Until the applicable RAM procedure, templates, standards and transition rules are assigned, the process is not sufficiently implementable or auditable.

**Complete the reference set**, at minimum covering the applicable RAM management instruction, RAM prediction/data guidance, FMEA/FMECA method, availability/maintainability analysis, FRACAS interface, RAM evidence/verification template and relevant EN 50126/EN 50128/EN 50129/EN 50716 interfaces as applicable to the Solution.

### RAM-09 - Tailoring needs protected RAM minimums

Priority: **Medium**

L03000 allows reduction or combination of lifecycle activities and merging of deliverables. It states that traceability, verification and safety principles are preserved, but RAM is not named in that protection clause.

**Add RAM to the protected principles** and require tailoring records to state:

- which RAM activities and deliverables are applicable or not applicable;
- the technical justification for exclusions or combinations;
- who approved the decision;
- how RAM targets and acceptance evidence remain covered.

### RAM-10 - KPIs do not yet demonstrate RAM performance

Priority: **Medium**

L03000 delegates measures to `G-KPI L03001`, but the process does not identify RAM KPI expectations. Process efficiency measures alone will not show whether RAM objectives are being achieved.

**Add RAM-related KPI candidates**, tailored to project applicability, such as:

- percentage of RAM requirements with approved allocation and verification method;
- RAM analysis and evidence completion at each milestone;
- predicted/assessed target compliance and open RAM gap count;
- overdue RAM actions and residual RAM risk;
- failure report closure and recurrence rate;
- maintainability/availability test or demonstration status;
- quality and currency of RAM data used in predictions/models.

## Suggested minimum RAM lifecycle outputs

| Lifecycle point | Minimum RAM output or decision record |
| --- | --- |
| Bid/context and planning | RAM applicability assessment, RAM assumptions, initial targets/constraints, RAM role, RAM plan and applicable methods |
| Requirements and architecture | RAM requirement hierarchy, allocation, margins, operational profile, maintainability/support concept, RAM trade-off records |
| Design and development | Reliability prediction, FMEA/FMECA or justified alternative, maintainability and availability analyses, RAM risk/action log, supplier RAM data |
| Integration and verification | RAM verification matrix, approved models/calculations, test and analysis results, configuration/data quality record, deviation and residual-risk assessment |
| Qualification and acceptance | consolidated RAM compliance statement, open-action disposition, target compliance and acceptance recommendation |
| Handover and lifecycle feedback | baseline RAM data, maintenance/monitoring assumptions, FRACAS handover, field-data update rules and lessons learned |

## Overall disposition

**Major revision required for RAM assurance before final approval.** The process architecture is suitable and several RAM touchpoints are stronger than in the former process. The missing items are mainly control specificity rather than a need for another standalone RAM process. Adding the RAM control block, minimum outputs, R.A.C.I. ownership, references, protected tailoring rules and RAM KPIs should preserve the benefits of L03000 while preventing loss of RAM assurance at the transition from the former gated process.
