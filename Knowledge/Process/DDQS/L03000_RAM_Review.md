# L03000 DDQS Process - RAM Review

## Scope and basis

This review compares `G-PRD_L03000_00d09_EN_for_final_review_cleaned.docx` with `06.1 DDQ - Design  Develop and Qualify the Solution.pdf` (release L.2.2.0), with focus on reliability, availability, maintainability and lifecycle RAM control.

The comparison is based on the process text, its named activities, references, transition/KPI pointers, and R.A.C.I./input-output sections available in the two files. It does not verify the content of documents that are only referenced by the processes. The review recognises that L03000 is an overall development process and is not intended to reproduce the detailed RAMS methods and work instructions owned by the dedicated SRS RAMS process.

## Executive conclusion

L03000 is structurally broader and more integrated than the former DDQ process. It explicitly includes RAM in requirements capture and concept/architecture decisions, calls out reliability engineering and prediction in qualification, and strengthens lifecycle topics such as obsolescence, component availability and maintainability. It also improves generic traceability from requirements through verification evidence.

However, RAM is still mainly mentioned as a discipline or design consideration. For an overall process, the key gap is not missing detailed RAM methods; those belong in the dedicated SRS RAMS process. The gap is that L03000 does not consistently define the interface to that process, the accountable role, the mandatory RAM Plan, the required RAM inputs/outputs and the evidence expected at development milestones. The former process at least named the RAMT Instruction and required engineering plans to include RAMT; L03000 currently contains no assigned RAM reference document and no explicit RAM role or RAM deliverable set.

**Recommendation:** retain the integrated L03000 structure and add targeted RAMS interface controls: the mandatory RAM Plan, RAM ownership in the R.A.C.I., references to the dedicated SRS RAMS process, high-level RAM inputs/outputs, and RAM-related transition/KPI criteria. Detailed RAM activities and methods should remain in the dedicated RAMS process rather than being duplicated here.

## Grave comments only

If the review is restricted to grave comments, raise the following three comments. They concern RAMS accountability, process usability and protection against loss of RAM control. The existing requirement to develop and maintain discipline-specific plans can cover the RAM Plan; do not raise the absence of a separate explicit RAM Plan sentence as a grave comment. Do not raise the detailed RAM method, FRACAS mechanics or KPI suggestions as grave comments against L03000; those belong in the dedicated SRS RAMS and FRACAS processes.

### Confirmation C-01 - RAM Plan coverage within discipline-specific planning

**Location:** DDQ-02 Plan and Coordinate Solution Development, specifically the existing requirement to develop and maintain discipline-specific plans; cross-check Activities and Deliverables and INPUT AND OUTPUT DETAILS.

The existing discipline-specific planning requirement can cover the RAM Plan and does not need to be duplicated with an explicit RAM sentence in L03000. However, the `INPUT AND OUTPUT DETAILS` section should identify the resulting discipline plan or integrated plan as a controlled output. If the RAM Plan is not visible there, the process has a traceability gap between the planning activity and its required deliverable. The review comment should request confirmation that the applicable RAM Plan, standalone or integrated, is captured through the discipline-plan structure and output list, and remains maintained throughout the lifecycle in accordance with EN 50126-1. Here, “to be confirmed” refers only to the document location, owner and reference in the supporting-plan set; it does not mean that the RAM Plan is optional.

This is a **confirmation/traceability point**, not a grave gap in the L03000 wording unless the process transition rules or project plan template fail to provide that coverage.

### G-01 - RAMS accountability and interfaces

**Location:** R.A.C.I. section, with supporting wording in DDQ-02 and INPUT AND OUTPUT DETAILS.

L03000 shall identify the accountable RAMS role and the interfaces between the Project RAM Manager, Safety Manager, SRS RAMS Manager and RAM/Safety work-package roles, where applicable. The process shall state who owns the integrated RAMS status, RAM Plan, requirements interface, evidence handover and escalation of residual RAM risks.

### G-02 - Mandatory interface to the dedicated SRS RAMS process

**Location:** DOCUMENTS TREE and the `Reference L2 docs: to be assigned` entries for DDQ-02, DDQ-03, DDQ-05 and DDQ-07; supporting wording in DDQ-05 and DDQ-07.

L03000 shall reference the dedicated SRS RAMS process as the controlling process for detailed RAM activities and methods. It shall define the required interface outputs at a high level, including RAM applicability/status, required RAMS deliverables, open actions, deviations, compliance status and evidence handover. Without this reference, the overall process does not establish how RAM assurance is performed or integrated into development acceptance.

### G-03 - Tailoring shall not remove mandatory plans and deliverables

**Location:** TAILORING GUIDELINES, specifically **Project Tailoring Documentation and Approval**.

