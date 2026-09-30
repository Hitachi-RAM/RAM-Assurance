# DSTW Split Brain - Technical Analysis

**Date:** 2026-09-28  
**Scope:** Preliminary safety and RAM assessment of the DIL-CU Split Brain risk and the independent supervision-channel proposal.  
**Status:** Engineering assessment for decision preparation; not a final safety case or architecture approval.

## 1. Executive conclusion

The Split Brain hazard remains credible for the 4x2oo2 geographically redundant configuration when the communication view of the two geo-sites is inconsistent. The most consequential cases are:

- simultaneous loss of the inter-site communication paths;
- loss or restart of both core routers at one site; and
- recovery or reintegration while more than one site can elect a master.

The independent TAS Platform supervision channel is technically feasible and is the strongest currently documented mitigation for these cases. It should proceed to detailed design and validation as the preferred safety mitigation, while the existing Master Token Protocol, Master Confirm Interface, and startup observer mechanisms remain part of the overall defence.

This is not yet an approved solution. The proposal remains subject to hardware selection, topology qualification, availability and CCF substantiation, exposure-time confirmation, ECMUX assessment, and management acceptance of cost and lifecycle impact.

## 2. Hazard and failure mechanism

The NMR architecture requires exactly one Master Computing Node at any time. A network partition can make an active master appear lost to an isolated subgroup. If that subgroup elects a new master, both subgroups may continue to communicate with external equipment independently. The hazardous condition is therefore not only the initial router or link failure; it is the subsequent master election and network reintegration.

The TAS Platform controls documented in the source material have different coverage:

| Control | Main coverage | Limitation requiring confirmation |
| --- | --- | --- |
| Master Token Protocol | Allows election when a valid master-shutdown token is received | Does not resolve a simultaneous loss that prevents the token from being sent or received |
| Master Confirm Interface | Allows an application-specific safety decision before master election | Decision logic, independence, and safety evidence are not yet defined here |
| Independent supervision channel | Compares master state received over a physically separate path with NMR state | It must remain independent in power, hardware, routing, geography, and failure causes |
| Startup observer | Prevents conflicting master selection during startup | Does not by itself establish the state of a running partitioned network |

## 3. Proposed architecture

The latest proposal adds:

- a third, standalone ToR switch for the supervision channel;
- a dedicated mini-router with MACsec capability;
- a physically separate supervision interface on each server blade;
- separate inter-site links for NMR sync channel A, NMR sync channel B, ServiceLink, and supervision; and
- a supervision route via the third location (Wels), without dynamic mixing or rerouting between ServiceLink and supervision traffic.

The proposal states that the supervision channel prevents a slave CN from becoming master when the main NMR network is partitioned. It also states that the channel improves recovery and availability behaviour for core-router outages and transient router reboots. These claims require confirmation by a final fault tree and representative integration tests.

The proposal does not improve safety inside a data centre if the reference two-channel design already prevents the relevant double-fault hazard. Its principal safety benefit is for loss or transient unavailability of the main inter-site/core-router paths. The additional device and ServiceLink routing also introduce availability and maintainability trade-offs.

## 4. RAM calculation review

### 4.1 Inputs from the preliminary workbook

| Input | Value | Comment |
| --- | ---: | --- |
| Core-router failure rate | 9,600 FIT per router | Workbook input |
| ToR-switch failure rate | 7,000 FIT per switch | Workbook input |
| Geo-sites | 2 | Workbook input |
| Availability zones per site | 3 | Workbook input |
| Partition-creating combinations | 6 | 2 crossed combinations x 3 cabinets |
| Split Brain allocated probability | $1 x 10^{-6}$ | 10% allocation of IPS unavailability $1 x 10^{-5}$ |
| Mixed core-router/ToR CCF factor | 0 | Assumes different device types, locations, and supplies |
| MTTR cases | 1, 4, 8, 12, 24, 72 h | Sensitivity analysis |

For one crossed core-router/ToR combination, the workbook uses:

$$
lambda_{sys} = lambda_{CR} U_{ToR} + lambda_{ToR} U_{CR}
$$

with:

$$
U = lambda x MTTR
$$

This is valid only where the first failure is detected and restored within the stated MTTR. For latent failures, the exposure term must instead use the relevant proof-test or diagnostic interval.

### 4.2 Results

