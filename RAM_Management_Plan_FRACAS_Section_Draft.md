# RAM Management Plan — Draft Section: FRACAS & In-Service Reliability Monitoring
**Irish Rail TPS Trackside NRO ETCS — Ref: Scope of Works Ref 308–313 (Section 12, RAM Management)**

> Status: DRAFT for bid/tender response use. Cross-references are to the "ETCS Project - Scope of Works_Pre Tender Publication_Trackside_V2" document. Content in *italics* marks assumptions to be confirmed with Irish Rail before contract award.

---

## 1. Purpose and Scope

This section of the RAM Management Plan (Ref 308) defines how the Contractor will:
- Implement and operate a **Failure Reporting, Analysis and Corrective Action System (FRACAS)** across the Design & Build (D&B) phase and the subsequent Maintenance Support Services Contract (MSSC) term (Ref 311, 313; Maintenance Contract).
- Deliver **In-Service Reliability Monitoring** for each National Rollout (NRO) phase, from APIS Stage 5 (Cert B, Conditional Certificate of Acceptance) until Cert A (Closure) (Ref 313).
- Demonstrate, via a Reliability Growth Model, that RAM targets and specifications are met in service, gating Cert A approval and warranty commencement.

Applies to all 9 NRO phases, each managed as an independent FRACAS/monitoring cycle per the phase's own certification timeline.

## 2. Applicable Requirements Traceability

| Ref | Requirement (paraphrased) | Plan section addressing it |
|---|---|---|
| 308 | RAM Management Plan due 8 weeks after contract commencement, compliant with EN 50126 | §1 (this document), delivered as part of the 8-week Engineering Management Plans package (Ref 214) |
| 309 | Plan describes all activities to demonstrate RAM targets/specs are met | §3–§6 |
| 310 | Compliance with Subset-026 Ch.2 RAM (issue 6), Subset-036, Subset-091 | §3 |
| 311 | Minimum RAM activities: apportionment, FMECA/RBD prediction, FRACAS | §3, §4 |
| 312 | Hardware robustness demonstrated via design review + prototype test | §3.3 |
| 313 | In-service reliability monitoring rules (APIS5→Cert A), FRACAS recording, reliability growth model | §5, §6 |
| Maintenance Contract | Maintenance-term FRACAS, DLP/post-DLP review cadence, obsolescence link | §7 |

## 3. RAM Programme Activities (Design Phase)

| Activity | Method / Standard | Deliverable |
|---|---|---|
| RAM target apportionment to sub-systems/components | Subset-026 Ch.2 apportionment method (§2.3) | RAM Apportionment Report |
| Predictive RAM analysis | FMECA (per IEC 60812) + Reliability Block Diagrams | FMECA Report, RBD model |
| Hardware robustness | Design review + prototype testing against mechanical/EMC constraints (Ref 312) | Design Review Records, Prototype Test Report |
| Cross-acceptance field data (re-used products) | In-service demonstrated MTBF, failure count/severity, replacements, corrective actions (Ref 34) | Product Service History Dossier |

*Assumption: numeric RAM targets to be apportioned against are those in "Irish Rail – TPS Technical Requirements" (TPS-ETCS-P6-REQ-SL-IE-001 v05) — to be confirmed/obtained, since only the generic 1998 ERTMS Subset-026 Ch.2 baseline values were available at the time of drafting.*

## 4. FRACAS Process Definition

### 4.1 Process Overview
A single, common FRACAS system will be used across design, in-service monitoring, and maintenance, to give end-to-end traceability of every failure from detection to closure.

**Failure lifecycle stages:**
1. **Detection** — failure identified via monthly screening, LEU event-recorder download, fault call, or maintenance inspection.
2. **Reporting** — logged in FRACAS within [X] working days of detection, with unique reference number.
3. **Analysis** — root-cause analysis (RCA), classification (Immobilising / Service / Minor, per Subset-026 Ch.2 §2.2.2.2), and criticality scoring.
4. **Corrective Action** — action defined, owner assigned, target closure date set.
5. **Verification** — effectiveness of corrective action confirmed (no recurrence).
6. **Closure** — record closed, contributing to reliability growth dataset.

