# IPS RAM Plan Ed02PD01 - Responses to RAM Review Comments

| Attribute | Value |
| --- | --- |
| Document reviewed | [RAMP IPS, 3BU 17300 2009 DUAPA, Ed02PD01](../RAMP_IPS_3BU_17300_2009_DUAPA_Ed02PD01.docx) |
| Date | 2026-11-02 |
| Scope | Comments 1-2: RAM demonstration and allocation; Chapter 6: supplementary SSS applicability; Chapter 7: software/platform failures, failover coverage, recovery and planned FRACAS |
| Status | Draft responses and proposed plan additions for author approval; review comments remain open pending approved changes/evidence |
| Classification | Confidential - project review material |

## Applied Skills

- [Railway-RAM](../../../../Skills/Railway-RAM.md): RAM planning, system boundaries and evidence.
- [REQ-Review](../../../../Skills/REQ-Review.md): traceability, acceptance criteria and closure.
- [RAM-Metrics](../../../../Skills/RAM-Metrics.md): availability definitions and field measurement.
- SRS-SKILL-0020, Document Review: source extraction and evidence-based review. Only this requested Markdown response is produced; the Word source is unchanged and no tracked-change deliverable is implied.

## 1. Executive Summary

**Accept both comments, with qualifications.** The plan already requires availability analysis and requirement refinement, but does not define an executable RAM demonstration programme or show the customer-to-IPS allocation. Referencing other documents alone does not close these gaps.

| Comment | Recommended disposition | Main qualification |
| --- | --- | --- |
| 1 - Missing RAM V&V concept | Accepted; add section 5.8, **RAM Verification & Demonstration**, and extend section 6.1 deliverables. | Verification metadata already exists in the available IPS SSS. Consolidate and supplement it rather than implying no verification planning exists anywhere. Geo-redundancy testing must follow the applicable release baseline. |
| 2 - Missing customer targets and split | Accepted; extend section 4.2 with applicable customer requirements, boundaries and allocation method, and link Table 7 to the controlled traceability record. | The 99.9999% figures are IPS service-level requirements, not the stated customer DSTW-ZE target. Their approved numerical derivation has not been established by the reviewed evidence. Do not invent a split or claim traceability is complete. |
| 3 - Hardware-only analysis of a software-heavy platform | Accepted; Chapter 7 defines complementary platform failure analysis, failover/recovery verification and software/configuration/upgrade event handling through the planned FRACAS. | A planned FRACAS is a valid lifecycle measure, not current evidence of six-nines availability. Relative HW/SW downtime contributions have not been established by project data. |

## 2. Sources, Assumptions and Limitations

Repository information was used as follows.

| Ref. | Source | Evidence and limitation |
| --- | --- | --- |
| S1 | [IPS RAM Plan Ed02PD01](../RAMP_IPS_3BU_17300_2009_DUAPA_Ed02PD01.docx) | Full extracted body and tables: sections 4-6 and all 37 Table 7 DPRs. Text in images, embedded objects, headers and footers is not covered by the body extraction. |
| S2 | [IPS SSS, available Ed01 PDF](../SSS_IPS_3BU_17300_2051_DTAPA_Ed01.pdf) | Requirement origins, verification metadata and target releases. S1 cites Ed01PD02; confirm differences against that controlled edition before baselining this proposal. |
| S3 | [DIL RAMS SSS Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx) | DIL-CU definition; REQ-00406/00407 and customer origins; VIL availability requirements. |
| S4 | [EL4 PH review copy](../EL4_PH_PleaseReview_Clean.docx) | D2.2 customer requirement text and external IDs, including 02_104 and 02_107-110. Draft solution/comment fields are proposals, not evidence of customer-approved qualifications. Confirm equivalence to the controlled [PH_RAMS] Ed02 cited by S1. |
| S5 | [DIL/VIL RAM Plan Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf) | Existing availability classes and analysis approach; not an approved IPS numerical budget split. |
| S6 | [Company RAMS/independent validation procedure, draft with comments](<../../../../Knowledge/Process/RAM-Process/G-PRC_S06001_03_EN_d02 Manage Project RAMS and Independent Validation Activities_comments_RAM-AT.docx>) | Planning, RAM/V&V responsibilities, interface coordination and evidence traceability. Confirm the currently approved process revision; this draft is not represented as a released authority. |
| S7 | [Split-brain technical assessment](../../Split%20Brain/Output/Split-Brain-technical-analysis-20260928.md) and [repository topology](../../Split%20Brain/split-brain-topology.png) | Context for dual-core-router loss, network partition and reintegration tests. The attached topology likewise illustrates this concern; it is not proof of an approved mitigation or verified behaviour. |
| S8 | [Customer performance description V2.1](../2026-03-27_OBB_RA-DSTW-D1_Leistungsbeschreibung_V2.1.pdf) | Refers RAM evidence and monitoring to the RAMS specification. Not treated as the exact [CRS_DSTW], 3BU 17300 0004 DSAPC Ed06, cited in S1. |
| S9 | [Requirements lessons learned](../../../../Knowledge/Lessons_Learned/Requirements_Lessons.md) and [existing VIL allocation assessment](VIL_Availability_Requirements_Allocation.md) | Review principles and known boundary/restoration issues; secondary guidance, not new contractual requirements. |

**Assumptions:** Proposed responsibilities below are role-level assignments for confirmation under the SEMP/V&V Plan. Annual downtime conversions assume continuously required service over 365 days. No failure rates, numerical component budgets, test results or customer approvals are assumed.

**Limitations:** The exact controlled [CRS_DSTW] baseline and an approved numerical IPS allocation were not established. This addresses three review comments, supplemented by the SSS applicability review in Chapter 6, not a clause-by-clause EN 50126 compliance assessment. Proposed text below describes future work; it does not assert that the plan has already been amended.

## 3. Comment 1 - RAM Verification and Validation Concept

### 3.1 Proposed reply to the reviewer

> **Accepted.** Sections 5 and 6 currently identify RAM analyses and deliverables but do not sufficiently define how each applicable DPR will be verified and how the IPS contribution to operational RAM performance will be demonstrated.
>
> We propose adding section 5.8, "RAM Verification & Demonstration", covering a requirement-to-evidence matrix, analysis and inspection activities, a release-specific failover and recovery test campaign, and operational data collection through FRACAS. The matrix will identify the method, applicable configuration/release, acceptance criterion, responsible role and evidence reference for every Table 7 DPR.
>
> The existing SSS verification assignments will be retained and reconciled with this programme. Server loss, AZ loss, communication failures and reintegration will be covered for the applicable configuration. Geo-site loss and automatic/manual geo switch-over will be demonstrated for the release in which those functions are required. A short failover test demonstrates behaviour and timing; it does not alone demonstrate 99.9999% long-term availability.
>
> Closure requires the revised plan and controlled matrix, links to the applicable V&V/test plans, defined acceptance criteria and assigned evidence deliverables. Completed test reports will be required at the corresponding demonstration milestone, not represented as already available.

### 3.2 Source-based finding

S1 section 5.6 states:

> "An analysis of SW reliability is not part of the Reliability Analysis where only permanent random HW faults and system failures will be analysed."

Section 6.1 lists the RAM Plan, recommended preliminary analysis/HW-FMEA and required Reliability Analysis. It does not list a DPR verification matrix, failover campaign or operational RAM demonstration report. Section 6.3 concerns plan updates, not a defined field-performance reporting regime.

**Implication:** retain the random-HW prediction scope, but explicitly address software, configuration, orchestration, network partitions and operational recovery through complementary evidence. Hardware prediction alone does not substantiate service availability.

### 3.3 Proposed section 5.8 - RAM Verification & Demonstration

The following is proposed plan text, subject to approval:

> RAM compliance will be demonstrated through a combination of reviewed RAM analyses, design/configuration inspections, representative integration and system tests, and operational performance assessment. Verification will establish that allocated requirements are met; validation will establish that the integrated IPS-supported service satisfies its intended operational needs under the agreed conditions.
>
> The RAM-AM will maintain the RAM requirement-to-evidence matrix with Requirements Management. The V&V lead will control test specifications, execution and reporting under the applicable V&V Plan. Design owners will supply configuration, capacity, redundancy and recovery evidence. The designated validator will assess operational suitability and evidence completeness in accordance with the project organisation.
>
> Each matrix entry will identify the requirement and parent origin, target release, service/failure boundary, method, acceptance criterion, analysis/test reference, responsible role, execution milestone, result, evidence revision and open deviations. Missing criteria or evidence will remain explicit open items and will not be recorded as compliant.
>
> Numerical availability claims will be supported by dependency-aware RAM models using justified reliability, detection, restoration, maintenance and common-cause assumptions. Tests will verify model assumptions and service behaviour under faults and recovery. No unsupported constant random failure rate will be assigned to systematic software faults.

#### A. Proposed DPR verification coverage

This table covers **all 37 DPRs in S1 Table 7**. It is an initial method/coverage proposal, not an executed verification record. **A** = analysis, **T** = test, **I** = inspection/design review. These methods supplement rather than silently replace S2 metadata; reconcile terminology and assignments in the controlled matrix.

For each row, add the owner, exact acceptance criterion, procedure/report ID, milestone and result before the relevant verification activity. All results are currently **not assessed**.

