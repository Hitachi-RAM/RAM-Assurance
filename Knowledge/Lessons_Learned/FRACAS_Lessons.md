# FRACAS Lessons Learned

## Purpose

FRACAS lessons learned are collected to preserve recurring failure
investigation issues, root cause analysis experience, corrective action
weaknesses and reliability growth opportunities from railway signalling and
ETCS projects.

The database supports reliability growth by making failure evidence, recurrence
patterns, causal mechanisms and action effectiveness available to future
engineering teams. It helps teams distinguish symptoms from causes, identify
systemic issues and use field experience to improve design, manufacture,
maintenance, operation and verification.

The lessons improve future investigations and corrective actions by providing
reusable questions, analysis techniques, evidence expectations and closure
criteria. Project-specific event records, customer information and controlled
evidence shall remain in the relevant project FRACAS system and records. This
database contains generic lessons and anonymised examples.

## Usage Guidance

### Recording Lessons

- Record a lesson after a significant failure investigation, FRACAS review,
  supplier investigation, corrective-action review, reliability-growth review,
  field campaign or project retrospective.
- Record the failure description, root cause, impact, corrective action,
  preventive action and recommendation separately.
- Distinguish confirmed causes from suspected causes, assumptions and missing
  evidence.
- Record one reusable lesson per entry. Split unrelated failure mechanisms or
  actions into separate entries.
- Remove confidential customer, supplier and project information before adding a
  lesson to this project-independent repository.
- Reference the originating FRACAS record, analysis, test, maintenance record,
  supplier report or review wherever available.

### Reusing Lessons During Investigations

- Review relevant lessons when an event is opened, classified, prioritised or
  assigned for investigation.
- Use the lessons as prompts for evidence collection, causal analysis,
  containment, corrective action and effectiveness verification.
- Check applicability against the system boundary, configuration, environment,
  operational context, lifecycle phase and failure history.
- Record the lesson identifier in the investigation or action record when it
  has been applied or assessed as not applicable.
- Close actions only when implementation and effectiveness evidence meet the
  agreed acceptance criteria.

### Supporting FRACAS Implementation

The FRACAS procedure and project plan should define how lessons are captured,
reviewed, approved, stored and fed back to engineering. The implementation
should provide controlled event identification, failure classification, cause
analysis, action ownership, due dates, effectiveness verification, trend
analysis and escalation of recurring or safety-significant issues.

The FRACAS system should link events to configuration items, requirements,
FMEA or FMECA records, reliability predictions, availability models, change
requests, supplier records and maintenance evidence where applicable.

## Lesson Template

Copy the following template for each new entry. Replace the placeholder text
with verified information and retain the field names for consistent searching.

```markdown
### FL-XXX - Short descriptive title

**Lesson ID:** FL-XXX
**Category:** Failure Reporting / Root Cause Analysis / Corrective Actions /
Preventive Actions / Verification / Reliability Growth / Supplier Issues /
Design Issues / Manufacturing Issues / Maintenance Issues / Operational Issues /
Data Quality

**Failure Description:**
Describe the failure, fault, error, degraded condition or service impact.

**Root Cause:**
State the confirmed physical, human, process or systemic cause. Separate
confirmed causes from assumptions and suspected causes.

**Impact:**
Describe safety, reliability, availability, maintainability, operational,
customer, contractual, cost or schedule impact.

**Corrective Action:**
State the action that contains the issue or removes the confirmed cause.

**Preventive Action:**
State the action that reduces recurrence in other units, designs, suppliers or
projects.

**Recommendation:**
State the reusable practice future projects should apply.

**Related Standards:**
List applicable standards or approved methods and confirm the current project
edition before use.

**Related RAM Process:**
Identify the applicable FRACAS, FMEA, RAM Plan, reliability-growth,
configuration, supplier, maintenance or verification activity.

**Keywords:**
List searchable terms.

**Status:** Proposed / Approved / Superseded
```

## FRACAS Lessons Database

The following lessons are generic railway signalling and ETCS examples. They
shall be checked against the project FRACAS procedure, available evidence,
contractual requirements and approved methods before being used for a specific
event.

### FL-001 - Define the Problem Before Investigating the Cause

