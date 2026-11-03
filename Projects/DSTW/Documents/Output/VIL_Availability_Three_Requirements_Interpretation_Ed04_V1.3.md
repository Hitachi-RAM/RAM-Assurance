# VIL Availability Requirements - Plain-Language Interpretation

| Document information | Value |
| --- | --- |
| Subject | EL4-DIL-SSS-REQ-00587, EL4-DIL-SSS-REQ-00569 and EL4-DIL-SSS-REQ-00570 |
| Version | 1.3 |
| Edition | 04 |
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

A supplied discussion email proposes additional maximum times for full-instance startup, single-node reintegration and shutdown preceding an application restart. These are recorded in this edition as **proposals/assumptions for discussion, not approved requirements or meeting decisions**.

## 2. Source basis and precedence

The analysis compares:

1. The original customer [D2.2 Teillastenheft RAMS V1.3](../D2.2_Teillastenheft_RAMS_V1.3.pdf), clauses 5.4.0-1 to 5.4.0-7, automatic-correction definition 02_111, and calculation assumptions 02_195 and 02_196.
2. The current [SSS DIL RAMS Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx), chapter 3.1.4.3.2, including the accepted VIL-instance requirements and their comments.
3. The [DPR Requirements [VIL-Instance]](<../DPR Requirements [VIL-Instance].pdf>) and [RAMP DIL/VIL Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf) as supporting assessment and modelling sources.
4. The email [RE VIL Availability (related) Requirements](<../RE VIL Availability (related) Requirements.msg>), signed by Florian Moser and containing a proposed basis for a discussion scheduled on 3 November 2026.

The SSS RAMS is the source for the current accepted system-requirement wording and values used below. D2.2 provides the original customer requirement context and RAM calculation assumptions; it does not, by itself, resolve a later conflict in the current SSS RAMS. The approved configuration and hierarchy of these documents should be confirmed before a formal compliance claim.

The D2.2 PDF refers to a “Tabelle 2” for event categories, but the supplied document does not include a populated VSTW availability table mapping specific fault scenarios to the 2-minute, 10-minute, manual, or no-impact categories. No specific event can therefore be assigned definitively from the supplied sources alone.

The email is an engineering discussion input, not a record of agreed decisions. Its assumptions and proposed times are not treated here as accepted requirement values.

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

### Reading the supplied availability calculation table: 10-minute case

The supplied calculation table adds an assumed **MTTF of 17,520 h** (two 365-day years) to the 10-minute automatic-recovery case:

| Quantity in the table | Value | Meaning |
| --- | ---: | --- |
| MTTR | 0.1667 h = 10 min | Mean time to restore service for one event |
| MTTF | 17,520 h = 2 years | Assumed mean operating time before the next failure/event in this scenario |
| Calculated availability | 99.9990% (rounded) | Availability calculated from the MTTF and MTTR |

Using the rounded table inputs:

```text
A = MTTF / (MTTF + MTTR)
  = 17,520 / (17,520 + 0.1667)
  = 99.9990487% (approximately 99.9990%)
```

In plain language, the table assumes a 10-minute service interruption **about once per two years on average**. Ten minutes of downtime spread over two years is about **5 minutes per year**. It does **not** mean one event can last only 5 minutes: an individual event can take the full 10 minutes, while the assumed long interval between events keeps the long-term average availability high.

The table's result is slightly above the 99.999% target. Conversely, if 99.999% is treated as an exact availability target and MTTR is exactly 10 minutes, the simple equation gives a required MTTF of about **16,666.5 h (1.90 years)** and an annualized downtime equivalent of **5.256 minutes per year**. Thus, the table's 17,520 h is a chosen/calculated MTTF assumption that gives a small margin; it is **not uniquely specified by the availability requirement**.

MTTF is a statistical mean, not a promise that an event will occur exactly every two years. Actual events can occur closer together or farther apart. The calculation also assumes the event in this scenario causes a 10-minute service interruption; if redundancy maintains service during the recovery, that node-recovery interval is degraded operation rather than 10 minutes of service downtime.

### What this means for proposed VIL restart and shutdown times

The availability table links a **duration per service-affecting event** to an assumed **mean interval between events**. It does not by itself set component startup or shutdown deadlines. Apply the distinction to the proposed VIL times as follows:

