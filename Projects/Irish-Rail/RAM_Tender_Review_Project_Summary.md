# Irish Rail TPS Trackside NRO ETCS Tender — RAM Review Project Summary

**Role:** RAM Assurance review of the Irish Rail (Iarnród Éireann) TPS Trackside National Rollout (NRO) ETCS Level 1 tender
**Date range:** September 2026 (session)
**Prepared by:** AI assistant (Copilot SDK, RAM Workspace agent) with F. Moser

---

## 1. Documents Reviewed

| Document | Role |
|---|---|
| `ETCS_RAM_chapter2.pdf` | Generic ERTMS/ETCS RAMS Requirements Specification, Chapter 2 – RAM (Subset-026, issue 6). Baseline RAM standard referenced as mandatory by the tender. |
| `ETCS Project - Scope of Works_Pre Tender Publication_Trackside_V2.pdf` | Main D&B technical scope (164 pages). Contains Section 12 "RAM Management" (Ref 308–313) and safety/engineering management requirements. |
| `CV\12_Scope of work trackside NRO_live updates_V7.pdf` | Updated/expanded version of the Scope of Works — contains more detailed spares provisioning clauses (Ref 105–107) not present in the V2 pre-tender issue. |
| `ETCS Project - Maintenance Contract_Pre Tender Publication_Trackside NRO_V2.pdf` | Maintenance Support Services Contract (MSSC) — post-commissioning maintenance, spares, obsolescence, FRACAS, performance regime. |
| `1_TPS Trackside NRO ETCS System Supplier_PQQ_V8_.docx` | Pre-Qualification Questionnaire — track-record/experience criteria. |
| `CV\14_Conditions of Tendering T240510 D9 32 030726.pdf` | Tender process rules, evaluation weightings, pricing schedule requirements. |
| `CV\15_Tender Response Document T240510 D9 32 010726 -1.pdf` | Detailed award criteria descriptions and scoring guidance (mirrors/expands Conditions of Tendering). |

**Extraction method:** PDFs/DOCX converted to plain text via Word COM automation (files are large, e.g. 3.5 MB Scope of Works PDF); keyword-context extraction used to locate RAM-relevant clauses within long single-line text blobs.

---

## 2. Key RAM Topics Identified

- **Governing standard:** ERTMS/ETCS RAMS Requirements Specification Chapter 2 (Subset-026, issue 6), Subset-036, Subset-091, plus EN 50126 generally.
- **RAM Management Plan:** mandatory deliverable, due within **8 weeks of contract commencement** (Ref 308), bundled with other engineering management plans (Requirements, Configuration, V&V, Safety, Quality, Human Factors, Cyber Security, EMC).
- **RAM activities (Ref 311, minimum):** RAM target apportionment; predictive RAM analysis via **FMECA** + **Reliability Block Diagrams (RBD)**; **FRACAS** implementation.
- **In-service reliability monitoring:** runs from APIS Stage 5 (Cert B) until Cert A (Closure), ~24 weeks; monthly equipment screening incl. LEU event-recorder downloads; gated by a Contractor-proposed, PM-accepted **Reliability Growth Model**; this demonstration is required before Cert A / Warranty start.
- **FRACAS:** required across three overlapping regimes — design-phase (Ref 311/313), quality-process (Ref 451–453, bi-weekly reporting), and maintenance-term (MSSC, quarterly reviews during the 24-month Defects Liability Period, six-monthly thereafter).
- **Maintainability:** contractual fault response times — 60 min (05:00–01:00) / 300 min (01:00–05:00); permanent fix within 1 week of a temporary fix.
- **Obsolescence management:** rolling 3-year plan submitted annually (by 1 April), covering Contractor's and sub-contractors'/OEM equipment; Contractor bears cost of managing obsolescence for continuous availability/supply/support.
- **Spare parts:** strategic spares for long-lead/vulnerable items at **minimum 10% of installed elements** (Ref 107); Minimum Stock Holding (MSH, Schedule 7 of MSSC); Consumable Spares vs. Contractor's Parts vs. IÉ Parts ownership model; generic ERTMS baseline requires a **Parts Provisioning Plan** sized against item MTBF.
- **Bid evaluation weighting:** "Equipment Supply, Installation, Test & Commission" (200/1000 pts) scores supply-chain reliability; "System Support & Maintenance" (50/1000 pts) scores spares management, maintenance strategy, and support over a 5-year initial period (contract can run up to 30 years).
- **Quantitative RAM baseline (generic ERTMS, not yet confirmed as project-specific):** operational availability ≥0.99973 (quantifiable HW+transmission contribution ≥0.99984); MTTRS: Onboard 1.737h, Trackside Centralised 0.869h, Trackside Distributed 1.737h.