**Lesson ID:** FL-001
**Category:** Failure Reporting

**Failure Description:**
An event was recorded as "ETCS unavailable" without identifying the affected
unit, operating mode, configuration, start and end times, observed symptom or
service consequence.

**Root Cause:**
The event-reporting form allowed a general narrative without mandatory failure
classification and minimum event data.

**Impact:**
Investigators could not determine whether events were identical, related,
recurring or caused by the same configuration. Trend analysis was unreliable.

**Corrective Action:**
Reconstruct the event from logs, maintenance records, operator reports and
configuration data, then update the FRACAS record with a bounded problem
statement.

**Preventive Action:**
Make system, subsystem, configuration, symptom, operating context, time,
detection source and service impact mandatory fields before an event can enter
investigation.

**Recommendation:**
Write a problem statement that describes what failed, where, when, under which
conditions and with what effect before selecting a root-cause method.

**Related Standards:**
EN 50126-1:2017; approved FRACAS procedure.

**Related RAM Process:**
Failure reporting, event classification, FRACAS data quality review.

**Keywords:**
Problem statement, event data, failure reporting, configuration, symptom

**Status:** Approved example

### FL-002 - Separate Symptom, Failure Mode and Root Cause

**Lesson ID:** FL-002
**Category:** Root Cause Analysis

**Failure Description:**
A repeated signalling reset was recorded with "software failure" as the root
cause, although the available evidence only showed a reset symptom.

**Root Cause:**
The investigation used the affected discipline as the cause and did not
separate symptom, failure mode, physical mechanism and systemic cause.

**Impact:**
The action focused on restarting the equipment and did not address the actual
trigger. Similar events continued after closure.

**Corrective Action:**
Reopen the investigation and apply an evidence-based method such as 5-Why,
fault-tree analysis or an equivalent method appropriate to the event.

**Preventive Action:**
Require FRACAS records to distinguish symptom, failure mode, failure mechanism,
root cause, local effect, higher-level effect and end effect.

**Recommendation:**
Do not accept a discipline label, failed component or error message as the
root cause without evidence showing the causal mechanism.

**Related Standards:**
EN 50126-1:2017; IEC 60812 where FMEA or failure-mode evidence is used.

**Related RAM Process:**
Root-cause analysis, FMEA feedback, corrective-action review.

**Keywords:**
Symptom, failure mode, mechanism, root cause, 5-Why

**Status:** Approved example

### FL-003 - Verify Corrective Action Effectiveness

**Lesson ID:** FL-003
**Category:** Verification

**Failure Description:**
A firmware update was marked complete after installation, but there was no
objective evidence that the original failure mechanism could no longer occur.

**Root Cause:**
Action implementation was treated as action effectiveness, and the closure
criteria were not defined when the action was assigned.

**Impact:**
The event was closed prematurely and the failure risk remained uncertain in the
installed configuration.

**Corrective Action:**
Define and execute a regression test using the original failure conditions and
confirm the installed software and configuration baseline.

**Preventive Action:**
Require every corrective action to include an owner, due date, implementation
evidence, effectiveness criterion, verification method and closure approver.

**Recommendation:**
Close an action only after confirming both that it was implemented and that it
controls the identified failure mechanism.

**Related Standards:**
EN 50126-1:2017; applicable software and verification standards.

**Related RAM Process:**
Corrective-action control, configuration management, verification and closure.

**Keywords:**
Corrective action, effectiveness, regression test, closure evidence

**Status:** Approved example

### FL-004 - Investigate Repeat Failures as a Systemic Issue

**Lesson ID:** FL-004
**Category:** Reliability Growth

**Failure Description:**
Several interlocking units experienced the same intermittent communication
loss, but each event was closed as an isolated local repair.

**Root Cause:**
FRACAS records were not linked by failure mode, part number, software baseline,
environment or supplier lot.

**Impact:**
The common contributor was not identified, and the installed base continued to
experience avoidable service interruptions.

**Corrective Action:**
Group historical events and compare configuration, environment, maintenance,
supplier and operating data to identify common contributors.

**Preventive Action:**
Use recurrence rules and trend dashboards to escalate repeated or similar
failures for system-level investigation.