**Suggested single bullet:**

> Tailoring shall comply with applicable CENELEC standards and contractual requirements and shall identify mandatory plans/deliverables that shall not be omitted, including the RAM Plan and Safety Plan where applicable; any reduction or combination shall be justified and approved.

## Main changes with RAM relevance

| Topic | Former 06.1 DDQ | New L03000 | RAM assessment |
| --- | --- | --- | --- |
| Requirements | Requirements were formalised through SRR and subsequent design reviews; RAMT was referenced in engineering planning material. | RAM is explicitly listed among functional, non-functional, safety, quality, cybersecurity, environmental and regulatory requirements. | **Improved visibility**, but no explicit RAM target hierarchy, allocation, assumptions or acceptance-criteria control is stated. |
| Architecture and design | Architecture, design, PDR and CDR provided formal review points. | Concept trade-offs, high-level architecture, interfaces, design justification and LCC considerations are integrated across the lifecycle. | **Improved integration**, but RAM trade-offs and required RAM analysis evidence are not defined. |
| Reliability | Qualification included reliability engineering and prediction as an industrialisation interface. | Reliability engineering and prediction are explicitly included in product qualification coordination. | **Retained/improved**; L03000 should reference the dedicated RAMS process for method and evidence detail. |
| Maintainability and availability | No strong standalone RAM work-product chain is visible in the extracted process; process gates provided control points. | Obsolescence addresses maintainability, component availability and long-term availability; sustainability includes repairability and modularity. | **Partly improved**, but maintainability demonstration, restoration/repair assumptions and availability model are absent. |
| Verification and qualification | TRR, TQR and FQR created explicit readiness, qualification and acceptance gates. | Integration, verification, validation and qualification are continuous and evidence is consolidated through traceability. | **More flexible**; L03000 should define the RAMS evidence interface and defer detailed RAM verification rules to the dedicated RAMS process. |
| Lifecycle feedback | The former process included engineering-discipline/value-creation controls and named RAMT instruction material. | L03000 is lifecycle-oriented and points to L03001 KPIs, but no explicit FRACAS or operational RAM feedback loop is stated. | **Potential regression** unless the feedback/data loop is added or clearly delegated. |
| Roles and references | RAMT appears in engineering plans and a RAMT Instruction is listed. | Generic Project Engineer/Solution Development Team responsibilities are defined; activity references are repeatedly marked `to be assigned`. | **Gap**: RAM authority, competence, independence and reference documents are not controlled. |
| Tailoring | The former gated process made the applicable reviews and activities visible. | Tailoring may reduce/combine activities and merge deliverables while preserving traceability, verification and safety principles. | **Clarification required**: the RAM Plan remains mandatory; L03000 should explicitly protect it and make tailoring of the remaining RAM activities justified and traceable. |

## Where to raise the comments in L03000

Use the following locations in the new process when entering review comments. Where a finding affects more than one control point, raise it at the first listed location and cross-reference the other locations in the same comment.

| Review finding | Exact L03000 location for the comment | Required linked update |
| --- | --- | --- |
| RAM-01 RAM plan and planning baseline | **DDQ-02 Plan and Coordinate Solution Development**, at the existing requirement for discipline-specific plans; cross-check **Activities and Deliverables** and **INPUT AND OUTPUT DETAILS**. | Confirm that the applicable RAM Plan is covered by the discipline-plan structure and maintained through the lifecycle; no separate RAM sentence is required in L03000. |
| RAM-02 RAM allocation and flow-down | **DDQ-03 Capture and Manage Requirements**, immediately after “Identify and formalise ... RAM ... requirements”; cross-reference **DDQ-05 Design Solution** for allocation to Solution Items. | Add target hierarchy, allocation, margins, assumptions, interfaces and residual-gap control to the requirements and configuration baselines. |
| RAM-03 RAM analyses and work products | **DDQ-05 Design Solution**, after “Perform analyses and trade-offs supporting design decisions”; cross-reference **DDQ-07 Integrate, Verify & Validate Solution**. | Reference the dedicated SRS RAMS process for the applicable RAM methods and detailed work products; keep L03000 focused on applicability, planning and inputs/outputs. |
| RAM-04 RAM verification and acceptance | **DDQ-07 Integrate, Verify & Validate Solution**, after the activities for verification methods, evidence and qualification; also in **G-TRN L03000 Design, Develop and Qualify Solution Transition Rules**. | Define the required RAMS evidence interface and milestone status; reference the dedicated SRS RAMS process for detailed RAM verification rules. |
| RAM-05 Maintainability and availability | **DDQ-05 Design Solution**, after the design trade-off activities; cross-reference **DDQ-09 Manage Obsolescence within Solution Development** for lifecycle availability and maintainability. | Require maintainability/availability applicability and required inputs to be addressed, while referring detailed analyses and acceptance rules to the dedicated SRS RAMS process. |
| RAM-06 FRACAS and lifecycle feedback | **DDQ-07 Integrate, Verify & Validate Solution**, after “Identify issues ...”; cross-reference **DDQ-13 Manage Engineering Discipline** and **INPUT AND OUTPUT DETAILS** for handover. | Define the interface with the dedicated FRACAS/RAMS process and the required handover outputs; do not duplicate the FRACAS procedure in L03000. |
| RAM-07 RAM role and competence | **R.A.C.I.** section for the full L03000 process. | Add RAM Engineer/RAM Manager (or approved equivalent) and assign responsibility/accountability for planning, analyses, evidence, deviations and feedback. |
| RAM-08 References | **DOCUMENTS TREE** and each activity’s `Reference L2 docs: to be assigned` line, especially DDQ-02, DDQ-03, DDQ-05 and DDQ-07. | Assign/reference the dedicated SRS RAMS process and the FRACAS process; detailed prediction, FMEA/FMECA, availability and maintainability methods should remain there. |
| RAM-09 Tailoring | **TAILORING GUIDELINES**, under “Tailoring of the standard process shall be justified and traceable”; cross-reference **Activities and Deliverables**. | State that a RAM Plan is mandatory in standalone or integrated form. Require applicability, exclusion/combination justification, approval and residual coverage for other RAM activities. |
| RAM-10 RAM KPIs | **MEASURES** section and **G-KPI L03001 Design, Develop and Qualify Solution KPIs** in the DOCUMENTS TREE. | Add RAM completeness, target compliance, open-gap, action closure, failure recurrence and data-quality KPIs. |

