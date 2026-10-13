# DSTW VIL - Availability Requirements Analysis and SW Allocation

| Attribute | Value |
| --- | --- |
| Task | ELFOUR-1730: analyse 3BU_17300_1257_DTAPA, chapter 3.1.4.3.2, and allocate VIL availability requirements to SW components |
| Analysis date | 2026-10-13 |
| Classification | Hitachi Rail - Internal |
| Status | Engineering proposal for review; not an approved requirements baseline or a compliance demonstration |
| Primary baseline | SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx |
| Scope | All six active requirements in "VIL Availability"; DPR diagnosis and recovery considerations included as supporting dependencies |
| Configuration | Basic redundancy as the primary configuration; georedundancy and later-release requirements identified separately |
| Deliverable | Traceable functional SW allocation, quantitative interpretation, verification criteria, findings and closure actions |

## 1. Executive summary

**The six VIL availability requirements can be allocated functionally to ELEKTRA Core and ECMUX and refined to their runtime applications, redundancy services, communication, diagnosis and lifecycle functions. Their numerical availability targets remain VIL-instance targets: they must not simply be copied to every SW component.**

The DPR assessment [S2] provides a useful initial allocation to Core/MUX and relevant SSS_VIL requirements. It is not sufficient to close the task because:

1. **The manual restoration input changed:** current REQ-00569 specifies **6 h**, whereas the DPR uses **0.5 h**. The RAM plan also contains different restoration figures.
2. **Hot-hot redundancy does not mask every SW failure:** SSS_VIL REQ-01155 restarts the affected application on **all redundant nodes**, including both diverse SW channels where applicable. REQ-00229 limits collateral restart between CC, RCU and DGP, but does not remove the interruption of the affected application.
3. **Patch continuity is not proven by redundancy alone:** version compatibility, CDS authorization, continued interface operation and sequential reintegration must work together. Related requirements have later target releases than the parent RAMS requirements.
4. **The DPR CN calculation is not a complete VIL availability model:** it does not establish the contributions of ECMUX, systematic SW failures, application-wide restart, common infrastructure dependencies or end-to-end service recovery.
5. **Detection and recovery timing remain incomplete:** SSS_VIL REQ-01462/01463/01464 contain TBD detection limits. Reintegration has no stated maximum duration.

**The requirement-to-SW-component allocation (requirements list, allocation matrix and per-component obligations) is in Section 5.2, Tables A-C.**

Recommended disposition: retain the parent requirements, establish the component obligations in Sections 5 and 6, and close the baseline/release/timing issues before claiming compliance. The DPR recommendation of node recovery **< 10 min** is a useful proposed redundancy-restoration objective, but it is not a replacement for the **2 min** service-restoration scenario.

## 2. Sources, precedence and limitations

### 2.1 Source register

| Ref. | Source | Evidence used |
| --- | --- | --- |
| S1 | [SSS DIL RAMS, Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx) | Chapter 3.1.4.3.2; six accepted parent requirements; associated LH/PH text; REQ-00329/00330 diagnosis dependencies |
| S2 | [DPR Requirements [VIL-Instance]](<../DPR Requirements [VIL-Instance].pdf>) | All 6 pages: initial allocation, SSS_VIL references, automatic recovery and preliminary CN results |
| S3 | [SSS VIL, 3BU_15000_6955_DTAPA, 01 RL](../SSS_VIL_3BU_15000_6955_DTAPA.pdf) | Sections 3.1, 4.2, 4.3.2, 4.5.2.2, 4.5.5, 4.6, 4.7, 4.8 and 4.9; PDF pages 12-18, 28, 36-50 and 53-54 |
| S4 | [SEMP VIL, Ed01](../SEMP_VIL_3BU_15000_6955_DPAPA_ED01.pdf) | Section 1.2.4, PDF p.17: GENSYS, CAR-RED, country-specific SW and ECMUX work packages; section 3.2, pp.42-43: platform and communication suppliers |
| S5 | [RAMP DIL/VIL, Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf) | Sections 3.4, 4, 5.6 and 6.2, PDF pp.20-25: availability classes, refinement, HW analysis scope and RAM evidence |
| S6 | [SSS DIL Central Unit Part 1, Ed02PD01](../SSS_CU_Part1_3BU_17300_1255_DTAPA_Ed02PD01.docx) | REQ-00443, 00439, 00991; software actualization REQ-01302, 01294, 01298 and associated release/status fields |
| S7 | [Preliminary RAM estimation, Ed02, 20260910](<../../Split Brain/Prelim_RAM_Estimation_DSTW_Ed02_20260910.xlsx>) | Limited contextual check: sheet "4.1 Calculations 2x(2oo2)", CN rows 20-23, availability units and explicit geo-link/router CCF considerations |
| S8 | [Manage Project RAMS and Independent Validation Activities, draft with comments](<../../../../Knowledge/Process/RAM-Process/G-PRC_S06001_03_EN_d02 Manage Project RAMS and Independent Validation Activities_comments_RAM-AT.docx>) | Sections concerning RAM plans, system allocation, traceability, test specification review and validation of system/subsystem RAM reports |

For this analysis, **S1 is the controlling supplied input for parent wording and numbers**. S2 is an assessment of an earlier input, not a replacement specification. S3 provides existing candidate child requirements, but their individual statuses include Draft and In negotiation. S5 is a released plan with inconsistent or older inputs; approval of a plan does not resolve those inconsistencies.

The S1 edition has a provisional change-log date, and its verification fields are still placeholders. Its approval/current-baseline status must be confirmed by configuration management. No source was modified.

The January workbook named in S2, `Prelim_RAM_Estimation_DSTW_Ed01p11_20260116.xlsx`, was not found in this repository. S7 is a **different, newer workbook**, not substituted as the validated source of S2. Its cached values and selected formulas were inspected; it was not recalculated or comprehensively audited.

### 2.2 Method and assumptions

- Follow EN 50126 RAM lifecycle principles: define service and boundaries, refine and allocate requirements, model dependencies, and establish traceable verification evidence. No clause-by-clause standards compliance is claimed.
- For SW, allocate observable behaviour and timing, not an invented constant failure rate. The RAMP explicitly separates random HW reliability analysis from SW reliability assurance.
- Source facts, engineering interpretations and proposed requirements are identified separately.
- Annual conversions assume continuous required service for **365 d = 8760 h = 31,536,000 s**. These are interpretation aids, not an agreed contractual observation interval.
- Exact service-loss criteria, treatment of partial station restrictions, exclusions for planned breaks and recovery-class counting require customer/project agreement.
- A VIL redundant node is **not synonymous with a Core CN**: S3 section 3.1.1 expressly distinguishes them because ECMUX uses a different redundancy implementation.
- Proposed implementation ownership below must be confirmed in component specifications/designs. SSS_VIL usually allocates at ELEKTRA Core/ECMUX level, not to every library or process.

## 3. Parent requirements and quantitative interpretation

Requirement identifiers follow the original EL4-DIL-SSS-REQ and EL4-VIL-SSS-REQ identifiers. Recommendations and verification methods are written in words without new identifiers.

### 3.1 Complete parent inventory

Requirement content below is a concise engineering synopsis, not a verbatim replacement of S1.

| Parent | Status / category in S1 | Required outcome | Allocation interpretation | Principal verification gap |
| --- | --- | --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 | Accepted / DPR | Class 2 overall VIL-instance availability >= 99.995% | Joint VIL service objective covering the required Core, ECMUX and interface paths; shared failures count once | Service boundary, observation period, downtime rules and complete dependency model |
| EL4-DIL-SSS-REQ-00569 | Accepted / DPR | Class 2 availability distribution: >= 99.9979% for MTTR 6 h; >= 99.999% for 10 min; >= 99.9996% for 2 min | Separate failure/recovery scenarios; allocate detection, safe reaction, restart and complete service restoration to affected components | Recovery classification, maximum versus mean times, event-rate evidence and TBD component timings |
| EL4-DIL-SSS-REQ-00570 | Accepted / DPR | >= 99.7154% for outages without operational impact, identified as FK4 | Monitor degraded/redundancy-loss conditions and restore them; distinguish these from operational service loss | Definition and measurement of FK4, especially loss of one redundancy partner |
| EL4-DIL-SSS-REQ-00573 | Accepted / MCR | Minor VIL SW patches **or HW changes** without operational restrictions | Core, ECMUX, communication and lifecycle functions must support the approved compatible rolling-maintenance procedure; IPS owns supporting HW actions | Version compatibility, maintained service, update coordination and release coverage |
| EL4-DIL-SSS-REQ-00818 | Accepted / MCR | Major VIL SW upgrades, especially safety-relevant changes, **or HW changes**, during operational breaks | Controlled shutdown/activation/restart across Core and ECMUX with operational authorization | Approved update procedure, break definition and acceptance of the source's additional handover expectations |
| EL4-DIL-SSS-REQ-00574 | Accepted / MCR | Operational downtime no longer than affected-component restart plus reintegration time | Bound and measure the end-to-end restoration path; do not invent an absolute maximum from this relative wording | Numeric restart/reintegration limits, clock boundaries and multi-component critical path |

