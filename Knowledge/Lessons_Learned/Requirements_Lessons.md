# Requirements Lessons Learned

## Purpose

Requirements lessons learned are collected to preserve recurring weaknesses,
review findings, successful practices and corrective actions from railway
signalling, ETCS and RAM projects.

The database supports RAM activities by improving the quality of reliability,
availability, maintainability and lifecycle requirements before they are
allocated, analysed, verified or placed under contract. It also supports the
identification of assumptions and interfaces that may affect safety,
operations, performance and service recovery.

The lessons improve future specifications by providing reusable review prompts,
early warning of common defects and examples of the evidence needed to show
that a requirement is clear, complete, consistent, traceable, testable and
verifiable. Project-specific requirements and evidence remain in the relevant
project records; this database contains generic lessons and anonymised examples.

## Usage Guidance

### Recording Lessons

- Record lessons after requirements reviews, RAM analyses, tenders, decisions,
  tests or failure investigations identify reusable requirements issues.
- Record the issue, root cause, impact, recommendation and preventive action.
- Use one lesson for one recurring weakness and split materially different
  causes, impacts or preventive actions into separate entries.
- Remove confidential customer, supplier and project information before adding
  a lesson to this project-independent knowledge repository.
- Reference the originating review, requirement set, clarification, calculation,
  test or FRACAS record where available.

### Reusing Lessons During Reviews

- Review the database when preparing a RAM Plan and requirements review plan.
- Use relevant lessons as prompts during system, subsystem, interface,
  operational, safety and RAM requirements reviews.
- Check each lesson against scope, lifecycle phase, operations, architecture,
  contract requirements and applicable standards.
- Record whether each lesson is applicable, not applicable or requires analysis,
  and record the resulting action in the project review log.
- Confirm closure with objective evidence such as a requirement, traceability
  record, analysis, test specification or acceptance record.

### Supporting RAM Plans and Tender Activities

The RAM Plan should identify how requirements lessons are used, who owns the
requirements review activity and how actions are tracked to closure. During
tendering, the database should be used to challenge unqualified commitments,
unstated assumptions, incomplete customer requirements and missing evidence
obligations before the response is approved.

## Lesson Template

Copy the following template for each new entry. Replace the placeholder text
with verified information and retain the field names for consistent searching.

```markdown
### RL-XXX - Short descriptive title

**Lesson ID:** RL-XXX
**Category:** Reliability / Availability / Maintainability / Safety / RAM /
Verification / Validation / Interface Requirements / Operational Requirements /
Performance Requirements / Tender Requirements

**Requirement Issue:**
Describe the requirement weakness and, where useful, provide an anonymised
example.

**Root Cause:**
State why the weakness was introduced or not detected earlier.

**Impact:**
Describe the effect on RAM analysis, safety, operations, delivery, verification,
acceptance, cost or schedule.

**Recommendation:**
State what future projects should do.

**Preventive Actions:**
List the process, review, template, training or governance actions required.

**Related Standards:**
List applicable standards or approved methods. Confirm the current project
edition before use.

**Related RAM Process:**
Identify the applicable RAM Plan, requirements review, allocation, analysis,
verification, tender or change-control activity.

**Keywords:**
List searchable terms.

**Status:** Proposed / Approved / Superseded
```

## Requirements Lessons Database

The following lessons are generic railway RAM examples. They shall be checked
against project-specific requirements, contracts, operating rules and approved
processes before being used as acceptance criteria.

### RL-001 - Replace Ambiguous Requirement Language

**Lesson ID:** RL-001
**Category:** RAM

**Requirement Issue:**
An ETCS subsystem requirement stated that the equipment shall restore service
"as soon as possible" after a failure, without defining the start event, end
event, operating state, measurement method or maximum restoration time.

**Root Cause:**
The requirement was copied from an operational expectation without converting
the expectation into a measurable engineering obligation.

**Impact:**
Designers, operators and verifiers interpreted the requirement differently.
The availability model and test procedure could not use the same restoration
definition.

**Recommendation:**
Replace subjective wording with a defined event, measurable time, operating
conditions and acceptance criterion. State any exclusions and degraded modes.

**Preventive Actions:**
Add an ambiguity-wording checklist to requirements reviews and search for terms
such as adequate, appropriate, rapid, normally, efficient and as soon as
possible.