---

## 3. RAM Task List Demanded by the Contract

| # | Task | Timing | Source |
|---|---|---|---|
| 1 | Produce & submit RAM Management Plan | 8 weeks after contract commencement | Ref 308 |
| 2 | Demonstrate RAM target/spec compliance strategy | Ongoing | Ref 309 |
| 3 | Comply with RAMS Subset-026 Ch.2, Subset-036, Subset-091 | Design phase | Ref 310 |
| 4 | Allocate/apportion RAM targets to sub-systems/components | Design phase | Ref 311 |
| 5 | Predictive RAM analysis (FMECA + RBD) | Design phase | Ref 311 |
| 6 | Implement FRACAS (monitoring + corrective action) | Design through operation | Ref 311, 313 |
| 7 | Demonstrate hardware mechanical/EMC robustness | Design/manufacture | Ref 312 |
| 8 | Run in-service reliability monitoring (monthly screening) | APIS 5 → Cert A | Ref 313 |
| 9 | Propose Reliability Growth Model for PM acceptance | Before Cert A | Ref 313 |
| 10 | Supply cross-acceptance field data per re-used product | On request | Ref 34 |
| 11 | Feed FMEA/FTA into Preliminary Hazard Analysis | Concept/design | Ref 264–266 |
| 12 | Track non-compliances via FRACAS; bi-weekly quality reporting | Throughout | Ref 452–453 |
| 13 | Establish/maintain maintenance-term FRACAS (MSSC) | Maintenance contract start | Maintenance Contract |
| 14 | Meet fault response times (60/300 min) | Operational phase | Maintenance Contract |
| 15 | Attend joint FRACAS/performance review meetings | Quarterly (DLP) / six-monthly (post-DLP) | Maintenance Contract |
| 16 | Submit rolling 3-year Obsolescence & Technology Management Plan | Annually (1 April) | Maintenance Contract §2.6 |
| 17 | Provide spares traceability + causal failure data | Ongoing | Maintenance Contract |
| 18 | Meet contractual Service Levels (Performance Regime) | Ongoing | Maintenance Contract §4 |
| 19 | Supply strategic spares (≥10% of installed elements) + MSH list | Per design/supply phase | Scope of Works (V7) Ref 107 |
| 20 | Maintain asset register (equipment) & per-spare asset records | Ongoing | Ref 105; Maintenance Contract |
| 21 | Bid-stage: describe supply-chain reliability & monitoring approach | Tender submission | Conditions of Tendering / Tender Response Doc |
| 22 | Bid-stage: evidence reliability-growth monitoring track record | PQQ submission | PQQ V8 |

---

## 4. Certification & Contract Lifecycle Glossary

| Term | Meaning |
|---|---|
| **APIS** | Approval to Place In Service — CRR's external regulatory approval process, 6 stages |
| **CRR** | Commission for Railway Regulation — Ireland's National Safety Authority |
| **IM-SAP / SAP** | (Infrastructure Manager) Safety Approval Panel — IÉ's internal review board issuing Cert E→A |
| **Cert E → D → C → B → A** | Concept → Preliminary Design → Detailed Design (authorises installation) → Interim Operation (prerequisite for APIS 5) → Completion/Closure (~24 weeks after Cert B; gates Warranty) |
| **AsBo / NoBo / DeBo** | Assessment Body (Contractor-engaged) / Notified Body (TSI conformity) / Designated Body (national rules conformity) |
| **GASC / SASC / ASPSC** | Generic Application Safety Case / Specific (or Application-Specific Project) Safety Case |
| **MSSC** | Maintenance Support Service Contract — the separate post-D&B maintenance contract |
| **DLP** | Defects Liability Period — 24 months from the Conditional Certificate of Acceptance (APIS 5) |
| **FRACAS** | Failure Reporting, Analysis, and Corrective Action System |
| **NRO / TPS** | National Rollout (9-phase programme) / Train Protection System |

**Lifecycle mapping (from Scope of Works Table 4):** EN 50126 stages ↔ IM-SMS-014 Cert ↔ CRR/APIS stage, with per-phase applications required from Cert C/APIS 3 onward (9 separate phase applications), while Cert E/D and APIS 1/2 are single, project-wide applications.

---

## 5. FRACAS & In-Service Reliability Monitoring — Timeline