All six parent requirements target DIL_OBB_1.0.x in S1; EL4-DIL-SSS-REQ-00818 also lists IFC_BLOCK_1.0.0. Parent allocations include DIL/VIL, and IPS for the change/downtime requirements.

EL4-DIL-SSS-REQ-00571 and EL4-DIL-SSS-REQ-00572 are **historical identifiers** described by S2 as deleted and merged into EL4-DIL-SSS-REQ-00569. They do not appear as active requirements in the analysed S1 chapter and must not be allocated as additional independent obligations.

### 3.2 Formulae and calculated equivalents

For an availability target `A` expressed as a fraction:

```text
U = 1 - A
D_allowed = U * T_required

For a simple stationary alternating up/down model:
A = MUT / (MUT + MDT)
MUT_required = A * MDT / (1 - A)
lambda_equivalent = 1 / MUT_required
FIT_equivalent = lambda_equivalent [h^-1] * 10^9
```

MUT is mean up time; MDT is mean downtime from loss of required service to restoration. A source MTTR can be inserted for MDT **only if it covers that entire downtime**. The formula is not a proof for a multi-state redundant VIL and does not make systematic SW faults exponential random failures.

| Scenario | A as fraction | U | Equivalent allowed duration [s / 365 d] | Equivalent duration [min / 365 d] |
| --- | --- | --- | --- | --- |
| Overall, EL4-DIL-SSS-REQ-00587 | 0.999950 | 5.0e-5 | 1576.800 | 26.2800 |
| Manual, EL4-DIL-SSS-REQ-00569 | 0.999979 | 2.1e-5 | 662.256 | 11.0376 |
| Automatic, 10 min, EL4-DIL-SSS-REQ-00569 | 0.999990 | 1.0e-5 | 315.360 | 5.2560 |
| Automatic, 2 min, EL4-DIL-SSS-REQ-00569 | 0.999996 | 4.0e-6 | 126.144 | 2.1024 |
| FK4, EL4-DIL-SSS-REQ-00570 | 0.997154 | 2.846e-3 | 89751.456 | 1495.8576 |

The FK4 duration represents exposure to the defined **non-operational-impact condition**, not permitted operational service downtime. The 120 s or 600 s event-restoration criteria are not annual downtime budgets.

| EL4-DIL-SSS-REQ-00569 scenario | Assumed MDT [s] | Conditional required MUT [h] | Conditional required MUT [365 d years] | Equivalent rate [FIT] |
| --- | --- | --- | --- | --- |
| Manual, current S1 input | 21600 | 285708.286 | 32.6151 | 3500.074 |
| Automatic, 10 min | 600 | 16666.500 | 1.90257 | 60000.600 |
| Automatic, 2 min | 120 | 8333.300 | 0.95129 | 120000.480 |

These are **calculated scenario equivalents, not proposed SW component failure-rate budgets**. The rates correspond respectively to approximately 3.500e-6, 6.000e-5 and 1.200e-4 failures/h under the stated model.

Changing the manual input from 0.5 h to 6 h increases the conditional required MUT from 23809.024 h to 285708.286 h, a **factor of 12** at unchanged availability. The input discrepancy is therefore material.

S5 states that recovery classes concern scenarios/fault categories and are not subcomponents of overall downtime. Do not mechanically add their targets or use them as Core/MUX budget shares. If agreed measured categories are mutually exclusive, observed downtime can be aggregated once; if categories overlap, a disjoint counting rule is required. The overall target must still be demonstrated separately.

## 4. Evaluation of DPR RAM considerations

### 4.1 Accepted reasoning and required corrections

| DPR consideration [S2] | Assessment against supplied current sources | Allocation consequence |
| --- | --- | --- |
| Allocate overall availability to Core and MUX | Correct direction, but shared hardware/platform/network dependencies are not independent blocks | Both component teams contribute; retain instance-level numerical ownership with VIL/RAM |
| Core 2x2oo2 basic and 4x2oo2 georedundant | Supported by EL4-VIL-SSS-REQ-00181; EL4-VIL-SSS-REQ-00182; the 1oo2/1oo4 abstraction applies to complete Core CNs, not to diverse channels individually | NMR and application integration must preserve safe operation in supported degraded states |
| MUX 2x1oo1 hot-hot | Supported by EL4-VIL-SSS-REQ-00227. Georedundant ECMUX is **not simply four active nodes**: EL4-VIL-SSS-REQ-00228 describes 2x1oo1 plus possible standby reintegration and is In negotiation | Keep J4S/ECMUX recovery separate from Core 4x2oo2; do not claim a settled geo concept |
| Core and MUX can fail together on shared hardware | Important dependency warning; exact placement is not proven by S2 alone | Check actual VM/host/failure-domain mapping and count common failures once |
| EL4-VIL-SSS-REQ-00221 supports automatic recovery | It guarantees interruption-free integration when a node is started; it does not specify automatic restart initiation or a duration | Add separate detection, recovery initiation, timing and full-redundancy-restoration obligations |
| EL4-VIL-SSS-REQ-01155 enables fast correction | Correct as a mechanism, **not evidence of seamless availability**; all replicas of the application restart | Include synchronized application loss and RCU/CC/DGP restart dependencies in service-loss analysis |
| EL4-VIL-SSS-REQ-00285 and EL4-VIL-SSS-REQ-00288 support diagnosis continuity | Supported. In basic configuration EL4-VIL-SSS-REQ-00288 is one RaSTA connection with **two transport channels on different nodes** | Allocate DGP/datalogger continuity and channel-status reporting; do not equate number of connections with number of channels |
| Patches have no operational restriction | Required by S1, but update compatibility and release coverage are unresolved | Test Core and ECMUX rolling update, CDS consistency and interface continuity together |
| Major upgrades require seamless takeover | S2 overstates this as a general guarantee. S1 requires an operational break; associated LH/PH text introduces handover expectations and also an interruption interval | Clarify approved procedure; do not silently substitute a zero-downtime upgrade requirement |
| EL4-DIL-SSS-REQ-00991 requires automatic recovery | Supported by S6, but its status is In negotiation and recovery methods are expressly open | Allocate jointly to Core/NMR and ECMUX/J4S, with approved recovery procedures |

### 4.2 Preliminary CN numerical results

S2 p.6 presents the following historical results. Decimal group spaces in the PDF have been normalized. The FiT column is interpreted as FIT; the underlying workbook is unavailable.

| CN 1oo2 + network scenario | Reported rate [FIT] | Rate [failures/h] | Reported MTBF [years] | Reported availability [%] |
| --- | --- | --- | --- | --- |
| MTTR 2 min | 4.449 | 4.449e-9 | 25658 | 99.99999999 |
| MTTR 5 min | 4.451 | 4.451e-9 | 25645 | 99.99999996 |
| MTTR 10 min | 4.455 | 4.455e-9 | 25623 | 99.99999992 |
| MTTR 1 h | 4.493 | 4.493e-9 | 25410 | 99.99999955 |
| MTTR 4 h | 4.627 | 4.627e-9 | 24671 | 99.99999814 |

An independent arithmetic check with `MTBF = 1/lambda` and `A = 1/(1 + lambda * MDT)` is consistent with these magnitudes. Minor differences follow from rounded FIT inputs. For example, 4.455 FIT and MDT = 600 s give MTBF approximately 25624 years and A approximately 99.999999926%.

**Engineering interpretation:** these values indicate strong calculated margin for the limited modeled HW path. They do not show that a real VIL instance has a 25,000-year field-demonstrated MTBF, or that every failure restores service in 2 min.

Evidence not established by this DPR table:

- Full Core-plus-ECMUX service topology and all required adjacent/field interfaces.
- Failure/repair coverage, restart success, failover interruptions and degraded-state exposure.
- Synchronized systematic SW failure or incompatible configuration across replicas.
- CCF from shared hosts, storage, power, networks, timing or deployment/authorization services.
- Mapping of modeled repair time to both **service restoration** and **redundancy restoration**.
- Rates, mission conditions and prediction provenance sufficient to reproduce the complete model.