**Related Standards:**
EN 50126-1:2017; approved requirements engineering method.

**Related RAM Process:**
Requirements review, RAM requirements allocation and availability modelling.

**Keywords:**
Ambiguity, measurable requirement, restoration time, degraded mode

**Status:** Approved example

### RL-002 - Define Verification Criteria With the Requirement

**Lesson ID:** RL-002
**Category:** Verification

**Requirement Issue:**
A reliability requirement specified a target but did not state whether
compliance would be demonstrated by analysis, test, field data, inspection or
a combination of methods.

**Root Cause:**
Verification planning was postponed until after the requirement baseline and
was treated as a test-team responsibility only.

**Impact:**
The selected evidence did not match the requirement boundary or the available
data. Re-analysis and late clarification delayed acceptance.

**Recommendation:**
Define the verification method, input data, model boundary, operating profile,
configuration baseline and acceptance decision with the requirement.

**Preventive Actions:**
Maintain a requirements verification matrix from the first baseline review and
make RAM, safety, design and verification roles jointly review it.

**Related Standards:**
EN 50126-1:2017; EN 50129 where safety-related evidence is applicable.

**Related RAM Process:**
Requirements review, verification planning, RAM evidence management.

**Keywords:**
Verification method, evidence, reliability, test, analysis, acceptance

**Status:** Approved example

### RL-003 - Separate Acceptance Criteria From Performance Intent

**Lesson ID:** RL-003
**Category:** Validation

**Requirement Issue:**
A trackside system requirement expressed an intended operational performance
but did not define the pass or fail criteria for route proving, movement
authority delivery or degraded operation.

**Root Cause:**
The operational concept described desired behaviour, but the requirement set
did not translate it into observable validation outcomes.

**Impact:**
Validation teams could demonstrate representative behaviour but could not make
a repeatable compliance decision for all required scenarios.

**Recommendation:**
Define acceptance criteria for normal, degraded, boundary and recovery cases,
including scenario inputs, expected outputs, tolerances and data to be retained.

**Preventive Actions:**
Review acceptance criteria at the same gate as the requirement and link each
criterion to a validation scenario and responsible owner.

**Related Standards:**
EN 50126-1:2017; applicable operational and customer requirements.

**Related RAM Process:**
Validation planning, requirements baseline review and evidence acceptance.

**Keywords:**
Acceptance criteria, validation, scenarios, degraded operation, pass or fail

**Status:** Approved example

### RL-004 - Allocate Explicit RAM Targets

**Lesson ID:** RL-004
**Category:** Reliability

**Requirement Issue:**
The system specification required high reliability and high availability but
did not allocate numerical targets to subsystems, functions or operating modes.

**Root Cause:**
Allocation was assumed to be an analysis output rather than a controlled
requirements activity, and system boundaries were not agreed early.

**Impact:**
Subsystem designs could not be compared consistently and contributors to the
system target were not controlled.

**Recommendation:**
Define system RAM targets, measures, conditions and boundaries, then allocate
them to the responsible functions or subsystems with documented rationale.

**Preventive Actions:**
Include a RAM allocation table in the RAM Plan and require allocation review
before subsystem requirements are baselined.

**Related Standards:**
EN 50126-1:2017; approved reliability and availability methods.

**Related RAM Process:**
RAM planning, requirements allocation, reliability prediction and availability
analysis.

**Keywords:**
RAM targets, allocation, reliability, availability, system boundary

**Status:** Approved example

### RL-005 - Define the Availability Measure and Time Boundary

**Lesson ID:** RL-005
**Category:** Availability

**Requirement Issue:**
A customer availability requirement used the term availability without
specifying inherent, achieved or operational availability, or defining whether
logistics and planned maintenance were included.

**Root Cause:**
The same term was used by the customer, RAM team and operations team with
different implicit definitions.

**Impact:**
The availability model, contractual target and acceptance evidence were not
comparable.

**Recommendation:**
Define the availability measure, numerator and denominator, system boundary,
time period, excluded events, maintenance assumptions and data source.

**Preventive Actions:**
Add an availability-definition checklist and glossary to the requirements
review. Confirm the definition during tender clarification and contract review.

**Related Standards:**
EN 50126-1:2017; approved availability modelling method.

**Related RAM Process:**
RAM requirements review, availability analysis, tender compliance review.