**Recommendation:**
Treat repeated symptoms as evidence of a possible common-cause or systemic issue
until the investigation demonstrates otherwise.

**Related Standards:**
EN 50126-1:2017; approved reliability-growth method.

**Related RAM Process:**
FRACAS trend analysis, reliability growth, installed-base monitoring.

**Keywords:**
Repeat failure, recurrence, common cause, trend, reliability growth

**Status:** Approved example

### FL-005 - Verify Supplier Corrective Actions Independently

**Lesson ID:** FL-005
**Category:** Supplier Issues

**Failure Description:**
A supplier report stated that a defective power module had been corrected, but
it did not identify affected serial numbers, the design change or the evidence
from production and field units.

**Root Cause:**
The supplier corrective-action process did not define the information and
acceptance evidence required by the integrator.

**Impact:**
The project could not confirm containment of the installed base or assess the
residual recurrence risk.

**Corrective Action:**
Request the failure analysis, affected population, containment status, change
record, test evidence and implementation status from the supplier.

**Preventive Action:**
Define supplier FRACAS data requirements, response times, action acceptance
criteria and audit rights in the supplier quality and RAM interface.

**Recommendation:**
Treat a supplier corrective-action report as an input to review, not as proof of
effectiveness, until objective evidence has been assessed.

**Related Standards:**
EN 50126-1:2017; applicable supplier quality and project RAM requirements.

**Related RAM Process:**
Supplier management, FRACAS interface, configuration control and verification.

**Keywords:**
Supplier corrective action, containment, serial number, evidence, audit

**Status:** Approved example

### FL-006 - Preserve Complete Evidence Before Hardware Reset

**Lesson ID:** FL-006
**Category:** Data Quality

**Failure Description:**
A wayside controller was reset before diagnostic logs, volatile data and the
operator timeline were captured, leaving only a general report of the symptom.

**Root Cause:**
The maintenance response prioritised rapid restoration but did not include an
evidence-preservation step.

**Impact:**
The original failure mechanism could not be reproduced or distinguished from
secondary effects introduced by the reset.

**Corrective Action:**
Define an evidence-preservation sequence and update the event record with all
available logs, timestamps, configuration and maintenance actions.

**Preventive Action:**
Train operators and maintainers on evidence capture, escalation thresholds and
when a reset, replacement or software reload may destroy useful data.

**Recommendation:**
Balance service restoration with evidence preservation and record any evidence
lost before the investigation begins.

**Related Standards:**
EN 50126-1:2017; approved FRACAS and maintenance procedures.

**Related RAM Process:**
Event reporting, maintenance interface, data-quality control and investigation.

**Keywords:**
Evidence preservation, diagnostic log, reset, timestamp, data quality

**Status:** Approved example

### FL-007 - Define Effectiveness Verification at Action Assignment

**Lesson ID:** FL-007
**Category:** Corrective Actions

**Failure Description:**
A connector replacement was assigned as the corrective action for intermittent
loss of an axle-counter interface, but no criterion was defined for proving
that the replacement addressed the failure.

**Root Cause:**
The action description stated what would be changed but not how success would be
measured under representative operating and environmental conditions.

**Impact:**
The action could be implemented and reported complete without demonstrating a
reduction in recurrence or service impact.

**Corrective Action:**
Define inspection, electrical, environmental and operational checks appropriate
to the connector failure mechanism.

**Preventive Action:**
Make an effectiveness criterion mandatory for every FRACAS action before the
action is approved.

**Recommendation:**
Specify the expected observable change, evidence source, observation period and
acceptance threshold when the action is assigned.

**Related Standards:**
EN 50126-1:2017; IEC 60812 where connector failure modes are analysed in FMEA.

**Related RAM Process:**
Corrective-action management, verification, FMEA update and closure review.

**Keywords:**
Effectiveness criterion, connector, corrective action, recurrence

**Status:** Approved example

### FL-008 - Assign One Accountable FRACAS Owner

**Lesson ID:** FL-008
**Category:** Preventive Actions

**Failure Description:**
An investigation remained open while engineering, maintenance and the supplier
assumed that another organisation owned the next decision.

**Root Cause:**
The FRACAS process defined participating functions but did not assign one
accountable owner for event progression and escalation.