S5 specifies MIL-HDBK-217F-based Alcarel for HW prediction, within an EN 50126 RAM framework. The S2 table alone does not demonstrate that each input was produced by that method. No independent HW prediction is performed here.

S7 contains explicit geo-link/router CCF considerations, including an assumed beta value of 0.02; it would be incorrect to claim that all repository calculations omit CCF. That assumption does not establish VIL-wide CCF coverage. Also, sheet "4.1 Calculations 2x(2oo2)" mixes availability **fractions** at I20 with **percentages** at I21; J20/J21 apply corresponding different conversions. Normalize units before reuse rather than treating that distinction itself as an arithmetic error.

The S2 recommendation **node recovery < 10 min** is retained as a **proposal for restoring full redundancy**, subject to definition of the start/end states and feasible recovery conditions. A permanently failed HW unit cannot necessarily be physically repaired automatically; SW recovery must distinguish restartable faults from faults requiring IPS/maintenance intervention.

## 5. Allocation down to VIL SW components

### 5.1 Component and ownership breakdown

| SW component / function | Source basis | Availability responsibility | Boundary / qualification |
| --- | --- | --- | --- |
| ELEKTRA Core - CC application | S3 EL4-VIL-SSS-REQ-00229, internal ECMUX command interface, pp.47/50 | Preserve the required control path; restore application and field/adjacent-system state after CC restart | CC failure restarts CC and RCU, not DGP; confirm detailed CC subfunction allocation in design |
| ELEKTRA Core - RCU application | S3 EL4-VIL-SSS-REQ-00229, p.50 | Restore its required application services independently without restarting CC or DGP | Do not assume loss of RCU has no operational impact; classify affected services |
| ELEKTRA Core - DGP application | S3 pp.37-40/48/50, EL4-VIL-SSS-REQ-00285; EL4-VIL-SSS-REQ-00229; EL4-VIL-SSS-REQ-01006 | Collect/serialize diagnosis; maintain redundant diagnosis paths and recover independently | DGP restart must not restart CC/RCU; diagnosis loss may affect restoration and RAM observability |
| CAR-RED / GENSYS runtime and libraries | S4 section 1.2.4 | Support redundant application execution, messaging and restart isolation | Includes CAR library, EP handler library and CAR console; exact mechanism ownership is a design allocation, not specified by S1 |
| TAS Platform Core - NMR service | S3 EL4-VIL-SSS-REQ-00181; EL4-VIL-SSS-REQ-00182 | Core CN fault isolation, supported degraded operation, synchronization and reintegration | Basic 2x2oo2 versus geo 4x2oo2; diverse-channel safety does not imply immunity to every common SW fault |
| ECMUX application, including diagnosis/maintenance and field-specific elements | S3 section 4.9; S4 section 1.2.4 | Maintain field-element command/notification paths, isolate relevant faults, restore OC service and report degradation | Includes the specified IO/signal/TDS elements; assess partial field-service loss, not only whole-instance outage |
| TAS Platform J4S fault-tolerance service | S3 EL4-VIL-SSS-REQ-00227; EL4-VIL-SSS-REQ-00228 | ECMUX redundant-node operation, fault reaction and reintegration | Basic 2x1oo1; geo standby behaviour remains In negotiation |
| RaSTA communication functions and supporting RJC libraries | S3 sections 4.5.2.2/4.7; S4 section 3.2 | Preserve transport paths; reconnect; report connection/channel status; enforce approved interface timing | RJC is a supplier/component dependency; confirm exact library-to-interface mapping in design |
| Datalogger/application diagnosis function | S3 EL4-VIL-SSS-REQ-00285; EL4-VIL-SSS-REQ-00288; EL4-VIL-SSS-REQ-00294; EL4-VIL-SSS-REQ-00295; EL4-VIL-SSS-REQ-00296; EL4-VIL-SSS-REQ-00297 | Continued diagnosis with a remaining node, buffered delivery and detection of lost diagnosis | Primarily ELEKTRA Core/DGP; ECMUX feeds diagnosis through its internal interface |
| TAS Platform Core - CDS and VIL consistency checks | S3 EL4-VIL-SSS-REQ-01458; EL4-VIL-SSS-REQ-01459; EL4-VIL-SSS-REQ-01460, pp.44-45 | Authorize valid VM versions and prevent incompatible/duplicate nodes becoming active | Authorization rejection can cause permanent shutdown; failure behaviour of CDS is a RAM dependency requiring analysis |
| VIL application/VM lifecycle and update coordination | S3 EL4-VIL-SSS-REQ-01155; EL4-VIL-SSS-REQ-01156; EL4-VIL-SSS-REQ-01457, S6 software actualization | Controlled application restart, shutdown, rolling updates, synchronized startup and service re-entry | Functional owner proposal; **not** a confirmed separately named SW component |
| CAE data preparation / OREST | S4 section 1.2.5; S3 EL4-VIL-SSS-REQ-01505 | Provide correct compatible station data for update/restart | Offline enabling tool, not a continuously required runtime block unless design proves otherwise |
| IPS / ADM / external diagnosis collector | S1/S6 and S4 section 3.2 | Infrastructure placement/repair, activation support, external diagnosis and recovery dependencies | Outside VIL application SW; retain explicit interface obligations, not fictional internal ownership |

### 5.2 Main result: requirements of chapter 3.1.4.3.2 allocated to VIL SW components

Chapter 3.1.4.3.2 "VIL Availability" of S1 contains **six requirements**. Sub-chapter "IPS Availability" is deleted/empty and contributes none. All six are Accepted, Mandatory, Scope System, Target Release DIL_OBB_1.0.x (EL4-DIL-SSS-REQ-00818 additionally IFC_BLOCK_1.0.0).

**Allocation rule:** the numerical availability targets (EL4-DIL-SSS-REQ-00587, 00569, 00570) are **VIL-instance targets** and are **not divided into per-component availability values**: the inputs for a defensible split (component event rates, topology, common dependencies, recovery coverage) do not exist yet. What is allocated to each SW component is the **function, behaviour and timing** that the instance target depends on. Roles are written as **Lead**, **Supporting** or **Not allocated**, rather than introducing new abbreviations.

#### How to read the allocation and verification columns

The tables use existing source requirement identifiers. No new requirement or test identifiers are assigned.

- **Allocated obligation:** the behaviour the component contributes to satisfying the original requirement.
- **Recommended clarification or implementation detail:** a recommendation for review, not an additional approved requirement. The DPR recommendation for full-redundancy restoration in less than 10 min remains a recommendation, not a contractual HW repair limit.
- **Verification method:** the review, analysis or test needed to demonstrate the behaviour. These are planned checks, not completed tests or compliance results.

For example, Core service continuity after a CN failure is checked by fault injection and observing the surviving service. Demonstrating overall numerical availability additionally requires the reviewed VIL-instance RAM model and justified data.

#### Table A - Requirements (source: S1, chapter 3.1.4.3.2)

| # | Requirement ID | Title | Requirement text (S1, shortened where noted) | Value / class | Parent allocation (S1) |
| --- | --- | --- | --- | --- | --- |
| 1 | EL4-DIL-SSS-REQ-00587 | Availability - [VIL-Instance] - Overall | The [VIL-Instance] shall have a class 2 overall availability of at least 99.995 %. | A >= 0.99995 (class 2) | DIL, VIL |
| 2 | EL4-DIL-SSS-REQ-00569 | Availability distribution of [VIL-Instance] | The distribution of the availability of a [VIL-Instance] must correspond to class 2. This means in particular an availability of 99.9979 % (MTTR = 6 h), 99.999 % (MTTR = 10 min), 99.9996 % (MTTR = 2 min). | 0.999979 / 0.99999 / 0.999996 | DIL, VIL |
| 3 | EL4-DIL-SSS-REQ-00570 | Availability - [VIL-Instance] - Outages with no operational Impact | Outages of a [VIL-Instance] with no operational impact shall have an availability of at least 99.7154 % (defect class FK4). | A >= 0.997154 | DIL, VIL |
| 4 | EL4-DIL-SSS-REQ-00573 | Availability - VIL - Minor SW/HW Change | Minor changes of the [VIL] [SW] (= Patches) or the [HW] shall be carried out without operational restrictions. | No operational restriction | DIL, VIL, IPS |
| 5 | EL4-DIL-SSS-REQ-00818 | Availability - VIL - Major SW/HW Change | Major changes of the [VIL] [SW], especially with safety impact, (= Upgrades) or the [HW] shall be carried out during operational breaks. | Execution in operational breaks | DIL, VIL, IPS |
| 6 | EL4-DIL-SSS-REQ-00574 | Availability - VIL - Operational Downtime | The operational downtime shall not be longer than the restart time of the affected component, as well as the time for the re-integration into the overall system. | Downtime <= restart + re-integration | DIL, VIL, IPS |

