# Railway RAM Lessons Learned Database

## Document Purpose

This document provides a reusable database of lessons learned from railway
Reliability, Availability, Maintainability and Life Cycle Cost (RAM) activities.
It is intended to support consistent planning, analysis, review, verification
and assurance across railway signalling and transportation projects.

The database is project-independent. Project-specific facts, evidence and
actions shall remain in the relevant project records. Each lesson shall be
supported by a traceable source wherever possible and shall be written so that
another project team can apply it without relying on undocumented context.

The lessons support activities performed in accordance with the applicable
project process and standards, including EN 50126-1:2017, EN 50716, EN 50129,
IEC 60812 and the approved reliability prediction method.

## Usage Guidelines

### Recording a Lesson

- Record a lesson after a significant review, calculation, failure
 investigation, tender, supplier assessment, verification activity or design
 decision.
- State the observed situation separately from the lesson and the recommended
 action.
- Record one clear lesson per entry. Split unrelated findings into separate
 entries.
- Identify whether the lesson is confirmed by project evidence or remains an
 engineering recommendation.
- Remove confidential customer, supplier and project information before adding
 a lesson to this project-independent database.
- Reference the source document, review record, FRACAS record or calculation
 whenever it is available.

### Applying a Lesson

- Review this database during RAM planning, requirements reviews, tender
 preparation, design reviews and verification planning.
- Check the applicability of each lesson against the system scope, lifecycle
 phase, architecture, operational concept and contractual requirements.
- Do not copy a recommendation without checking its assumptions and available
 evidence.
- Record the adopted action, rejected action or justified non-applicability in
 the project record.
- Confirm that actions are allocated to an owner and closed with objective
 evidence.

### Maintaining the Database

- Use a unique lesson identifier and retain the original lesson history when
 an entry is revised.
- Review lessons for technical accuracy, clarity, duplication and continued
 applicability before approval.
- Mark superseded lessons and link to the replacement entry rather than
 deleting useful history.
- Keep standards references and company process references current.
- Protect project-sensitive information and use generic wording in this
 repository.

## Lesson Template

Copy the following template for each new lesson. Replace all placeholder text
with verified information and remove fields that are genuinely not applicable.

```markdown
### LL-XXX - Short descriptive title

**Status:** Proposed / Approved / Superseded
**Domain:** RAM Planning / Requirements / Reliability / Availability /
FMEA / FRACAS / Supplier Data / Tendering / Verification / Design Review
**Lifecycle phase:** Concept / System definition / Design / Implementation /
Integration / Validation / Operation / Maintenance / Disposal
**Source:** Project, document, review, calculation or FRACAS reference
**Date recorded:** YYYY-MM-DD
**Owner:** Responsible role or function

**Context:**
Describe the system, activity, decision or event that generated the lesson.

**Observation:**
State what happened or what was identified, using evidence where available.

**Lesson learned:**
State the reusable engineering insight in one or two clear sentences.

**RAM impact:**
Describe the effect on reliability, availability, maintainability, LCC,
requirements compliance, evidence or assurance.

**Recommendation:**
State the action that future projects should take.

**Required evidence:**
List the records, calculations, reviews, tests or approvals needed to confirm
application of the lesson.

**Applicability and limitations:**
State where the lesson applies, the assumptions involved and any conditions
that require a project-specific assessment.

**Keywords:**
List searchable terms.
```

## Example Lessons

The following entries are illustrative examples. They demonstrate the expected
level of detail and shall be replaced or supplemented with verified project
evidence before being treated as company experience.

### LL-001 - Establish RAM Planning Inputs Before Baseline Approval

**Status:** Approved example
**Domain:** RAM Planning
**Lifecycle phase:** Concept and system definition
**Source:** Illustrative planning review record
**Owner:** Project RAM Manager

**Context:**
The initial RAM Plan was prepared before the operational concept, system
boundaries, RAM targets, maintainability concept and contractual assumptions
were fully baselined.

**Observation:**
Several activities had to be re-planned when the system scope and operational
assumptions were clarified. The change affected responsibility allocation,
analysis inputs and the planned evidence set.

**Lesson learned:**
The RAM Plan is only a reliable control document when its inputs, interfaces,
assumptions, deliverables, responsibilities and approval points are defined
before the plan is baselined.

**RAM impact:**
Weak planning inputs can create gaps in RAM evidence, duplicated analysis,
late resource demand and unclear ownership of residual RAM risks.