**Keywords:**
Availability, inherent, achieved, operational, downtime, maintenance

**Status:** Approved example

### RL-006 - Maintain Bidirectional Requirement Traceability

**Lesson ID:** RL-006
**Category:** RAM

**Requirement Issue:**
Several RAM requirements were copied into subsystem specifications without a
link to the originating customer requirement, allocation decision or planned
verification evidence.

**Root Cause:**
Traceability was treated as a document index rather than a controlled link
between need, requirement, design allocation and evidence.

**Impact:**
The project could not demonstrate that all customer RAM needs were covered or
that each allocated requirement had planned evidence.

**Recommendation:**
Maintain bidirectional traceability from source need to allocated requirement,
design element, analysis or test and acceptance record.

**Preventive Actions:**
Use a controlled traceability matrix and review orphan, duplicate and
many-to-one links at each requirements baseline.

**Related Standards:**
EN 50126-1:2017; project configuration and requirements management procedures.

**Related RAM Process:**
RAM Plan, requirements allocation, verification matrix and configuration
management.

**Keywords:**
Traceability, allocation, customer requirement, evidence, baseline

**Status:** Approved example

### RL-007 - Specify Interface Behaviour, Not Only Interface Names

**Lesson ID:** RL-007
**Category:** Interface Requirements

**Requirement Issue:**
An ETCS onboard and trackside interface requirement named the communication
interface but did not define message timing, data validity, loss handling,
recovery behaviour, version compatibility or failure indication.

**Root Cause:**
The interface control document listed physical and logical connections but did
not capture the required behaviour for nominal and degraded conditions.

**Impact:**
Subsystem teams made incompatible assumptions about timeout, retry, stale data
and recovery behaviour. RAM and safety analyses used inconsistent failure
effects.

**Recommendation:**
Specify interface inputs, outputs, timing, validity, error handling, degraded
behaviour, ownership, configuration and verification for each relevant state.

**Preventive Actions:**
Review interface requirements jointly with system, software, RAM, safety and
integration representatives before the interface baseline is approved.

**Related Standards:**
EN 50126-1:2017; applicable ETCS and project interface specifications.

**Related RAM Process:**
Interface management, FMEA, RAM analysis, integration and verification
planning.

**Keywords:**
Interface, ETCS, timeout, stale data, degraded mode, recovery

**Status:** Approved example

### RL-008 - Record Operational Assumptions as Requirements Inputs

**Lesson ID:** RL-008
**Category:** Operational Requirements

**Requirement Issue:**
Reliability and availability requirements assumed a defined traffic pattern,
operating duration, environmental profile and maintenance access arrangement,
but these assumptions were not recorded in the specification.

**Root Cause:**
Operational information was available in separate planning documents and was
not controlled as an input to the RAM requirements.

**Impact:**
Predictions and availability results were not reproducible when traffic,
duty-cycle or access assumptions changed.

**Recommendation:**
State operational assumptions with the requirement and identify their owner,
source, validity period and change impact on RAM analyses.

**Preventive Actions:**
Maintain an operational assumptions register and review it at each RAM Plan,
requirements, design and validation gate.

**Related Standards:**
EN 50126-1:2017; approved reliability and availability methods.

**Related RAM Process:**
RAM planning, operational concept review, reliability prediction and
availability analysis.

**Keywords:**
Operational assumptions, duty cycle, traffic pattern, maintenance access

**Status:** Approved example

### RL-009 - State Safety-Related RAM Assumptions Explicitly

**Lesson ID:** RL-009
**Category:** Safety

**Requirement Issue:**
A safety-related signalling requirement assumed that a failure would be
detected and placed in a safe state, but did not identify the detection time,
diagnostic coverage, safe-state definition or required evidence.

**Root Cause:**
Safety assumptions were left in the safety analysis and were not reflected in
the allocated system and RAM requirements.

**Impact:**
RAM, safety and verification teams could not confirm whether the same failure
handling assumptions were used across their analyses.

**Recommendation:**
Identify safety-related assumptions in the requirement set and link detection,
diagnostic, containment, safe-state and recovery expectations to the relevant
analyses and verification activities.

**Preventive Actions:**
Perform a joint RAM and safety review of assumptions before baseline approval
and record ownership of each assumption.