Historical IDs EL4-DIL-SSS-REQ-00571 (auto-correction 10 min) and -00572 (2 min) are not part of the chapter; per S2 they were merged into EL4-DIL-SSS-REQ-00569.

#### Table B - Allocation matrix (requirement x VIL SW component)

Component columns follow Section 5.1: **CC / RCU / DGP** = ELEKTRA Core applications; **CAR-RED** = CAR-RED/GENSYS runtime; **NMR** = TAS Platform Core NMR service; **CDS** = TAS Platform Core Cluster Deployment Supervisor; **ECMUX** = ECMUX application; **J4S** = TAS Platform J4S service; **RaSTA** = RaSTA/RJC communication functions; **VIL lifecycle and update coordination** describes a function whose implementation owner remains to be confirmed, not a separately established SW component name.

| Requirement | CC | RCU | DGP | CAR-RED | NMR | CDS | ECMUX | J4S | RaSTA | VIL lifecycle and update coordination |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 Overall | Supporting | Supporting | Supporting | Supporting | Lead | Supporting | Supporting | Lead | Supporting | Supporting |
| EL4-DIL-SSS-REQ-00569 Distribution | Supporting | Supporting | Supporting | Supporting | Lead | Supporting | Supporting | Lead | Supporting | Supporting |
| EL4-DIL-SSS-REQ-00570 No-impact outages | Not allocated | Not allocated | Lead | Not allocated | Lead | Not allocated | Supporting | Lead | Supporting | Not allocated |
| EL4-DIL-SSS-REQ-00573 Minor change | Supporting | Supporting | Supporting | Supporting | Supporting | Supporting | Supporting | Supporting | Supporting | Lead |
| EL4-DIL-SSS-REQ-00818 Major change | Supporting | Supporting | Supporting | Not allocated | Supporting | Supporting | Supporting | Supporting | Not allocated | Lead |
| EL4-DIL-SSS-REQ-00574 Operational downtime | Supporting | Supporting | Supporting | Not allocated | Lead | Supporting | Supporting | Lead | Supporting | Lead |

#### Table C - Allocated obligations per requirement and component

"SSS_VIL basis" lists candidate existing source requirements, not an approved trace. The last column describes recommendations in words; Section 6 provides their full wording.

| Parent | SW component | Role | Allocated obligation | SSS_VIL / SSS_DIL basis | Recommended clarification or implementation detail |
| --- | --- | --- | --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 | TAS NMR (Core) | Lead | Hot-hot 2x2oo2 service; Core service continues after HW failure of one CN | EL4-VIL-SSS-REQ-00181 (geo: 00182) | Core service continuity after one CN failure |
| EL4-DIL-SSS-REQ-00587 | TAS J4S (ECMUX) | Lead | Hot-hot 2x1oo1 service; ECMUX service continues after loss of one node | EL4-VIL-SSS-REQ-00227 (geo: 00228) | ECMUX service continuity after one redundant-node failure |
| EL4-DIL-SSS-REQ-00587 | NMR + J4S | Lead | Only one synchronized subgroup remains active after partition | EL4-VIL-SSS-REQ-00222 | Split-brain prevention |
| EL4-DIL-SSS-REQ-00587 | CC, RCU, DGP | Supporting | Continue application service synchronously on the remaining node | EL4-VIL-SSS-REQ-00181, 00229 | Core service continuity after one CN failure, CC/RCU/DGP restart isolation |
| EL4-DIL-SSS-REQ-00587 | CAR-RED / GENSYS | Supporting | Provide CHILL runtime supporting hot-hot processing | EL4-VIL-SSS-REQ-01465 | Core service continuity after one CN failure |
| EL4-DIL-SSS-REQ-00587 | ECMUX application | Supporting | Keep field-element command/notification paths operating on the remaining node | EL4-VIL-SSS-REQ-00227; S3 section 4.7.1 | ECMUX service continuity after one redundant-node failure |
| EL4-DIL-SSS-REQ-00587 | RaSTA | Supporting | One transport channel per redundant node so connections stay available with one node | S3 section 4.7 (EL4-VIL-SSS-REQ-01006), EL4-VIL-SSS-REQ-00288 | Communication-path continuity, recovery and status reporting |
| EL4-DIL-SSS-REQ-00587 | CDS | Supporting | Prevent invalid/duplicate/incompatible VMs from becoming active | EL4-VIL-SSS-REQ-01458, 01459, 01460 | VM/application configuration authorization and compatibility |
| EL4-DIL-SSS-REQ-00587 | VIL lifecycle and update coordination | Supporting | Two (basic) / four (geo) redundant nodes started and supervised as one instance | EL4-VIL-SSS-REQ-00218 (geo: 00219) | Core service continuity after one CN failure, ECMUX service continuity after one redundant-node failure |
| EL4-DIL-SSS-REQ-00569 | NMR | Lead | Detect node failure, recover automatically, reintegrate CN within the 120 s / 600 s criteria | EL4-DIL-SSS-REQ-00439, EL4-DIL-SSS-REQ-00991, EL4-VIL-SSS-REQ-00221 | Operational service restoration within 120 s, Operational service restoration within 600 s, Numeric failure detection/reaction limits, Interruption-free node reintegration, DPR recommendation: full-redundancy restoration in less than 600 s |
| EL4-DIL-SSS-REQ-00569 | J4S | Lead | Same for ECMUX nodes | EL4-DIL-SSS-REQ-00439, EL4-DIL-SSS-REQ-00991, EL4-VIL-SSS-REQ-00221 | Operational service restoration within 120 s, Operational service restoration within 600 s, Numeric failure detection/reaction limits, Interruption-free node reintegration, DPR recommendation: full-redundancy restoration in less than 600 s |
| EL4-DIL-SSS-REQ-00569 | CC, RCU, DGP, ECMUX | Supporting | Automatic stop/restart of the failed application with restart isolation (RCU: RCU only; DGP: DGP only; CC: CC + RCU); restore state | EL4-VIL-SSS-REQ-01155, 00229, 01461 | Operational service restoration within 120 s, Operational service restoration within 600 s, CC/RCU/DGP restart isolation |
| EL4-DIL-SSS-REQ-00569 | CAR-RED / GENSYS | Supporting | Runtime support for isolated application restart and re-synchronization | EL4-VIL-SSS-REQ-00229, 01465 | CC/RCU/DGP restart isolation |
| EL4-DIL-SSS-REQ-00569 | DGP | Supporting | Diagnosis available whenever one node runs, so faults stay detectable | EL4-VIL-SSS-REQ-00285, 00288 | Application diagnosis continuity |
| EL4-DIL-SSS-REQ-00569 | RaSTA | Supporting | Reconnect after restart; failed path must not block other paths | EL4-VIL-SSS-REQ-00221, 00244, 00245 | Communication-path continuity, recovery and status reporting |
| EL4-DIL-SSS-REQ-00569 | CDS | Supporting | Authorization on restart must not delay or block valid recovery | EL4-VIL-SSS-REQ-01458 | VM/application configuration authorization and compatibility |
| EL4-DIL-SSS-REQ-00569 | VIL lifecycle and update coordination | Supporting | Controlled/synchronized (re)start of redundant nodes; numeric detection times (TBD in EL4-VIL-SSS-REQ-01462; EL4-VIL-SSS-REQ-01463; EL4-VIL-SSS-REQ-01464) | EL4-VIL-SSS-REQ-00220, 01155, 01462-01464 | Operational service restoration within 120 s, Operational service restoration within 600 s, Numeric failure detection/reaction limits |
| EL4-DIL-SSS-REQ-00570 | DGP | Lead | Provide application diagnosis; record redundancy loss events with start/end | EL4-VIL-SSS-REQ-00285, 00288, 00294-00297 | Application diagnosis continuity, Redundancy-loss and FK4 recording |
| EL4-DIL-SSS-REQ-00570 | NMR | Lead | Detect redundancy loss of a CN, report it, restore full redundancy | EL4-DIL-SSS-REQ-00439, EL4-VIL-SSS-REQ-00181 | DPR recommendation: full-redundancy restoration in less than 600 s, Redundancy-loss and FK4 recording |
| EL4-DIL-SSS-REQ-00570 | J4S | Lead | Detect redundancy loss of an ECMUX node, report it, restore full redundancy | EL4-DIL-SSS-REQ-00439, EL4-VIL-SSS-REQ-00227 | DPR recommendation: full-redundancy restoration in less than 600 s, Redundancy-loss and FK4 recording |
| EL4-DIL-SSS-REQ-00570 | ECMUX application | Supporting | Feed diagnosis to DGP via the internal diagnosis interface | EL4-VIL-SSS-REQ-00564, 01006 | Redundancy-loss and FK4 recording |
| EL4-DIL-SSS-REQ-00570 | RaSTA | Supporting | Report connection and transport-channel status at startup and on change | EL4-VIL-SSS-REQ-00244, 00245 (origin EL4-DIL-SSS-REQ-00329; EL4-DIL-SSS-REQ-00330) | Communication-path continuity, recovery and status reporting |
| EL4-DIL-SSS-REQ-00573 | VIL lifecycle and update coordination | Lead | Rolling patch: withdraw, update, restart, reintegrate one partner at a time without operational restriction | EL4-VIL-SSS-REQ-00218, 00221; EL4-DIL-SSS-REQ-01302, EL4-DIL-SSS-REQ-01294 | Minor-change continuity |
| EL4-DIL-SSS-REQ-00573 | NMR, J4S | Supporting | Operate with one partner withdrawn; reintegrate the patched partner seamlessly | EL4-VIL-SSS-REQ-00221; EL4-DIL-SSS-REQ-00443 | Interruption-free node reintegration, Minor-change continuity |
| EL4-DIL-SSS-REQ-00573 | CDS | Supporting | Version consistency check between nodes and applications during update | EL4-VIL-SSS-REQ-01458, 01459, 01460 | VM/application configuration authorization and compatibility |
| EL4-DIL-SSS-REQ-00573 | CC, RCU, DGP, ECMUX, CAR-RED | Supporting | Keep running on the unpatched node; compatible with the mixed-version window | EL4-VIL-SSS-REQ-01459, 01460 | Minor-change continuity, VM/application configuration authorization and compatibility |
| EL4-DIL-SSS-REQ-00573 | RaSTA | Supporting | Interfaces remain connected through the node that stays in service | EL4-VIL-SSS-REQ-00288, S3 section 4.7 | Communication-path continuity, recovery and status reporting |
| EL4-DIL-SSS-REQ-00818 | VIL lifecycle and update coordination | Lead | Controlled maintenance shutdown (graceful application shutdown, OS shutdown, no automatic reboot); activation only in an operational break | EL4-VIL-SSS-REQ-01156, 01457 | Major changes during authorized operational breaks |
| EL4-DIL-SSS-REQ-00818 | CC, RCU, DGP, ECMUX | Supporting | Graceful shutdown and controlled restart; persistent state handling | EL4-VIL-SSS-REQ-01156, 01502 | Major changes during authorized operational breaks |
| EL4-DIL-SSS-REQ-00818 | NMR, J4S | Supporting | Coordinated restart/reintegration of all nodes after upgrade | EL4-DIL-SSS-REQ-01294, EL4-DIL-SSS-REQ-01298 | Numeric restart/reintegration limits, Major changes during authorized operational breaks |
| EL4-DIL-SSS-REQ-00818 | CDS | Supporting | Authorize/reject new image versions; permanent shutdown on rejection | EL4-VIL-SSS-REQ-01458, 01460 | VM/application configuration authorization and compatibility |
| EL4-DIL-SSS-REQ-00574 | NMR, J4S | Lead | Bound reintegration time of the restarted CN/ECMUX node | EL4-VIL-SSS-REQ-00221, 00220 | Numeric restart/reintegration limits |
| EL4-DIL-SSS-REQ-00574 | VIL lifecycle and update coordination | Lead | Bound restart time; define numeric limits and end-to-end critical path | EL4-VIL-SSS-REQ-00220, 01155 | Numeric restart/reintegration limits |
| EL4-DIL-SSS-REQ-00574 | CC, RCU, DGP, ECMUX | Supporting | Restore operational state and interfaces after restart (readiness) | EL4-VIL-SSS-REQ-01155, 00229 | Operational service restoration within 120 s, Operational service restoration within 600 s, Numeric restart/reintegration limits |
| EL4-DIL-SSS-REQ-00574 | RaSTA | Supporting | Re-establish connections within the restart/reintegration bound | EL4-VIL-SSS-REQ-00221 | Communication-path continuity, recovery and status reporting |
| EL4-DIL-SSS-REQ-00574 | CDS | Supporting | Startup authorization within the restart bound | EL4-VIL-SSS-REQ-01458 | Numeric restart/reintegration limits, VM/application configuration authorization and compatibility |

