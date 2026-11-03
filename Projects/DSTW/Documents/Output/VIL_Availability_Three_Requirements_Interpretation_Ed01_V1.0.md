# VIL Availability Requirements - Plain-Language Interpretation

| Document information | Value |
| --- | --- |
| Subject | EL4-DIL-SSS-REQ-00587, EL4-DIL-SSS-REQ-00569 and EL4-DIL-SSS-REQ-00570 |
| Version | 1.0 |
| Edition | 01 |
| Date | 2026-11-03 |
| Status | Engineering interpretation for review; not an approved requirement baseline or compliance demonstration |
| Scope | Meaning and relationship of the three VIL-instance availability requirements, including the original D2.2 RAMS assumptions |

## 1. Executive summary

The three requirements address different availability questions:

| Requirement | Question | Short interpretation |
| --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 | How available must the VIL be overall? | The complete VIL service must achieve at least 99.995% availability. |
| EL4-DIL-SSS-REQ-00569 | How is availability assessed for different restoration scenarios? | Separate targets apply to manually corrected disturbances and disturbances automatically corrected within 10 or 2 minutes. |
| EL4-DIL-SSS-REQ-00570 | What about errors that do not affect operation? | A separate 99.7154% target applies to the no-operational-impact error scenario; it is not an allowance for service outage. |

The percentages are stated at VIL-instance/VSTW service level. They are not independent percentages to assign unchanged to each software component.

The main unresolved input is the manual restoration basis for EL4-DIL-SSS-REQ-00569. The original customer D2.2 Teillastenheft assumes **MRT = 0.5 h** for manual correction of a disturbance. The current SSS RAMS requirement text says **MTTR = 6 h**, and the RAM plan gives **225 min** in one table. The D2.2 source separately assumes **MRT = 1 h** for manual correction of an error without operational impact. These inputs must not be conflated.

## 2. Source basis and precedence

The analysis compares:

1. The original customer [D2.2 Teillastenheft RAMS V1.3](../D2.2_Teillastenheft_RAMS_V1.3.pdf), clauses 5.4.0-1 to 5.4.0-7, automatic-correction definition 02_111, and calculation assumptions 02_195 and 02_196.
2. The current [SSS DIL RAMS Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx), chapter 3.1.4.3.2, including the accepted VIL-instance requirements and their comments.
3. The [DPR Requirements [VIL-Instance]](<../DPR Requirements [VIL-Instance].pdf>) and [RAMP DIL/VIL Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf) as supporting assessment and modelling sources.

The SSS RAMS is the source for the current accepted system-requirement wording and values used below. D2.2 provides the original customer requirement context and RAM calculation assumptions; it does not, by itself, resolve a later conflict in the current SSS RAMS. The approved configuration and hierarchy of these documents should be confirmed before a formal compliance claim.

The D2.2 PDF refers to a “Tabelle 2” for event categories, but the supplied document does not include a populated VSTW availability table mapping specific fault scenarios to the 2-minute, 10-minute, manual, or no-impact categories. No specific event can therefore be assigned definitively from the supplied sources alone.

## 3. EL4-DIL-SSS-REQ-00587 - Overall VIL availability

### Requirement

The current SSS RAMS requires the VIL instance to have **class 2 overall availability of at least 99.995%**. The D2.2 customer clauses 5.4.0-1 and 5.4.0-3 state an availability of at least 0.99995 and assign each VSTW to availability class 2.

### Plain-language meaning

This is the overall “is the station's VIL service available when required?” target. It concerns the service as a whole, rather than one computer or software module. The availability demonstration must use an agreed service boundary and account for required elements and dependencies, including Core, ECMUX, communications and shared resources.

### Numerical scale

For illustration only, assuming continuous required service over a 365-day year:

```text
Unavailability = 1 - 0.99995 = 0.00005
Equivalent unavailable time = 0.00005 * 525,600 min/year
                            = 26.28 min/year
```

The requirement does not itself define a 365-day observation period or say exactly how partial operational restrictions, planned operational breaks, or overlapping events are counted. The 26.28 minutes is an annualized equivalent, not a quoted contractual annual downtime limit.

## 4. EL4-DIL-SSS-REQ-00569 - Availability by disturbance/restoration scenario

### Requirement values

| Scenario | Availability target in current SSS RAMS | D2.2 context |
| --- | ---: | --- |
| Manually corrected disturbance | 99.9979%; current SSS RAMS text states MTTR = 6 h | Clause 5.4.0-4 sets the availability target. Assumption 02_195 uses MRT = 0.5 h for manual correction of a disturbance. |
| Automatically corrected within 10 min | 99.999% | Clause 5.4.0-6 |
| Automatically corrected within 2 min | 99.9996% | Clause 5.4.0-7 |

D2.2 assumption 02_111 defines automatic correction for a safe computing unit: after the disturbance is detected, the unit enters a safe state, performs a self-test, and automatically recommissions the disturbed module after a successful test. The definition applies to the other availability requirements in that chapter.

### Plain-language meaning

The requirement separates disturbances by their restoration scenario. For automatic cases, it is not enough that a component reboots: the VIL must complete the required recovery and make the required operation usable again within the applicable 2- or 10-minute period. The precise start and end points for that clock, including whether re-synchronisation, interface recovery and operational readiness are included, need agreement.

The availability values also constrain how often disturbances of each restoration duration can occur. For an illustrative simple alternating up/down model:

```text
A = MUT / (MUT + MDT)
MUT = A * MDT / (1 - A)
```