**Impact:**
Investigation ageing increased, evidence became harder to recover and the
customer received inconsistent status information.

**Corrective Action:**
Assign an accountable event owner and establish the next decision, due date and
escalation path for each open investigation.

**Preventive Action:**
Define a FRACAS RACI covering event acceptance, analysis, action approval,
effectiveness verification, closure and reporting.

**Recommendation:**
Use one accountable owner even when analysis and corrective actions are
performed by several disciplines or organisations.

**Related Standards:**
EN 50126-1:2017; approved FRACAS governance procedure.

**Related RAM Process:**
FRACAS governance, action tracking, reporting and escalation.

**Keywords:**
FRACAS owner, RACI, accountability, escalation, ageing

**Status:** Approved example

### FL-009 - Control Investigation Delay and Data Ageing

**Lesson ID:** FL-009
**Category:** Failure Reporting

**Failure Description:**
A recurring ETCS onboard event was investigated several months after detection,
when logs had been overwritten and the vehicle configuration had changed.

**Root Cause:**
The process did not define investigation priority, response time, evidence
retention or escalation for overdue events.

**Impact:**
The investigation relied on incomplete evidence and could not confidently
separate the original failure from later configuration changes.

**Corrective Action:**
Prioritise the event, reconstruct the configuration history and document all
missing evidence and resulting uncertainty.

**Preventive Action:**
Set event triage, investigation and escalation intervals based on safety,
service, recurrence and data-loss risk.

**Recommendation:**
Treat investigation delay as a technical risk because evidence quality degrades
with time, resets, repairs and configuration changes.

**Related Standards:**
EN 50126-1:2017; project FRACAS and configuration procedures.

**Related RAM Process:**
Event triage, evidence retention, configuration management and reporting.

**Keywords:**
Investigation delay, data ageing, log retention, configuration history

**Status:** Approved example

### FL-010 - Use a Controlled Failure Classification

**Lesson ID:** FL-010
**Category:** Failure Reporting

**Failure Description:**
Similar events were classified inconsistently as fault, error, failure,
degraded operation or nuisance alarm across different maintenance teams.

**Root Cause:**
The project had no controlled classification dictionary with decision rules and
examples for system, subsystem and operational impact.

**Impact:**
Failure rates, recurrence counts, availability reports and investigation
priorities were not comparable.

**Corrective Action:**
Reclassify historical events using an approved dictionary and record the basis
for any uncertain classification.

**Preventive Action:**
Baseline failure categories, impact levels, examples, mandatory fields and
training for all event-reporting roles.

**Recommendation:**
Use controlled failure classification before trend analysis or KPI calculation,
and retain the original report alongside any corrected classification.

**Related Standards:**
EN 50126-1:2017; approved FRACAS data and KPI method.

**Related RAM Process:**
Failure classification, KPI reporting, data quality and FRACAS governance.

**Keywords:**
Failure classification, fault, error, degraded mode, KPI consistency

**Status:** Approved example

### FL-011 - Reconcile FRACAS Data Before Trend Analysis

**Lesson ID:** FL-011
**Category:** Data Quality

**Failure Description:**
The FRACAS dashboard showed a reduction in failures, but maintenance records
contained duplicate events, missing closures and inconsistent equipment IDs.

**Root Cause:**
Data sources were combined without reconciliation rules, ownership or a change
log for corrections.

**Impact:**
The apparent reliability improvement could not be distinguished from a data
processing effect.

**Corrective Action:**
Reconcile event identifiers, timestamps, configuration items, status and
closure data against source maintenance and operational records.

**Preventive Action:**
Define data-quality checks, source ownership, correction approval, duplicate
handling and audit history before publishing FRACAS KPIs.

**Recommendation:**
Assess data completeness, consistency, accuracy and timeliness before using
FRACAS trends to support reliability or availability claims.

**Related Standards:**
EN 50126-1:2017; approved RAM KPI and data-management method.

**Related RAM Process:**
FRACAS data management, KPI reporting, reconciliation and RAM assurance.

**Keywords:**
Data quality, reconciliation, duplicate, KPI, installed base

**Status:** Approved example