#### Reading the result

- **Every one of the six requirements has at least one lead component**, and all ten component groups carry at least one allocation.
- The **recovery requirements (EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00574)** depend on the same chain: detection, application restart, reintegration, reconnection. The numerical timing limits cannot be allocated per stage until SSS_VIL REQ-01462/01463/01464 (detection time, TBD) are filled.
- **EL4-DIL-SSS-REQ-00573; EL4-DIL-SSS-REQ-00818** are driven by lifecycle, CDS and NMR/J4S behaviour rather than by the applications themselves. Their release allocation (S3 EL4-VIL-SSS-REQ-00221; EL4-VIL-SSS-REQ-01445: 1.1.0; S6 EL4-DIL-SSS-REQ-01302: 2.0.0) is a finding (F03).
- Components **owned outside VIL SW** (IPS for HW placement/repair, ADM for external diagnosis, OREST for station data) carry interface obligations only and are intentionally not listed as VIL SW components.
- **Ownership to confirm:** the RaSTA/RJC and CDS rows are functional proposals; if the design assigns the function to a different library or process, only the owner column changes, not the obligation.

### 5.3 Parent-to-component traceability matrix

Existing SSS_VIL references in this table are **candidate supporting links** unless stated as their explicit origins. Their presence does not establish that a formal DIL-RAMS-to-component trace already exists.

| Parent | Lead functional allocation | Other required contributors | Existing candidate child requirements | Recommended clarification or implementation detail | Verification method |
| --- | --- | --- | --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 | ELEKTRA Core/NMR and ECMUX/J4S; VIL integration owns aggregate result | CAR-RED/GENSYS, required RaSTA paths, lifecycle, CDS, IPS placement and dependencies | EL4-VIL-SSS-REQ-00218, 00181, 00227, 00222; geo: 00219, 00182, 00228 | Core service continuity after one CN failure; ECMUX service continuity after one redundant-node failure; Split-brain prevention; CC/RCU/DGP restart isolation; Interruption-free node reintegration; VM/application configuration authorization and compatibility; Communication-path continuity, recovery and status reporting | Baseline, configuration and traceability review; Core CN, ECMUX-node and shared-host failure tests; Automatic recovery and node reintegration tests; CC/RCU/DGP/ECMUX application failure tests; Partition, invalid/duplicate VM and CDS failure/rejection tests; Supported-load tests and release/variant coverage review plus RAM model |
| EL4-DIL-SSS-REQ-00569 | Recovery chain in Core/NMR and ECMUX/J4S | CC/RCU/DGP, runtime supervision, RaSTA reconnect, diagnosis, lifecycle and IPS where intervention is required | EL4-VIL-SSS-REQ-00221, 01155, 00229, 01461-01464, 00285; S6 EL4-DIL-SSS-REQ-00439; EL4-DIL-SSS-REQ-00991 | Operational service restoration within 120 s; Operational service restoration within 600 s; CC/RCU/DGP restart isolation; Application diagnosis continuity; Numeric failure detection/reaction limits; Interruption-free node reintegration; DPR recommendation: full-redundancy restoration in less than 600 s | Core CN, ECMUX-node and shared-host failure tests; Automatic recovery and node reintegration tests; CC/RCU/DGP/ECMUX application failure tests; Communication/channel/interface failure tests; Diagnosis continuity and recovery tests; Partition, invalid/duplicate VM and CDS failure/rejection tests; scenario-specific RAM model |
| EL4-DIL-SSS-REQ-00570 | Degradation monitoring in NMR/J4S plus DGP/ECMUX diagnosis | RaSTA status functions, IPS/ADM and maintenance | EL4-VIL-SSS-REQ-00285, 00288, 00244, 00245, 01006; architectural support 00181/00227 | Application diagnosis continuity; DPR recommendation: full-redundancy restoration in less than 600 s; Redundancy-loss and FK4 recording | Core CN, ECMUX-node and shared-host failure tests; Diagnosis continuity and recovery tests; Degraded operation, repair and FK4 record checks plus FK4 exposure records |
| EL4-DIL-SSS-REQ-00573 | Update/lifecycle coordination across Core and ECMUX | NMR, J4S, CAR-RED, RaSTA, CDS, configuration/build chain, IPS/ADM | EL4-VIL-SSS-REQ-00218, 00221, 01458-01460, 01445; S6 EL4-DIL-SSS-REQ-01302; EL4-DIL-SSS-REQ-01294 | Minor-change continuity; Numeric restart/reintegration limits; VM/application configuration authorization and compatibility | Rolling patch and supporting HW replacement tests; Partition, invalid/duplicate VM and CDS failure/rejection tests; Supported-load tests and release/variant coverage review |
| EL4-DIL-SSS-REQ-00818 | Controlled maintenance and activation of Core and ECMUX | CC/RCU/DGP, lifecycle, CDS, OMC authorization, IPS/ADM | EL4-VIL-SSS-REQ-01156; EL4-VIL-SSS-REQ-01457, 01458-01460; S6 EL4-DIL-SSS-REQ-01294; EL4-DIL-SSS-REQ-01298 | Numeric restart/reintegration limits; Major changes during authorized operational breaks; VM/application configuration authorization and compatibility | Major upgrade, maintenance shutdown and activation tests; Partition, invalid/duplicate VM and CDS failure/rejection tests; Supported-load tests and release/variant coverage review |
| EL4-DIL-SSS-REQ-00574 | Lifecycle plus end-to-end re-entry of Core and ECMUX | NMR/J4S, CC/RCU, RaSTA reconnect, state reload and field/adjacent-system interrogation | EL4-VIL-SSS-REQ-00220; EL4-VIL-SSS-REQ-00221; EL4-VIL-SSS-REQ-01155; EL4-VIL-SSS-REQ-00229; supporting maintenance/consistency requirements | Operational service restoration within 120 s; Operational service restoration within 600 s; CC/RCU/DGP restart isolation; Numeric restart/reintegration limits; Major changes during authorized operational breaks | Automatic recovery and node reintegration tests; CC/RCU/DGP/ECMUX application failure tests; Communication/channel/interface failure tests; Major upgrade, maintenance shutdown and activation tests; Cold/synchronized startup timing tests |