| Table 7 DPR | Proposed method | Required verification evidence / check |
| --- | --- | --- |
| EL4-IPS-SSS-REQ-00010-DPR | I + T | Redundant alerting configuration; inject infrastructure/network/application faults and loss of one alerting instance; verify alarms remain available. |
| EL4-IPS-SSS-REQ-00013-DPR | A + I + T | Geo topology, surviving-site capacity and compute/storage/network recovery; system test for the approved number of sites. |
| EL4-IPS-SSS-REQ-00014-DPR | I + T | Dedicated virtual networks, SDN configuration and QoS behaviour under representative competing traffic. |
| EL4-IPS-SSS-REQ-00021-DPR | T | Primary connection failure; automatic geo connection switch-over, traffic restoration and measured interruption. |
| EL4-IPS-SSS-REQ-00022-DPR | I + T | Authorised manual geo switch-over procedure and successful traffic restoration. |
| EL4-IPS-SSS-REQ-00024-DPR | I + T | Cross-site configuration/binary/VM/image consistency, synchronization failure and recovery. |
| EL4-IPS-SSS-REQ-00025-DPR | I + T | Locally available, consistent configurations, VMs and images, including local storage fault/recovery cases. |
| EL4-IPS-SSS-REQ-04009-DPR | A + I + T | Database service model against 99.9999%; database instance/dependency failover and recovery evidence. |
| EL4-IPS-SSS-REQ-01102-DPR | I + T | Two connections to the power-supply monitor; demonstrate continued communication after individual path loss. |
| EL4-IPS-SSS-REQ-01103-DPR | I + T | Two connections to Datennetz 2020; individual path failure and recovery at the agreed interface. |
| EL4-IPS-SSS-REQ-01301-DPR | A + I + T | Core-network model against 99.9999%; router/link failover and common-dependency assessment. |
| EL4-IPS-SSS-REQ-01304-DPR | I + T | Two-fold server-cabinet connectivity; topology inspection and individual path fault tests. |
| EL4-IPS-SSS-REQ-01306-DPR | I + T | Two-fold connection to each RaSTA network; individual path fault tests. |
| EL4-IPS-SSS-REQ-02001-DPR | A + I + T | Storage-volume service model against 99.9999%; storage failures, read/write continuity and recovery. |
| EL4-IPS-SSS-REQ-02002-DPR | I + T | At least two storage-server OS devices in RAID1; member loss, boot and rebuild checks. |
| EL4-IPS-SSS-REQ-02003-DPR | I + T | Additional common application-storage devices exist and provide the specified space/function. |
| EL4-IPS-SSS-REQ-03101-DPR | I + T | At least two compute-server OS devices in RAID1; member loss, boot and rebuild checks. |
| EL4-IPS-SSS-REQ-04015-DPR | A + I + T | Compute/storage distribution across three AZs; surviving capacity and service behaviour during AZ loss. |
| EL4-IPS-SSS-REQ-04025-DPR | I + T | VM AZ placement and behaviour during local AZ failure/recovery. |
| EL4-IPS-SSS-REQ-04026-DPR | A + I + T | Multi-region VM placement and geo failure/recovery for the applicable release. |
| EL4-IPS-SSS-REQ-04030-DPR | T | Server restart followed by automatic restart and correct operation of its VMs. |
| EL4-IPS-SSS-REQ-04031-DPR | I + T | Compute scale-in/out per AZ; capacity and continued-service checks. |
| EL4-IPS-SSS-REQ-04032-DPR | I + T | Network scale-in/out per AZ; capacity and continued-service checks. |
| EL4-IPS-SSS-REQ-04033-DPR | I + T | Storage scale-in/out per AZ; capacity, consistency and continued-service checks. |
| EL4-IPS-SSS-REQ-05104-DPR | A + I + T | Application-file storage model against 99.9999%; service access during fault/recovery. |
| EL4-IPS-SSS-REQ-05105-DPR | A + I + T | Data-preparation-file storage model against 99.9999%; service access during fault/recovery. |
| EL4-IPS-SSS-REQ-05106-DPR | A + I + T | Configuration-file storage model against 99.9999%; service access and consistency during fault/recovery. |
| EL4-IPS-SSS-REQ-05306-DPR | A + I + T | PKI service model against 99.9999%; certificate-management service failover and dependency recovery. |
| EL4-IPS-SSS-REQ-06306-DPR | A + I + T | Message-broker model against 99.9999%; failover and specified message-delivery behaviour. |
| EL4-IPS-SSS-REQ-08306-DPR | A + I + T | Redundant NMR communication paths; path isolation, partition and recovery behaviour. |
| EL4-IPS-SSS-REQ-09902-DPR | I + T | Server loss; redistribution follows the balanced increment rule and respects remaining capacity. |
| EL4-IPS-SSS-REQ-09903-DPR | T | Server reintegration does not redistribute operating services or cause additional disruption. |
| EL4-IPS-SSS-REQ-09906-DPR | I + T | Required substation service group is colocated on one physical server; check placement after recovery. |
| EL4-IPS-SSS-REQ-09911-DPR | I + T | INFRA instances occupy different servers/AZs with balanced distribution, including after faults. |
| EL4-IPS-SSS-REQ-09912-DPR | A + I + T | Verify the selected permitted INFRA redundancy configuration and its actual quorum/failover behaviour. |
| EL4-IPS-SSS-REQ-09913-DPR | I + T | SERVICE instances occupy different servers/AZs with balanced distribution, including after faults. |
| EL4-IPS-SSS-REQ-09914-DPR | A + I + T | Verify the selected permitted SERVICE redundancy configuration and its actual quorum/failover behaviour. |

**Release gate:** S2 assigns REQ-00013, REQ-00021, REQ-00022, REQ-00024 and REQ-04026 to **IPSS OBB 2.0.0**, while S1 identifies **IPSS OBB 1.0.0**. Confirm these allocations against S1's cited SSS edition. Retain later-release requirements visibly as planned/deferred with a baseline reference; do not mark them passed or automatically applicable to 1.0.0.

#### B. Failover and recovery campaign

| Campaign case | Proposed test scope | Acceptance basis / evidence |
| --- | --- | --- |
| Server loss | Abrupt loss of a compute server at representative maximum approved load; VM/application recovery and redistribution. | Applicable DPRs, approved surviving capacity, placement rules, service interruption and recovery limits. |
| AZ loss | Loss of one approved AZ failure domain, including its compute/storage/network resources; repeat for materially different AZ roles. | Required service remains within its agreed continuity/recovery criteria; no unjustified assumption that AZ equals one rack or that all AZs are independent. |
| Network path/router loss | Each redundant link/router path; loss of both core routers at one site; inter-site partition and asymmetric connectivity. | Path recovery, application reachability and partition behaviour; assess common dependencies and safe master control jointly with VIL/safety V&V. |
| Storage/service failure | Storage member/node, database, broker and relevant cluster instance loss; degraded operation and rebuild. | Correct read/write/service behaviour, data consistency, quorum and measured recovery against approved criteria. |
| Geo-site loss and switch-over | Automatic connection switch-over, authorised manual rerouting, loss/isolation of a whole site, and operation at the surviving site. | Applicable release, approved topology/capacity, data consistency and agreed service recovery criteria; test both directions where applicable. |
| Restoration/reintegration | Restore server, AZ, router and site after each applicable fault; controlled failback where supported. | No forbidden redistribution under REQ-09903, conflicting master state or additional unapproved interruption; full redundancy restoration recorded separately. |

Test procedures must define fault injection, initial state, release/build/configuration, load, repetitions, instrumentation/time resolution, preconditions, safe abort/rollback and expected results. Timing starts/ends and numerical limits must come from approved requirements or agreed derived criteria, **not an invented universal switch-over time**.

Measure fault occurrence, detection, alarm delivery, loss/restoration of the required service and restoration of full redundancy separately. A VM restart or network ping alone is not evidence that the operational interlocking function is restored. A safe shutdown may be the correct safety outcome but still counts as RAM downtime where the required service is lost. Execute disruptive faults in an authorised representative test environment.

The topology supplied with the review makes simultaneous core-router loss and partition recovery particularly relevant. Test the approved supervision/fencing/master-election implementation; do not assume the proposed independent supervision channel is already implemented or qualified.

#### C. Operational demonstration and field data

Proposed plan provision:

> IPS operational RAM evidence will be collected through the project FRACAS arrangements, aligned with the customer monitoring and demonstration obligations. Records will identify the affected service/component and configuration, required-service exposure, fault/detection/alarm times, service interruption and restoration, full redundancy restoration, failure cause, operational impact, corrective action and evidence quality.
>
> Product, platform and external-interface causes will remain distinguishable. Customer/supplier data responsibilities, event reconciliation, time synchronization, planned-maintenance treatment, justified exclusions, observation periods and reporting cadence will be agreed before operational assessment. Unavailable data and unresolved attribution will be reported explicitly.
>
> The operational programme will address the five-year demonstration obligation after commissioning of the first VSTW in customer requirement 02_142 and the monitoring/reporting obligations in 02_141, 02_143 and 02_144. Any proposed scope limitation or population-based interpretation requires customer agreement; it is not introduced by this plan unilaterally.

For a defined service and observation interval:

```text
A_observed = 1 - D / T_required
```

`D` is the union of qualifying service-down intervals, in seconds; `T_required` is the required-service observation time, in seconds. Count simultaneous causes once for that service. Also retain per-component records and customer outage classes; do not conceal common-site failures by pooling dependent instances as independent evidence.

Report measured performance separately from prediction, including exposure, population/configuration comparability, uncertainty and unresolved events. Short zero-failure campaigns or a short outage-free field period do not independently establish a six-nines claim.

## 4. Comment 2 - Customer Targets and Availability Allocation

### 4.1 Proposed reply to the reviewer

> **Accepted.** The plan references [PH_RAMS] and [CRS_DSTW], and section 4 calls for apportionment, but it does not present the applicable customer targets or the allocation linking them to the IPS DPRs in Table 7.
>
> We propose adding a customer RAM requirements table and an availability-allocation subsection to section 4.2. These will identify the customer requirement IDs, system/service boundaries, applicable outage classes, IPS contribution and verification evidence. The system RAM allocation will distinguish VIL, IPS platform services, ADM and network contributions, including common dependencies and customer-provided infrastructure.
>
> The customer DSTW-ZE overall target is at least 99.999%; the 99.9999% values in Table 7 apply to individual IPS services. They will remain identified as derived subsystem/service targets until their approved allocation and parent traceability are confirmed. We will not infer a numerical split from those percentages alone.
>
> Closure requires a controlled customer-to-system-to-IPS traceability record and an approved allocation showing that the combined contributions meet the applicable system targets without double-counting shared infrastructure. Any unapproved budgets or missing customer-baseline references will remain open.

### 4.2 Source-based finding

S1 section 4 already states:

> "This Dependability Analysis should also provide a proper apportionment and refinement of these requirements according to the system design."

Section 6.2 states:

> "The Solution Element – IPS Solution OBB 1.0.0 (IPSS OBB 1.0.0) is subject to the DPR requirements stated in [SSS_IPS] (see Table 7 below) and furthermore in [PH_RAMS]."

These are valid intentions/references, **not an allocation result**. Table 7 has no parent/customer column, budget, boundary or compliance evidence.

### 4.3 Applicable customer requirements to add to section 4.2

The following are concise synopses of the customer text in S4, not replacements for the controlled originals. Decimal fractions are converted to percentages. Confirm IDs and applicability against controlled [PH_RAMS]/[CRS_DSTW] before issue.

| Customer external ID | Clause | Target / obligation in available PH text | Relevance to IPS |
| --- | --- | --- | --- |
| 02_95 / 02_98 | 5.1.0-1 / 5.2.0-2 | Required-function availability definition; top-down availability calculation. | Agree service boundary, conditions and restoration-time definition. |
| 02_100 | 5.3.0-1 | RZ includes VSTW instances/HW, network, cooling, additional applications, UPS and physical location; distributed over at least two sites. | Establish external dependencies and responsibility interfaces; do not equate IPS alone to this entire boundary. |
| 02_104 / 02_106 | 5.3.0-5 / 5.3.0-7 | DSTW-ZE availability >= 0.99999 = **99.999%**, class 1. | Parent system objective; S3 REQ-00406 explicitly cites these origins and allocates to DIL, VIL and IPS. |
| 02_107 | 5.3.0-8 | DSTW-ZE manual-fault category availability >= 0.999998 = **99.9998%**. | Allocate manual-restoration failures and justify elapsed restoration assumptions. |
| 02_108 | 5.3.0-9 | DSTW-ZE faults with no operational impact: category value >= 0.997154 = **99.7154%**. | Track diagnosed/degraded states separately; do not automatically add them to operational downtime. |
| 02_109 | 5.3.0-10 | DSTW-ZE automatically remedied within **600 s**: category availability >= 0.999996 = **99.9996%**. | Classify applicable IPS-caused outages and verify automatic recovery. |
| 02_110 / 02_111 | 5.3.0-11 / 5.3.0-12 | DSTW-ZE automatically remedied within **120 s**: category availability >= **99.9996%**; automatic recovery includes safe state, self-test and recommissioning. | Demonstrate operational recovery, not only infrastructure restart. |
| 02_113 / 02_115 | 5.4.0-1 / 5.4.0-3 | Each VSTW availability >= 0.99995 = **99.995%**, class 2. | Separate instance-level target from common/system-wide outages. |
| 02_116 / 02_117 | 5.4.0-4 / 5.4.0-5 | VSTW manual category >= **99.9979%**; no-operational-impact category >= **99.7154%**. | Account for IPS effects at individual-instance level using the correct categories. |
| 02_118 / 02_119 | 5.4.0-6 / 5.4.0-7 | VSTW automatic recovery within **600 s** / **120 s**; respective category availability >= **99.999%** / **99.9996%**. | Coordinate platform and VIL recovery timing and classification. |
| 02_120 | 5.4.0-8 | Non-safety-relevant VSTW software/configuration changes must not reduce operation below permitted availability. | Verify relevant platform/update dependencies; do not assume planned interruptions are automatically excluded. |
| 02_84 | 4.8.0-6 | Demonstrate required MRT during component replacement. | Maintenance demonstrations; distinguish active repair from elapsed service restoration. |
| 02_141-02_144 | 5.8.0-1 to 5.8.0-4 | FRACAS provision; demonstrate specified availability within five years after first VSTW commissioning; individual-component monitoring; regular customer reports. | Define field evidence, data ownership, service/component reporting and agreed cadence. |