| MTTR | Mixed partition exposure, both sites | Share of $10^{-6}$ budget | Independent double-core-router exposure, one pair |
| ---: | ---: | ---: | ---: |
| 8 h | 1.63 s/year | 5.16% | 0.37 s/year |
| 24 h | 14.65 s/year | 46.45% | 3.35 s/year |
| 72 h | 131.83 s/year | 418.04% | 30.13 s/year |

The independent double-core-router case is not the dominant contributor at the stated 8-hour MTTR. The mixed core-router/ToR partition mechanism is more significant in the workbook model. At 72 hours, however, the mixed mechanism exceeds the allocated budget; therefore the 8-hour assumption must not be treated as an administrative value. Detection, dispatch, repair, and restoration controls need to be demonstrated.

The workbook separately treats common-cause failure of the two identical core routers using a 2% factor. This path must remain separate from the mixed-device calculation, which assumes beta = 0. The CCF factor, its scoring basis, and the allocation of external geolink CCF require formal justification before the result can support a safety claim.

### 4.3 Core-router 1oo2 sensitivity with and without CCF

This sensitivity calculation uses 10,000 FIT per core router, as a separate assumption from the 9,600 FIT workbook input. The two core routers are modelled as an active 1oo2 hot-redundant pair with perfect failure detection and switchover, identical MTTR, exponential failure behaviour, and restoration to full redundancy after repair. The low-unavailability approximations below are appropriate for comparison but do not replace a final Markov model or fault tree.

For each core router:

$$
\lambda = \frac{10{,}000}{10^9} = 1.0 \times 10^{-5}\ \mathrm{h^{-1}}
$$

#### Independent failures only

Without CCF, system loss requires the second router to fail while the first router is under repair. The approximate system failure rate is:

$$
\lambda_{sys,ind} = 2\lambda^2 MTTR
$$

The corresponding RAM parameters are:

$$
MTBF_{sys} = \frac{1}{\lambda_{sys,ind}}
$$

$$
U_{ind} \approx \lambda_{sys,ind}MTTR = 2(\lambda MTTR)^2
$$

$$
A = 1-U, \qquad DT = U \times 525{,}600\ \mathrm{min/year}
$$

| MTTR (h) | $\lambda_{sys}$ (FIT) | MTBF (h) | MTBF (y) | Availability (%) | Unavailability | Downtime (min/y) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 0.2 | $5.000 \times 10^9$ | 570,776 | 99.99999998 | $2.000 \times 10^{-10}$ | 0.000105 |
| 4 | 0.8 | $1.250 \times 10^9$ | 142,694 | 99.99999968 | $3.200 \times 10^{-9}$ | 0.001682 |
| 8 | 1.6 | $6.250 \times 10^8$ | 71,347 | 99.99999872 | $1.280 \times 10^{-8}$ | 0.006728 |
| 12 | 2.4 | $4.167 \times 10^8$ | 47,565 | 99.99999712 | $2.880 \times 10^{-8}$ | 0.015137 |
| 24 | 4.8 | $2.083 \times 10^8$ | 23,782 | 99.99998848 | $1.152 \times 10^{-7}$ | 0.060549 |

#### Including CCF with beta = 0.02

The beta-factor model assumes that 2% of each router's failure rate is associated with causes capable of failing both routers together. The CCF and remaining independent rates are:

$$
\lambda_{CCF} = \beta\lambda = 0.02(1.0 \times 10^{-5})
= 2.0 \times 10^{-7}\ \mathrm{h^{-1}} = 200\ FIT
$$

$$
\lambda_{ind} = (1-\beta)\lambda = 9.8 \times 10^{-6}\ \mathrm{h^{-1}}
$$

A CCF causes immediate loss of both redundant routers, whereas the independent contribution still requires two failures within the repair interval. The combined system failure rate and unavailability are therefore approximated by:

$$
\lambda_{sys} = \lambda_{CCF} + 2\lambda_{ind}^{2}MTTR
$$

$$
U_{sys} \approx \lambda_{sys}MTTR
$$

| MTTR (h) | $\lambda_{sys}$ (FIT) | MTBF (h) | MTBF (y) | Availability (%) | Unavailability | Downtime (min/y) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 200.192 | 4,995,203 | 570.23 | 99.99997998 | $2.002 \times 10^{-7}$ | 0.1052 |
| 4 | 200.768 | 4,980,865 | 568.59 | 99.99991969 | $8.031 \times 10^{-7}$ | 0.4221 |
| 8 | 201.537 | 4,961,877 | 566.42 | 99.99983877 | $1.612 \times 10^{-6}$ | 0.8474 |
| 12 | 202.305 | 4,943,033 | 564.27 | 99.99975723 | $2.428 \times 10^{-6}$ | 1.2760 |
| 24 | 204.610 | 4,887,349 | 557.92 | 99.99950894 | $4.911 \times 10^{-6}$ | 2.5810 |

