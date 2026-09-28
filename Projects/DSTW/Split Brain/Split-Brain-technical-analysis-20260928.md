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
