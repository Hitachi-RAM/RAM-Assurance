# DSTW FRACAS — Project Summary

**Date:** 2026-09-13
**Prepared by:** RAM / FRACAS team (AI-assisted session)
**Scope:** Definition of a project-level FRACAS (Failure Reporting, Analysis and Corrective Action System) for the DSTW (Digitales Stellwerk / Digital Interlocking OBB) project.

---

## 1. Objective

Define a DSTW project FRACAS aligned with:
- the DSTW RAMS contractual requirements,
- the corporate FRACAS procedure, and
- prior project experience (ProVIS-based failure data collection).

Deliver a first set of working documents: a FRACAS Plan, a data register template, a KPI catalogue, and a customer data-exchange specification.

---

## 2. Source Documents Reviewed

| Document | Role |
|---|---|
| `SSS_DI_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx` | DSTW RAMS specification — primary source of contractual FRACAS/availability requirements |
| `Technical_Concept_DSTW_3BU_17300_0010_DSAPC.docx` | DSTW technical concept — FRACAS implementation description, FK classes, reporting cadence |
| `RAMP_IPS_3BU_17300_2009_DUAPA_Ed01.docx` | IPS RAM Plan |
| `RAMP_VIL_3BU_17300_1209_DUAPA_Ed01.docx` | VIL RAM Plan |
| `G-PRC_L0609_00_EN - FRACAS_draft.docx` | Corporate FRACAS procedure (roles, activities, deliverables, RACI) |
| `EL4-SSS_RAMS-Requirements_allocated_to_VIL.xlsx` | Supplementary requirement allocation (not fully mined) |

---

## 3. Key Findings from Requirements Analysis

### 3.1 Contractual FRACAS obligations (DSTW RAMS spec)

| Requirement ID | Summary |
|---|---|
| EL4-DIL-SSS-REQ-00671 | Supplier must provide an EN 50126-1 aligned FRACAS system for all delivered systems/subsystems. |
| EL4-DIL-SSS-REQ-00672 | Supplier must prove required availability values (DC, VIL, FES, OC) within 5 years of first VIL commissioning. |
| EL4-DIL-SSS-REQ-00673 | FRACAS must monitor availability of each individual DSTW component. |
| EL4-DIL-SSS-REQ-00674 | FRACAS must provide the customer with regular reports. |
| EL4-DIL-SSS-REQ-00675 | Reporting must show availability classes 1–3, down to module level with failure cause where practicable. |
| EL4-DIL-SSS-REQ-00676 | SLA: 5 min (VIL) / 30 min (FES, OC) fault clearance — **status: "In negotiation"**, start/stop timestamp undefined. |
| EL4-DIL-SSS-REQ-00678 to -00681 | System integrator/supplier responsibilities for monitoring, non-compliance coordination, and accountability. |
| EL4-DIL-SSS-REQ-00319 / -00321 | Faults/errors/failures must be reported to OMC (IF-61) and DDSP (SDI); OMC failure-category allocation flagged as an open point in the requirement itself. |

### 3.2 Project-specific commitments (Technical Concept)

- FK1–FK4 failure classification scheme with defined operational-impact criteria.
- Internal repair-data review: **monthly workshops**.
- Customer service workshop and report: **twice per year**, covering predictive maintenance, Service Center activity, patches/updates, repairs, availability, and continuous improvement (KVP).
- Customer supplies MDM/DDSP data; Hitachi performs the FRACAS analysis and demonstration.

---

## 4. Clarifications Obtained from the User

| Topic | Decision / input |
|---|---|
| Lifecycle scope | All phases: manufacturing, T&C, warranty, O&M. |
| Data source/tooling | Previously used ProVIS for failure data, analysed via Excel/R — adopted as the interim toolchain, pending a formal tool decision. |
| Data ownership | Customer holds the operational data but must share it with Hitachi. |
| FRACAS level | Project-level FRACAS (not product-level). |
| Reporting frequency | Confirmed via Technical Concept: monthly internal, twice-yearly customer workshop. |
| SLA definition | Confirmed as unresolved ("In negotiation") — start/stop timestamps and exclusions not agreed. |
| KPI targets | Confirmed as not yet baselined — treated as open/TBD throughout. |
| Configuration hierarchy | Recommended: System → DC/VIL/IPS/ADM and FES/OC → Module → LRU → Serial Number. |

---

## 5. Deliverables Produced

All files generated in `DSTW - FRACAS/` (Word via `python-docx`, Excel via `openpyxl`):

| # | File | Content |
|---|---|---|
| 1 | `DSTW_FRACAS_Plan_v0.1.docx` | Full project FRACAS plan: purpose, scope/lifecycle, requirements references, objectives, roles/RACI, interim toolchain, data framework, FK1–FK4 classification, RAM/KPI monitoring, corrective-action workflow, FRB cadence, reporting, compliance demonstration, records, and an Open Points log. |
| 2 | `DSTW_FRACAS_Register_Template_v0.1.xlsx` | Controlled register: README, Installed Base, Event Register, Corrective Actions, KPI Dashboard, Lookups — with data validation, conditional formatting, and dashboard formulas. |
| 3 | `DSTW_FRACAS_KPI_Catalogue_v0.1.xlsx` | 14 KPI definitions (availability by system/subsystem, empirical failure rate, MTBF, MTTR/MRT, both SLA KPIs, recurrence rate, CA ageing/effectiveness) with formula, population, exclusions, data source, target status, and a Change Log sheet. |
| 4 | `DSTW_FRACAS_Data_Exchange_Specification_v0.1.docx` | Customer/Hitachi data-exchange agreement draft: data content, exchange mechanism/frequency, data-quality ownership, security, reconciliation/dispute process, open points, and approval block. |

Generation scripts retained in the session workspace (`build_fracas_plan.py`, `build_fracas_register.py`, `build_kpi_catalogue.py`, `build_data_exchange_spec.py`) for reproducibility/versioning.

---

## 6. Open Points Carried Forward

| ID | Open point | Owner (proposed) |
|---|---|---|
| OP-1 | FRACAS tool decision (interim ProVIS/Excel/R vs. future dedicated tool) | Project RAM WPL |
| OP-2 | Customer data exchange agreement (format, frequency, access) | Project RAM WPL / Project Manager |
| OP-3 | SLA start/stop timestamp definition (EL4-DIL-SSS-REQ-00676) | RAMS Manager / Project Manager |
| OP-4 | KPI catalogue targets and formal formulae | Project RAM WPL |
| OP-5 | FK1–FK4 classification allocation rules, incl. OMC reporting scope | RAMS Manager / Customer |
| OP-6 | Reporting calendar detail (exact dates, workshop scheduling) | Project RAM WPL |

---

## 7. Suggested Next Steps

1. Circulate `DSTW_FRACAS_Plan_v0.1.docx` and the Requirements Matrix (from the earlier session output) for internal review.
2. Confirm the interim toolchain (ProVIS + Excel + R) with the FRACAS tooling owner.
3. Send `DSTW_FRACAS_Data_Exchange_Specification_v0.1.docx` to the customer for review/negotiation (addresses OP-2, DX-1 to DX-6).
4. Raise a formal clarification request for the SLA definition (OP-3) and FK classification rules (OP-5).
5. Baseline KPI targets in `DSTW_FRACAS_KPI_Catalogue_v0.1.xlsx` once contract-level values are confirmed (OP-4).
6. Populate the Installed Base sheet in the register template from the project configuration/PBS.