S3 REQ-00407 traces the DSTW-ZE restoration-category targets to 02_107, 02_109 and 02_110 and includes a **6 h** manual MTTR assumption. That duration is a system-specification input to reconcile, not a duration stated in the quoted PH prose above. Confirm underlying customer tables, restoration definitions and current baseline rather than substituting active repair time.

### 4.4 Proposed availability-allocation subsection

Proposed plan text:

> The DIL system RAM allocation will identify the required operational service, outage-impact class, applicable release and failure boundary before assigning IPS budgets. IPS will demonstrate its allocated contribution and service-level DPRs using the same measurement and restoration definitions as the parent requirement.
>
> The allocation will distinguish VIL application functions, IPS compute/storage/platform functions, ADM functions and communication paths. Internal IPS network equipment will be counted either within the IPS allocation or as an explicitly separated network contribution, not both. External networks, power, cooling, site services and other customer-provided dependencies will be represented with agreed interface assumptions and evidence responsibilities.
>
> Shared causes, correlated software/configuration failures, common maintenance and failover interruptions will be explicitly modelled. ADM or management-service loss will be mapped to its actual operational effect: immediate service loss, degraded operation, delayed diagnosis/restoration or loss of maintenance capability. It will not automatically be treated as an independent series failure of the interlocking service.
>
> Numerical budgets will be approved by the system RAM/design authority and flowed into the applicable subsystem requirements. Until approval, unallocated values will be marked open and compliance will not be claimed.

#### Allocation record needed

| Contribution | Boundary / treatment | Numerical budget status |
| --- | --- | --- |
| VIL | Application-specific failures and recovery affecting the defined system/instance service; exclude separately counted platform causes. | Open for the system-impact allocation; the existing 99.995% instance target is not a class-1 budget. |
| IPS platform | Compute, virtualization, storage and required platform services; count each dependency once. | Open; Table 7 service targets are known, but their aggregate system budget is not established. |
| ADM | Only the effects relevant to the defined required service; include diagnostic/restoration dependencies. | Open; quantify based on operational effect, not an assumed series relationship. |
| Network | Explicitly separate IPS-internal and external paths and their responsibility boundaries. | Open; the core-network 99.9999% DPR is known but is not the full network allocation. |
| Shared/interface causes | Site/power/cooling, common software/configuration, partition, maintenance and common failover effects. | Open; assign uniquely or model jointly to avoid omissions and duplication. |

For a common boundary and observation basis:

```text
U_system = P(loss of the defined required service)
U_target = 1 - A_target
```

For mutually exclusive attributed outage contributions, an additive budget may be used. For dependent/overlapping events, use the union of failure events in a fault tree, state model or equivalent dependency-aware model. The sum of event probabilities can be used as a conservative upper bound only when the events completely cover the relevant service-loss causes.

```text
U_system <= U_VIL + U_IPS_platform + U_ADM_relevant
            + U_network + U_shared/interface
```

This is **a modelling/budget framework, not the verified IPS split**. A product of subsystem availabilities requires justified independent series-service assumptions. Do not subtract the VIL-instance unavailability from the class-1 system budget: S3 distinguishes large-scale system impact from individual-instance outages.

#### Meaning of the 99.9999% targets

**Inputs:** S1 Table 7 sets 99.9999% for database systems, core network, storage volumes, three INFRA file-storage services, PKI and message broker.

**Assumption:** continuous required service, 365 days/year; conversions illustrate scale, not a contractual reporting period.

**Formula and calculation:**

```text
U = 1 - A
D_year = U x 365 x 24 x 3600 s

Customer DSTW-ZE:
A = 0.99999;  U = 0.00001
D_year = 0.00001 x 31,536,000 s = 315.36 s/year

Individual IPS service:
A = 0.999999; U = 0.000001
D_year = 0.000001 x 31,536,000 s = 31.536 s/year
```

**Result:** one such IPS service's unavailability equals 10% of the class-1 system unavailability limit **only if the service boundaries, outage categories and accounting basis are comparable**. This numerical ratio does not prove that a 10% allocation was approved.

**Traceability already visible in S2:** REQ-02001 lists DIL REQ-00406 as an origin; REQ-04009 lists DIL REQ-00307. The core-network, file-storage, PKI and broker targets list feature EL4-FL-FEA-0015. These are useful existing links, but neither an origin link nor a feature reference provides the missing numerical allocation rationale. Preserve them and complete the chain rather than stating that no upstream links exist.

The file-storage and database services may share storage, servers and network paths. Treat their 99.9999% requirements as simultaneous service obligations, **not automatically eight independent serial budgets**. Likewise, successful service-level predictions do not by themselves prove the complete IPS or DSTW-ZE target.

### 4.5 Detailed answer: how to split the target between VIL, IPS, ADM and network

#### 4.5.1 What is established, and what is not

**Source finding:** S3 introduces DIL-CU availability as follows: "According to [Figure 1: System Overview] the [DIL-CU] comprises the subsystems [VIL], [ADM] and [IPS]." It also states that IPS provides the necessary server hardware and network components. REQ-00406 specifies class 1 overall availability of at least 99.999%; its comment identifies "System, Subsystem outages with large-scale operational impact". Its origins are PH 02_104 and 02_106, and its Allocation field names DIL, VIL and IPS. **That field assigns responsibility; it does not assign numerical fractions of the unavailability budget.**

The existing [external-network/DIL-CU review](Review_RAMP_DIL_VIL_External_Network_and_DIL-CU_Availability.md) and [VIL allocation analysis](VIL_Availability_Requirements_Allocation.md) support this boundary/impact distinction. Both are engineering proposals, not approved allocation authority. No approved four-way numerical allocation was established by the sources reviewed here.

| Requirement level | Established target | Why it is not already the requested split |
| --- | --- | --- |
| Customer DSTW-ZE / DIL-CU, PH 02_104/02_106 -> DIL REQ-00406 | >= 99.999%, class 1; large-scale operational impact | This defines the parent objective and relevant outage population, not each subsystem's permitted contribution. |
| Individual VIL instance, DIL REQ-00587 | >= 99.995%, class 2 | A local instance outage and a large-scale CU outage are different top events. The entire instance unavailability cannot be inserted as a class-1 VIL budget. |
| IPS database, storage, core network, file services, PKI and broker DPRs | >= 99.9999% for each applicable defined service | Service-specific obligations; not an established aggregate IPS allowance or proof of their numerical derivation from PH. |
| ADM overall | DIL REQ-01481: >= 99.99%, class 3; ADM REQ-04641: >= 99.995%, class 2 | Parent/child discrepancy remains open. Neither number is the allowable contribution of ADM-caused class-1 outages. |
| External network | No applicable numerical budget established in this review | Its inclusion and responsibility depend on the target boundary; the IPS core-network DPR does not cover every external path. |

**Terminology:** use technical availability of the defined system/function where confirmed by the contractual definition. "Database service" identifies the assessed function; it is not a reason to change the availability accounting category. The controlled requirements' downtime inclusions/exclusions govern. Software faults are technical causes too.

#### 4.5.2 Allocation method

**Allocate unavailability, not percentages of availability.** For the class-1 parent:

```text
A_parent >= 0.99999
U_parent,max = 1 - A_parent,min = 0.00001 = 10 ppm

b_VIL + b_IPS + b_ADM + b_network + b_shared + b_reserve <= 10 ppm
```

Here 1 ppm = 0.000001 of required time. Each b is a proposed allowance for causes that produce the SAME defined class-1 top event. Reserve is unallocated design margin, not an outage cause. Under complete event coverage, the sum of cause-event unavailabilities is a conservative upper bound on their union; independence is not required for that bound. Joint effects must also be covered. An exact model/measurement counts overlapping outage time only once.

1. **Define the top event.** Agree the meaning of large-scale impact/FK1, affected functions/instances, required operating time, service-loss/restoration criteria and exclusions. Separately assess the class-2 instance and class-3 management objectives.
2. **Map the architecture to that event.** Identify how VIL, IPS, ADM and communication failures can cause it. Use a fault tree, state model or equivalent cause/dependency model, including failures during degraded operation and unsuccessful recovery. Do not assume the four elements form independent series blocks.
3. **Set non-overlapping responsibility boundaries.** For example, count internal IPS switches either under IPS or in a separately identified network budget. Keep external network paths separate. Assign common power/site/configuration causes once, or model them explicitly as shared events.
4. **Estimate achievable contributions.** Use relevant hardware prediction, redundancy/common-cause assessment, observed software/platform incidents, recovery tests and applicable operational FRACAS data. Separate expected values from unquantified causes and uncertainty. A budget can be assigned before these data are complete, but that is a design constraint, not demonstrated feasibility.
5. **Negotiate budgets against architecture and feasibility.** Give tighter allowances to common services with broad impact where necessary, and account for realistic restoration and fault containment. There is no universal equal-share rule. Retain margin for integration and incomplete knowledge.
6. **Approve and flow down.** The system RAM/design authority approves the allocation and derived requirements; each solution-element owner accepts its boundary and allowance. Trace each IPS service obligation to the service-dependency model as well as the parent requirement.
7. **Verify and measure.** Compare predicted contributions and later FRACAS-based actual contributions with their budgets. Reconcile system downtime using common event IDs; retain every affected service/instance without multiplying a shared event into several system outages.

| Budget owner / branch | Contribution to allocate for the class-1 top event | Specific caution |
| --- | --- | --- |
| VIL | VIL-originating common application/configuration/communication faults and recovery that produce large-scale impact | Do not charge a separately counted IPS-host failure again as an independent VIL cause. A single-instance failure belongs to the instance assessment unless it also satisfies the agreed class-1 criterion. |
| IPS | Shared compute, virtualization, storage and required platform-service failures with the relevant large-scale effect | Local replica loss with uninterrupted function consumes no technical service-down time; failed failover or common configuration faults can consume it. |
| ADM | ADM-caused large-scale functional loss or additional service-down time caused by impaired diagnosis/restoration | Management GUI unavailability alone need not stop interlocking operation. ADM can instead affect restoration duration; model that dependency, rather than multiplying ADM uptime into CU uptime. |
| Network | In-boundary network loss/partition causing the top event, with internal/external demarcation | Internal IPS networking is not a fifth independent copy of the same network failure. External dependencies require owner evidence or explicitly conditional results. |
| Shared/interface | Common site, power, cooling, time, configuration, integration or change causes not already assigned | Count once; assess recovery and correlated impact across redundant instances. Include only within the agreed boundary, or explicitly state external conditions. |

The PH restoration categories must also be satisfied. A total budget meeting 10 ppm does not by itself establish the manual/automatic restoration-category requirements in section 4.3. Apply the same causal/dependency allocation to each applicable category and reconcile it with the overall target.

#### 4.5.3 Worked numerical illustration - NOT a DSTW allocation proposal

**Assumptions:** one common class-1 top event; all branches use the same required-time and downtime definitions; cause coverage is complete; 365-day continuously required service. The shares below are arbitrary teaching values to illustrate the arithmetic, **not derived from the specifications, not recommended design targets and not approved project commitments**.