**Reading the last two columns:** recommendations are written in words and explained further in Section 6. Verification methods are planned checks detailed in Section 7.2, not successful verification results.

### 5.4 Supporting diagnosis allocation

EL4-DIL-SSS-REQ-00329 and EL4-DIL-SSS-REQ-00330 are outside chapter 3.1.4.3.2 but explicitly considered in S2. S1 allocates EL4-DIL-SSS-REQ-00329 to DIL/IPS and EL4-DIL-SSS-REQ-00330 to DIL/IPS/ADM; the latter remains In negotiation. S3 EL4-VIL-SSS-REQ-00244; EL4-VIL-SSS-REQ-00245 explicitly references both as origins and allocates reporting functions to Core/ECMUX.

Allocate connection and transport-channel reporting to the relevant RaSTA endpoints, with DGP/datalogger forwarding and ECMUX diagnosis input. Endpoint status alone does **not** prove that the location of every underlying open/closed-network fault is diagnosable; IPS/ADM must provide infrastructure correlation. Diagnosis loss must be detectable even when the normal delivery channel is unavailable.

## 6. Recommended implementation details and clarifications

**All entries below are recommendations for review traced to source requirements, not new approved requirements.** Component specifications, releases and safety acceptance require review through the requirements/change process. No SW FIT allocations are invented.

This table describes recommendations, their responsible component/function and the evidence needed to check them. Original requirement IDs provide traceability. No new requirement IDs are assigned and the source baseline is not changed.

| Subject | Source requirement / supporting trace | Recommended implementation detail or clarification | Component / function | Verification method and unresolved parameter |
| --- | --- | --- | --- | --- |
| Core service continuity after one CN failure | EL4-DIL-SSS-REQ-00587; EL4-VIL-SSS-REQ-00181 | In basic configuration, ELEKTRA Core shall maintain its specified service after a HW failure affecting one CN, with the remaining CN operating within its approved safety constraints. | Core/NMR and CAR-RED integration | Core CN, ECMUX-node and shared-host failure tests; supported fault set and service-loss criteria approved |
| ECMUX service continuity after one redundant-node failure | EL4-DIL-SSS-REQ-00587; EL4-VIL-SSS-REQ-00227 | In basic configuration, ECMUX shall maintain its specified field-interface service after a HW failure affecting one ECMUX redundant node. | ECMUX/J4S | Core CN, ECMUX-node and shared-host failure tests; observe every required field-interface path |
| Split-brain prevention | EL4-DIL-SSS-REQ-00587; EL4-DIL-SSS-REQ-00569; EL4-VIL-SSS-REQ-00222 | Following a partition of redundant nodes, the VIL redundancy services shall permit at most one synchronized subgroup to remain active. | NMR, J4S and VIL integration | Partition, invalid/duplicate VM and CDS failure/rejection tests; approved selection/fencing rules, service-loss accounting and partition recovery |
| Operational service restoration within 120 s | EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00574; EL4-VIL-SSS-REQ-01155; EL4-VIL-SSS-REQ-01462; EL4-VIL-SSS-REQ-01463; EL4-VIL-SSS-REQ-01464 | For each approved 2 min automatic-correction scenario, the affected VIL SW shall restore the required operational service within 120 s of service loss, including any detection delay after that loss, fault reaction, restart, synchronization, interface recovery and operational-state restoration. | Affected Core/ECMUX application plus platform/lifecycle | Automatic recovery and node reintegration tests; CC/RCU/DGP/ECMUX application failure tests; Communication/channel/interface failure tests; scenario list and timestamp definitions approved; maximum criterion reflects LH "within", not merely a mean |
| Operational service restoration within 600 s | EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00574; EL4-VIL-SSS-REQ-01155; EL4-VIL-SSS-REQ-01462; EL4-VIL-SSS-REQ-01463; EL4-VIL-SSS-REQ-01464 | For each approved 10 min automatic-correction scenario, the affected VIL SW shall restore the required operational service within 600 s of service loss using the same end-to-end boundary as Operational service restoration within 120 s. | Affected Core/ECMUX application plus platform/lifecycle | Automatic recovery and node reintegration tests; CC/RCU/DGP/ECMUX application failure tests; Communication/channel/interface failure tests; define classification relative to 2 min scenarios and avoid double counting |
| CC/RCU/DGP restart isolation | EL4-DIL-SSS-REQ-00587; EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00574; EL4-VIL-SSS-REQ-01155; EL4-VIL-SSS-REQ-00229 | Core restart management shall limit application restart to RCU for RCU failure, DGP for DGP failure, and CC plus RCU for CC failure; the affected application shall restart across redundant nodes and both diverse channels where applicable. | Core lifecycle, CAR-RED and application teams | CC/RCU/DGP/ECMUX application failure tests; prove that uninvolved applications are not restarted; record affected service interruption |
| Application diagnosis continuity | EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00570; EL4-VIL-SSS-REQ-00285; EL4-VIL-SSS-REQ-00288 | The application-diagnosis function shall remain available with one operational redundant node, using the basic datalogger connection's transport channels on different nodes. | DGP/datalogger plus RaSTA | Diagnosis continuity and recovery tests; collector behaviour and detection of total delivery loss specified |
| Numeric failure detection/reaction limits | EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00439; EL4-DIL-SSS-REQ-00991; EL4-VIL-SSS-REQ-01462; EL4-VIL-SSS-REQ-01463; EL4-VIL-SSS-REQ-01464 | Each failure detection/reaction mechanism shall have an approved numeric timing limit compatible with the applicable end-to-end recovery requirement. | NMR/J4S, runtime supervision and communication teams | Automatic recovery and node reintegration tests; Communication/channel/interface failure tests; fill detection TBDs and document timing allocation; no invented per-stage values |
| Interruption-free node reintegration | EL4-DIL-SSS-REQ-00587; EL4-DIL-SSS-REQ-00569; EL4-VIL-SSS-REQ-00221 | When a redundant node starts while its VIL instance is operational, Core and ECMUX shall integrate it without interrupting that instance's specified service. | NMR/J4S, runtime and communication | Automatic recovery and node reintegration tests; full supported load and configuration/version checks; release gap addressed |
| DPR recommendation: full-redundancy restoration in less than 600 s | EL4-DIL-SSS-REQ-00569; EL4-DIL-SSS-REQ-00570; DPR recovery proposal | For approved automatically recoverable node faults, the recovery mechanisms shall restore the defined full-redundancy state in less than 600 s from detection of redundancy loss, without interrupting surviving service. | NMR/J4S and lifecycle; IPS interface where necessary | Automatic recovery and node reintegration tests; Degraded operation, repair and FK4 record checks; **new engineering proposal**, not a contractual 10 min maximum for HW repair; node/fault/start/end definitions required |
| Redundancy-loss and FK4 recording | EL4-DIL-SSS-REQ-00570; diagnosis support | The VIL diagnosis functions shall record the start, end, affected component and agreed FK4 classification of each detected redundancy-loss condition. | NMR/J4S event producers, ECMUX diagnosis and DGP | Degraded operation, repair and FK4 record checks; approved FK4 interpretation, location/identity and recovery records; do not classify all degradation as FK4 automatically |
| Minor-change continuity | EL4-DIL-SSS-REQ-00573; EL4-VIL-SSS-REQ-00221; EL4-VIL-SSS-REQ-01458; EL4-VIL-SSS-REQ-01459; EL4-VIL-SSS-REQ-01460; EL4-DIL-SSS-REQ-01302 | For each approved compatible minor patch or supporting HW-maintenance procedure, VIL update coordination shall preserve operational service while a redundancy partner is withdrawn, changed, restarted and reintegrated before proceeding to the next partner. | VIL lifecycle, Core/ECMUX, CDS and IPS/ADM interface | Rolling patch and supporting HW replacement tests; no operational restrictions; compatible version combinations, rollback and supported starting redundancy state approved |
| Numeric restart/reintegration limits | EL4-DIL-SSS-REQ-00574 | For every supported restart/activation procedure, VIL integration shall specify numeric restart and reintegration limits and demonstrate that operational downtime does not exceed their approved combined end-to-end critical-path bound. | Core/ECMUX lifecycle and interface integration | Major upgrade, maintenance shutdown and activation tests; Cold/synchronized startup timing tests; define overlap/parallelism, time origins and final operational-readiness criteria |
| Major changes during authorized operational breaks | EL4-DIL-SSS-REQ-00818; EL4-VIL-SSS-REQ-01156; EL4-VIL-SSS-REQ-01457 | The VIL shall activate a major change only within the authorized operational-break procedure, including controlled application/OS shutdown where required and completion of service re-entry before return to operation. | Core/ECMUX lifecycle with OMC/IPS/ADM | Major upgrade, maintenance shutdown and activation tests; maintenance shutdown shall not automatically reboot; subsequent activation is a separate authorized step |
| VM/application configuration authorization and compatibility | EL4-DIL-SSS-REQ-00587; EL4-DIL-SSS-REQ-00573; EL4-DIL-SSS-REQ-00818; EL4-VIL-SSS-REQ-01458; EL4-VIL-SSS-REQ-01459; EL4-VIL-SSS-REQ-01460 | The VIL consistency mechanisms shall prevent unauthorized, duplicate or incompatible VM/application configurations from becoming operational during startup, reintegration and update. | CDS plus Core/ECMUX consistency checks | Rolling patch and supporting HW replacement tests; Partition, invalid/duplicate VM and CDS failure/rejection tests; Supported-load tests and release/variant coverage review; test rejection and authorization-service loss without bypassing safety checks |
| Communication-path continuity, recovery and status reporting | EL4-DIL-SSS-REQ-00587; EL4-DIL-SSS-REQ-00569; EL4-VIL-SSS-REQ-00244; EL4-VIL-SSS-REQ-00245 and internal-interface requirements | Required VIL communication functions shall preserve or restore approved redundant paths and report connection/channel state changes without allowing a failed communication path to block recovery of an unaffected path. | RaSTA functions, Core CC/DGP and ECMUX | Communication/channel/interface failure tests; Diagnosis continuity and recovery tests; reconnection limits and fault containment established in component design |

