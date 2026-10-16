# VIL Redundancy Restoration Time - Basic 2x2oo2 Configuration

| Attribute | Value |
| --- | --- |
| Date | 2026-10-16 |
| Status | Engineering proposal for review; not an approved requirements baseline or compliance demonstration |
| Scope | Automatic recovery of one complete 2oo2 redundancy partner in the basic VIL configuration without georedundancy |
| Proposed limit | Full redundancy restored within 600 s of failure occurrence |
| Classification | Hitachi Rail - Internal |

## 1. Executive summary

**A maximum of 600 s is a reasonable proposed end-to-end limit for restoring one failed redundancy partner in the basic 2x2oo2 configuration.** It is a limit on the duration of degraded operation, not merely a boot-time allowance.

This proposal is consistent in magnitude with the DPR recommendation of node recovery **< 10 min**, recorded in the repository availability allocation assessment. The proposed wording below uses **within 600 s**, meaning **<= 600 s**. The project must agree whether the approved boundary is strict (< 600 s) or inclusive (<= 600 s).

Acceptance remains conditional on:

- Fault-injection evidence demonstrating recovery and uninterrupted service on the surviving partner.
- A complete availability model confirming the contribution of degraded-state exposure.
- Defined recovery conditions, clock boundaries and completion criteria.

The strong overall availability requirement alone does not prove that 600 s is acceptable. Conversely, it does not justify imposing a universal 120 s or 300 s recovery limit without an allocation or model demonstrating that need. Faster recovery remains a design preference.

## 2. Architecture and terminology

For this note, the informal expression "one VIL instance fails" means **one complete 2oo2 redundancy partner fails**. In the project documentation, a VIL instance denotes the complete station interlocking with its redundant nodes. Use "redundancy partner" or "node" in the requirement to avoid ambiguity.

| State | Available computing architecture | RAM significance |
| --- | --- | --- |
| Normal | 2x2oo2 | Two complete redundant computing nodes available |
| One complete partner failed | 1x2oo2 | Operation can continue, but no remaining node-level availability redundancy |
| Remaining 2oo2 loses operational capability before the first partner recovers | No operational computing node | Service interruption |

The remaining 2oo2 retains its internal safety architecture. It does not retain the node-level availability redundancy provided by the second 2oo2.

This is a computing-node abstraction, not a complete Core-plus-ECMUX service model. ECMUX, interfaces and shared infrastructure must be represented according to their actual topology.

## 3. Timing metric and boundaries

Use **redundancy-restoration time, $T_{\mathrm{RR}}$**, rather than an undefined "startup time", MTTR or MRT. The project documentation uses MTTR for restoration of service; service may never be lost during the single-partner failure considered here.

| Metric | Start | End | Interpretation |
| --- | --- | --- | --- |
| Service interruption | Loss of a required operational function | Required function restored | Expected to be absent for a single-partner failure intended to be masked by redundancy; verify separately |
| Redundancy-restoration time, $T_{\mathrm{RR}}$ | Failure occurrence of one complete redundancy partner | Required redundancy restored and confirmed | Proposed maximum: 600 s |
| Technical startup time | Restart initiation | Relevant runtime/application started | Sub-budget only; not sufficient as a RAM acceptance metric |
| Mean redundancy-restoration time | Same boundaries as $T_{\mathrm{RR}}$ | Same boundaries as $T_{\mathrm{RR}}$ | Model input supported by the timing distribution, recovery success probability and treatment of unsuccessful recovery |

The elapsed recovery path includes:

$$
\begin{aligned}
T_{\mathrm{RR}} ={}& T_{\mathrm{detection}}
                  + T_{\mathrm{isolation/initiation}} \\
                 &+ T_{\mathrm{restart/checks}}
                  + T_{\mathrm{synchronisation/reintegration}} \\
                 &+ T_{\mathrm{confirmation}}
                  \;\leq\; 600\,\mathrm{s}
\end{aligned}
$$