| Cause contribution / margin | Illustrative budget (ppm) | Share of parent unavailability budget | Equivalent downtime per 365-day year |
| --- | --- | --- | --- |
| VIL-originating class-1 contribution | 3.0 | 30% | 94.608 s |
| IPS-originating class-1 contribution, excluding separately budgeted network | 3.0 | 30% | 94.608 s |
| ADM-relevant class-1 contribution | 0.5 | 5% | 15.768 s |
| Separately bounded network contribution | 1.5 | 15% | 47.304 s |
| Shared/interface contribution | 1.0 | 10% | 31.536 s |
| Unallocated margin | 1.0 | 10% | 31.536 s |
| **Total allowance** | **10.0** | **100%** | **315.360 s** |

```text
D_i = b_i [ppm] x 10^-6 x 31,536,000 s
Allocated cause budgets = 9 ppm; remaining margin = 1 ppm
Upper bound at those cause budgets: U_parent <= 9 x 10^-6
Corresponding lower bound: A_parent >= 0.999991 = 99.9991%
```

These are allowance conversions and a conditional budget check, not performance predictions. Approval would require defensible engineering values in place of the illustrative shares. The IPS row is an aggregate CLASS-1 EFFECT budget, not the availability specification for every IPS service. Existing 99.9999% service requirements would still apply independently.

**How six nines relates to the parent:** one service at 99.9999% has U = 1 ppm, numerically 10% of the parent's 10 ppm allowance. Only if the relevant service outages all meet the parent impact criterion on the same accounting basis can that 1 ppm be treated directly as a bound on that service's parent contribution. It does NOT establish that IPS as a whole was allocated 1 ppm. Several service targets cannot be treated as independent, disjoint budgets: a storage outage can also interrupt the database and broker. Conversely, different service outages at different times can accumulate. A service-dependency/impact model is needed to derive the aggregate IPS contribution.

#### 4.5.4 Proposed detailed reply to the reviewer

> Accepted. The RAM Plan will list the applicable customer requirements from the controlled [PH_RAMS]/[CRS_DSTW] baseline, including the 99.999% class-1 DSTW-ZE objective, applicable restoration categories, individual VSTW objectives and operational demonstration obligations. The table will identify the corresponding DIL requirements, IPS relevance and verification references. Table 7 will remain the IPS DPR inventory and will be supplemented by customer-to-system-to-IPS traceability.
>
> The system-level allocation will distribute the permissible unavailability for the defined class-1 top event across VIL-originating, IPS-originating, relevant ADM, network and shared/interface causes, with agreed margin. The allocation will be based on operational impact and dependencies, not on multiplying the existing VIL, IPS and ADM availability percentages, which have different boundaries and outage classes. Internal IPS network contributions will be counted once. External network assumptions and responsibility boundaries will be explicit.
>
> The current 99.9999% IPS service targets will be retained as applicable derived requirements. However, the available documentation does not establish their approved numerical derivation or an approved aggregate IPS budget. The system RAM/design authority will establish or provide the controlled allocation and its justification, including recovery-category constraints. Until that is available, the allocation remains open; a new table in the plan alone will not close the numerical traceability issue.
>
> Actual technical availability and attributed outage contributions will subsequently be determined through monitoring and FRACAS over the agreed observation period. Complete downtime/exposure records permit this retrospective calculation without a software failure-rate prediction. They demonstrate achieved performance but do not replace the required design-stage allocation record.

**Required closure evidence:** approved impact/boundary definitions; controlled customer baseline; allocation/dependency report with numerical budgets and margin; approval by the system RAM/design authority; service-level parent links and derivation rationale; resolved ADM discrepancy; network responsibility/data agreements; and corresponding model/test/FRACAS verification references. Insert the source table and allocation summary in RAM Plan section 4.2; retain the detailed allocation as a controlled referenced system-level record.

## 5. Risks, Recommendations and Closure Actions

| Action | Risk / missing evidence | Proposed owner | Closure criterion |
| --- | --- | --- | --- |
| A1 | Wrong or mixed baselines/releases; exact CRS and cited IPS SSS edition not confirmed. | Requirements Manager + SEM | Controlled source revisions, applicability and deferred geo features recorded. |
| A2 | Structural redundancy mistaken for verified service continuity. | IPS V&V lead + design owners | Approved release-specific campaign with measurable criteria, representative load and fault/reintegration coverage. |
| A3 | No complete requirement-to-evidence demonstration path. | RAM-AM + Requirements Manager + V&V lead | Controlled matrix covering all 37 Table 7 DPRs and applicable customer obligations, with owners, criteria, milestones and evidence references. |
| A4 | Six-nines claims lack approved system allocation; shared causes may be omitted or counted twice. | DIL system RAM lead + design authority | Approved boundary/class-specific allocation and dependency model, traced to IPS service requirements. |
| A5 | Active repair, service restoration and redundancy restoration confused. | RAM-AM + maintenance/V&V leads | Agreed timing definitions and justified recovery inputs reflected consistently in requirements, model, tests and FRACAS. |
| A6 | Field evidence or contractual demonstration scope insufficient. | RAM-AM + service lead + customer interface | Agreed FRACAS protocol covering five-year demonstration, component/service records, cadence, data quality and unresolved attribution. |
| A7 | Plan changes not wired to controlled deliverables. | Document owner + SEM | Sections 4.2, 5.8 and 6.1 updated; traceability, test specifications/reports and operational RAM reports scheduled in the documentation plan and linked to V&V arrangements. |

**Recommended decision:** accept both review comments for implementation. Close the planning comments only after the revised plan and referenced controlled records are reviewed and approved; keep outstanding analysis/test/field evidence open to its planned lifecycle milestone.

**Reusable lesson:** recommend adding the approved customer-to-service allocation pattern and requirement-to-evidence fields to the RAM Plan template/review checklist after project agreement. No process or template change is made by this note.

## 6. Supplementary Review - Additional SSS Requirements Relevant to IPS

**Review date: 2026-11-02. Conclusion: yes, additional requirements should be identified in this RAM Plan.** The current Table 7 covers IPS DPRs only. It does not cover all applicable cabinet requirements or the monitoring, maintenance and operational-evidence dependencies on ADM and its Workflow Manager.

These are **additional requirements identified by this review**, not necessarily newly created requirements. The cabinet upload is byte-identical to the existing cabinet SSS copy in the repository. No Word source was modified.

### 6.1 Additional sources and applicability rules

| Ref. | Uploaded document | Review use |
| --- | --- | --- |
| N1 | [Generic Server/Network Cabinet SSS, 3BU 16000 0002 DTAPA, Ed05PD02](../SSS_Generic_Server_Network_Cabinet_3BU_16000_0002_DTAPA_Ed05PD02.docx) | Direct IPS hardware requirements, including requirement status, IPSS release applicability, power/network fault tolerance and maintenance. |
| N2 | [ADM SSS, 3BU 17300 2101 DTAPA, Ed01](../SSS_ADM_3BU_17300_2101_DTAPA_Ed01.docx) | ADM service target, monitoring interfaces, diagnostic coverage, maintenance and FRACAS dependencies. |
| N3 | [ADM Workflow Manager SSS, 3BU 17300 2125 DTAPA, Ed01](../SSS_ADM-WFM_3BU_17300_2125_DTAPA_Ed01.docx) | Maintenance workflow persistence, interrupted execution, fault handling and evidence. |

The review used indexed visible body/table extracts, requirement text and adjacent attributes. Existing sources S1-S3 were used to check omissions and parent links. Text inside images/embedded objects and deleted revisions is not covered.

**Applied methodology:** the Railway-RAM, REQ-Review and Document Review skills listed above; RAM-Metrics for target interpretation and operational evidence.

Apply the following distinction:

1. **Direct IPS obligation:** the requirement addresses IPS hardware/platform behaviour and identifies the applicable IPSS release. Record it in the IPS RAM requirements register.
2. **Supporting/interface obligation:** the requirement belongs to ADM or WFM, but supplies an IPS diagnostic, recovery, maintenance or evidence function. Cross-reference it with its original owner; do not silently reallocate application implementation to IPS.
3. **Conditional/open requirement:** draft, in-negotiation, optional, proposed for descoping, or without an applicable IPSS release. Record its disposition explicitly; neither assume compliance nor promote it to an approved commitment.

**Recommended structure:** retain Table 7 as the original IPS DPR inventory. Add a separately titled table in section 6.2, **"Additional RAM requirements and supporting interface obligations"**, with source, ID, synopsis, status, release, ownership, applicability, verification method and evidence reference. Include MDR/FUR/GCR/DOR requirements where their effect is RAM-relevant; the category suffix alone is not an adequate selection rule. All tables below identify proposed **RAM Plan section numbers**, not sections of this review.

### 6.2 Direct cabinet requirements to include

Unless stated otherwise, the following N1 requirements are **approved, mandatory and explicitly include IPSS OBB 1.0.0**. Synopses preserve their scope; the RAM Plan should reference the full controlled text.