## Findings and required improvements

### RAM-01 - RAM Plan coverage in discipline-specific planning

Priority: **Medium**

L03000 already requires discipline-specific plans to be developed and maintained. That generic requirement can cover the RAM Plan, standalone or integrated, and no separate RAM sentence is necessary in the overall process. The review point is to confirm that the process transition rules, plan template or project implementation identifies this coverage and maintains the plan throughout the lifecycle in accordance with EN 50126-1.

**Add a confirmation to the implementation or transition material such as:**

> Where RAM requirements or RAM-related risks apply, the applicable discipline-specific plan shall identify and maintain the RAM Plan or approved integrated plan section and its interface with the dedicated SRS RAMS process. The plan reference, owner and location in the supporting-plan set shall be recorded, and the applicable plan shall be listed as a controlled output in INPUT AND OUTPUT DETAILS.

The plan may be proportionate to the system and project context, but its existence and continued maintenance shall not be removed by tailoring.

### RAM-02 - No explicit RAM allocation and flow-down

Priority: **High**

The requirements activity does not state that system RAM targets shall be decomposed and allocated to Solution Items, interfaces, operating modes or maintainability resources. A generic RTM alone does not demonstrate that a top-level RAM target is achievable.

**Add a requirement such as:**

> RAM requirements and targets shall be flowed down and allocated to the applicable Solution Items, functions, interfaces and operational scenarios. Allocation assumptions, margins, dependencies and residual gaps shall be recorded and controlled through the requirements and configuration baselines.

### RAM-03 - Interface to detailed RAM activities is unspecified

Priority: **Medium**

L03000 is not expected to reproduce the detailed RAMS process. However, it names reliability engineering and prediction without clearly identifying the dedicated process that defines the applicable analyses and work products. The overall process should establish the interface and applicability decision; the dedicated SRS RAMS process should define the detailed methods, model boundaries, data quality and uncertainty treatment.

**Add a process reference and high-level interface requirement such as:**

> The applicability, planning and required outputs of RAM activities shall be established in accordance with the dedicated SRS RAMS process. L03000 shall maintain the relevant interfaces, milestones, responsibilities and acceptance evidence without duplicating the detailed RAM methods.

The detailed analysis set should therefore be controlled in the dedicated RAMS process and referenced from L03000.

### RAM-04 - RAM verification interface and acceptance status are not explicit

Priority: **Medium**

L03000 requires verification evidence generally, and it mentions reliability qualification, but it does not identify the RAMS process as the owner of detailed RAM verification methods and acceptance rules. L03000 should retain the milestone interface, status and evidence handover without duplicating the detailed RAM verification procedure.

**Add an interface requirement such as:**

> RAM verification and acceptance shall be planned and performed in accordance with the dedicated SRS RAMS process. The applicable L03000 milestone shall record RAMS evidence status, open actions, deviations and the acceptance recommendation.

Add this RAMS status check to the applicable lifecycle milestone or to the L03000 transition rules.

### RAM-05 - Maintainability and availability interface is only implicit