Here, `MUT` is mean operating time between events and `MDT` is mean time in the corresponding unavailable state. This simplified relationship is useful for explaining the numbers; it is not a complete model of the redundant VIL, common-cause failures, or systematic software faults.

For the manual target of 99.9979%, the annualized unavailability equivalent is about **11.04 minutes**. If the assumed mean restoration duration is 0.5 h, the simple model gives a mean up time of about **23,809 h (2.72 years)**. If it is 6 h, it gives about **285,708 h (32.6 years)**. These are mathematical equivalents, not specified failure-frequency limits.

### Manual restoration input discrepancy

| Source | Manual disturbance input | How to treat it |
| --- | ---: | --- |
| Original D2.2 assumption 02_195 | MRT = 0.5 h | Original customer calculation assumption for manual correction of a disturbance |
| DPR | 0.5 h | Consistent with D2.2 assumption 02_195 |
| Current SSS RAMS requirement text | MTTR = 6 h | Current parent-requirement wording; not the value stated by D2.2 assumption 02_195 |
| RAM plan Table 9 | 225 min | Another inconsistent input; must be reconciled with the approved baseline |

The documents do not establish that the terms MRT and MTTR have identical measurement boundaries. Confirm both the approved value and what the clock includes (for example detection, dispatch, travel, repair, testing and return to service) before calculating or claiming compliance.

### What 2 minutes and 10 minutes do not tell us

The time classes alone do not identify which events belong in each class. The missing event-mapping table means examples such as an application restart or a connection recovery are only candidates for assessment, not confirmed classifications. Nor do the sources say whether a disturbance restored in under 2 minutes is counted only in the 2-minute category or also in the 10-minute category.

## 5. EL4-DIL-SSS-REQ-00570 - Errors without operational impact

### Requirement

The current SSS RAMS wording requires at least **99.7154%** availability for VIL-instance outages without operational impact and associates the case with FK4 in its comment. The original D2.2 clause 5.4.0-5 describes **errors without operational impact**. D2.2 assumption 02_196 uses **MRT = 1 h** for manually correcting an error.

### Plain-language meaning

This is a separate measure for an agreed error condition that is present **without affecting operation**. It is not a target that allows the VIL service itself to be unavailable for 24.9 hours per year.

For illustration, the complement of 99.7154% over a continuously required 365-day year is:

```text
1 - 0.997154 = 0.002846
0.002846 * 525,600 min/year = 1,495.86 min/year = 24.93 h/year
```

That is an annualized equivalent for the complementary state under the selected availability interpretation. It must not be reported as allowed operational service downtime. If D2.2's 1 h MRT is used in a simple two-state model, it implies roughly 350 h mean time in the non-error state between entries into the error state. This is only an illustrative calculation; the requirement does not state this event frequency.

### FK4 and degraded redundancy

D2.2 defines FK4 as “other errors” in the DSTW central unit or field equipment. The current SSS comment associates REQ-00570 with FK4, but the sources do not provide measurable rules for event assignment or for when the FK4 condition starts and ends. In particular, they do not establish that every loss of one redundancy partner is FK4. The project fault-class material identifies loss of redundancy with risk of total failure as potentially more severe. The customer must agree the classification for each relevant degraded state.

## 6. How the three requirements fit together

1. **REQ-00587** sets the overall VIL service availability objective.
2. **REQ-00569** sets targets for availability associated with manual, 10-minute automatic and 2-minute automatic disturbance scenarios.
3. **REQ-00570** addresses the separate no-operational-impact error scenario.

The targets should not be mechanically added or copied as budgets to individual software components. A component-level allocation should state what each software component contributes—such as detection, safe reaction, restart, restoration, diagnosis or state recording—while keeping the numeric service targets at VIL-instance level. The project RAM plan describes recovery categories as different scenarios, not component shares of one downtime budget. A full compliance method must define how scenarios are classified and how overlapping events are counted.

## 7. Decisions needed before a compliance demonstration

| Decision / clarification | Why it is needed |
| --- | --- |
| Confirm the controlled baseline and precedence between D2.2, the current SSS RAMS and the RAM plan. | The manual disturbance restoration inputs differ materially. |
| Agree MRT/MTTR definitions and clock boundaries; decide whether D2.2's 0.5 h and 1 h assumptions remain applicable. | They apply to different scenarios and may not measure the same interval. |
| Supply or approve the VSTW event mapping referenced as “Tabelle 2”. | The availability categories cannot be assigned conclusively without it. |
| Define the service boundary, observation period and treatment of partial restriction and planned breaks. | Needed to calculate REQ-00587 consistently. |
| Define automatic restoration start/end points and clarify whether 2-minute events are also counted in the 10-minute category. | Needed to verify and count REQ-00569 events. |
| Define the events, start/end clock and reporting rules for the no-impact error state and FK4 association. | Needed to demonstrate REQ-00570 without confusing degraded operation with service outage. |
| Approve the rules for overlap and aggregation between the three requirements. | Prevents double-counting or omission of downtime. |

## 8. References and related analysis

- [D2.2 Teillastenheft RAMS V1.3](../D2.2_Teillastenheft_RAMS_V1.3.pdf)
- [SSS DIL RAMS Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx)
- [DPR Requirements [VIL-Instance]](<../DPR Requirements [VIL-Instance].pdf>)
- [RAMP DIL/VIL Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf)
- [VIL availability explanation and modelling discussion](./VIL_Availability_Explanation.md)
- [VIL availability requirements allocation to software components](./VIL_Availability_Requirements_Allocation.md)

**Applied engineering guidance:** Railway RAM and RAM Metrics. Calculations above use the stated source values and simplified assumptions; they are not measured availability results or an approved VIL prediction.