**Related Standards:**
EN 50126-1:2017; EN 50129; applicable software and safety standards.

**Related RAM Process:**
RAM and safety interface management, FMEA, hazard analysis and verification
planning.

**Keywords:**
Safety assumption, diagnostic coverage, safe state, detection, containment

**Status:** Approved example

### RL-010 - Make Performance Requirements Measurable Under Defined Load

**Lesson ID:** RL-010
**Category:** Performance Requirements

**Requirement Issue:**
An ETCS processing requirement specified a response time without defining
message load, concurrent events, hardware configuration, clock reference or
allowable percentile and tolerance.

**Root Cause:**
The requirement was derived from an average demonstration case rather than the
operational and degraded scenarios that drive worst-case behaviour.

**Impact:**
Different test environments produced different results, and the relationship
between performance and availability or failure handling was unclear.

**Recommendation:**
Define the event start and end, workload, operating mode, configuration,
measurement method, tolerance and acceptance threshold for each performance
requirement.

**Preventive Actions:**
Review performance requirements against nominal, peak, degraded and recovery
scenarios and include the agreed workload in the verification specification.

**Related Standards:**
EN 50126-1:2017; applicable ETCS and project performance specifications.

**Related RAM Process:**
Requirements review, operational scenario definition and verification planning.

**Keywords:**
Performance, response time, workload, peak load, degraded mode, tolerance

**Status:** Approved example

### RL-011 - Specify Maintainability Conditions and Restoration Boundaries

**Lesson ID:** RL-011
**Category:** Maintainability

**Requirement Issue:**
A maintainability requirement specified a maximum repair time without defining
whether fault finding, isolation, access, waiting for spares, testing and return
to service were included.

**Root Cause:**
The target was copied from a maintenance objective without a common maintenance
task definition or resource assumption.

**Impact:**
Supplier estimates, availability models and maintenance demonstrations used
different restoration boundaries.

**Recommendation:**
Define the maintenance task, start and end events, personnel competence, tools,
access conditions, spares, test equipment, information and environmental
constraints.

**Preventive Actions:**
Create a maintainability requirement checklist and validate it with operations,
maintenance, design, supplier and RAM representatives.

**Related Standards:**
EN 50126-1:2017; approved maintainability and availability methods.

**Related RAM Process:**
Maintainability analysis, maintenance concept, availability modelling and
verification planning.

**Keywords:**
Maintainability, MTTR, restoration, fault finding, maintenance task

**Status:** Approved example

### RL-012 - Resolve Customer Requirement Meaning Before Baseline

**Lesson ID:** RL-012
**Category:** RAM

**Requirement Issue:**
The customer used the term system failure to mean loss of a service, while the
supplier used it to mean failure of one equipment item. The requirement did not
define the service boundary.

**Root Cause:**
The term was accepted without a glossary, example scenarios or clarification
of the customer operating concept.

**Impact:**
Failure classification, RAM targets, reporting and acceptance evidence were
misaligned between the parties.

**Recommendation:**
Clarify critical terms with definitions, boundaries and examples before
baselining the requirement. Record the agreed interpretation in the contract
and project glossary.

**Preventive Actions:**
Use a customer clarification log during tender and early project phases, and
review unresolved terms as requirements risks.

**Related Standards:**
EN 50126-1:2017; applicable customer and contractual specifications.

**Related RAM Process:**
Tender clarification, requirements review, RAM terminology and contract
compliance review.

**Keywords:**
Customer requirement, terminology, service boundary, failure definition

**Status:** Approved example

### RL-013 - Qualify Tender RAM Assumptions and Deviations

**Lesson ID:** RL-013
**Category:** Tender Requirements

**Requirement Issue:**
A tender response confirmed a RAM target while relying on unstated assumptions
about traffic, environmental conditions, supplier data, maintenance resources
and exclusions from the availability measure.

**Root Cause:**
Bid text was prepared before the assumptions and deviations register had been
reviewed by engineering, commercial and operations stakeholders.

**Impact:**
The commitment was interpreted as unconditional and created delivery,
commercial and evidence risk after contract award.

**Recommendation:**
Classify each tender RAM response as compliant, conditional, deviated,
clarification required or not applicable. State the assumption and planned
evidence for every conditional commitment.

**Preventive Actions:**
Require RAM approval of the tender compliance matrix, assumptions register and
deviations before bid submission.