| Proposed time | If operation is interrupted | If operation continues on the redundant partner |
| --- | --- | --- |
| Full VIL startup: 4 min | A 4-minute full-service interruption could be a candidate for the automatic-within-10-min scenario, if the event is classified there and the 4-minute end-to-end restoration is demonstrated. Under the 99.999% target, a simple model with a 4-minute interruption needs about 6,666.6 h (0.76 years) mean up time between such events. One such event every two years would average about 2 min/year. | Not applicable to a completely stopped VIL: if service was already operating, assess whether this is instead a planned transition or an in-service recovery. The cited 3–4-minute planned-update interval does not establish a general cold-start time. |
| Single-node startup and reintegration: 10 min | If customers lose required VIL operation for the duration, it is service downtime and must be assigned to the applicable REQ-00569 scenario; 10 minutes is the longest automatic restoration category, not permission to have frequent 10-minute outages. | The 10 minutes is time to restore redundancy, not service MTTR. It does not consume REQ-00569 operational-outage time if the service truly remains usable. It may contribute to a separately defined degraded/no-impact state under REQ-00570. The requirement does not itself impose a 10-minute reintegration limit. |
| Application shutdown after fault detection: proposed <=10 s | This is only one part of a synchronized application restart. If the restart interrupts service and is assigned to the 2-minute scenario, the **complete service-restoration interval**—with an agreed start point and including all required detection/recovery steps—must fit within 120 s. A 10-second shutdown leaves at most 110 s for the remaining steps only if the 120-second clock starts after detection; if it starts at the failure/service impact, detection time also consumes the 120 s. | If redundancy keeps all required operation usable despite the application action, classify the actual degraded condition with the customer; do not count shutdown duration alone as an operational outage. |

These are conditional interpretations, not confirmed assignments or approved sub-limits. In particular, do not treat “10 minutes to reintegrate a node” as equivalent to “10 minutes of VIL service outage.” The availability model must measure **service usability** and degraded redundancy separately.

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

That is an annualized equivalent for the complementary state under the selected availability interpretation. It must not be reported as allowed operational service downtime.

The supplied table provides a particular model for its “Fehler OC” column: **MTTF = 8,760 h (one year), MTTR = 25 h, and availability = 99.7154%**. Under that model, one 25-hour no-impact condition per mean year is approximately equivalent to 24.93 h/year of exposure. This differs from D2.2 assumption 02_196, which states **MRT = 1 h** for manual correction of an error. MRT (repair time) is not necessarily the same as MTTR (total restoration time); if the table applies to this same error case, the extra 24 hours between MRT and MTTR need a documented explanation (for example detection, logistics, waiting, testing or return to service). The screenshot labels the column “Fehler OC”; confirm that its scope and event definition are the VIL-instance case before using its 25 h / 8,760 h assumptions as VIL inputs.

If 1 h were used as the **entire** down-state duration in the simple equation, the 99.7154% target would imply about 350 h mean up time between entries into that error state. That is a different model from the table's 25 h MTTR and 8,760 h MTTF; do not mix these results.

### FK4 and degraded redundancy

D2.2 defines FK4 as “other errors” in the DSTW central unit or field equipment. The current SSS comment associates REQ-00570 with FK4, but the sources do not provide measurable rules for event assignment or for when the FK4 condition starts and ends. In particular, they do not establish that every loss of one redundancy partner is FK4. The project fault-class material identifies loss of redundancy with risk of total failure as potentially more severe. The customer must agree the classification for each relevant degraded state.

## 6. Email assumptions and proposed timing limits

The email proposes working assumptions for discussion. The table separates its statements from what can be concluded from the supplied requirements:

| Email proposal or assumption | Relationship to the requirements | Assessment / confirmation needed |
| --- | --- | --- |
| Overall 99.995% means at most 26.28 min/year across all unplanned operational outages combined. | REQ-00587; annualized from a continuous 365-day year. | 26.28 min/year is the correct mathematical equivalent under that time-base assumption. “Unplanned outages combined” is an event-accounting interpretation, not explicit wording in the requirement. Confirm the observation period, required-service denominator, treatment of partial restrictions and planned outages. |
| The three REQ-00569 values divide operational downtime into manual, 10-minute and 2-minute buckets. | REQ-00569 scenario availability values. Their annualized equivalents are 11.04, 5.26 and 2.10 min/year respectively. | Useful proposed accounting model, but the supplied RAM plan describes the cases as different scenarios, not component shares of the overall budget. Confirm whether buckets are mutually exclusive, whether their downtime is aggregated, and how the overall target constrains the sum. Do not assume the bucket budgets can be spent independently. |
| For the 10-minute case, MTTF = 17,520 h means one 10-minute recovery event per two years and about 5 min/year of average downtime. | Calculation table supplied with the discussion; MTTR = 10 min, MTTF = 17,520 h, availability rounds to 99.9990%. | This is a consistent example under a simple alternating up/down model: one 10-minute interruption per two years averages about five minutes per year. MTTF is a mean, not a fixed recurrence schedule. The exact 99.999% target with 10-minute MTTR instead corresponds to about 16,666.5 h MTTF; 17,520 h is an assumption giving a small margin. Confirm what event and service boundary the table models. |
| The “Fehler OC” column assumes MTTF = 8,760 h and MTTR = 25 h for 99.7154%. | REQ-00570 no-operational-impact scenario; D2.2 assumption 02_196 separately gives MRT = 1 h to correct an error. | The table's 25 h total restoration time and 1 h repair-time assumption are not interchangeable. If both refer to the same event, account for the remaining 24 h. Confirm the column's scope/event definition and whether these values are intended for the VIL instance. |
| Hot-hot 2x2oo2 with seamless switchover gives zero operational interruption for any single failure. | Could support REQ-00587 and make a single-node failure a degraded-state event rather than service downtime. | Treat only as a conditional architecture assumption for a specified single-failure set. “Any single failure” is broader than demonstrated evidence: software-wide restart, common-cause failures, interfaces, switchover failures and partial service loss need separate treatment and verification. |
| An outage of one redundancy partner with continued operation is assigned a 24.93 h/year budget under REQ-00570. | Email interprets the 99.7154% complement as annual time in a no-impact condition. | 24.93 h/year is the annualized complement of the percentage, not permission for that duration of service outage. The state must meet the approved no-impact event definition; a node failure is not automatically FK4. |
| Maximum VIL node startup and integration of 10 min is acceptable because it restores redundancy while the other node continues service; a second independent hardware failure during recovery is negligible. | Proposed limit for REQ-00570/degraded operation; email cites EL4-VIL-SSS-REQ-00221. | The 10 min value is a proposal, not a parent limit established by REQ-00570. “Negligible” second-failure probability cannot be concluded without failure-rate, repair-time and common-cause evidence. Confirm event classification, start/end timestamps, availability-zone independence and successful takeover assumptions. |
| Maximum full VIL startup of 4 min is supported by a 3–4 min software-update statement and is within a 5 min VIL SLA; it could fit the REQ-00569 10-minute class. | Startup from a cold/stopped state; email also cites EL4-VIL-SSS-REQ-00220 and EL4-DIL-SSS-REQ-00676. | Four minutes is a proposed limit, not a measured general startup time. The 3–4 min statement concerns a particular planned update sequence, not necessarily every cold start or fault recovery. The supplied RAMP lists REQ-00676 (5 min VIL / 30 min FES and OC) as In negotiation; verify its current status and clock definition. A planned update during an operational break is not automatically a REQ-00569 disturbance. Automatic recovery within 10 min must be shown for the relevant event. |
| A software failure under EL4-VIL-SSS-REQ-01155 restarts the affected application on all redundant nodes; REQ-00229 scopes collateral Core restarts. | Potential service-affecting disturbance under REQ-00569. | Consistent with the cited VIL requirement wording in principle. Confirm exact application scope, service effects, and whether simultaneous restarts are required in each fault case. Availability clock should cover the service impact until operation is restored, not only the shutdown interval. |
| Maximum VIL shutdown time after detection should be **<= 10 s** to limit the impact of a software failure and meet the 2-minute automatic-recovery target. | Proposed sub-time for the REQ-00569 2-minute scenario; total target is 120 s. | This is an engineering proposal, not a value derived or required by the parent. If adopted, it is only one part of the end-to-end recovery budget. Detection, shutdown, restart, self-test, synchronization, interface restoration and operational readiness must all fit the agreed 120 s clock; detection limits are still TBD in related requirements. Confirm whether 10 s is achievable and how it is measured. |

