# VIL shutdown time after fault detection - 5 s isolation and 30 s shutdown

| Attribute | Value |
| --- | --- |
| Date | 2026-11-01 |
| Project | DSTW / VIL |
| Purpose | Preserve the email-review discussion, proposed shutdown-only wording, rationale and approval conditions |
| Status | Discussion note; proposed values, not an approved requirement or compliance demonstration |
| Scope | Single-node fault isolation and shutdown; whole-instance shutdown required by a detected fault |
| Exclusions | Fault-detection latency before detection, subsequent startup, self-tests, recovery and reintegration |
| Handling | Retain with the source documents; their sensitivity and contractual handling restrictions continue to apply |

## Applied Skills

- SRS Document Review (SRS-SKILL-0020): source-based review methodology, separating mechanical corrections from engineering judgement. This note records the discussion; it is not a tracked-change review of the source document.

## 1. Executive summary

The defensible argument is **a fast protective response followed by a bounded shutdown**, not that availability figures mathematically require exactly 5 s or 30 s.

- **5 s** is a proposed maximum for isolating the faulted node. Its adequacy requires the safety/interface fault-containment assessment; a shorter required reaction time takes precedence.
- **30 s** is a proposed maximum for completing node or whole-instance shutdown. It requires a feasible shutdown sequence, bounded dependencies and measured worst-supported-condition evidence.
- These are separate completion milestones. For the single-node proposal, both clocks start at fault detection: isolation within 5 s and shutdown within 30 s, **not 5 s plus another 30 s**.
- Whole-instance controlled shutdown is not automatically required for every node fault. The approved fault-handling logic must determine when it is required.
- No approval of the values or demonstration of compliance occurred in this conversation.

## 2. Source basis and boundaries

Repository information was used:

| Source | Relevant evidence / limitation |
| --- | --- |
| [Timing specification discussion, Ed01, 2026-10-29](../VIL_Timing_Specification_Discussion_Startup_Integration_Shutdown_Ed01_20261029.docx) | Chapter 4 proposes application shutdown <= 10 s, single-node isolation within 2-5 s, node shutdown <= 30 s, and whole-instance shutdown <= 30 s. Section 6 proposes 5 s isolation explicitly. These are proposal values, not independently validated inputs. |
| [Email response: RE VIL Availability (related) Requirements](<../RE VIL Availability (related) Requirements.msg>) | Original subject of the consistency review. The discussion was subsequently narrowed to shutdown after fault detection only. |
| [VIL availability requirements allocation](VIL_Availability_Requirements_Allocation.md) | Identifies incomplete detection/recovery limits, unresolved service/FK4 accounting, and maintenance/shutdown sequencing issues. It is itself an engineering proposal. |
| [VIL availability explanation](VIL_Availability_Explanation.md) | Distinguishes service downtime from no-operational-impact exposure and identifies unresolved interpretation of scenario budgets. |
| [VIL redundancy restoration proposal](VIL_Redundancy_Restoration_Time.md) | Separates service interruption from degraded-state exposure. Its 600 s restoration proposal is outside this note's shutdown-only scope. |
| [Requirements lessons, RL-005](../../../../Knowledge/Lessons_Learned/Requirements_Lessons.md) | Supports explicit availability measures, system boundaries, time periods and exclusions. |

The timing paper's cited updated RAM workbooks were not found under their cited filenames in the repository during the original review. Their claimed results were not independently reproduced. No standards clause or safety response deadline is established by this note.

### Clock definitions proposed for agreement

| Quantity | Start | End | Proposed maximum |
| --- | --- | --- | --- |
| Single-node isolation | Timestamp of detection of an applicable node-level fault | Faulted node prevented from influencing the specified external safety interfaces and surviving partner, as defined by the approved isolation design | 5 s |
| Single-node shutdown | Same fault-detection timestamp | Affected node's defined shutdown sequence complete; no automatic restart included in this measurement | 30 s |
| Whole-instance post-fault shutdown | Timestamp of detection of a fault for which the approved reaction requires whole-instance shutdown | All applicable applications and VMs/operating systems stopped, with required persistent-status handling completed or an explicitly approved alternative outcome recorded | 30 s |

Any delay between fault detection and a shutdown command is included in these proposed post-detection limits. The source's controlled-shutdown wording instead starts at the shutdown trigger. Adopting a fault-detection start is therefore a refinement that needs approval, not a verbatim existing requirement. A planned shutdown remains measured from its command, not a nonexistent fault detection.

## 3. Reasoning: why propose 5 s isolation?

**Engineering purpose:** fault containment must not depend on successful completion of a potentially slow or hung shutdown. The isolation milestone should prevent the identified faulty influence before the node finishes stopping.

**Why the exact number remains provisional:** the source proposes a 2-5 s range and later selects 5 s, but provides no verified safety derivation or measured implementation budget for that selection. Five seconds can be discussed as a candidate ceiling, not declared safe merely because it appears in the paper.

Approval needs:

1. Identification of the hazardous or service-disrupting effects the isolation must prevent.
2. The allowable response time for each relevant fault, interface and operating condition.
3. A budget and tests demonstrating that the isolation mechanism meets that bound, including when the affected application is unresponsive.
4. Confirmation that the surviving partner retains required service for the approved single-node scenarios.

If the required protective response is shorter than 5 s, use that shorter bound. Isolation timing and orderly OS shutdown timing must not be confused.