- **Per phase:** Design & Engineering Mgmt Plans (weeks 0–8) → Design/Enabling Works → Test & Commissioning (APIS 3/4) → **APIS 5/Cert B** (Conditional Certificate of Acceptance; starts 24-month DLP) → **Reliability Monitoring + FRACAS** (~24 weeks, monthly screening incl. LEU event-recorder downloads) → **Cert A** (Reliability Growth Model demonstration) → **Warranty Period** starts.
- **Across the 9-phase NRO rollout:** monitoring/FRACAS windows and DLPs for different phases run concurrently (staggered), requiring one continuously-operating FRACAS system rather than a one-off exercise per phase.
- **Open question flagged:** relationship between the Cert-A-gated Warranty Period and the APIS-5-gated 24-month DLP is not explicitly reconciled in the source documents (concurrent vs. nested vs. sequential).

*(Gantt-style visualisation generated during the session: `fracas_timeline.png`, saved to this project folder.)*

---

## 6. Spare Parts — Key Findings

- **Ownership model:** Minimum Stock Holding (MSH, Schedule 7 of MSSC) = IÉ Initial Parts + Contractor's Parts; Consumable Spares (Contractor-resupplied indefinitely) vs. fixed MSH list — distinction relevant for pricing.
- **Sizing rule:** ≥10% of installed elements for long-lead/vulnerable assets (Scope of Works V7, Ref 107); generic ERTMS baseline additionally calls for a formal **Parts Provisioning Plan** sized against each item's MTBF (Subset-026 §2.2.2.4.3) — the two approaches (flat % vs. MTBF-driven) may need reconciling with IÉ.
- **Traceability:** full asset register (Ref 105) + per-spare asset records including repair/replacement history; repairable-spares causal data must feed the reliability analysis/FRACAS.
- **Commercial:** MSSC Pricing Schedule Tables 04 (Equipment Supply Charges) and 05 (Programming & Maintenance Tools Support Charges); spares pricing subject to Indexation under D&B Contract Clause 20.
- **Bid scoring:** spares management explicitly scored under Award Criterion 2C "System Support & Maintenance" (50 points); supply-chain reliability/long-lead items scored under 2B "Equipment Supply, Installation, Test & Commission" (200 points).

---

## 7. Artifacts Produced This Session

| File | Description | Location |
|---|---|---|
| `fracas_timeline.png` | Gantt-style chart: single-phase FRACAS/monitoring timeline + 9-phase overlap view | Project folder |
| `RAM_Management_Plan_FRACAS_Section_Draft.md` | Draft RAM Management Plan section covering FRACAS process definition, in-service monitoring implementation, reporting cadence, and open items | Project folder |
| `RAM_Tender_Review_Project_Summary.md` | This document | Project folder |

---

## 8. Open Questions / Gaps for Irish Rail Clarification

1. **Project-specific RAM targets:** confirm availability of "Irish Rail – TPS Technical Requirements" (TPS-ETCS-P6-REQ-SL-IE-001 v05), referenced in Appendix B but not provided — needed to apportion project-specific availability/MTBF/MTTR targets beyond the generic 1998 ERTMS baseline.
2. **Numeric Service Levels:** the Maintenance Contract Performance Regime references Service Levels/Service Points, but numeric thresholds sit in a Schedule not captured in the extracted text.
3. **Life Cycle Cost (LCC):** no explicit LCC deliverable found in the Scope of Works or Maintenance Contract — confirm scope.
4. **Reliability Growth Model acceptance criteria:** no defined statistical acceptance method (confidence level, test plan) specified beyond "accepted by the Project Manager."
5. **Independent RAM assessment:** unlike Safety (ISA/AsBo mandated), no independent RAM verification role is specified — confirm whether third-party RAM audit is expected.
6. **DLP vs. Warranty relationship:** clarify whether these run concurrently, sequentially, or one nested within the other.
7. **MSH detailed list/BOM:** referenced in the Activity Schedule but not seen in the reviewed documents — needed to validate the 10% spares rule against actual equipment quantities.
8. **Spares sizing methodology:** confirm whether IÉ expects the MTBF-driven Parts Provisioning Plan (generic ERTMS baseline) in addition to, or instead of, the flat 10% rule.

---

## 9. Suggested Next Steps

- Request the missing reference documents (Technical Requirements REQ-SL-IE-001, Project Milestones Tracker D1-A-04, MSSC Performance Regime Schedule, MSH Activity Schedule/BOM) from Irish Rail.
- Convert `RAM_Management_Plan_FRACAS_Section_Draft.md` into the bid's Word template.
- Draft the Parts Provisioning Plan methodology (MTBF-driven spares sizing model) as a standalone RAM deliverable.
- Consolidate the open questions above into a formal Tender Query submission to Irish Rail.