**Related Standards:**
EN 50126-1:2017; applicable customer tender requirements.

**Related RAM Process:**
Tender review, RAM compliance assessment, assumptions and deviations control.

**Keywords:**
Tender, RAM commitment, assumption, deviation, compliance matrix

**Status:** Approved example

### RL-014 - Plan Verification Activities Before Requirement Freeze

**Lesson ID:** RL-014
**Category:** Verification

**Requirement Issue:**
Requirements were baselined before the verification team had confirmed the
test environment, data source, analysis method, acceptance evidence and
independence needed for RAM claims.

**Root Cause:**
Verification planning was treated as a downstream activity rather than an
input to requirement quality and feasibility assessment.

**Impact:**
Requirements were technically plausible but not demonstrably verifiable in
the planned lifecycle phase. Rework affected schedule and evidence quality.

**Recommendation:**
Review the verification method, evidence and acceptance criterion before each
RAM requirement baseline. Resolve unavailable data and unsuitable methods early.

**Preventive Actions:**
Make verification planning a required input to requirements reviews and record
open verification risks in the RAM Plan and requirements review log.

**Related Standards:**
EN 50126-1:2017; EN 50129 where applicable to safety-related evidence.

**Related RAM Process:**
Requirements review, verification planning, RAM Plan and evidence management.

**Keywords:**
Verification planning, requirement baseline, evidence, feasibility, rework

**Status:** Approved example

### RL-015 - Tailor EN 50126 Lifecycle Requirements Explicitly

**Lesson ID:** RL-015
**Category:** RAM

**Requirement Issue:**
A project tailored lifecycle activities for a software or subsystem change but
did not record which RAM activities, requirements, evidence and reviews were
retained, combined or excluded.

**Root Cause:**
Tailoring was documented as a general statement about project size rather than
as a controlled technical decision linked to system scope and risk.

**Impact:**
Stakeholders could not demonstrate that RAM requirements remained applicable or
that omitted activities had been technically justified and approved.

**Recommendation:**
Document lifecycle tailoring by activity and deliverable. State applicability,
technical justification, owner, approval, resulting evidence and interfaces to
requirements, safety and verification processes.

**Preventive Actions:**
Include a tailoring and applicability assessment in the RAM Plan and review it
at lifecycle transitions and whenever the change scope is revised.

**Related Standards:**
EN 50126-1:2017; applicable project safety and software standards.

**Related RAM Process:**
RAM planning, lifecycle tailoring, requirements review, verification and
configuration change control.

**Keywords:**
EN 50126, lifecycle, tailoring, applicability, RAM evidence, change scope

**Status:** Approved example

## Review Process

### Review Timing

Review this database at least during the following activities:

- RAM Plan preparation and lifecycle tailoring.
- Customer requirement and contract clarification.
- System, subsystem, interface, operational and safety requirements reviews.
- Tender compliance and assumptions reviews.
- Requirements baseline, change-control and configuration audits.
- Verification and validation planning reviews.
- Major design reviews, failure investigations and project retrospectives.

### Applying Lessons to Future Reviews

The requirements review lead shall select applicable lessons before the review
and include them in the review checklist or review agenda. Reviewers shall
record the lesson identifier when a finding is raised or when a lesson has been
considered and found not applicable. The review record shall identify the
affected requirement, owner, action, due date and required evidence.

Lessons shall be fed back into the RAM Plan, requirements review plan,
verification matrix, tender compliance matrix and requirements management
guidance where relevant. Any project-specific interpretation shall be recorded
in the project repository rather than silently changing this generic database.

### Tracking Recurring Issues

Track recurring issues by category, project phase, source, affected requirement
type, root cause and effectiveness of the preventive action. A recurring issue
should be escalated for process improvement when it appears in more than one
project, remains open after a review cycle or causes repeated rework, delay,
non-compliance or evidence gaps.

The RAM Process owner or delegated requirements authority should review the
trend, assign an improvement action and update the relevant checklist,
template, training or procedure. Superseded lessons shall remain traceable to
their replacement and shall not be deleted without an approved record.

## Document Control

| Version | Date | Description | Author | Reviewer | Status |
| --- | --- | --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | Initial requirements lessons database | RAM Engineering | RAM Assurance | Draft |