### 4.2 Minimum Data Fields per Record
Equipment ID / location case reference; failure date/time detected; detection method (screening / event recorder / fault call); failure mode & symptom; criticality classification; root cause; corrective action; verification evidence; closure date; contribution to MTBF/MTTR calculation.

### 4.3 Governance
| Forum | Cadence | Purpose |
|---|---|---|
| Internal Contractor FRACAS board | Monthly (aligned to screening cycle) | Review open records, approve RCA/corrective actions |
| Joint Contractor–IÉ FRACAS/performance review | **Quarterly during the 24-month Defects Liability Period (DLP)**; **six-monthly thereafter** | Review performance, reliability, availability, maintainability; agree improvements (per Maintenance Contract) |
| Lessons Learned workshops | Per Ref 453–455 | Feed FRACAS trends into project/organisational lessons learned |

### 4.4 Tooling
*Assumption: Contractor's standard FRACAS tool (e.g., [tool name]) will be proposed to IÉ for review, comment and acceptance, per the Maintenance Contract requirement that the Contractor "propose a FRACAS system for review, comment and acceptance by IE."*

## 5. In-Service Reliability Monitoring (per NRO Phase)

| Rule | Implementation |
|---|---|
| Start | After phase testing complete **and** after APIS 5 / Cert B is granted |
| End | Up to Cert A approval for that phase (~24 weeks / 6 months typical, per Scope of Works Cert A timing) |
| Screening frequency | Minimum monthly; increased/decreased based on failure count trend |
| Screening scope | Failures present at time of check **and** latent failures since previous check, captured via **LEU event-recorder download** |
| Client support | IÉ provides maintenance records, event-recorder logs, and track access/protection for failure-investigation site visits |
| Recording | All findings logged in FRACAS (§4) |
| Exit condition | Demonstrate RAM targets/specifications met in service via a **Reliability Growth Model**, proposed by Contractor, accepted by the Project Manager — this demonstration gates Cert A and the start of the Warranty Period |

### 5.1 Reliability Growth Model (proposed approach)
*Assumption — to be confirmed/refined with IÉ:* Duane or Crow-AMSAA growth model applied to the cumulative failure data gathered during the ~24-week monitoring window, trended against the apportioned MTBF/MTTRS targets (§3), to demonstrate convergence to target reliability before Cert A submission.

## 6. Reporting

| Report | Frequency | Content |
|---|---|---|
| Quality/FRACAS status update | Bi-weekly (Ref 452) | Quality inspections, failure reporting, open non-conformities |
| Reliability monitoring summary | Monthly (aligned to screening) | Screening results, new/closed FRACAS records, trend vs. target |
| Reliability Growth demonstration report | Prior to Cert A submission | Cumulative data, growth model fit, target achievement evidence |
| DLP/maintenance performance review pack | Quarterly (DLP) / Six-monthly (post-DLP) | Performance, reliability, availability, maintainability review; improvement actions |

## 7. Interfaces to Other Plans

- **Obsolescence & Technology Management Plan** (Maintenance Contract §2.6, annual, from 1 April): obsolescence risk data sourced partly from FRACAS failure/replacement trends.
- **Spares Management**: repairable-spares traceability and causal failure data (Maintenance Contract) feed directly into the FRACAS root-cause dataset and reliability analysis.
- **Safety Management**: FMEA/FTA outputs fed into the Preliminary Hazard Analysis with traceability to the ETCS Hazard Log (Subset-113) (Ref 264–266) — kept consistent with the RAM FMECA to avoid duplicate/conflicting failure mode taxonomies.

## 8. Open Items to Confirm with Irish Rail Before Finalising
1. Numeric RAM targets/apportionment source document (TPS-ETCS-P6-REQ-SL-IE-001 v05) — request copy.
2. Relationship between Cert-A-gated Warranty Period and the APIS-5-gated 24-month DLP (concurrent, sequential, or nested?).
3. Acceptance criteria/statistical method expected for the Reliability Growth Model demonstration at Cert A (none specified in Scope of Works beyond "accepted by the Project Manager").
4. Numeric Service Levels/Service Points under the Maintenance Contract Performance Regime (Schedule not seen in extracted text).