#### CCF relevance to Split Brain

Without CCF, the 1oo2 architecture benefits from the very low probability that two independent router failures overlap during MTTR. With a 2% beta factor, the 200 FIT CCF term is already much larger than the independent double-failure rate of 0.2 to 4.8 FIT over the evaluated MTTR range. For an 8-hour MTTR, including CCF increases estimated downtime from 0.0067 to 0.8474 min/year, by approximately a factor of 126, and reduces MTBF from about 71,347 years to 566 years.

CCF is relevant because identical core routers can share firmware, configuration, management actions, environmental conditions, power dependencies, maintenance errors, or systematic defects. Such causes can defeat both channels simultaneously and bypass the protection expected from 1oo2 redundancy. In the Split Brain context, simultaneous core-router loss or reboot can partition the network and create the precondition for conflicting master election, particularly during recovery and reintegration.

The 2% beta factor is an assumption, not a demonstrated property of the design. It must be justified by a documented CCF assessment covering physical and functional separation, diversity, power, environment, communications, configuration, maintenance, diagnostics, and test evidence. The result also shows why reducing MTTR alone cannot adequately control CCF: MTTR reduces CCF downtime, but the approximately 200 FIT occurrence rate remains. Prevention and mitigation therefore require design independence and a genuinely separate supervision path in addition to restoration controls.

## 5. Technical findings

| ID | Finding | Consequence |
| --- | --- | --- |
| F-01 | Split Brain is principally a network-partition and master-election problem, not simply a component unavailability problem. | Availability compliance alone cannot demonstrate safety. |
| F-02 | The independent supervision channel addresses the decision information needed during partition and reintegration. | It is a credible preferred mitigation, subject to independence proof. |
| F-03 | The RAM result is highly sensitive to MTTR and latent-fault assumptions. | The allocated $10^{-6}$ budget cannot be accepted without verified operational assumptions. |
| F-04 | The supervision proposal adds hardware and a new ServiceLink topology. | Safety improvement must be balanced against new availability, maintenance, and qualification failure modes. |
| F-05 | The current evidence does not include a complete final fault tree, FMEA, or test result. | No residual-risk or SIL-related conclusion can yet be closed. |

## 6. Required validation work

1. Freeze the final topology, including ToR, core-router, mini-router, Wels, power, cable, routing, and MACsec boundaries.
2. Produce a fault tree for hazardous dual-master operation, including independent failures, CCFs, transient reboots, maintenance states, and reintegration.
3. Demonstrate independence of NMR channels, supervision, ServiceLink, power, cabinets, routing, and common management functions.
4. Confirm the supervision-channel failure reaction for loss, stale messages, delayed messages, malformed messages, and restoration.
5. Define and substantiate detection time, repair time, proof-test interval, and exposure time. Recalculate the budget using the verified values.
6. Select and qualify the MACsec-capable mini-router and confirm throughput, failure rate, diagnostics, spares, and maintainability.
7. Assess ECMUX behaviour and external-equipment effects during partition, blocked election, and reintegration.
8. Test at minimum: single-router loss, dual-router loss, router reboot, ToR/core crossed failure, inter-site link combinations, Wels-link loss, stale supervision, and recovery.
9. Reconcile the final result with the applicable DIL-CU/VIL requirements and document the allocation of responsibility for external geolinks.

## 7. Decision status

The technical evidence supports continuing with the independent supervision-channel option as the preferred candidate. It does **not** support recording the architecture as approved, the Split Brain risk as closed, or the RAM allocation as demonstrated. The remaining decision is management acceptance of cost and lifecycle impact after the validation work above has produced the required safety and RAM evidence.

## Sources

- [Independent supervision-channel experimental proposal](TEP-Independentsupervisionchannel-Experimentalproposal-280926-0956-378.pdf)
- [Split Brain analysis and proposals](TEP-Split-brainanalysisandproposalsforDIL-CU-280926-0954-374.pdf)
- [Split Brain technical report](TR-SplitBrain-280926-0956-376.pdf)
- [Preliminary RAM estimation workbook](Prelim_RAM_Estimation_DSTW_Ed02_20260910.xlsx)