Priority: **Medium**

Obsolescence and sustainability text refers to maintainability, repairability and component availability. L03000 should not detail the maintainability and availability methods, but it should identify when the dedicated SRS RAMS process is applicable and ensure that its outputs inform design, LCC, qualification and acceptance.

**Improve the design and qualification activity** with an interface to the dedicated SRS RAMS process and require the resulting maintainability/availability status to be considered in the maintenance concept, support solution, LCC and operational scenarios.

### RAM-06 - FRACAS and lifecycle RAM feedback interface is not explicit

Priority: **Medium**

The extracted L03000 text does not explicitly identify the dedicated FRACAS/RAMS process as the owner of failure reporting, analysis and corrective action. L03000 should define the development-process interface and handover, while the detailed FRACAS activities remain in the dedicated procedure.

**Add an interface requirement such as:**

> Relevant failure, test, supplier, maintenance and operational data shall be transferred to and managed in accordance with the dedicated FRACAS/RAMS process. Resulting actions, lessons learned and RAM performance status shall be available to L03000 design, verification and acceptance activities.

Define the interface with the corporate FRACAS process and the handover point from development into service/maintenance activities.

### RAM-07 - RAM responsibility and competence are not visible in the R.A.C.I

Priority: **High**

The new process identifies the Project Engineer, Solution Development Team and Heads of Engineering Disciplines, but the extracted R.A.C.I. does not visibly identify a RAM authority or RAM engineering role. Generic accountability can result in RAM tasks being assigned without the required competence or independence.

**Improve the R.A.C.I.** by naming the RAM Engineer/RAM Manager (or approved equivalent) and assigning responsibility or accountability for RAM planning, requirements, allocation, analyses, reviews, verification evidence, deviations and lifecycle feedback. Define required competence and the independence of RAM assessment where contractual or safety rules require it.

### RAM-08 - References and transition rules are incomplete

Priority: **High**

The new document repeatedly contains `Reference L2 docs: to be assigned`. The former process at least listed the RAMT Instruction. Until the applicable RAM procedure, templates, standards and transition rules are assigned, the process is not sufficiently implementable or auditable.

**Complete the reference set**, at minimum covering the applicable RAM management instruction, RAM prediction/data guidance, FMEA/FMECA method, availability/maintainability analysis, FRACAS interface, RAM evidence/verification template and relevant EN 50126/EN 50128/EN 50129/EN 50716 interfaces as applicable to the Solution.

### RAM-09 - Tailoring shall preserve mandatory RAM controls

Priority: **Medium**

EN 50126-1 permits tailoring to the type and size of the system, but this does not remove the requirement to establish and maintain a RAM Plan. L03000 allows reduction or combination of lifecycle activities and merging of deliverables. It states that traceability, verification and safety principles are preserved, but RAM is not named in that protection clause.

The review concern is therefore not that every RAM activity must always be performed in an identical form. The concern is that L03000 does not explicitly state that the RAM Plan is mandatory in whatever proportionate or integrated form is appropriate, nor how the remaining RAM activities are selected and justified.

**Add RAM to the protected principles** and require the tailoring rules to state that the RAM Plan shall always be established and maintained. Tailoring records should also state:

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

## Suggested minimum RAMS interface outputs

The following are high-level L03000 interface outputs. The detailed RAM analyses, methods, templates and acceptance calculations should remain controlled by the dedicated SRS RAMS process and be referenced rather than repeated here.

| Lifecycle point | Minimum RAM output or decision record |
| --- | --- |
| Bid/context and planning | RAM applicability assessment, RAM assumptions, initial targets/constraints, RAM role, RAM plan and applicable methods |
| Requirements and architecture | RAM requirement hierarchy, allocation, margins, operational profile, maintainability/support concept, RAM trade-off records |
| Design and development | RAMS process applicability/status, required RAMS outputs, RAM risks/actions, supplier RAMS inputs and design decision interfaces |
| Integration and verification | RAMS verification status, evidence handover, open actions, deviations and residual-risk status |
| Qualification and acceptance | consolidated RAMS compliance status, open-action disposition, target compliance and acceptance recommendation |
| Handover and lifecycle feedback | baseline RAM data, maintenance/monitoring assumptions, FRACAS handover, field-data update rules and lessons learned |

## Overall disposition

**Targeted clarification required for RAM assurance before final approval.** The L03000 architecture is suitable as an overall development process and should not duplicate the dedicated SRS RAMS process. It should explicitly preserve the mandatory RAM Plan, identify RAMS ownership and interfaces, reference the dedicated RAMS and FRACAS processes, define high-level inputs/outputs and milestone status, and protect these controls during tailoring. Detailed RAM activities and methods should remain in the dedicated RAMS process.