For minor and major changes, change classification follows the approved impact analysis, not only the label "patch" or "upgrade". HW replacement remains an IPS/maintenance action with explicit VIL SW continuity obligations.

## 7. RAM model and verification strategy

### 7.1 Required instance model

Define required station service `S` using the actual configured Core, ECMUX and interface topology. Model unavailability as the union of service-loss events:

```text
U_VIL = P(Core service lost OR required ECMUX service lost
          OR required interface lost OR shared dependency lost)

Conservative component/event-budget condition, if used:
sum(b_i) <= U_VIL_limit
P(service-loss event i) <= b_i

For mutually independent series blocks only:
A_VIL = product(A_i)

Independent identical 1oo2 illustration only:
U_1oo2 = u_node^2
```

The series product and squared-unavailability expression are **not valid substitutes for the actual common-cause model**. Partial station restrictions require a service/severity definition. Shared events must not be double counted in an exact model; a union-bound budget can deliberately be conservative.

No numeric `b_i` shares are assigned here: component event rates, topology, common dependencies and recovery coverage are insufficient. In particular, assigning 99.995% separately to Core and ECMUX would not ensure 99.995% for their joint service.

Use a fault tree or state model appropriate to the evidence. Include fully redundant, degraded, service-lost/restarting and maintenance states; include partition/authorization effects and the time spent exposed to a second failure. Separate HW random failures from systematic SW failure scenarios and operationally measured SW incidents.

Recovery timing shall be decomposed without double-counting concurrent stages:

```text
t_service_restore = elapsed time on the actual critical path from service loss
                    to restored operational service

Typical sequential contributors:
detection after loss + fault reaction + self-test/restart + state synchronization
+ connection recovery + application/field-state re-entry

t_redundancy_restore = elapsed time from defined redundancy-loss detection
                       to re-established approved redundancy
```

Self-test/safe-state steps cited by S2 must be confirmed for the actual failure mechanism in platform design; they are not automatically the same sequence for every fault. A surviving node can maintain service while redundancy takes longer to restore.

### 7.2 Verification matrix

This table describes recommended reviews, analyses and tests. No new test identifiers are assigned. Pass criteria describe what the evidence must demonstrate. No activities are reported as executed by this analysis; only source review and report checks were performed.

All tests require approved fault injection, safety controls, timestamped observations and traceable reports. Testing establishes functional/timing performance for tested scenarios, not statistical proof of extreme availability by itself.

| Verification scenario | Required observations / pass basis |
| --- | --- |
| Baseline/configuration review | Approved service definition, topology, releases and all six parent-to-child-to-test links; component and external-interface owners assigned |
| One Core CN failure; one ECMUX-node failure; shared-host loss | Correct fault isolation, safe surviving service and all required paths; correlated failures classified once; Basic and geo claims tested only where supported |
| Automatic fault recovery and node reintegration | Complete service recovery within 120 s or 600 s for the approved class; uninterrupted reintegration; separately measure proposed < 600 s redundancy restoration for recoverable node faults |
| CC, RCU, DGP and ECMUX application failures | All-replica/diverse-channel behaviour per EL4-VIL-SSS-REQ-01155; restart isolation per EL4-VIL-SSS-REQ-00229; actual affected service downtime and restoration |
| Loss of one transport channel, complete connection, internal interface and OC/adjacent path | Continued redundant path where supported; detection/reaction and reconnect limits; actual service readiness, not only socket-up status |
| DGP/collector outage; diagnosis-channel failover; buffer overflow and restart | EL4-VIL-SSS-REQ-00285; EL4-VIL-SSS-REQ-00288 continuity; status reports at startup/change; bounded recovery; buffer and loss indication per EL4-VIL-SSS-REQ-00294; EL4-VIL-SSS-REQ-00295; EL4-VIL-SSS-REQ-00296; EL4-VIL-SSS-REQ-00297 |
| Prolonged degraded operation and repair | FK4 classification and exposure timestamps; independent service-loss accounting; escalation for unrecoverable faults; restoration of full redundancy |
| Supported rolling patches and HW replacement | No operational restrictions; each reintegration completed before next withdrawal; permitted version combinations and adverse/failure cases including rollback assessed |
| Major upgrade/maintenance shutdown and activation | Authorized break; controlled shutdown without auto-reboot; complete state/interface restoration; downtime within approved restart/reintegration bound |
| Cold/synchronized startup at representative maximum load | Startup-window behaviour per EL4-VIL-SSS-REQ-00220, applicable reintegration path, final service readiness and worst supported critical-path time |
| Network partition; invalid/duplicate VM; CDS failure or rejection | One active synchronized subgroup at most; no invalid activation; measure safe shutdown/service impact and recovery; no bypass of authorization |
| Full configured station workload and later-release feature review | Required Core/ECMUX capacities and interfaces maintained during recovery/update; release and variant coverage documented without extending Basic results to geo |