| N1 requirement ID | Requirement / IPS RAM significance | Where to list and address it in the RAM Plan | Verification/evidence to add |
| --- | --- | --- | --- |
| GENCAB:HW-SSS:REQ:0024 | Network availability of a location >= **99.9999%**. | Section 4.2 target/boundary table and section 6.2 supplementary register. Cross-reference IPS REQ-01301; do not assume "location network" and "core network" have identical boundaries. | Section 5.6 dependency-aware network analysis; proposed 5.8 model review and supporting failover tests. |
| GENCAB:HW-SSS:REQ:0031 | A single HW-component failure must not cause operational restrictions; source comment limits this to single LRU failures. | Sections 4.1 and 6.2; derive the applicable failure list in 5.4. | FMEA and representative LRU fault-injection tests in 5.8; identify required SW support and coverage limits. |
| GENCAB:HW-SSS:REQ:0081 | HW-component failure shall be diagnosed. | Sections 4.1/4.3 and 6.2; link IPS monitoring and ADM alert obligations. | FMEA diagnostic coverage; end-to-end fault/alarm tests and detection-latency evidence in 5.8. No numerical detection limit is supplied by this requirement. |
| GENCAB:HW-SSS:REQ:0095 | Failure of one network connection shall not affect availability of other connections. | Sections 3.3, 4.1 and 6.2. | Network fault-containment tests in 5.8, not just demonstration of a second cable. |
| GENCAB:HW-SSS:REQ:0097 | Failure of one server shall not affect availability of other servers. | Sections 3.3, 4.1 and 6.2. | Server-loss and redistribution tests; check surviving service load and isolation. |
| GENCAB:HW-SSS:REQ:0098 | A PDU failure shall have no operational consequences. | Sections 3.2/3.3 and 6.2. | Feed mapping, FMEA and authorised PDU-loss test in 5.8. |
| GENCAB:HW-SSS:REQ:0099 | A UPS failure shall have no operational consequences. | Sections 3.2/3.3 and 6.2; state customer UPS interface responsibilities. | Demonstrate downstream independence and surviving supply; retain external UPS evidence/assumptions explicitly. |
| GENCAB:HW-SSS:REQ:0083 | UPS phase wiring shall tolerate HW failures; one phase outage must not affect other phases. | Sections 3.2/3.3 and 6.2. | Wiring/protection review and phase-loss verification, coordinated with electrical V&V. |
| GENCAB:HW-SSS:REQ:0044 | Availability-critical servers/routers/switches require at least two independent power supplies. | Sections 3.2/3.3 and 6.2. This supports a qualified hardware redundancy statement, not a claim that every component is redundant. | BOM/configuration and independent-feed inspection; loss-of-supply tests. |
| GENCAB:HW-SSS:REQ:0011 | Cabinet supports two independent three-phase supplies. | Sections 3.2 and 6.2; include power boundary in 5.6. | Cabinet supply design and installation/interface inspection. |
| GENCAB:HW-SSS:REQ:0113 | Each server connects to each switch in its server cabinet. | Sections 3.2/3.3 and 6.2. | Topology inspection and path-loss tests. Source comment explicitly says this does **not** require two links from every server to every individual switch. |
| GENCAB:HW-SSS:REQ:0114 | Internal-network switches connect to the two network-cabinet routers. | Sections 3.2/3.3 and 6.2. | Approved connectivity matrix and router/path failure tests. |
| GENCAB:HW-SSS:REQ:0115 | External-network switches connect to two network-cabinet routers. **Approved but optional**, IPSS OBB 1.0.0. | Section 6.2 with an explicit selected/not-selected disposition; sections 3.2/3.3 if selected. | Confirm deployment applicability before assigning tests or claiming coverage. |
| GENCAB:HW-SSS:REQ:0086 | Planned/corrective maintenance and LRU replacement shall not impair other LRUs or overall system operation/reliability. | Sections 4.3, 5.7 and 6.2. | Maintenance/replacement demonstrations at load; assess degraded redundancy and reintegration. |
| GENCAB:HW-SSS:REQ:0087 | HW exchange/cabling through successful power-on within **45 min (2700 s)** of **1 h (3600 s) MRT**. | Sections 4.3, 5.7 and 6.2; reconcile with restoration inputs in 5.6. | Timed maintenance demonstration with defined personnel, tools, spares and initial state. The remaining 15 min is described in the source comment for SW/update/integration; do not treat 45 min as full service restoration. |
| GENCAB:HW-SSS:REQ:0010 | HW maintenance-free, or minimum maintenance interval **6 months**. | Sections 4.3, 5.7 and 6.2. | Approved maintenance schedule and supplier instructions; account for any service impact. Do not equate this automatically to a requirement on patch cadence. |
| GENCAB:HW-SSS:REQ:0106 | Servers/cables accessible for maintenance; servers can be pulled out fully during operation using cable-management arms. | Sections 4.3, 5.7 and 6.2. | Physical maintenance-access demonstration without unintended cable/service interruption. |
| GENCAB:HW-SSS:REQ:0116 | Cabinet temperature/humidity sensor; status supplied to PDU. | Sections 3.2, 4.3 and 6.2. | Sensor-to-PDU-to-monitoring chain verification, linked to ADM REQ-01130. |
| GENCAB:HW-SSS:REQ:0118 | HW remotely exposes performance data. | Sections 4.3 and 6.2; field data provision in proposed 5.8. | Interface/data checks and evidence availability under degraded operation. Performance data alone is not a complete outage record. |
| GENCAB:HW-SSS:REQ:0046 | Three server cabinets plus one network cabinet limited to **22.2 kW**. | Section 3.2 operating assumptions and 5.6 shared-power/cooling dependencies; cross-reference in 6.2. | Power/cooling capacity evidence for the approved load/configuration. It is not a failure-rate or availability target. |
| GENCAB:HW-SSS:REQ:0059; GENCAB:HW-SSS:REQ:0063 | EMC and indoor-storage environmental conditions. | Section 5.1 prediction/qualification conditions and 6.2 supporting constraints. | Reference qualification and storage evidence; do not infer compliance merely from a Ground Benign prediction assumption. |

**Important quantitative qualification:** N1 REQ-0088 is **draft**, not approved. It specifies compute-server class-1 support using **99.9998% at MTTR 6 h**, **99.9996% at 10 min**, and **99.9996% at 2 min**, and cites DIL-CU availability distribution. List it as a pending allocation input in sections 4.2/6.2 and assess in 5.6; these are not an approved numerical split between IPS, VIL and ADM.

### 6.3 ADM requirements to cross-reference as IPS dependencies

For N2, the implementation owner remains ADM unless the controlled allocation says otherwise. Include these in the section 6.2 **supporting/interface** register rather than relabelling them IPS DPRs.

| N2 requirement ID(s) | Requirement / relevance | Status / release and proposed RAM Plan location |
| --- | --- | --- |
| EL4-ADM-SSS-REQ-04641-DPR | ADM overall availability >= **99.995%, class 2**; origin DIL REQ-01481. | Approved, IPSS OBB 1.0.0. Sections 4.2/6.2 and model in 5.6, **with the parent/child conflict in 6.5 below left open**. |
| EL4-ADM-SSS-REQ-04632-MDR | Data for RAM statistics: VIL-instance starts, stops with reasons, and each remote-control-line state transition. | In negotiation, IPSS OBB 1.0.x. Sections 4.3/6.2 and proposed 5.8 operational evidence. Confirm event completeness and agreed interface, not just data visibility in a GUI. |
| EL4-ADM-SSS-REQ-04651-MDR | Data inputs required by FRACAS; source explicitly references IPS REQ-00029 and REQ-00031. | In negotiation, IPSS OBB 1.0.x. Sections 6.2 and proposed 5.8; evidence/reporting deliverables in 6.1. This is a concrete platform-to-ADM-to-FRACAS traceability path. |
| EL4-ADM-SSS-REQ-00003-FUR; EL4-ADM-SSS-REQ-00004-FUR; EL4-ADM-SSS-REQ-00005-FUR | Health endpoint for liveness/readiness, database schema installation/upgrade/downgrade artifact, and use of the system message broker. | Approved, IPSS OBB 1.0.0. Sections 5.6/6.2 and 5.8 tests of health detection, schema compatibility and database/broker outage recovery. Do not infer a maximum recovery time or successful rollback from artifact delivery alone. |
| EL4-ADM-SSS-REQ-01104-FUR; EL4-ADM-SSS-REQ-01105-FUR; EL4-ADM-SSS-REQ-01108-FUR; EL4-ADM-SSS-REQ-01110-FUR; EL4-ADM-SSS-REQ-01112-FUR; EL4-ADM-SSS-REQ-01115-FUR; EL4-ADM-SSS-REQ-01117-FUR; EL4-ADM-SSS-REQ-01119-FUR; EL4-ADM-SSS-REQ-01121-FUR; EL4-ADM-SSS-REQ-01122-FUR; EL4-ADM-SSS-REQ-01123-FUR; EL4-ADM-SSS-REQ-01124-FUR; EL4-ADM-SSS-REQ-01130-FUR | Alerts for PDU, NSP, IPS base layer, nodes, links, disks, PSU, fans, NTP, memory, network health, CPU and cabinet environment. | Approved; confirm individual release assignments in the controlled matrix. Sections 4.3/6.2, FMEA coverage in 5.4 and end-to-end alarm verification in 5.8. |
| EL4-ADM-SSS-REQ-01301-FUR; EL4-ADM-SSS-REQ-01302-FUR; EL4-ADM-SSS-REQ-01303-FUR; EL4-ADM-SSS-REQ-01304-FUR; EL4-ADM-SSS-REQ-01305-FUR; EL4-ADM-SSS-REQ-01306-FUR; EL4-ADM-SSS-REQ-01307-FUR; EL4-ADM-SSS-REQ-01308-FUR; EL4-ADM-SSS-REQ-01309-FUR; EL4-ADM-SSS-REQ-01310-FUR; EL4-ADM-SSS-REQ-01311-FUR; EL4-ADM-SSS-REQ-01312-FUR; EL4-ADM-SSS-REQ-01313-FUR | Platform/service monitoring: Alert Manager, certificate manager, Elasticsearch, ETCD, Keycloak, default/system applications, resources, database, broker, Prometheus, general alarms and Ceph. | Approved, IPSS OBB 1.0.0. Sections 5.4/5.6/6.2 and 5.8; include failures of monitoring itself and shared database/storage dependencies. |
| EL4-ADM-SSS-REQ-01413-FUR; EL4-ADM-SSS-REQ-01415-FUR; EL4-ADM-SSS-REQ-01502-FUR | Missing-component alarm with configurable delay; timestamp/service/category information; site power-supply health. | Approved, IPSS OBB 1.0.0. Sections 4.3/6.2 and 5.8. Record alarm delays in detection/restoration assumptions and do not assume transient faults always produce retained alarms. |
| EL4-ADM-SSS-REQ-03205-FUR; EL4-ADM-SSS-REQ-03207-FUR; EL4-ADM-SSS-REQ-03208-FUR; EL4-ADM-SSS-REQ-03209-FUR; EL4-ADM-SSS-REQ-03211-FUR | Database-disturbance/retrofit/normal modes; GUI functions disabled in disturbance/retrofit; infrastructure alarms suppressed during retrofit. | Approved, IPSS OBB 1.0.0. Sections 5.4/5.6/6.2 and 5.8: model diagnostic blind periods and verify return to monitoring after maintenance/database recovery. A "healthy platform" cannot be inferred from absence of alarms. |
| EL4-ADM-SSS-REQ-08319-FUR; EL4-ADM-SSS-REQ-08321-MDR; EL4-ADM-SSS-REQ-08322-MDR; EL4-ADM-SSS-REQ-08325-MDR | IF-72 monitoring interface; diagnostic/logging provision via SDI; maintenance update interface; two independent physical SMI/SDI channels. | Approved, IPSS OBB 1.0.0. Sections 3.2/4.3/6.2 and 5.8 interface/path-failure tests. Link to IPS interface responsibilities; do not assume application redundancy follows from two physical links. |
| EL4-ADM-SSS-REQ-04612-DOR; EL4-ADM-SSS-REQ-04621-DOR | EULYNX maintainability compliance and printed/electronic support documentation/user manuals. | Approved, IPSS OBB 1.0.0. Sections 4.3/5.7/6.2; reference manual/review deliverables in 6.1. |
| EL4-ADM-SSS-REQ-08401-MDR; EL4-ADM-SSS-REQ-08402-MDR; EL4-ADM-SSS-REQ-08403-MDR; EL4-ADM-SSS-REQ-08404-MDR | DGP diagnosis reception/storage, at least **6 JSON messages/s per station**, payload from **up to 160 stations**. | Approved, IPSS OBB 1.0.0. Sections 5.6/6.2 and 5.8 representative-load/recovery tests. Treat as a workload dependency; this does not establish a general IPS maximum-station capacity or an agreed retention duration. |

**Existing IPS requirements exposed by these new cross-links:** S2 REQ-00031-MDR (approved) collects HW/workload monitoring data for ADM; REQ-00029-MDR, REQ-00032-MDR and REQ-00044-MDR (in negotiation) cover monitoring/log diagnosis, alert triggers and syslog transmission; REQ-00047-FUR (approved) covers environmental warning/limit monitoring. All target IPSS OBB 1.0.0 in S2 and are absent from the DPR-only Table 7. Add them to the new section 6.2 register, with sections 4.3/5.4 and proposed 5.8 covering their verification. They are **not new SSS requirements**, but newly identified omissions from the RAM Plan's inventory. Reconcile against S1's cited SSS edition before issue.

### 6.4 Workflow Manager requirements relevant to maintenance and recovery

N3 reuses **RETROFITGUI** identifiers; retain these identifiers for traceability. The following entries are **approved in the source**, but their individual release attributes use **RETROFIT** versions, not an IPSS release. The document identifies reuse for DIL/IPSS; confirm the component-version-to-IPSS mapping before recording applicability as closed.