### Event timing definitions proposed in the email

The email usefully distinguishes three clocks that should not be combined into one generic “startup time”:

1. **Full-instance startup:** from the complete VIL being non-operational (cold or stopped) until full operational readiness.
2. **Node startup and reintegration:** one failed or newly started node boots, self-tests and reintegrates while a surviving partner continues the service.
3. **Application shutdown after fault detection:** shutdown of the affected application(s) as part of the synchronized restart following a software failure.

These are different scenarios and require separate start/end events, test cases and owners. In particular, node reintegration without service interruption is not the same measure as service-restoration time. Whether the degraded node-out state is counted under REQ-00570 depends on the customer's approved event classification.

The suggested **4 min**, **10 min** and **<= 10 s** limits should remain labelled proposed until accepted through the project requirements/change process and supported by timing evidence. The 4-minute proposal does not, by itself, prove either the in-negotiation 5-minute SLA or an automatic-recovery category. Similarly, a 10-second shutdown does not prove that the complete automatic recovery will fit within 120 seconds.

## 7. How the three requirements fit together

1. **REQ-00587** sets the overall VIL service availability objective.
2. **REQ-00569** sets targets for availability associated with manual, 10-minute automatic and 2-minute automatic disturbance scenarios.
3. **REQ-00570** addresses the separate no-operational-impact error scenario.

The targets should not be mechanically added or copied as budgets to individual software components. A component-level allocation should state what each software component contributes—such as detection, safe reaction, restart, restoration, diagnosis or state recording—while keeping the numeric service targets at VIL-instance level. The project RAM plan describes recovery categories as different scenarios, not component shares of one downtime budget. A full compliance method must define how scenarios are classified and how overlapping events are counted.

## 8. Decisions needed before a compliance demonstration

| Decision / clarification | Why it is needed |
| --- | --- |
| Confirm the controlled baseline and precedence between D2.2, the current SSS RAMS and the RAM plan. | The manual disturbance restoration inputs differ materially. |
| Agree MRT/MTTR definitions and clock boundaries; decide whether D2.2's 0.5 h and 1 h assumptions remain applicable. | They apply to different scenarios and may not measure the same interval. |
| Supply or approve the VSTW event mapping referenced as “Tabelle 2”. | The availability categories cannot be assigned conclusively without it. |
| Define the service boundary, observation period and treatment of partial restriction and planned breaks. | Needed to calculate REQ-00587 consistently. |
| Define automatic restoration start/end points and clarify whether 2-minute events are also counted in the 10-minute category. | Needed to verify and count REQ-00569 events. |
| Define the events, start/end clock and reporting rules for the no-impact error state and FK4 association. | Needed to demonstrate REQ-00570 without confusing degraded operation with service outage. |
| Approve the rules for overlap and aggregation between the three requirements. | Prevents double-counting or omission of downtime. |
| Decide whether the email's 4 min full startup, 10 min node reintegration and <= 10 s application shutdown proposals are adopted; assign owners and verification methods. | They are discussion proposals, not established parent requirements or verified performance limits. |
| Confirm the current status and clock rules for EL4-DIL-SSS-REQ-00676. | The email cites a 5 min VIL SLA; the supplied RAMP lists that requirement as In negotiation. |

## 9. References and related analysis

- [D2.2 Teillastenheft RAMS V1.3](../D2.2_Teillastenheft_RAMS_V1.3.pdf)
- [SSS DIL RAMS Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx)
- [DPR Requirements [VIL-Instance]](<../DPR Requirements [VIL-Instance].pdf>)
- [RAMP DIL/VIL Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf)
- [RE VIL Availability (related) Requirements email](<../RE VIL Availability (related) Requirements.msg>)
- [VIL availability explanation and modelling discussion](./VIL_Availability_Explanation.md)
- [VIL availability requirements allocation to software components](./VIL_Availability_Requirements_Allocation.md)

**Applied engineering guidance:** Railway RAM and RAM Metrics. Calculations above use the stated source values and simplified assumptions; they are not measured availability results or an approved VIL prediction.