**Recommendation:**
Create an input and assumption register before approving the RAM Plan. Link
each planned activity to an output, owner, review point and verification
record, and update the plan through controlled lifecycle changes.

**Required evidence:**
Approved RAM Plan, RAM input register, responsibility matrix, assumptions log
and plan review record.

**Applicability and limitations:**
Apply to all projects. Tailor the depth of planning to the system size and
change scope, but retain clear RAM ownership and traceability.

**Keywords:**
RAM Plan, assumptions, scope, responsibilities, lifecycle planning

### LL-002 - Make RAM Requirements Quantitative and Verifiable

**Status:** Approved example
**Domain:** Requirements
**Lifecycle phase:** System definition and requirements baseline
**Source:** Illustrative requirements review record
**Owner:** Requirements Manager and Project RAM Manager

**Context:**
RAM requirements used terms such as high reliability, rapid restoration and
minimal service disruption without defined measures, conditions or acceptance
criteria.

**Observation:**
Different teams interpreted the same requirement differently, and the planned
verification method could not be selected consistently.

**Lesson learned:**
A RAM requirement must define the measure, operating conditions, boundary,
calculation or test method, data requirements and acceptance criterion.

**RAM impact:**
Ambiguous requirements prevent meaningful allocation, prediction, validation
and contract compliance assessment.

**Recommendation:**
Review every RAM requirement for clarity, completeness, consistency,
traceability, testability and verifiability. Link it to the applicable system
function, assumption, allocated target and verification evidence.

**Required evidence:**
Requirements review record, RAM requirements specification, allocation table,
verification cross-reference and approved assumptions.

**Applicability and limitations:**
Apply to quantitative and qualitative RAM requirements. The appropriate
measure depends on the operational concept and contractual framework.

**Keywords:**
RAM requirements, allocation, verification, acceptance criteria, traceability

### LL-003 - Baseline Reliability Prediction Inputs and Method

**Status:** Approved example
**Domain:** Reliability Prediction
**Lifecycle phase:** Design and detailed analysis
**Source:** Illustrative reliability prediction review
**Owner:** Reliability Engineer

**Context:**
A reliability prediction was produced with incomplete part data, unclear
environmental conditions and mixed assumptions from more than one prediction
method.

**Observation:**
The result could not be reproduced independently, and changes in part quality,
temperature, duty cycle and mission profile were not visible in the report.

**Lesson learned:**
The prediction result is only as credible as its controlled input data,
selected methodology, model boundary and documented assumptions.

**RAM impact:**
Uncontrolled inputs can hide the principal contributors, distort allocated
targets and weaken design decisions based on FIT or MTBF results.

**Recommendation:**
Define the prediction method before calculation. Baseline part data,
environment, duty cycle, mission profile, quality level, derating and model
boundary, then perform sensitivity analysis on the main contributors.

**Required evidence:**
Approved method statement, input data register, calculation model, assumptions,
source data, contributor ranking, sensitivity analysis and review record.

**Applicability and limitations:**
Use the company-approved method first. Where a different method is required,
document the rationale and do not combine results without an engineering basis.

**Keywords:**
Reliability prediction, FIDES, IEC 61709, SN 29500, FIT, MTBF, sensitivity

### LL-004 - Separate Failure and Restoration Assumptions in Availability Models

**Status:** Approved example
**Domain:** Availability
**Lifecycle phase:** System definition, design and validation
**Source:** Illustrative availability model review
**Owner:** RAM Engineer

**Context:**
An availability calculation used MTBF and MTTR values but did not distinguish
inherent, achieved and operational availability or document logistics and
service-restoration assumptions.

**Observation:**
The reported result appeared precise, but the effect of detection delay,
spares, access time, repair resources, testing and operational restrictions
could not be assessed.

**Lesson learned:**
An availability result is meaningful only when its availability definition,
architecture, failure assumptions, restoration assumptions and time boundaries
are explicit.

**RAM impact:**
Unclear definitions can lead to incorrect target comparisons and an unrealistic
view of service performance.

**Recommendation:**
State the availability measure and model boundary. Separate failure rate,
detection, repair, logistics, preventive maintenance, restoration and
operational downtime inputs, and test the sensitivity of the result.

**Required evidence:**
Reliability block diagram, model description, MTBF and MTTR sources,
downtime assumptions, maintenance concept, calculation and independent review.