This is a critical-path representation. Activities that run in parallel must not be double-counted.

**If startup alone takes 600 s and synchronisation or reintegration follows afterwards, the proposed end-to-end limit is not met.**

Completion requires more than "VM running" or "processes started". The recovered partner must be accepted, state-consistent and capable of fulfilling its specified redundancy role. Verification must demonstrate that it can maintain the specified service if the previously surviving partner is subsequently lost.

## 4. Availability reasoning

### 4.1 Inputs and assumptions

| Item | Basis |
| --- | --- |
| Overall VIL availability target | $A \geq 99.995\%$, as recorded in the repository availability analyses |
| Proposed recovery duration | $t_{\mathrm{RR}} = 600\,\mathrm{s} = \frac{1}{6}\,\mathrm{h}$ |
| Service during recovery | Surviving partner maintains the specified operational functions without interruption |
| Automatically recoverable fault | Restart/reintegration can correct the fault without physical hardware replacement |
| Independent-failure calculation | Constant surviving-node failure rate over the recovery window; common-cause failures assessed separately |
| Surviving-node failure rate and degradation frequency | Not established for this assessment; required before quantitative acceptance |

### 4.2 Service downtime is not degraded-state exposure

For continuous required service over a 365-day year:

$$
\begin{aligned}
D_{\mathrm{allowed}}
  &= (1-A)\,T_{\mathrm{required}} \\
  &= (1-0.99995)\times 31{,}536{,}000\,\mathrm{s} \\
  &= 1{,}576.8\,\mathrm{s} \\
  &= 26.28\,\mathrm{min}
\end{aligned}
$$

This is the allowed service downtime **per 365-day year**.

The annual conversion is an interpretation aid, not an agreed contractual observation interval.

A 600 s redundancy-restoration event does **not** consume 600 s of this service-downtime budget if the specified service continues uninterrupted. It increases exposure to loss of the remaining operational node instead.

### 4.3 Independent second-failure exposure

Define:

| Symbol | Definition | Unit |
| --- | --- | --- |
| $\lambda_{\mathrm{2oo2}}$ | Rate at which the remaining complete 2oo2 node loses operational capability | $\mathrm{h}^{-1}$ |
| $t_{\mathrm{RR}}$ | Duration of the degraded recovery window | $\mathrm{h}$ |
| $f_{\mathrm{degradation}}$ | Frequency of entry into this degraded state | $\mathrm{h}^{-1}$ |

For a fixed recovery window and an exponential independent surviving-node failure model:

$$
P_{\mathrm{second\ failure}}
= 1 - e^{-\lambda_{\mathrm{2oo2}}\,t_{\mathrm{RR}}}
$$

For $\lambda_{\mathrm{2oo2}}\,t_{\mathrm{RR}} \ll 1$:

$$
P_{\mathrm{second\ failure}}
\approx \lambda_{\mathrm{2oo2}}\,t_{\mathrm{RR}}
$$

For rare, non-overlapping degradation events:

$$
f_{\mathrm{double\ loss}}
\approx f_{\mathrm{degradation}}
        \,\lambda_{\mathrm{2oo2}}
        \,t_{\mathrm{RR}}
$$

Here, $f_{\mathrm{double\ loss}}$ is an approximate frequency of service-loss events caused by an independent second-node failure during recovery. It is not the service unavailability itself. Calculating unavailability also requires the resulting service-restoration duration and the other service-loss contributions.

**Result:** doubling redundancy-restoration time approximately doubles this independent second-failure exposure under the stated assumptions. No VIL-specific probability is calculated because the necessary surviving-node failure rate and event frequency have not been established.

Do not use the approximately 4.455 FIT redundant-system result reported in the historical DPR table as the failure rate of the surviving single 2oo2 node. These are different system levels.

### 4.4 Limitations and risks

