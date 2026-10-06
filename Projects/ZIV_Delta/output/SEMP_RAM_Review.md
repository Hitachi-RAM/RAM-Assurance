# SEMP RAM Review

## Review Basis

**Document:** `SEMP_3BU_61914_0002_DPAPA_ED01PD01.docx` (Edition 01 proposal for ZIV Delta)  
**Review date:** 2026-10-06  
**Assessment:** RAM-focused review of the SEMP, cross-checked against the referenced Generic RAM Plan, `3BU_15000_1712_DUAPA`, Edition 07.

Two comments are recommended before the SEMP is baselined. The SEMP recognizes RAM as part of the solution and names a RAM-AM, but project-specific RAM planning/evidence and assured RAM-AM involvement are not clear in the current plan.

## Review Comment Log

### RAM-01 — Identify the project-specific RAM plan and evidence

**Severity:** Medium  
**References:** SEMP Sections 8, 9, 12.1 and 16.9; Generic RAM Plan, phase-related RAM activities and deliverables.

**Source evidence:**

- Section 9, Table 8 lists: “RAM Plan | Provides details of the tasks and activities about Reliability, Availability and Maintainability of the Solution. | [4]”.
- Section 12.1, Table 12 identifies [4] as “Generic RAM Plan”, Edition 07.
- Section 16.9 states: “Not applicable.”
- The solution deliverables in Sections 8.1 and 8.2 do not identify a project-specific RAM Plan, RAM analysis or RAM demonstration report.
- The Generic RAM Plan calls for establishing a project-specific RAM Plan and lists RAM analysis as mandatory, with the applicable RAM deliverables to be tailored and justified.

**Issue and impact:** The SEMP appears to use the generic method document as the plan for the ZIV Delta solution, while also stating that subordinate plans are not applicable. It does not identify where project-specific RAM requirements/acceptance criteria, planned analyses, responsibilities, RAM evidence or tailoring decisions are controlled. This leaves the RAM basis for the design, verification and acceptance gates unclear. This is a SEMP traceability gap; it does not establish that the project has no RAM requirements or separate RAM plan.

**Recommendation:** Identify the controlled ZIV Delta RAM Plan by document ID and edition in the plan and deliverable tables, and reconcile Section 16.9. The project plan should link to the approved project RAM requirements and define applicable analyses/demonstration, responsibility, evidence and milestone/acceptance points. Where a generic activity or deliverable is not applicable, record the project-specific rationale and approval rather than leaving applicability implicit.

**Required evidence:** Controlled ZIV Delta RAM Plan or approved tailoring record; trace from contractual/project RAM requirements to RAM activities and acceptance evidence; aligned SEMP plan and deliverables references. Confirm against the CDRL and project RAM requirements.

### RAM-02 — Assure RAM-AM participation and CCB membership

**Severity:** Medium  
**References:** SEMP Sections 13.1.1, 13.1.4 and 13.12; Generic RAM Plan, “RAM Assurance Manager”.

**Source evidence:**

- The SEMP CCB membership table (Section 13.1.4) does not list the RAM-AM.
- In the milestone involvement tables (Section 13.12), RAM-AM involvement is “AR” (attend on request) at several design and test gates, including PDR, CDR and TRR1-LAB. The SEMP defines AR as “Attend on request”.
- The team roster in Section 13.1.1 labels the assigned role “Project Manager (RAM-AM)”, rather than “RAM Assurance Manager (RAM-AM)”.
- The Generic RAM Plan states that the RAM-AM “must accompany each project and participate in all essential meetings and reviews” and “must be a permanent member of the CCB”. It also requires functional independence from design and implementation activities subject to RAM assessment.

**Issue and impact:** The SEMP does not establish permanent RAM-AM membership of the CCB, and on-request attendance does not assure RAM input at essential reviews or decisions affecting RAM requirements, configuration and evidence. The role label also makes the appointed function unclear. The SEMP should show how the RAM-AM's required independence is preserved.

**Recommendation:** Add the RAM-AM to the CCB membership table and define required participation at RAM-relevant design, verification, validation and acceptance gates. Correct the roster role label to “RAM Assurance Manager (RAM-AM)” and state how functional independence is maintained. If the project intends to tailor the generic requirements, record the rationale and approval.

**Required evidence:** Updated CCB membership and milestone involvement tables; clear RAM-AM role/appointment and independence statement; review records demonstrating RAM input at required gates, or an approved tailoring rationale.

## Action List

| ID | Recommended action | Suggested owner |
| --- | --- | --- |
| A1 | Identify and reference the controlled project RAM Plan; align the SEMP plan list, deliverables and subordinate-plan applicability statement. Confirm its coverage against the CDRL and project RAM requirements. | SEM / RAM-AM |
| A2 | Update CCB membership and milestone participation; correct the RAM-AM role label and document functional independence or approved tailoring. | SEM / Project Manager / RAM-AM |

## Assumptions and Limitations

- The review covers the SEMP and the Generic RAM Plan available in the workspace. The CDRL, project RAM requirements, Project Management Plan and any separately controlled ZIV Delta RAM Plan were not available for review. A project-specific RAM Plan may exist outside the reviewed workspace; verify before treating RAM-01 as a project-level absence.
- No numerical RAM target or customer requirement has been inferred. The SEMP refers project requirements to the CDRL, which was not reviewed.
- This is a preliminary RAM-focused document review, not a complete EN 50126 compliance assessment or a safety-authority determination.