**Applicability and limitations:**
Tailor the model to the contractual availability definition and operational
concept. Do not infer operational availability from inherent availability alone.

**Keywords:**
Availability, MTBF, MTTR, MDT, downtime, RBD, maintenance concept

### LL-005 - Link FMEA Failure Modes to Detection and Higher-Level Effects

**Status:** Approved example
**Domain:** FMEA
**Lifecycle phase:** Design and verification planning
**Source:** Illustrative FMEA workshop review
**Owner:** FMEA Moderator

**Context:**
An FMEA listed component failures but combined several failure modes in one row
and did not consistently record detection, local effect, higher-level effect or
end effect.

**Observation:**
The analysis could not demonstrate complete coverage of failure behaviour or
provide a clear basis for diagnostic and verification requirements.

**Lesson learned:**
Each function and failure mode needs a traceable cause-to-effect chain, an
identified detection method and a defined mitigation or recommended action.

**RAM impact:**
Incomplete failure-mode analysis can hide contributors to service failure,
unavailable states, maintenance demand and verification gaps.

**Recommendation:**
Use one row per function and failure mode. Record cause, local effect,
higher-level effect, end effect, detection, mitigation, assumptions and action
owner, then link significant results to design and test records.

**Required evidence:**
FMEA, item and function list, interface assumptions, workshop attendance,
review record, action log and traceability to requirements or tests.

**Applicability and limitations:**
Apply IEC 60812 principles and the approved project method. The level of detail
shall reflect the analysis boundary and the intended use of the FMEA.

**Keywords:**
FMEA, failure mode, detection, mitigation, effect, IEC 60812

### LL-006 - Integrate FRACAS With RAM Analysis and Design Change Control

**Status:** Approved example
**Domain:** FRACAS
**Lifecycle phase:** Integration, validation and operation
**Source:** Illustrative failure investigation review
**Owner:** FRACAS Manager

**Context:**
Failure records were closed after a local repair without checking whether the
failure affected RAM predictions, FMEA assumptions, requirements or design
changes.

**Observation:**
Recurring symptoms were recorded in different systems, and lessons from field
failures were not consistently fed back into engineering analyses.

**Lesson learned:**
FRACAS is effective when failure data is classified consistently and the
investigation outcome is connected to corrective action, RAM evidence and
controlled design change.

**RAM impact:**
Weak feedback delays reliability growth, hides recurring failure mechanisms and
leaves obsolete assumptions in RAM analyses.

**Recommendation:**
Define interfaces between FRACAS, FMEA, reliability prediction, availability
analysis, requirements management and configuration control. Close an issue
only after the technical cause, action effectiveness and required analysis
updates have been assessed.

**Required evidence:**
FRACAS record, failure data, root-cause analysis, corrective action, recurrence
check, updated RAM analysis where applicable and change-control record.

**Applicability and limitations:**
Apply to development, integration, validation and in-service failures. Scale
the investigation to the severity, recurrence risk and available evidence.

**Keywords:**
FRACAS, reliability growth, root cause, corrective action, feedback loop

### LL-007 - Define Supplier RAM Data Requirements Before Contract Award

**Status:** Approved example
**Domain:** Supplier Data
**Lifecycle phase:** Tendering and procurement
**Source:** Illustrative supplier data review
**Owner:** Supplier RAM Interface Manager

**Context:**
Supplier requests asked for reliability and maintainability information without
defining the required format, boundary, operating conditions, evidence or due
date.

**Observation:**
Supplier submissions were difficult to compare and contained inconsistent
definitions, assumptions and levels of supporting evidence.

**Lesson learned:**
Supplier RAM data must be specified as a controlled deliverable with common
definitions, input conditions, acceptance criteria and traceability.

**RAM impact:**
Poorly defined supplier data can prevent allocation assessment, integration of
predictions and confirmation of system-level RAM compliance.

**Recommendation:**
Issue a supplier RAM data requirement before contract award. Define the data
items, templates, units, model boundary, environmental and duty assumptions,
source evidence, review gates, configuration status and non-conformance process.

**Required evidence:**
Supplier data requirements, tender response template, agreed data dictionary,
supplier deliverable schedule, review comments and approved data submissions.

**Applicability and limitations:**
Tailor the data set to supplier scope and criticality. Contractual acceptance
criteria shall be agreed with the responsible project functions.

**Keywords:**
Supplier data, procurement, RAM deliverables, data dictionary, allocation