Use the agreed worst supported station/configuration and degraded conditions for timing tests. S3 allows Core communication with up to four ECMUX instances and ECMUX control of up to 400 OCs; this is a load/configuration boundary, not four ECMUX redundancy partners.

Statistical verification shall combine reviewed RAM models, justified HW inputs, qualified SW processes, scenario tests and FRACAS/operational evidence. Under a Poisson assumption, zero events over exposure `T` give the one-sided upper rate `lambda_upper = -ln(1 - confidence)/T`; therefore a short zero-failure test cannot justify the DPR's very low rates.

## 8. Findings, risks and decisions required

| ID | Priority | Finding and evidence | RAM / requirements impact | Required disposition |
| --- | --- | --- | --- | --- |
| F01 | High | EL4-DIL-SSS-REQ-00569: S1 manual MTTR 6 h; S2 0.5 h; S5 Table 9 manual 225 min and section 4.1 manual MRT 0.5 h | Material model/input conflict; factor 12 in conditional MUT between S1/S2 | RAM + requirements owner to confirm approved manual restoration basis and update DPR/plan/model |
| F02 | High | S5 Table 9 shows 99.9999% for VIL 10 min, whereas S1/S2 specify 99.999% | Factor 10 discrepancy in unavailability | Reconcile to the approved parent baseline; do not silently select the stricter figure |
| F03 | High | S1 EL4-DIL-SSS-REQ-00573 targets 1.0.x; S3 EL4-VIL-SSS-REQ-00221; EL4-VIL-SSS-REQ-01445 target 1.1.0; S6 EL4-DIL-SSS-REQ-01302 targets 2.0.0 | Patch continuity/reintegration evidence may not cover the delivery of the parent requirement | Resolve release allocation, implementation evidence or formally approved deviation |
| F04 | High | EL4-VIL-SSS-REQ-01155 restarts the affected application on all nodes; Core isolation is defined by EL4-VIL-SSS-REQ-00229 | A systematic SW fault can defeat availability replication | Model/test application-wide service loss; do not claim HW redundancy masks it |
| F05 | High | EL4-VIL-SSS-REQ-01462; EL4-VIL-SSS-REQ-01463; EL4-VIL-SSS-REQ-01464 detection limits are TBD; EL4-VIL-SSS-REQ-00221 has no recovery duration | 120/600 s service restoration is not yet verifiable end-to-end | Approve numeric component timing budgets and recovery scenarios |
| F06 | High | Hot-hot architecture and S2 CN results do not cover the complete VIL service/dependency boundary | Apparent numerical margin can conceal ECMUX, common-cause or interface losses | Complete the instance model and dependency/fault-containment analysis |
| F07 | High | S1 main EL4-DIL-SSS-REQ-00818 text requires breaks; associated LH asks for redundancy takeover; PH describes a no-operational-VSTW interval of 3-4 min. S2 claims seamless takeover | Conflicting expectations for safety-relevant updates | Obtain an approved update concept and clarify hierarchy of main requirement versus supporting LH/PH text |
| F08 | High | S6 EL4-DIL-SSS-REQ-01294 describes node-by-node activation but is In negotiation and notes a mismatch to customer requirements. EL4-VIL-SSS-REQ-01156 cites it while shutting down the entire instance | Maintenance/update sequencing is not reconciled | Review serial/parallel activation, whole-instance shutdown and patch/upgrade variants together |
| F09 | Medium | EL4-DIL-SSS-REQ-00574 is relative to undefined restart/reintegration durations | An arbitrarily long restart could appear compliant | Add approved numeric limits and service-readiness endpoints; treat PH 3-4 min as a clarification input, not a universal agreed limit |
| F10 | Medium | EL4-DIL-SSS-REQ-00570 describes "outages" without operational impact; classification and clock rules are absent | FK4 and service-loss accounting can be mixed | Agree degraded-state/FK4 measurement and transition rules |
| F11 | Medium | S1/S2 comment refers to "equal availabilities", but VIL 2 min and 10 min values are unequal | Ambiguous rationale/event-frequency interpretation | Correct explanatory text and define mutually exclusive or overlapping recovery scenarios |
| F12 | Medium | S3 geo EL4-VIL-SSS-REQ-00219; EL4-VIL-SSS-REQ-00182 target 2.0.0; ECMUX EL4-VIL-SSS-REQ-00228 is In negotiation with a standby concept | Basic compliance cannot demonstrate geo compliance | Keep separate configuration/release evidence and approve ECMUX geo design |
| F13 | Medium | EL4-DIL-SSS-REQ-00330, EL4-DIL-SSS-REQ-00439 and EL4-DIL-SSS-REQ-00991 remain In negotiation; network status is not complete location diagnosis | Recovery/diagnosis traceability has open upstream conditions | Close detection/recovery methods and IPS/ADM diagnostic coverage |
| F14 | Medium | S5 section 6.2 still lists EL4-DIL-SSS-REQ-00571; EL4-DIL-SSS-REQ-00572; EL4-DIL-SSS-REQ-00573; EL4-DIL-SSS-REQ-00818; EL4-DIL-SSS-REQ-00574 are not in that availability list | Historical plan coverage is incomplete for this task | Update RAM deliverable coverage to the six current parents and supporting tests |
| F15 | Medium | CDS gating/rejection and common-version consistency can affect multiple VMs; service-loss behaviour is unquantified | Shared SW/deployment dependency can dominate HW residual failures | Assess CDS failure/recovery, version-rejection states and approved rolling-update compatibility |

The 3-4 min interval appears in S1's PH text for major update activation through completion of general interrogation and restored operational data. It is relevant context for F07/F09, **not** proof that every restart or every upgrade satisfies EL4-DIL-SSS-REQ-00574.

### Suggested clarification wording

These are proposals, not changes to customer requirements:

- **EL4-DIL-SSS-REQ-00569:** define the three recovery scenarios, whether the 120/600 s limits are per-event maxima, the approved manual restoration assumption, the required observation/exposure basis and class-counting rules. Retain all three specified availability values unless the approved baseline changes.
- **EL4-DIL-SSS-REQ-00570:** define FK4 as an explicit list of non-operational-impact states, with condition start/end, exposure denominator and rules for transition to service loss.
- **EL4-DIL-SSS-REQ-00573:** state the approved minor-change/compatible-version envelope and require zero operational restriction during the complete supported maintenance sequence.
- **EL4-DIL-SSS-REQ-00818:** define required authorization, allowed service interruption and handover behaviour for each major-change procedure, resolving the LH/PH inconsistency.
- **EL4-DIL-SSS-REQ-00574:** state approved maximum restart and reintegration durations and measure downtime until all required operational functions, interfaces and state are restored.

## 9. Actions and completion criteria

| Action | Proposed accountable owner | Output / closure evidence |
| --- | --- | --- |
| A01 - Confirm baseline and numerical interpretation | DIL requirements lead + RAM lead | Approved resolution of F01/F02/F10/F11; service and clock definitions |
| A02 - Confirm component/design ownership | VIL architect + Core/ECMUX/platform leads | Each proposed SW requirement allocated to an actual component specification; interface agreements with IPS/ADM |
| A03 - Resolve delivery releases and update concept | VIL project/requirements lead + change control | F03/F07/F08/F12 disposition; compatible patch/upgrade procedures and approved release scope |
| A04 - Complete detection and recovery timing | Core/ECMUX/NMR/J4S/communication leads | Approved budgets and scenario matrix; definition of < 600 s redundancy restoration and unrecoverable-fault handling |
| A05 - Complete RAM dependency model | RAM lead + VIL/IPS architects | Core/ECMUX/communication/shared-service model, CCF assumptions, source data and scenario results |
| A06 - Execute integrated verification | VIL V&V lead with component teams | Specifications and reports for the reviews and tests described in Section 7.2, timing records, load/configuration coverage and anomaly closure |
| A07 - Update RAM documentation and operational monitoring | RAM lead + requirements lead + FRACAS/operations | Updated DPR/RAMP traceability; recovery/service-loss/FK4 records and compliance monitoring rules |

**ELFOUR-1730 closure recommendation:** accept this report as an allocation proposal, not as evidence that the VIL availability targets are met. Close the task only when the six parent requirements have approved component-level refinements, release coverage, verification links and accepted dispositions for the material findings. Final RAM compliance requires the reviewed instance model and verification evidence, not merely the existence of hot-hot redundancy.