| N3 requirement ID(s) | RAM relevance and required evidence | Where to identify it in the RAM Plan |
| --- | --- | --- |
| RETROFITGUI:SSS:REQ:0024; RETROFITGUI:SSS:REQ:0025; RETROFITGUI:SSS:REQ:0027 | Persist scenario structure/current execution state and variables; resume interrupted scenarios. Test application/database interruption during representative maintenance workflows and recovery of the correct execution state. | Section 6.2 supporting requirements; 5.7 maintenance and proposed 5.8 recovery campaign. Persistence is not proof of exactly-once execution or safe automatic rollback. |
| RETROFITGUI:SSS:REQ:0028; RETROFITGUI:SSS:REQ:0029; RETROFITGUI:SSS:REQ:0007; RETROFITGUI:SSS:REQ:0155; RETROFITGUI:SSS:REQ:0130 | Scenario/task timing and state, per-execution log files, log location and IF-08 events. Link workflow evidence to maintenance duration, failures and field records. | Sections 5.7/6.2, proposed 5.8 field evidence and 6.1 evidence deliverables. These records alone do not measure end-to-end interlocking downtime. |
| RETROFITGUI:SSS:REQ:0055; RETROFITGUI:SSS:REQ:0048; RETROFITGUI:SSS:REQ:0081; RETROFITGUI:SSS:REQ:0083 | Task timeouts and SUCCESSFUL/WARNING/FAILURE handling. Verify failure and NOK responses remain visible and lead to the intended workflow disposition. REQ-0083 defines SUCCESSFUL by absence of Java exceptions, not by proof of operational service restoration. | Sections 5.4/5.7/6.2 and proposed 5.8 timeout/error-path tests; define service-level success separately. |
| RETROFITGUI:SSS:REQ:0177; RETROFITGUI:SSS:REQ:0178; RETROFITGUI:SSS:REQ:0179; RETROFITGUI:SSS:REQ:0188 | Parallel scenarios, prohibition on a second execution in the same running tab, and configurable concurrency. Assess maintenance actions on redundant resources; a per-tab restriction is not a system-wide maintenance interlock. | Sections 5.4/5.7/6.2 and proposed 5.8 concurrency tests. Any cross-resource exclusion rule must be derived and approved, not assumed to be present in N3. |
| RETROFITGUI:SSS:REQ:0212; RETROFITGUI:SSS:REQ:0213; RETROFITGUI:SSS:REQ:0214 | Health probes, database installation/upgrade/downgrade artifact, system broker dependency. Verify readiness/recovery and schema compatibility under the approved platform configuration. | Sections 5.6/6.2 and proposed 5.8; link to existing IPS database/storage/broker DPRs. |

Do **not** copy every WFM GUI, XML-format or programming-language requirement into the RAM Plan. Keep detailed application verification in its own V&V records and reference only the RAM-relevant evidence. N3 contains no identified numerical WFM availability target that can fill the missing IPS budget allocation.

### 6.5 Conflicts, conditional requirements and required clarification

| Priority / finding | Source evidence | Treatment in the IPS RAM Plan |
| --- | --- | --- |
| **High - ADM parent/child target mismatch** | N2 REQ-04641-DPR says: "The [ADM] shall have a class 2 overall availability of at least 99,995%." Its cited parent S3 REQ-01481 says: "The [ADM] shall have a class 3 overall availability of at least 99.99 %." | Show **both** in section 4.2 with their source/status and open discrepancy. A stricter child is not inherently infeasible, but its intentional derivation and approved boundary must be confirmed. Do not silently select one, call them equivalent, or treat either as the approved IPS allocation. |
| **High - maintenance time is not service restoration** | N1 REQ-0087 says: "The manual corrective maintenance actions of a HW component (incl. router, switches, control plane, computing server, storage engine) like exchange, cabling, etc. up to the successful power-on shall be done within 45 minutes of an MRT = 1 hour." N1 draft REQ-0088 separately uses 6 h MTTR for its manual category. | Sections 4.3/5.6/5.7: reconcile HW repair, SW integration, dispatch/logistics, service restoration and full redundancy restoration. The 1 h MRT and 6 h MTTR are not automatically contradictory, but require distinct boundaries and justified model inputs. |
| **High - diagnostic evidence may be unavailable** | N2 REQ-03211 suppresses infrastructure/HW alarms in retrofit; REQ-03208 disables infrastructure GUI functions during database disturbance. | Cover monitoring loss and recovery in 5.4/5.6/5.8; define retained/raw evidence and operational procedures. Do not assume suppressed alarms establish outage-free operation. |
| **Medium - draft hardware allocation and maintainability obligations** | N1 REQ-0088, REQ-0122 (7-year continuous use), REQ-0124 (replacement tools), REQ-0134/0135/0137 (spares storage), REQ-0139 (balanced server distribution), REQ-0142 (cooling assessment), REQ-0027/0028 (manuals), REQ-0082 (LRU/MAC labelling), and REQ-0131 (grounding concept) are draft and include IPSS OBB 1.0.0. | List as **pending**, not approved, in 6.2. Address their respective availability/design rules in 3.3/4.2/5.6, lifecycle/environment in 3.2/5.1, and maintainability/manuals in 4.3/5.7/6.1. Link grounding/cooling evidence to common-cause assumptions. |
| **Medium - draft single-supply exception** | N1 REQ-0138 permits single supply for non-availability-related components only with monitoring and automatic backup switch-over; status draft, IPSS OBB 1.0.0. | Sections 3.2/6.2: document proposed exceptions separately from approved critical-HW dual-supply REQ-0044. Confirm component criticality, backup and approval before use in the RAM model. |
| **Medium - negotiated hardware/interface constraints** | N1 REQ-0145/0146 specify 7-year COTS life/spares supply; REQ-0123 addresses EN 50126 Basic Integrity; REQ-0129/0130 address external-network connections/cabling; REQ-0132 concerns grounding back-effects. All are in negotiation and target IPSS OBB 1.0.0. | Pending entries in 6.2; lifecycle/maintenance in 4.3/5.7, assurance method in 5.1, interface independence/common causes in 3.2/5.4/5.6. Do not turn useful-life figures into MTBF predictions. |
| **Medium - split-brain topology not yet baselined** | N1 REQ-0140/0141 require ToR/core-router and geo-interconnection wiring to follow the split-brain concept; both in negotiation, IPSS OBB 1.0.0. | Sections 3.2/3.3/6.2 with pending status; coordinated RAM/safety evidence in 5.4/5.8. Obtain the actual controlled concept and interface allocation; these requirements do not prove the independent supervision proposal has been implemented. |
| **Medium - pending ADM maintenance/master controls** | N2 REQ-04631 (preventive maintenance) and REQ-00011 (manual VIL master selection) are in negotiation for IPSS OBB 1.0.0; REQ-04632/04651 remain in negotiation for 1.0.x. | Section 6.2 open/interface entries and 4.3/5.7/5.8 where relevant. Confirm command authority, maintenance conditions and evidence provision without assuming safety functions belong to IPS. |
| **Medium - geo/DDSP release mismatch** | N2 REQ-00010 manual geo switch-over is in negotiation for **IPSS OBB 3.0.0**, while S2's IPS geo switch-over features target 2.0.0. N2 REQ-03106 consolidated DC view and REQ-04611 DDSP maintainability target **2.0.0**; N3 excludes DDSP integration in Phase 1 and describes it as planned for Phase 3. | Section 6.2 deferred/clarification register and release-specific 5.8 campaign. Reconcile phase terminology and releases across IPS/ADM/WFM; do not claim end-to-end manual geo operation or DDSP evidence for 1.0.0 from component-level requirements alone. |
| **Medium - re-used OMC/BFZ clauses are not automatically DSTW requirements** | N1 REQ-0089, REQ-0091/0092/0093/0094/0096 have BFZ-only target releases and OMC/subsystem wording. REQ-0090 is optional with no populated target release. N1 REQ-0008's 25-year useful-life statement and REQ-0009 obsolescence clause have BFZ-2.0 applicability. | Record a reuse/applicability decision in 6.2 before import. Do not substitute class-2 BFZ/OMC figures for DIL class-1 allocation or commit IPS to 25-year unchanged COTS life. |
| **Medium - proposed deletion/descoping** | N2 REQ-01125 cluster monitoring is **To be deleted**. N1 REQ-0121 automatic HW startup, REQ-0133 replacement without impact, REQ-0136 spares-storage effort and REQ-0143 labelling are **to be descoped**, not formally removed by that label alone. | Keep an explicit disposition/open change reference in 6.2; do not silently add as accepted new commitments or delete from an existing approved baseline. Use approved REQ-0086 for maintenance-impact coverage and confirmed active IPS restart requirements as applicable. |

### 6.6 Exact RAM Plan insertion map and closure

| RAM Plan location | Proposed addition |
| --- | --- |
| **2.1 Referenced Documents** | Add N1-N3 with controlled edition/revision and references to their applicable verification/interface records. Avoid duplicate cabinet references under the old and new filenames. |
| **3.2 Hardware Components / 3.3 RAM Design Rules** | Explicit source-linked power, phase, PDU/UPS, server/switch/router connectivity and failure-containment rules; approved configuration and pending topology decisions distinguished. |
| **4.1 Reliability Requirements** | Single-LRU fault tolerance, diagnosis and fault containment, with hardware/software/interface boundaries. |
| **4.2 Availability Requirements** | N1 location-network target; pending compute-server category allocation; ADM service target and parent discrepancy. Preserve service-specific and system-wide outage classes. |
| **4.3 Maintainability Requirements** | Approved hardware repair/maintenance/access obligations; diagnostic data provision; negotiated spares/lifecycle/application obligations visibly pending. |
| **5.1 / 5.4 / 5.6 / 5.7** | Environmental/prediction basis; FMEA diagnostic and common-cause coverage; shared service/dependency models; maintainability demonstrations and WFM recovery/concurrency evidence. |
| **Proposed 5.8 RAM Verification & Demonstration** | Extend the Chapter 3 proposal of this review beyond its original 37 DPRs: power/phase/PDU/UPS and LRU faults, alarm-chain failures/blind periods, ADM/WFM database and broker recovery, maintenance workflows and field-data handover. Retain the source verification method and supplement it where necessary through approved V&V planning. |
| **6.1 RAM Deliverables** | Add/identify the supplemental applicability register, diagnostic/FMEA coverage, maintenance timing evidence, coordinated ADM/WFM test reports, data handover specification and unresolved baseline/target decisions. These may be controlled sections of existing deliverables; separate documents are not necessarily required. |
| **6.2 RAM Requirements** | Keep original Table 7 traceable; add the supplementary table described in 6.1 of this review. Track direct IPS, supporting interface, pending, deferred and not-applicable dispositions with justification and owner. |
| **6.3 Periodical RAM activities report** | Report applicability/verification gaps and FRACAS evidence status, with links to the agreed operational reporting arrangements rather than treating plan revision history as a performance report. |

**Required closure actions:** Requirements Management and the IPS/DIL design and RAM leads should agree the ADM target discrepancy, confirm N1-N3 baselines and component/IPSS release mapping, assign direct/interface ownership, and populate the new register with evidence milestones. The V&V lead should incorporate the additional fault, maintenance and recovery cases; the service/data owner should agree usable FRACAS inputs and handling of diagnostic blind periods.

**Acceptance for this review update:** the additional sources, identifiable requirements, source statuses/releases, RAM significance, exact proposed plan locations and open discrepancies are documented above. This does **not** close their engineering verification or authorise unresolved draft/negotiated requirements.

## 7. Additional Comment - Software/Platform Failures, Failover and FRACAS

### 7.1 Executive assessment and proposed reply

**Disposition: accepted, with an evidence qualification.** A random-hardware prediction alone cannot demonstrate the availability of the complete IPS database, message-broker, PKI or storage service. However, the assertion that software/configuration/upgrades cause **most** IPS unavailability is not substantiated by project failure/exposure data. Treat these as potentially significant contributors requiring assessment, not an already measured distribution.

**Reply suitable for the review register:**