**Argument to use:** "We propose a separate short isolation deadline so that fault containment is not delayed by application or operating-system shutdown. Five seconds is a candidate allocation, subject to confirmation against the safety/interface response-time requirements and fault-injection evidence."

## 4. Reasoning: why propose 30 s shutdown?

**Engineering purpose:** provide an explicit maximum for the shutdown phase, preventing unbounded waits on applications, file operations, remote storage or operating-system termination.

**Source rationale:** Chapter 4 allocates 30 s to shutdown within a wider restoration-time proposal. That allocation is useful context, but it does not uniquely derive 30 s or establish that shutdown is feasible. This note does not specify subsequent restoration times.

The exact value must be supported by a critical-path budget for the applicable sequence:

`T_post_detection_shutdown = T_reaction_initiation + T_shutdown_critical_path <= 30 s`

Parallel actions are counted by their elapsed critical path, not by adding every action's duration. No measured sub-phase durations were supplied in this discussion.

For whole-instance shutdown, required persistent-status handling is a material dependency. An unavailable network/storage service or deadlocked process may make graceful completion within 30 s impossible. The project must define the approved timeout, escalation, data-validity handling and safe terminal state. Forced termination does not by itself prove successful state preservation.

**Argument to use:** "We propose 30 seconds as a bounded shutdown-phase allowance. It must be shown feasible for the required stop and persistent-status sequence, with an approved response to hung applications or unavailable storage. The value is not derived solely from the availability target."

## 5. Proposed email wording - shutdown only

### Single-node fault

> For a detected fault requiring shutdown of one VIL redundancy partner, I propose two completion limits measured from the same fault-detection timestamp: isolation of the faulted partner within 5 seconds and completion of its shutdown within 30 seconds. The separate isolation deadline prevents fault containment from waiting for orderly application/OS shutdown. The 30-second deadline bounds the shutdown phase itself; it does not include restart, self-tests or reintegration. Both values require confirmation by the responsible safety/interface and platform teams, including evidence that fault containment meets any shorter applicable response limit and that the surviving partner maintains required service.

### Whole-instance shutdown required by a fault

> Where the approved reaction to a detected fault requires shutdown of the complete VIL instance, I propose completion within 30 seconds of fault detection, including initiation of the reaction, stopping the applicable applications and VMs/operating systems, and the required persistent-status handling. This bounds shutdown only and excludes subsequent startup, restoration of service and reintegration. The proposed value must be supported by a shutdown critical-path budget and tests, with an explicitly approved outcome for hung applications or unavailable storage. It is a candidate engineering allocation, not a value demonstrated by the availability requirement.

## 6. Corrections to earlier conversation statements

| Earlier wording / implication | Corrected interpretation |
| --- | --- |
| 5 s is a justified safe response time | It is a proposal; its safety adequacy is not established. A shorter applicable response time takes precedence. |
| 30 s is proved by the 5-minute SLA | The SLA provides wider timing context, not a unique derivation of a shutdown-only limit. Its measurement boundaries also require agreement. |
| Whole-instance 30 s starts interchangeably at detection or command | These are different requirements. A post-detection limit includes the delay to command; the source's controlled-shutdown wording uses a trigger. |
| Any single fault causes zero operational interruption | This is conditional on containment, architecture and continued required service; it is not a universal guarantee. |
| Every application restart causes the same operational outage | Identify and verify the affected function and service impact; do not equate every application with complete train-control service loss. |
| A 10 s application shutdown guarantees 100 s for restart | Remaining time depends on detection and other phases. Under the paper's illustrative 5 s detection allowance, 120 - 5 - 10 = 105 s; shutdown alone does not guarantee recovery. |
| REQ-00569 is an approved additive split of the total annual budget | Scenario aggregation and class-counting rules remain open. Annual availability budgets do not determine shutdown maxima on their own. |
| FK4 exposure proves a 600 s node recovery is acceptable | FK4 classification and exposure rules require agreement; complete-service continuity and dependency risks remain to be assessed. Recovery is outside this note's scope. |

The source also discusses a separate **10 s application-stop proposal**. It must not be silently replaced by the 30 s node/instance limit; any application-level requirement remains separately allocated.

## 7. Risks, required evidence and actions

| Action | Proposed owner | Required evidence / decision |
| --- | --- | --- |
| Confirm applicable fault reactions and response limits | VIL architect + safety/interface leads | Defined fault set, isolation endpoint and response-time assessment; acceptance or tightening of 5 s |
| Allocate and assess shutdown sequence | Core/ECMUX/platform leads | Shutdown critical-path budget; explicit application/node/instance boundaries and reaction initiation delay |
| Resolve persistent-status failure handling | Design authority + storage/platform leads | Approved timeout/escalation and terminal-state/data-validity rules; no assumption that upload always succeeds |
| Verify adverse conditions | V&V lead | Timestamped tests covering maximum supported load, hung applications, unavailable storage/network and relevant VM/OS faults |
| Approve wording and record disposition | Requirements owner + responsible approvers | Baseline/release traceability, accepted maximum limits and closed material findings |

**Recommendation:** retain 5 s and 30 s as discussion candidates until the response-time assessment and shutdown evidence support approval. The strongest justification is functional containment plus demonstrated bounded completion, not an unsupported numerical availability margin.

**Limitation:** this is a corrected engineering summary of the conversation, not a full chat transcript, a safety assessment or an approval record. Source documents remain unchanged.