### LL-008 - Make Tender RAM Commitments Traceable to Evidence

**Status:** Approved example
**Domain:** Tendering
**Lifecycle phase:** Bid preparation and contract clarification
**Source:** Illustrative tender review
**Owner:** Bid RAM Manager

**Context:**
Tender responses stated RAM performance commitments without identifying the
assumptions, exclusions, verification method, evidence source or responsible
delivery team.

**Observation:**
Commitments were interpreted as firm requirements even where the supporting
design, operational data or supplier evidence was not yet available.

**Lesson learned:**
Every tender RAM commitment must be traceable to an assumption, calculation,
design provision, verification method and accountable owner.

**RAM impact:**
Unqualified commitments create delivery risk, commercial exposure and late
discovery of gaps between bid assumptions and the implemented system.

**Recommendation:**
Maintain a tender RAM compliance matrix. Classify each response as confirmed,
assumption-based, deviation, clarification required or not applicable, and
identify the evidence planned for contract execution.

**Required evidence:**
Tender compliance matrix, assumptions and deviations register, clarification
log, supporting calculations, approval record and handover to the project RAM
team.

**Applicability and limitations:**
Use the customer and contract definitions as the controlling basis. Do not
replace a contractual requirement with an internal target without approval.

**Keywords:**
Tendering, RAM commitment, compliance matrix, assumptions, deviations

### LL-009 - Define Verification Evidence When RAM Analyses Are Planned

**Status:** Approved example
**Domain:** Verification
**Lifecycle phase:** Requirements, design, integration and validation
**Source:** Illustrative verification planning review
**Owner:** RAM Verification Lead

**Context:**
RAM analyses were listed in the project plan, but the verification method,
acceptance criteria, required data and independent review expectations were not
defined at the time the requirements were baselined.

**Observation:**
The team completed calculations but later found that the available evidence did
not demonstrate compliance with the intended requirement or operating condition.

**Lesson learned:**
RAM verification must be planned with the requirement and analysis, not added
after the calculation is complete.

**RAM impact:**
Late definition of evidence can cause re-analysis, delayed acceptance and
unresolved disagreement about the validity of RAM results.

**Recommendation:**
For each RAM requirement, define the verification method, evidence owner,
acceptance criteria, input data, configuration baseline, review independence and
record to be retained. Update the verification matrix when assumptions change.

**Required evidence:**
RAM verification matrix, approved calculation or test procedure, input data,
configuration record, review report, result and acceptance record.

**Applicability and limitations:**
Select analysis, inspection, test or demonstration according to the requirement
and applicable process. Evidence must be proportionate but sufficient to support
the intended claim.

**Keywords:**
Verification, evidence, acceptance criteria, RAM requirements, configuration

### LL-010 - Use Design Reviews to Close RAM Interface Decisions

**Status:** Approved example
**Domain:** Design Reviews
**Lifecycle phase:** Preliminary and detailed design
**Source:** Illustrative design review record
**Owner:** Design Authority and Project RAM Manager

**Context:**
Design reviews considered functional and safety topics but did not consistently
record decisions affecting failure containment, diagnostics, maintenance access,
repair strategy, redundancy or RAM evidence.

**Observation:**
RAM assumptions remained open after design baseline approval, and later teams
had to reconstruct why a design choice had been made.

**Lesson learned:**
Design reviews are a control point for confirming that RAM assumptions and
allocations are implemented in the design and supported by objective evidence.

**RAM impact:**
Unresolved RAM interfaces can create hidden common-cause risks, maintenance
constraints, availability losses and evidence gaps.

**Recommendation:**
Include a RAM review checklist and decision log in each applicable design
review.
Track open RAM actions to an owner and closure criterion, and confirm updates to
the RAM Plan, FMEA, reliability model, availability model and verification
matrix before the design baseline is approved.

**Required evidence:**
Design review agenda, RAM checklist, decision and action log, updated analyses,
interface records, approval record and evidence of action closure.

**Applicability and limitations:**
Apply at design gates appropriate to the project lifecycle. The review shall
include the disciplines needed to resolve the identified RAM interfaces.

**Keywords:**
Design review, RAM assumptions, diagnostics, maintainability, action closure

## Review and Approval Record

Use this record to control changes to the database itself.

| Version | Date | Description of change | Author | Reviewer | Approval status |
| --- | --- | --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | Initial reusable lessons database | RAM Engineering | RAM Assurance | Draft |
