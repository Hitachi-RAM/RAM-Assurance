# IPS RAM Plan Ed02PD01 - Responses to RAM Review Comments

| Attribute | Value |
| --- | --- |
| Document reviewed | [RAMP IPS, 3BU 17300 2009 DUAPA, Ed02PD01](../RAMP_IPS_3BU_17300_2009_DUAPA_Ed02PD01.docx) |
| Date | 2026-11-02 |
| Scope | Comment 1: RAM verification and demonstration; Comment 2: customer targets and availability allocation; supplementary SSS applicability review in Chapter 6 |
| Status | Draft responses and proposed plan additions for author approval; neither comment is closed by this note |
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

**Limitations:** The exact controlled [CRS_DSTW] baseline and an approved numerical IPS allocation were not established. This is a response to two comments, supplemented by the SSS applicability review in Chapter 6, not a clause-by-clause EN 50126 compliance assessment. Proposed text below describes future work; it does not assert that the plan has already been amended.

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