> **Accepted.** The hardware reliability prediction addresses permanent random hardware failures only; it is not intended as the complete demonstration of the IPS service availability targets.
>
> Consistent with the approach in the other RAM Plans, software and platform faults will be recorded, analysed and followed through corrective action by the project FRACAS to be implemented. Its scope will explicitly include virtualization, orchestration, storage, databases, messaging, PKI, configuration changes and failed upgrades, including common-mode effects on redundant instances.
>
> FRACAS will be complemented by a service dependency/failure analysis and release-specific verification of fault detection, failover coverage, recovery, reintegration and upgrade/rollback behaviour. These activities will supply evidence before operational data are sufficient, while FRACAS will provide operational feedback and corrective-action effectiveness evidence.
>
> The RAM Plan will distinguish hardware prediction, platform assurance and measured operational performance. A future FRACAS, successful individual failover tests or architectural redundancy alone will not be presented as proof of 99.9999% service availability. Any uncovered contributions, unverified recovery assumptions or insufficient operational evidence will remain explicit limitations in the RAM demonstration.

### 7.2 Repository evidence and relationship to the existing FRACAS proposal

**Applied Skills:** Railway-RAM, REQ-Review, RAM-Metrics and SRS-SKILL-0020 Document Review, as listed above. The mapped local FRACAS skill was searched for but is not present in the Skills folder; the following corporate/project sources were used instead.

| Evidence | Relevance / limitation |
| --- | --- |
| S1 section 5.6: "An analysis of SW reliability is not part of the Reliability Analysis where only permanent random HW faults and system failures will be analysed." | Valid boundary for a HW prediction, but incomplete if used as the boundary of the entire service-availability demonstration. Clarify the distinction rather than inventing a software FIT prediction. |
| [Corporate FRACAS procedure, draft with RAM comments](<../../../../Knowledge/Process/RAM-Process/G-PRC_L0609_00_EN - FRACAS_draft_comments_RAM-AT.docx>) | Explicitly includes software failures and baseline-changing corrective actions, with effectiveness assessment in operation. Confirm approved revision before use as governing procedure. |
| [Existing FRACAS input for the RAM Plans](RAMP_FRACAS_input.md) | Draft IPS scope already includes virtualization, cluster management and ADM; proposes event-based pilot analysis followed by wider data collection/statistical assessment. It is not proof that FRACAS is operational. |
| [DSTW FRACAS project summary](../../DSTW_FRACAS_Project_Summary.md) | Records proposed project-level organisation, tool/data decisions and open points. Secondary planning information, not an approved service-availability demonstration. |
| [FRACAS lessons learned](../../../../Knowledge/Lessons_Learned/FRACAS_Lessons.md) | Supports configuration-linked events, timely evidence retention, recurrence analysis and effectiveness-based closure. |
| S2 Table 7 service requirements and N2/N3 monitoring/recovery requirements reviewed in Chapters 3 and 6 | Existing requirement anchors for service-specific verification and operational data; their individual release/status restrictions remain applicable. |

**Reconciliation with the earlier draft:** the separate FRACAS input proposes IPS section **5.8 FRACAS**, whereas this review already proposes **5.8 RAM Verification & Demonstration**. For this review, retain **5.8** for demonstration and use a new **5.9 FRACAS**, cross-referenced by 5.8. Agree numbering at plan integration; do not create two section 5.8 entries.

The earlier FRACAS draft's IPS adaptation says "No own IPS requirement". This must **not** override the explicit IPS service-level DPRs in S1/S2. Monitor those applicable targets as well as the IPS contribution to DIL-CU and the separately resolved ADM target. This note does not modify the other draft.

**Inputs and assumptions:** the user identifies OpenStack, Ceph, Kubernetes, RabbitMQ and PostgreSQL as the platform stack. S2 corroborates OpenStack/Kubernetes and the relevant service classes; N2 includes Ceph monitoring. Exact product versions, database/messaging deployment, clustering/quorum modes, PKI implementation and approved upgrade strategy remain to be confirmed from the controlled design. Candidate failure scenarios below are engineering proposals, not findings that those failures have occurred.

### 7.3 Proposed clarification of RAM Plan section 5.6

Replace the SW exclusion sentence with the following proposed wording, retaining the existing hardware prediction method:

> The quantitative hardware reliability prediction covers permanent random hardware failures using the approved prediction method and environmental assumptions. It forms one part of the IPS service-availability assessment and does not, by itself, demonstrate the complete service-level availability targets.
>
> Software, platform, configuration and upgrade-related faults will be addressed through a complementary service dependency and failure analysis, verification of detection, fault containment, failover and recovery behaviour, controlled change/release assurance, and the project FRACAS described in section 5.9. The analysis will cover shared dependencies and common-mode failures of redundant instances, and will distinguish service restoration from restoration of full redundancy.
>
> Systematic software faults will not be assigned unsupported constant hardware-like failure rates. Any empirical software/platform incident frequency or recovery input used quantitatively will identify its source, configuration, workload, exposure, uncertainty and applicability. Where evidence is insufficient, the unquantified contribution and the resulting limitation on the availability claim will be stated explicitly.

Do not equate compliance with a development process or use of redundant open-source products to numerical availability proof. Shared software/configuration, common databases, storage, network control and upgrade actions can defeat apparent HW independence.

### 7.4 Proposed analysis and verification coverage

Extend the HW-FMEA with a **platform/service failure analysis**, either as a distinct section or a linked analysis. For each scenario, record cause/trigger, affected function, local and operational effects, detection, redundancy/common dependencies, recovery path, service interruption, evidence, owner and residual limitation.

#### 7.4.1 Ready-to-insert addition to "RAM HW-FMEA"

**Insertion:** append the following paragraphs to the RAM Plan's **RAM HW-FMEA** chapter, identified by the author as **5.2**. The reviewed S1 edition numbers this chapter **5.4**; use the heading as the insertion anchor and confirm numbering in the current revision. Applied method: [HW-FMEA](../../../../Skills/HW-FMEA.md), with platform/service scope explicitly complementary to the hardware analysis.

> The RAM HW-FMEA will be complemented by a platform and service failure analysis addressing software, configuration, deployment and upgrade-related faults that may affect IPS availability and maintainability. The analysis will cover the applicable virtualization, orchestration, storage, database, message-broker and PKI services, including their interfaces, shared dependencies and common-mode failures affecting redundant instances. It may be documented as a separate section of the FMEA or as a referenced analysis.
>
> For each relevant function and failure mode, the analysis will identify credible causes, local and higher-level effects, operational consequences, detection methods, fault-containment measures, failover coverage and recovery arrangements. Service restoration and restoration of full redundancy will be distinguished. Assumptions, uncovered failure conditions and recommended actions will be recorded and traced to applicable RAM requirements and verification evidence.
>
> The results will define the fault, failover, recovery and upgrade scenarios to be verified during integration and system testing. Software and platform incidents will subsequently be recorded and analysed through the project FRACAS to be implemented, with corrective actions and their effectiveness tracked to closure. Operational findings will be used to update the analysis. Systematic software faults will not be assigned unsupported random hardware failure rates; this qualitative analysis alone does not demonstrate the numerical service-availability targets.

**Integration note:** this wording makes the complementary analysis a planned activity, rather than merely recommending it. Align the activity/deliverable status in RAM Plan section 6.1 and the verification matrix accordingly before approval. It does not require a separate document or a source-code-level software FMEA.

#### 7.4.2 Service scenarios and verification evidence

| Service / requirement anchor | Candidate failures and dependencies to assess | Required behaviour/evidence in proposed section 5.8 |
| --- | --- | --- |
| Virtualization/orchestration: OpenStack/Kubernetes; IPS REQ-04015/04025/04030 and REQ-09902/09903/09911-09914 | Control-plane/process loss, scheduling/API failure, wrong placement, resource exhaustion, restart loops and configuration errors. Distinguish control-plane unavailability from loss of already-running workloads. | Approved workload operation under control-plane failure, health/readiness behaviour, placement and surviving capacity, restart/redistribution and non-disruptive reintegration. |
| Database: IPS REQ-04009-DPR | PostgreSQL process/leader loss, replication lag, lost quorum/connectivity, full storage, schema/version mismatch and common configuration error, as applicable to the selected design. | Client-visible transaction success, writer authority/fencing, failover/reconnection and committed-data consistency against agreed limits. A restarted database process is not sufficient. |
| Message broker: IPS REQ-06306-DPR | RabbitMQ broker/leader loss, queue/quorum failure, partition, connection storms, resource alarms and failed upgrade, as applicable. | Publish/consume path recovery, acknowledgements and applicable durability/delivery semantics; check unacceptable loss, duplication or backlog against approved criteria, without inventing exactly-once guarantees. |
| Storage: IPS REQ-02001-DPR and REQ-05104/05105/05106-DPR | Ceph process/node/monitor/quorum loss, partition, capacity exhaustion, degraded replication, rebuild overload and erroneous shared configuration. | Application-visible volume/file access and data consistency, quorum behaviour, rebuild/rebalance impact and service operation at representative load during degraded/recovery states. |
| PKI: IPS REQ-05306-DPR | Certificate-service/database loss, renewal/rotation failure, expiry, time synchronization or trust/configuration error. | Management operations covered by the DPR, certificate issuance/renewal/rotation and dependent-service access. Distinguish current sessions from new connections; do not assume cached certificates demonstrate PKI service availability. |
| Shared configuration/upgrades: all affected service DPRs; ADM/WFM dependencies in Chapter 6 | Bad configuration propagated to every replica, incompatible versions/schema, failed rolling update, interrupted workflow, unavailable rollback or restore, monitoring disabled during maintenance. | Release/configuration compatibility review; representative failed/aborted update and recovery tests. Verify rollback where supported, otherwise the approved alternative recovery procedure; confirm user-visible service and data integrity before declaring restoration. |

Conduct fault injection only in an authorised representative test environment. Select scenarios using the approved architecture and operational envelope, not by assuming every listed clustering mode applies. Cross-reference existing service DPRs; no new numerical recovery limits or approved failure rates are created here.

**Failover coverage definition:** document the eligible fault classes for which automatic continued service/recovery is claimed; whether each can be detected, isolated and recovered; excluded/uncovered classes; manual recovery paths; and evidence for each. Include failure of the failover mechanism itself and shared/common-mode faults, not just removal of one healthy replica.

Report test outcomes per fault class, initial state and configuration, including failed attempts. A raw fraction of successful tests is **not** an operational coverage probability when the test scenarios do not represent the operational fault distribution. Do not enter 100% detection/switch-over coverage in the RAM model merely because all selected tests passed.

Measure, with agreed acceptance limits and clock resolution:

- Fault occurrence, detection, isolation, recovery initiation and restoration of the defined service.
- Client retries/reconnection, data resynchronization and any continuing degraded performance.
- Restoration of full redundancy separately from operational service restoration.
- Failed/late recovery, manual intervention and escalation paths.

Include recovery during existing degraded states, partitions, representative demand and permitted maintenance. Validate capacity, common dependencies and quorum/leader behaviour; a safe shutdown can be correct safety behaviour and still be RAM downtime.

#### 7.4.3 Clarification: how the 99.9999% target is to be demonstrated

**Response to the author's clarification:** correct. Extending the FMEA addresses failure coverage, but does not calculate availability or close the numerical demonstration comment. **FRACAS records, together with required-service exposure and complete service-downtime capture, can directly establish actual availability for the observed period.** No software failure-rate prediction or availability model is needed for that retrospective calculation. The principal response is therefore an operational availability demonstration using FRACAS, supported by pre-operational analysis and tests. A predictive model is a separate means of assessing expected availability before operational evidence exists.