### FL-012 - Use Trend Analysis to Find Emerging Issues

**Lesson ID:** FL-012
**Category:** Reliability Growth

**Failure Description:**
Monthly FRACAS meetings reviewed open events individually but did not examine
failure rates by location, age, software baseline, supplier lot or environment.

**Root Cause:**
The meeting focused on action status and lacked defined trend indicators and
thresholds for escalation.

**Impact:**
An emerging common contributor was identified only after service impact became
significant.

**Corrective Action:**
Analyse failure occurrence, recurrence, ageing, exposure and service impact by
relevant configuration, location and operating variables.

**Preventive Action:**
Add trend charts, thresholds and decision rules to the FRACAS reporting cycle
and assign an owner for reviewing emerging patterns.

**Recommendation:**
Use both event-level investigation and population-level trend analysis to manage
reliability growth.

**Related Standards:**
EN 50126-1:2017; approved reliability-growth and FRACAS KPI methods.

**Related RAM Process:**
FRACAS meetings, trend analysis, reliability growth and RAM reporting.

**Keywords:**
Trend analysis, recurrence, exposure, reliability growth, threshold

**Status:** Approved example

### FL-013 - Investigate Environmental Contributors to Connector Failures

**Lesson ID:** FL-013
**Category:** Design Issues

**Failure Description:**
Intermittent connector failures occurred on trackside equipment, but the
investigation considered only component replacement and did not assess moisture,
vibration, contamination, temperature or installation condition.

**Root Cause:**
The analysis boundary stopped at the connector and did not examine the
installation environment or interface with enclosure and maintenance practices.

**Impact:**
Replacement connectors experienced recurrence, causing service interruptions and
repeat maintenance effort.

**Corrective Action:**
Inspect failed samples, installation conditions and environmental exposure, and
correlate events with location, weather, vibration and maintenance history.

**Preventive Action:**
Update design, installation, inspection and environmental qualification
requirements when evidence confirms an environmental contributor.

**Recommendation:**
For recurring connector failures, investigate the complete physical and
operational environment rather than treating the connector as an isolated item.

**Related Standards:**
EN 50126-1:2017; IEC 60812; applicable environmental and design standards.

**Related RAM Process:**
Failure analysis, FMEA feedback, design review and maintenance improvement.

**Keywords:**
Connector, moisture, vibration, contamination, environment, recurrence

**Status:** Approved example

### FL-014 - Include Manufacturing and Maintenance Causes

**Lesson ID:** FL-014
**Category:** Manufacturing Issues

**Failure Description:**
A repeated relay contact problem was initially assigned to component quality,
although assembly torque, inspection records, storage conditions and
maintenance handling had not been examined.

**Root Cause:**
The investigation focused on the failed part and did not include manufacturing,
warehouse, installation and maintenance process evidence.

**Impact:**
The supplier replaced components without controlling the process conditions that
could create the same defect in future units.

**Corrective Action:**
Review batch history, assembly records, inspection results, handling, storage,
installation and maintenance work instructions.

**Preventive Action:**
Include manufacturing, installation and maintenance interfaces in the FRACAS
investigation checklist and supplier action review.

**Recommendation:**
Treat process conditions as possible causes whenever a failure is distributed
across units, batches, sites or maintenance teams.

**Related Standards:**
EN 50126-1:2017; IEC 60812 where process-related failure causes are analysed.

**Related RAM Process:**
Supplier FRACAS, manufacturing quality, maintenance feedback and FMEA update.

**Keywords:**
Manufacturing, relay, assembly, inspection, storage, maintenance handling

**Status:** Approved example

### FL-015 - Convert Missed Reliability Growth Opportunities Into Actions

**Lesson ID:** FL-015
**Category:** Reliability Growth

**Failure Description:**
Field failure data identified a rising failure contribution from a communication
module, but the project continued monitoring without changing the design,
maintenance strategy, supplier action or verification plan.

**Root Cause:**
FRACAS reporting was treated as a record of history rather than a decision input
for reliability growth and risk reduction.

**Impact:**
The project missed an opportunity to reduce recurrence before wider deployment
and could not demonstrate how field evidence influenced the RAM case.