- Common-cause failures and shared hosts, power, storage, networks or recovery services are not captured by the independent second-failure formula.
- Software recovery that restarts an application on all redundant nodes is a service-restoration scenario, not uninterrupted single-partner recovery.
- Repeated restart attempts, unsuccessful recovery and permanent faults require explicit model branches; a mean of successful recoveries alone is insufficient.
- Permanent hardware faults require a separate maintenance/replacement restoration requirement.
- Absence of georedundancy leaves the basic configuration dependent on its actual local failure domains; restart speed does not remove shared-site dependencies.
- Do not automatically classify this degraded condition as FK4 because service continues. The repository records that loss of redundancy with risk of total failure may be FK2. Customer classification requires confirmation.

## 5. Proposed requirements

The following wording is a proposal, not a quotation from an approved specification. "Specified service" and "required recovery infrastructure" must be resolved against the approved service boundary and architecture before baselining.

### 5.1 Automatic restoration of redundancy

> Following an automatically recoverable failure of one complete 2oo2 redundancy partner, with the other partner and required recovery infrastructure operational, the system shall restore the specified 2x2oo2 redundancy automatically within 600 s of failure occurrence. This interval shall include fault detection, recovery initiation, restart, required checks, state synchronisation and reintegration. Completion shall require confirmation that the recovered partner is accepted and capable of fulfilling its specified redundancy role.

### 5.2 Continuity during failure and reintegration

> Failure and reintegration of that redundancy partner shall not interrupt the specified operational service maintained by the surviving partner.

The project must separately define the response to failed automatic recovery, including alarm, escalation, retry policy and maintenance intervention. No requirement to bypass safety checks is implied.

## 6. Required evidence and actions

| Action / evidence | Acceptance purpose |
| --- | --- |
| Confirm the 600 s boundary and scope in requirements review | Resolve < 600 s versus <= 600 s, applicable fault classes and operating conditions |
| Define failure occurrence and observable completion events | Ensure detection delay is included and timestamps are traceable |
| Fault-inject applicable node, VM, application and host failures | Demonstrate the actual recovery paths; distinguish local recovery from multi-node restart |
| Test maximum supported station configuration and representative worst-case load/communication conditions | Establish performance under the specified operating envelope |
| Observe surviving-node operational service throughout recovery | Demonstrate continuity rather than assuming it from the topology |
| Verify recovered-node capability by subsequent controlled loss of the previously surviving partner | Demonstrate restored functional redundancy in a controlled test environment |
| Record recovery durations, success probability, retries and unsuccessful recoveries | Provide defensible availability-model inputs |
| Model complete Core, ECMUX, interfaces and shared failure domains | Confirm compliance at VIL service level, including common-cause contributions |
| Agree degraded-state severity classification with the customer | Avoid assuming FK4 when loss of redundancy may be FK2 |
| Define permanent-fault restoration and escalation separately | Prevent automatic-restart limits being applied to physical repair |

Finite testing supports the requirement but does not by itself prove an absolute maximum for every possible execution. The verification argument should combine test evidence with justified timing bounds and the defined operating envelope.

## 7. Repository basis and applied skills

Repository information was used:

- [VIL Availability Requirements Analysis and SW Allocation](VIL_Availability_Requirements_Allocation.md), especially Sections 4.1 and 4.2: automatic-recovery limitations, distinction between service and redundancy restoration, historical CN results and proposed node recovery < 10 min.
- [VIL Availability Requirements - Explanation and Suggestions](VIL_Availability_Explanation.md): availability targets, service-restoration boundaries, single-partner failure interpretation and FK2/FK4 classification uncertainty.

No new hardware reliability prediction, measured recovery performance or standards-clause compliance claim is made. The calculation is a simplified degraded-state exposure assessment supporting EN 50126 lifecycle reasoning.

### Applied Skills

- [Railway-RAM](../../../../Skills/Railway-RAM.md)
- [RAM-Metrics](../../../../Skills/RAM-Metrics.md)
- [Reliability-Prediction](../../../../Skills/Reliability-Prediction.md)
- [REQ-Review](../../../../Skills/REQ-Review.md)