**Applied Skills:** RAM-Metrics and Reliability-Prediction, together with the review methods above. The following is a proposed engineering method, using the service targets and evidence limitations identified in this repository; it is not an existing approved demonstration or a calculated compliance result.

| Evidence / activity | Role in demonstrating availability | Limitation |
| --- | --- | --- |
| FMEA / platform failure analysis | Defines service-loss scenarios, dependencies, common-mode failures and recovery paths to include in the model and tests. | Does not establish event frequencies or calculate numerical availability by itself. |
| Quantitative service-availability model | Calculates predicted service unavailability using justified failure/event frequencies, restoration times, redundancy and recovery behaviour. | A hardware-only model does not bound unknown software/configuration/upgrade contributions. |
| Representative failover/recovery tests | Establish interruption durations and validate modelled detection, switching and recovery behaviour, including failed recovery. | Do not establish operational incident frequencies; selected successful tests do not prove six-nines availability. |
| Operational monitoring supported by FRACAS | Directly calculates actual service availability from qualifying downtime and required-service exposure, including software/configuration/upgrade effects under the agreed accounting rules. | Requires complete records and agreed service boundaries, observation period and exclusions. Actual observed availability is not automatically a guarantee of future performance. |

**Inputs and assumptions for the numerical interpretation:** target A_target = 0.999999; illustrative required service time T = 365 x 24 x 3600 = 31,536,000 s; continuous service; no contractual exclusions assumed. Confirm the contractual observation period, service boundary, permitted degradation and exclusions before applying this annual interpretation.

```text
U_target = 1 - A_target = 0.000001
D_allowed = U_target x T = 31.536 s per 365-day year

A_measured = 1 - D_union / T_required
```

Here D_union is the duration of the union of qualifying service-down intervals, in seconds, and T_required is the corresponding required-service observation time, in seconds. Count overlapping outages once for that service. Measure at the defined service interface, not merely by process/node uptime. The annual downtime figure is a target interpretation, not a prediction.

**Operational demonstration:** compare A_measured with 0.999999 for each applicable service over the agreed observation period. Root-cause identification is not a prerequisite for counting downtime: an unresolved software/platform incident still contributes its qualifying service interruption. Component failures that do not interrupt the defined service contribute no service downtime. Failure records alone are insufficient unless required-service time and completeness of downtime capture are also established. Statistical confidence is an additional consideration where required by the acceptance criteria or when extrapolating beyond the observed period; it is not needed merely to calculate actual availability.

For a separate predictive assessment, the contribution of a rare service-affecting event class may be estimated as:

```text
U_i approximately equals nu_i x E[d_i]
```

Here nu_i is the operational event frequency in events/s, and E[d_i] is the mean service interruption in s/event. Both require applicable evidence. If recovery is modelled by branches, E[d_i] must include successful automatic recovery, failed automatic recovery and manual restoration, weighted by justified operational probabilities. Do not equate test pass fractions to those probabilities. This approximation assumes low unavailability and negligible overlap; it is not a substitute for modelling interacting redundant/degraded states. Use a suitable state-based or equivalent availability model where those interactions matter. Model common-mode events explicitly rather than assuming independent replicas or adding the same shared outage several times.

**Missing numerical evidence:** no complete operational service-downtime/exposure dataset demonstrating the target was established in this review. Actual compliance therefore remains to be demonstrated through the planned FRACAS-based measurement over the agreed period. Separately, the reviewed material does not establish validated IPS software/platform event frequencies, operational recovery probabilities or complete restoration-time inputs for a complete prediction. Those predictive inputs are not prerequisites for calculating actual availability from observed downtime. HW prediction standards do not supply missing software/configuration inputs; any predictive sensitivity cases must remain labelled assumptions rather than evidence of achieved compliance.

**Recommended ready-to-insert text for "RAM Verification & Demonstration" (proposed section 5.8):**

> Actual availability of each service subject to a 99.9999% requirement will be calculated using operational monitoring and the project FRACAS. For the agreed observation period, availability will be determined as A = 1 - D / T, where D is the total duration of qualifying service-down intervals, counting overlaps once, and T is the required-service time. Hardware, software/platform, configuration and change/upgrade-related interruptions will be included in accordance with the agreed accounting rules, irrespective of whether root-cause analysis is complete.
>
> Before operational evidence is available, hardware prediction, platform/service failure analysis and representative failover/recovery tests will assess the design and recovery arrangements. Any predictive service-availability model will identify its input sources, assumptions, common dependencies and unquantified contributions. Neither FMEA nor successful failover tests alone demonstrates numerical availability. Unsupported random software failure rates and assumed perfect failover coverage will not be used.
>
> Monitoring and the project FRACAS will provide correlated incident, configuration, service-down/up and exposure records sufficient to establish complete service-downtime accounting. Before demonstration starts, the project will agree the service boundaries, observation period, measurement resolution, exclusions, data completeness checks and acceptance criteria with the responsible acceptance authority. Statistical confidence criteria will be applied where required for acceptance or extrapolation; actual measured availability will remain distinguishable from predicted future performance.
>
> Operational demonstration will compare the calculated actual availability with the applicable target over the agreed observation period. Until complete measurement records support the target under the agreed acceptance criteria, operational compliance will remain open. The RAM assessment will identify missing evidence, responsible owners and demonstration milestones. A complete predictive model is not a prerequisite for calculating actual availability; the intention to implement FRACAS, without collected and validated data, is not itself a demonstration.

**Integration / closure:** retain the section 7.4.1 FMEA addition as supporting scope, but use the text above as the principal answer to the numerical demonstration comment. Link the service DPRs in the V&V matrix to the quantitative model, recovery-test evidence and operational demonstration report. Agree any staged or provisional acceptance explicitly; do not silently substitute qualitative assurance for the numerical target.

### 7.5 Proposed section 5.9 - Software/Platform FRACAS

The following is proposed plan text consistent with the user's stated approach:

> A project FRACAS will be implemented to record, classify and analyse hardware, software and platform failures and to track corrective and preventive actions. For IPS, this includes virtualization and orchestration, storage, databases, messaging, PKI, monitoring, configuration/deployment changes and failed upgrades. The IPS solution element supplies its event analyses and corrective-action evidence to the project-level consolidation.
>
> Event-based collection and analysis will be established during integration and pilot activities, using an agreed interim register and retained platform/ADM records where the final data-exchange solution is not yet available. Test incidents will remain distinguishable from operational incidents. Broader operational monitoring and statistical assessment will be introduced as comparable exposure and validated data become available. Implementation milestones, interim data responsibilities, access arrangements and reporting will be controlled in the FRACAS implementation plan.
>
> Each event will retain the affected service and release/configuration, symptom, known or suspected cause, operational impact, timing, recovery actions and associated change/upgrade. Root-cause analysis will distinguish product defects, configuration/deployment errors, resource/capacity limitations, external dependencies and unresolved causes. Common events affecting multiple replicas or services will be linked; diagnostic messages will not automatically be counted as separate service failures.
>
> Corrective actions will have an owner, planned completion, implementation record and effectiveness criterion. Closure will require appropriate regression/recovery verification and, where needed, follow-up operational exposure. Restart, patch deployment or temporary service restoration alone will not establish that the root cause has been eliminated.
>
> FRACAS reporting will distinguish predicted values, measured availability, indicative trends and unverified assumptions. Data gaps and their effect on the claim will remain visible. Missing records, unknown causes or an outage-free short observation period will not be treated as evidence of zero software downtime.

**Minimum IPS additions to the common FRACAS record:**

| Data group | Minimum content / purpose |
| --- | --- |
| Baseline and exposure | Service/cluster/AZ/site identifiers, SW/image/package versions, configuration revision, active topology, workload, required-service observation intervals and deployments/changes. Enables comparable exposure and recurrence analysis. |
| Event and effect | Correlated incident ID, affected services/instances, process/leader/quorum and client symptoms, service-loss/degradation criterion, and common-mode extent. Retain unknown cause until resolved. |
| Timing and recovery | Fault/detection/alarm times, service-down/up, automatic/manual recovery, restore/rollback/reintegration and full redundancy restoration; explicit missing/uncertain timestamps. |
| Change and diagnostics | Upgrade/configuration trigger, execution history, database/broker/storage/orchestration logs and metrics, time synchronization status, and retention/access arrangements. Protect relevant evidence before resets or redeployment. |
| Actions and effectiveness | Root-cause status, defect/supplier ticket, containment, approved corrective/preventive change, regression evidence, recurrence/exposure review and escalation. |

Retain the agreed availability accounting in Chapter 3: qualifying service-down intervals are counted once per service over required service time. Common platform outages must not be multiplied into independent instance exposure. Upgrade-related downtime is not excluded merely because the intervention was planned; show planned/unplanned categories and apply only agreed contractual exclusions.

**FRACAS rollout and contractual limit:** the separate FRACAS draft defers full statistical assessment until sufficient data and DDSP integration are available. This is a planning proposal, not authority to postpone customer requirement 02_142 / DIL REQ-00672. Its five-year deadline remains measured from first VSTW commissioning unless formally changed. Start interim evidence collection early, identify gaps and agree a recovery plan for data/evidence readiness; do not claim that completion of rollout alone guarantees statistical sufficiency.

### 7.6 Demonstration limits, risks and closure actions

**Six-nines scale:** as calculated in Chapter 4, 99.9999% corresponds to **31.536 s/year** for continuous required service over 365 days. Therefore outages due to upgrades, failover, recovery and shared configuration cannot be treated as automatically negligible. This conversion is an interpretation aid, not a new annual acceptance period.

The complete service assessment must cover HW, software/platform, change/maintenance and external/shared dependencies using the same service boundary, outage rules and release. Avoid adding overlapping contributions twice. Where empirical event frequencies or recovery distributions are unavailable, use justified evidence and sensitivity cases for design evaluation, but identify assumed values as assumptions and do not claim numerical compliance from the HW contribution alone. FRACAS can establish observed availability and support improvement; long-term capability or confidence claims still require adequate comparable exposure and a justified statistical method.

| RAM Plan location / proposed owner | Required change or evidence for closure |
| --- | --- |
| **5.1 and 5.6 - RAM-AM / platform design lead** | Separate HW prediction from complete service availability; adopt the scope wording in 7.3; identify service dependencies, configuration and unsupported numerical inputs. |
| **5.4 - RAM-AM / service owners** | Add or reference platform/service failure analysis, including common-mode faults, uncovered fault classes, diagnosis and recovery assumptions. |
| **5.7 and proposed 5.8 - maintenance / V&V lead** | Define failover coverage and service-specific recovery/upgrade criteria; schedule the tests in 7.4 with release/configuration, load, evidence references and open deviations. |
| **New 5.9 - RAM-AM / service lead / project integrator** | Baseline FRACAS scope, activation milestones, interim data collection, software event classification, supplier escalation and effectiveness-based closure. Reconcile section numbering with the separate FRACAS draft. |
| **4.2, 6.1 and 6.2 - Requirements Manager / RAM-AM** | Keep the database, broker, PKI and storage DPRs visible; link each to analysis, test and operational evidence. Add platform failure analysis, recovery/upgrade reports and FRACAS implementation/reporting records to controlled deliverables. |
| **6.3 - RAM-AM / project management** | Report coverage/evidence gaps, software/configuration/upgrade incidents, service downtime and corrective-action effectiveness. Keep the comment open until planning changes are approved; numerical compliance remains open until the corresponding evidence milestone is met. |

**Recommendation:** retain "software faults will be analysed through the FRACAS to be implemented", but add its scope, owner, interim implementation and evidence obligations, together with the pre-operational analysis and recovery verification above. This preserves consistency with the other RAM Plans without presenting a future process as an already demonstrated availability result.