**Corrective Action:**
Rank the contributor by occurrence, service impact, detectability, exposure and
recurrence, then define an improvement action with a measurable expected effect.

**Preventive Action:**
Include reliability-growth decisions and opportunity tracking in periodic FRACAS
and RAM reviews, with explicit acceptance or rejection rationale.

**Recommendation:**
Use FRACAS trends to prioritise design, supplier, maintenance and operational
improvements before failures become contractual or service-level issues.

**Related Standards:**
EN 50126-1:2017; approved reliability-growth and RAM assurance methods.

**Related RAM Process:**
Reliability growth, RAM reviews, design change control and lessons learned.

**Keywords:**
Reliability growth, opportunity, contributor, prioritisation, RAM case

**Status:** Approved example

## Reliability Growth Guidance

### Using Lessons for Reliability Growth

FRACAS lessons support reliability growth when they connect event evidence to a
measurable reduction in failure occurrence, service impact, repair demand or
recurrence. The reliability-growth loop should identify the significant failure
contributors, investigate their mechanisms, select proportionate actions,
implement the change and verify the result against a defined baseline.

Actions may include design improvement, software correction, supplier process
improvement, manufacturing control, maintenance change, environmental control,
operator guidance, diagnostic improvement or a targeted verification campaign.
The selected action should be based on evidence and should state its expected
RAM benefit and limitations.

### Tracking Recurring Issues

Track recurring issues by failure mode, cause, mechanism, configuration item,
software and hardware baseline, supplier, location, environment, operating
exposure, maintenance activity and service impact. Link related events rather
than counting each event in isolation. Escalate an issue when recurrence,
common-cause potential, safety significance, customer impact or action ageing
exceeds the project-defined threshold.

The trend record should distinguish a real change in failure behaviour from a
change in reporting, exposure, classification, configuration or data quality.
Retain the source population, exclusions and assumptions for each trend.

### Evaluating Corrective Actions

Evaluate corrective actions using four questions:

1. Was the action implemented on the intended configuration and population?
2. Does objective evidence show that the identified cause or mechanism is
   controlled?
3. Has the recurrence rate, failure effect or service impact changed as
   expected over an appropriate observation period?
4. Were unintended effects, new failure modes or transferred risks identified?

An action should not be closed solely because a part was replaced, a report was
received or a software version was released. If effectiveness is inconclusive,
retain the action as open, extend monitoring, revise the action or reopen the
investigation.

## Review Process

### Review Intervals

Review this database at least at the following intervals:

- At each scheduled FRACAS review and reliability-growth meeting.
- At RAM Plan and RAM assurance reviews.
- At major design, integration, validation and commissioning gates.
- After a significant, safety-related, recurring or common-cause failure.
- During supplier performance and corrective-action reviews.
- During project closeout and transfer to operation or maintenance.

The project FRACAS procedure may define more frequent reviews according to
contractual, operational and safety needs.

### Integration Into FRACAS Meetings

The FRACAS meeting owner should identify lessons from closed investigations,
overdue actions, recurring issues and trend analysis. Proposed lessons should
be reviewed for evidence, generic wording, technical accuracy and applicability
before approval. Each approved lesson should be linked to the relevant event,
action or review record without moving controlled event evidence into this
knowledge repository.

### Integration Into RAM Reviews

Review relevant lessons during RAM Plan updates, FMEA and FMECA reviews,
reliability prediction updates, availability analysis, maintainability reviews,
design reviews, verification planning and RAM case updates. Confirm whether
lessons require changes to requirements, assumptions, analyses, design,
maintenance instructions, supplier controls or verification evidence.

### Feedback Into Process and Knowledge Repositories

Recurring or systemic lessons should be assessed by the RAM Process owner for
inclusion in FRACAS procedures, templates, checklists, training or governance.
Generic technical guidance should be stored in the appropriate Knowledge area.
Project-specific evidence and decisions shall remain in the Projects area.

Superseded lessons should remain traceable to their replacement. Review this
database for duplicates, obsolete methods, changed standards references and
continued applicability before each controlled revision.

## Document Control

| Version | Date | Description | Author | Reviewer | Status |
| --- | --- | --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | Initial FRACAS lessons database | RAM Engineering | RAM Assurance | Draft |
