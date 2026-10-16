# NextGen_Bahnsignal - RAM Requirements Review

**Review date:** 2026-10-15  
**Status:** Engineering draft for joint review. Not an approved requirements baseline or a compliance declaration.  
**Subject:** LH Signalgeber requirements compared with the previous Signal Element feature list, with particular focus on LH-SIG-105.

## Executive Summary

**LH-SIG-105 is calculable as a functional disturbance-frequency requirement. It is not directly demonstrable through a conventional hardware MTBF calculation.**

The recommended position is:

> The numerical target is defined, but its event-counting rules, exposure basis and verification criteria require agreement. A component-based reliability prediction alone cannot demonstrate compliance.

The repository provides the following supporting information:

- **LH-SIG-94:** availability at least **0.9999**.
- **LH-SIG-95:** MTBF **100,000 h**.
- **LH-SIG-105:** one disturbance per **1,000 Signalgeber per year**.
- The previous feature list treats LH-SIG-105 separately in **SE:FL:FEA:0806**, specifying **0.001 functional disturbances per element-year**.
- The local clarification email quotes an OBB customer answer dated **12 December 2025**, describing a **non-safety-relevant failed switching operation**, for example a green light remaining dark at switch-on.

**Störungsrate is a RAM KPI**, even though it is neither availability nor necessarily the same failure population used for hardware MTBF.

The proposed project requirements must therefore keep technical useful life, hardware reliability, availability, maintainability and functional disturbance frequency separately traceable.

## Applied Skills

The following repository skills were applied:

- [Railway-RAM](../../../Skills/Railway-RAM.md): railway RAM assurance and lifecycle assessment.
- [REQ-Review](../../../Skills/REQ-Review.md): clarity, completeness, traceability and verifiability.
- [RAM-Metrics](../../../Skills/RAM-Metrics.md): metric definitions, exposure, event counting and reporting.
- [Reliability-Prediction](../../../Skills/Reliability-Prediction.md): distinction between predicted failure rates, observed disturbance frequency and lifetime evidence.

## Sources and Review Scope

Repository information was used from the following project documents:

| Reference | Source | Use |
| --- | --- | --- |
| S1 | [715 LH Signalgeber DSTW V1.1_Kom_SS_20250704.pdf](../715%20LH%20Signalgeber%20DSTW%20V1.1_Kom_SS_20250704.pdf) | Explicit requirement IDs, binding attributes and variant applicability; especially pp. 17-22. |
| S2 | [LH Signalgeber V2.0 signed.pdf](../LH%20Signalgeber%20V2.0%20signed.pdf) | Conventional and SEA customer requirements; approved 8 May 2024. |
| S3 | [FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx](../FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx) | Legacy product features; document 3BU 62200 1001 FLAPQ, ED01, change log dated 8 October 2025. |
| S4 | [RE_ Aufklärungen durch ÖBB bei LED Ausschreibung.msg](../RE_%20Aufkl%C3%A4rungen%20durch%20%C3%96BB%20bei%20LED%20Ausschreibung.msg) | Internal thread dated 8 January 2026 quoting the customer answer dated 12 December 2025. |
| S5 | [D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf](../D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf) | Additional environmental and enclosure-lifetime requirements where applicable. |
| S6 | [SSDD_iLED_01PD01.docx](../SSDD_iLED_01PD01.docx) | Architecture, diagnostic behaviour and reference to a separate RAM plan; not numerical compliance evidence. |

Company governance and repository guidance were also considered:

- [G-PRD_S06000_02_EN.pdf](../../../Knowledge/Process/RAM-Process/G-PRD_S06000_02_EN.pdf): project requirement analysis, RAM planning, RAM activities and monitoring; RAM demonstration and FRACAS deliverables.
- [Requirements_Lessons.md](../../../Knowledge/Lessons_Learned/Requirements_Lessons.md): RL-011, restoration boundaries, and RL-012, resolving customer meaning before baselining. These are approved example lessons, not historical project performance evidence.

### Scope and limitations

- The comparison covers all substantive requirements in the RAMS chapter, LH-SIG-84 through LH-SIG-116 and LH-SIG-139, plus selected RAM-relevant definitions, functional acceptance criteria, environmental conditions and evidence requirements.
- LH-SIG-83 and LH-SIG-117 are section headings, not substantive requirements.
- This is not a complete functional, electrical, optical, environmental or safety requirements review.
- Binding and applicability in the comparison follow **S1, DSTW LH V1.1**. The signed V2.0 belongs to a different document stream; version numbers alone do not establish contractual precedence.
- S4 refers to **LH 4.0**, which is not in the project folder, and quotes a feature-list identifier FLAPC. The supplied comparison file is FLAPQ. The applicable contractual baseline and official clarification record must be confirmed.
- Source requirements below are engineering summaries, not verbatim transcriptions.
- Proposed wording and statistical acceptance examples require approval before baselining.
- Customer-delivered documentation must satisfy LH-SIG-119, including its German-language requirement.

## Findings: RAM Requirements and Legacy Comparison

In the table below, feature numbers abbreviate **SE:FL:FEA:xxxx**.

| LH requirement | Customer requirement / intent | Previous FL | Assessment and project translation |
| --- | --- | --- | --- |
| **84, 88** | Installation and subsystem replacement using commercially available tools. | 1006; 0316/0317 | Covered in intent. Define the approved tools and maintenance demonstration conditions. |
| **85** | Replacement of defective front optical part, light source or electronics without housing removal or optical readjustment. | 1005 | Info in V1.1. LRU replacement is related but does not necessarily provide separate component replacement. Record objective disposition. |
| **86-87** | Housing-independent replaceable light-point or indicator subsystem without optical readjustment. | 1005 | Soll in V1.1. The signed V2.0 uses stronger wording for the light-point subsystem. Resolve the applicable baseline and approve objective disposition. |
| **89** | Replacement must preserve physical and functional properties. | 1005 | Carry into a measurable post-replacement acceptance requirement. |
| **90** | Installation or replacement maximum **10 min**, labelled MRT. | 0811; 1005 | 0811 changes maximum to mean repair time and excludes preparation; this is weaker. 1005 uses less than 10 min. Define a **600 s maximum task** with agreed start/end conditions. |
| **91** | Required visibility retained despite degradation, temperature and partial light-source failures throughout useful life. | 0219; 0810 | Explicit optical lifetime requirements and evidence are needed. Define permitted partial failures without weakening visibility requirements. |
| **92** | Specified axial intensity range must not be undershot during useful life. | 0808/0810 | 0808 references this ID but its normative text is availability and MTBF. An explicit optical lifetime requirement is needed. |
| **93** | Technical useful life at least **130,000 operating h**. | 0810; 0808 comments | Legacy **15 calendar years** is not generally equivalent for intermittent operation. Preserve the operating-hour target and address calendar ageing separately. |
| **94** | Availability at least **0.9999** throughout lifetime. | 0808 | Numeric target matches. Availability class, boundary, downtime inclusions and observation basis remain undefined. |
| **95** | MTBF **100,000 h**. | 0808: at least **200,000 h** | Legacy target is stronger if scope and operating profile match. Confirm the minimum-target interpretation and retain any binding product commitment separately. |
| **96** | Freedom to use circuit measures to achieve useful life. | Design principles | Info/design freedom, not an additional numerical target. |
| **97** | Operating hours stored locally. | 0407 | Accepted feature records powered hours, including dark time. V1.1 applicability is SEA. Define counter accuracy, retention and replacement behaviour. |
| **98** | Usage visible through an indicator at the signal site without dismantling or extra systems. | 0633 | Gap: feature is Descoped although V1.1 contains a Muss requirement for Conventional/SEA. |
| **99** | Green to 68% useful life; yellow 68.1-81.1%; red from 81.2%. | 0634 | Gap: feature is Descoped. Agree quantisation and rounding to resolve gaps between the stated percentage intervals. |
| **100** | Indicator position agreed with customer. | 0633 | A descoped feature does not demonstrate agreement on installation position. |
| **101** | Wired operating-hour readout after dismantling. | 0643 | Accepted CAN readout supports digital variants; confirm conventional-variant support and the readout configuration. |
| **102** | Wireless readout without dismantling. | 0644 | Soll objective in V1.1; feature is Descoped. Formal disposition is needed. |
| **103** | Lifetime boundary includes all necessary parts from the cable-side terminal, including the complete connector. | 0810 | Covered in intent. Do not assess only the electronic board. |
| **104** | Typical profile: 300 activations/day; 100 blinking sessions/day of 2 min; extremes from continuous use to activation once in two years. | 0810/0812/0813 | Conflicting legacy profiles include 300 sessions of 2 min and 100 sessions of 1 min. Agree variant-specific profiles; typical averages are not universal maxima. |
| **105** | One disturbance per **1,000 Signalgeber/year**. | 0806 | Numeric target is mapped. Event scope, counting rules, exposure and demonstration criteria are incomplete. |
| **106** | High impedance at the interlocking interface on disturbance, for conventional variants. | 0805 | Define impedance criteria and reaction times. |
| **107** | Disturbance disclosure at the interlocking interface for DSTW/SEA. | 0805; 0406 | Define diagnostic messages, coverage, latency and communication-failure behaviour. |
| **108-109** | No required periodic maintenance over useful life, except specified external cleaning. | 1001 | Broadly covered. Resolve wording about corrective intervention versus repair following random failures. |
| **110** | Any necessary maintenance/inspection interval at least **2 years**. | 1004 | Legacy ideal of no recurring inspection omits the explicit minimum interval. |
| **111** | At least **4 years** as maintenance/inspection interval objective. | 1004 | No explicit four-year objective identified. Record satisfaction or approved disposition. |
| **112** | Safety/application conditions must not require interlocking activation or state changes for inspection/maintenance. | 1003 | Legacy wording is weaker. Preserve the explicit prohibition and check dormant-use diagnostic assumptions. |
| **113** | SIL4 signalling safety documented in the approval safety case. | 0801/0807 | Safety-linked requirement, not a substitute for RAM evidence. |
| **114-116** | Applicable THR matrices for small light points, large light points and Signalgeber assemblies. | 0801 | Obtain controlled THR matrices. A generic scalar THR does not replace hazard-specific allocations. |
| **139** | Illuminated duration stored locally, for conventional variants. | 0407 | Gap: powered operating hours, including dark time, are not the same as illuminated duration. |

### Additional RAM-Relevant Requirements

| LH requirement | RAM relevance | Comparison / action |
| --- | --- | --- |
| **5-9** | Define Signalgeber types and complete-system boundaries. | Include the supplied optics, interface, connector, mounting, housing and thermal provisions as applicable. |
| **10-11** | Define disturbances and unspecified optical behaviour. | LH-SIG-10 is broad: loss of full functionality, optical inadequacy, interface deviations and flicker. Reconcile this definition with the narrower switching clarification. |
| **12-13** | Require disturbed-state reaction and dark/high-impedance outputs. | 0805 addresses non-recoverable faults; confirm coverage of other unspecified behaviour and digital-interface applicability. |
| **18** | Applicable standards include EN 50126-1. | Control editions and applicability in the project standards baseline. |
| **33, 35-36** | Alignment retention, replacement without readjustment and handling mass. | 0317/1005 cover replacement intent. Variant mass features are sometimes stricter. Define measurable installation and exchange acceptance. |
| **40-48** | Environmental resistance, snow, temperature, EMC, transport/storage, IP and railway pressure/suction loads. | Use the approved full environmental profile and qualification evidence. Legacy IP65 exceeds IP54, but an IP rating alone is not lifetime evidence. |
| **54-57, 63, 65** | Visibility, viewing angle, light distribution and intensity retention. | Functional failure-classification inputs and optical lifetime evidence, not MTBF targets. |
| **67-69** | Colour stability under temperature, ageing, supply variation and phantom light. | 0220 covers intent. Informal legacy colour deviations require approved customer agreement. |
| **71, 74, 81-82** | Fault disclosure, series-connection functionality, voltage-envelope behaviour and absence of flicker on single-pole disconnection. | Include in disturbance and interface verification. Legacy 0317 erroneously references LH-SIG-82 for mounting. |
| **76-77** | 1 Hz blinking, 1:1 duty ratio and waveform tolerances. | 0502 uses a tighter tolerance. Define whether each blink transition is a counted switching demand. |
| **118** | Required RAM evidence. | Installation documentation alone does not ensure a complete RAM compliance package. |
| **119-120** | German customer documentation and editable/noneditable digital delivery. | Generic English product documents do not satisfy the customer delivery requirement alone. |
| **121-123** | Maintenance manual, diagnostics, spares, measurement procedures and approved tools. | Check completeness and obtain written approval for deviations from the customer tool set. |
| **124-126** | Identification and machine-readable data support asset and FRACAS traceability. | Link identity, configuration, exposure and disturbance records. |
| **135** | Small-light-point intensity limits. | 0619 matches the nominal range, but **0624 permits a 21 cd night minimum versus the customer's 40 cd minimum**. Resolve variant-specific coverage and lifetime margins. |
| **136-138** | Indicator intensity, viewing angles and symbol recognition. | Verify recognition under permitted partial failures; do not import another customer's tolerated-pixel settings as automatic OBB acceptance. |

### Important Legacy Distinctions

- **Accepted feature status is not demonstrated customer compliance.**
- Legacy **30-year product support/lifetime** in 0809 is separate from **130,000 operating h technical useful life** and failure-free operation.
- S5 includes a **30-year UV enclosure durability** requirement requiring allocation where applicable.
- Environmental verification must distinguish **ambient, housing external and internal component temperatures**.
- S5 specifies **-40 to +70 degrees C ambient in track areas**, where applicable. LH-SIG-42/43 instead specify housing external temperature conditions.
- A legacy calculation assumption of **20 degrees C** is not a complete mission profile.

## LH-SIG-105: Interpretation

### Customer Clarification

S4 supports treating LH-SIG-105 as a requirement concerning **failed switching operations**, rather than simply applying the hardware failure rate from LH-SIG-95.

However:

1. The quoted answer calls LH-SIG-95 "availability"; technically it specifies **MTBF**. LH-SIG-94 is the separate availability requirement.
2. The thread refers to **LH 4.0**, which is not supplied. Applicability to this project requires confirmation.
3. A failed switching operation can have a hardware cause. **Do not exclude hardware-caused failed switching or safe-dark nuisance shutdowns without customer agreement.**
4. V1.1 assigns LH-SIG-105 to **Conventional and SEA**, not DSTW. Any extension to DSTW must be explicit.
5. The original annual allowance, the clarification's switching example and the broad LH-SIG-10 definition must be reconciled in an approved event catalogue.
6. "One event" and "one affected unit" are different metrics if the same unit experiences repeated disturbances.

### Inputs

| Parameter | Value | Source / status |
| --- | --- | --- |
| Allowed disturbance frequency | One disturbance per 1,000 Signalgeber-years | LH-SIG-105, interpreted as an event-rate target pending agreement. |
| Hardware MTBF | 100,000 h | LH-SIG-95; minimum-target interpretation requires confirmation. |
| Availability | At least 0.9999 | LH-SIG-94; measure and downtime boundary unresolved. |
| Typical activation count for illustration | 300 activations/day | LH-SIG-104; not a universal maximum or a complete demand definition. |

### Assumptions

The following assumptions apply only to the calculations explicitly identified below:

- A year is taken as **365 days**.
- Continuous exposure is **8,760 h/year**.
- A reciprocal mean event interval assumes a stationary event process.
- Per-demand conversion assumes the annual event frequency is driven solely by the specified switching demands.
- Statistical examples assume independent rare events, homogeneous representative exposure, a constant event frequency and complete observation.
- None of these assumptions creates a customer-approved acceptance criterion.

### Formula and Calculation

Define the measured disturbance frequency:

$$
r_D = \frac{K_D}{E}
$$

where:

- $K_D$ is the number of qualifying disturbance events;
- $E$ is accumulated eligible exposure in Signalgeber-years.

The proposed numerical interpretation is:

$$
r_D \leq \frac{1}{1000}
= 0.001\ \text{disturbances/(Signalgeber year)}
$$

This is directly calculable from event and exposure records.

Under the continuous-exposure assumptions:

$$
\nu_D = \frac{0.001}{8760}
= 1.142 \times 10^{-7}\ \text{events/h}
$$

$$
\text{Equivalent FIT units}
= \nu_D \times 10^9
= 114.2
$$

$$
\text{Mean event interval}
= \frac{1}{\nu_D}
= 8{,}760{,}000\ \text{h}
$$

### Result

| Conditional result | Value | Interpretation |
| --- | --- | --- |
| Disturbance-frequency target | 0.001 events/(Signalgeber year) | Proposed annual rate interpretation. |
| Time-normalised disturbance frequency | $1.142 \times 10^{-7}$ events/h | Conditional on continuous exposure. |
| Equivalent FIT units | 114.2 FIT | Unit equivalence only, not a hardware prediction. |
| Reciprocal mean event interval | 8,760,000 h | Not automatically the hardware MTBF required by LH-SIG-95. |

If both requirements count exactly the same events, LH-SIG-105 is much stricter:

$$
\frac{8{,}760{,}000}{100{,}000} = 87.6
$$

This is not necessarily a logical contradiction with a minimum MTBF requirement, but it is a substantial feasibility and verification issue.

### Conditional Per-Demand Interpretation

If there are 300 switch-on demands per day and all counted disturbances arise from those demands:

$$
D = 300 \times 365 = 109{,}500\ \text{demands/(Signalgeber year)}
$$

$$
p_D = \frac{0.001}{109{,}500}
= 9.13 \times 10^{-9}\ \text{failures/demand}
$$

This is an illustration, **not a customer-specified per-demand requirement**. Actual demand profiles, blinking transitions and dormant use must be defined before such a conversion is used.

## Why Hardware MTBF Prediction Alone Is Insufficient

A component-based prediction does not normally quantify all:

- intermittent activation failures;
- software, timing or interface faults;
- transient immunity problems;
- nuisance diagnostic shutdowns;
- optical performance excursions;
- repeated failed demands and recovery behaviour.

Use the company-approved reliability method for LH-SIG-95, and a **dedicated disturbance assessment, functional verification and operational evidence** for LH-SIG-105.

No FIDES, IEC 61709 or MIL-HDBK-217 prediction has been performed in this review. The calculations above are unit conversions and illustrative event-rate analysis.

The two-channel architecture described in S6 does not justify independent-channel assumptions without analysis. Common-cause supply, environmental, communication and systematic faults can produce multiple disturbances and invalidate naive statistical pooling.

## Proposed Project Requirements for LH-SIG-105

### Performance Wording - Subject to Customer Approval

> **NGB-RAM-DST-105-01:** Die Häufigkeit der gemäß dem freigegebenen Störungskatalog als LH-SIG-105-Ereignisse klassifizierten Störungen darf unter dem freigegebenen Einsatzprofil **0,001 Ereignisse je Signalgeberjahr** nicht überschreiten. Die Exposition ist gemäß der freigegebenen Expositionsdefinition zu bestimmen.

This wording retains the annual rate target without silently substituting hardware MTBF or a probability per switching demand.

### Supporting Requirements

The following are **proposed derived verification and evidence requirements**, not additional quoted customer requirements.

| Draft ID | Proposed requirement | Verification / approval |
| --- | --- | --- |
| **NGB-RAM-DST-105-02** | The approved event catalogue shall identify the non-safety-relevant failed switching operations covered by the customer clarification and their relationship to the broader LH-SIG-10 definition. | Joint classification review; confirm applicability of the quoted LH4.0 clarification. |
| **NGB-RAM-DST-105-03** | The counting specification shall define distinct events, repeated failed commands, persistent failures, recovery, restart events, blinking transitions and attribution at the agreed Signalgeber boundary. | Review with representative scenarios; no blanket exclusion of hardware-caused or safe-dark events. |
| **NGB-RAM-DST-105-04** | The exposure specification shall define accumulation of eligible Signalgeber-years, including installation, removal, powered time, illuminated time, dormant periods and incomplete observation. | Approve calendar versus powered versus in-service exposure and treatment of downtime. |
| **NGB-RAM-DST-105-05** | The demonstration system shall retain disturbance records linked to unit identity, configuration, event time, commanded state, observed state, recovery and associated exposure. | Logging and FRACAS data-quality verification; allocate data sources between device, interlocking, tools and FRACAS. |
| **NGB-RAM-DST-105-06** | The RAM demonstration plan shall define the statistical model, confidence level, sample exposure, common-cause treatment and acceptance rule before compliance is claimed. | Customer-approved demonstration plan. |
| **NGB-RAM-DST-105-07** | Verification shall exercise switching sequences under approved electrical, environmental, timing and mission conditions, including startup, restart, dormant use and blinking where applicable. | Robustness and interface tests; these do not alone prove the numerical annual rate. |
| **NGB-RAM-DST-105-08** | The RAM compliance matrix shall report MTBF, availability and LH-SIG-105 disturbance-frequency compliance separately using approved event classes and boundaries. | Traceability review; events may contribute to multiple KPIs. |

## Verification and Statistical Demonstration

### Proposed Evidence Strategy

1. Approve the event catalogue, counting rules and exposure definition.
2. Analyse relevant failure modes and design contributors, including transient and systematic causes.
3. Verify functional robustness under the approved mission and environmental profiles.
4. Assess whether historical fleet evidence is representative of the new hardware, software, interfaces and environment.
5. Define the agreed field demonstration and FRACAS reporting.
6. Keep compliance open until sufficient agreed evidence is available.

### Statistical Example: Zero Observed Events

**Illustrative assumptions only:** homogeneous independent Poisson events, complete observation and a **95% one-sided confidence criterion**. This is not a customer-specified acceptance rule.

With zero observed events:

$$
r_{D,U} = \frac{-\ln(0.05)}{E}
$$

To demonstrate $r_{D,U} \leq 0.001$:

$$
E \geq \frac{-\ln(0.05)}{0.001}
= 2995.7\ \text{Signalgeber-years}
$$

| Observation / example criterion | Result |
| --- | --- |
| Zero events in 1,000 Signalgeber-years | Upper rate approximately 0.002996 events/(Signalgeber year); insufficient for the example confidence criterion. |
| Zero events with upper rate at most 0.001 | Approximately **2,996 full Signalgeber-years** required, rounded upward. |
| One event with upper rate at most 0.001 | Approximately **4,744 full Signalgeber-years** required, rounded upward. |

For one event, the upper Poisson mean is obtained from:

$$
e^{-\mu_U}(1+\mu_U) = 0.05
$$

$$
\mu_U = 4.7438645,\qquad
E \geq \frac{\mu_U}{0.001} = 4743.9\ \text{Signalgeber-years}
$$

Common-cause disturbances, ageing, incomplete observation and configuration differences can invalidate simple pooling.

### Rate Target Versus Hard Annual Ceiling

A statistical rate target and a hard limit of one event in every fleet-year are not equivalent.

At an expected Poisson count of one:

$$
P(K \geq 2) = 1-e^{-1}(1+1) = 0.2642
$$

There is therefore a **26.4% probability of two or more events** even when the expected count is one. The customer must confirm the intended acceptance semantics.

## Availability and Maintainability Boundary

LH-SIG-90's replacement time is not automatically the downtime used for LH-SIG-94.

For a simplified uptime/downtime model:

$$
A = \frac{\text{MTBF}}{\text{MTBF}+\text{MDT}}
$$

Using MTBF = 100,000 h and $A = 0.9999$:

$$
\text{MDT} \leq 100{,}000
\left(\frac{1}{0.9999}-1\right)
= 10.001\ \text{h}
$$

This is conditional on the agreed availability measure and the simplified renewal model. It does not establish an approved downtime budget.

Using only a 10 min active replacement time would give:

$$
A = \frac{100{,}000}{100{,}000+10/60}
= 0.99999833
$$

That result excludes detection, mobilisation, access, spare logistics, testing and return to service. It is **not demonstrated operational availability**.

## Assumptions and Missing Information

| Item | Status / consequence |
| --- | --- |
| Contractual document hierarchy | Not confirmed. Different LH document streams and the quoted LH4.0 clarification must be reconciled. |
| LH-SIG-105 event catalogue | Not approved. Switching examples and the broad disturbance definition must be aligned. |
| Exposure denominator | Undefined. Calendar, powered, illuminated and in-service exposure are not interchangeable. |
| Repeated-event counting | Undefined. Affected-unit count differs from event count. |
| Statistical acceptance | Undefined. Confidence, sample, period and hard-ceiling interpretation need agreement. |
| BOM and component reliability inputs | Not supplied for a numerical hardware reliability prediction. |
| Mission and thermal profiles | Not approved. Continuous, intermittent, blinking and dormant use require separate consideration. |
| Field disturbance and exposure data | Not supplied. No actual rate or compliance conclusion can be established. |
| Maintenance demonstration | Not supplied. Maximum task time and full restoration boundary remain open. |
| RAM plan and numerical analyses | S6 refers to a separate RAM plan, but the complete project evidence was not supplied. |
| THR matrices | Controlled matrix values and allocations are required; no values are inferred here. |
| Informal PDF comments | A comment claiming current MTBF above 400,000 h has no supporting calculation in the supplied evidence and is not treated as demonstrated performance. |

## Risks

| Risk | Engineering consequence | Recommended control |
| --- | --- | --- |
| Treating LH-SIG-105 as not calculable | Quantitative customer target is lost during requirement translation. | Retain the rate target; identify unresolved verification conditions explicitly. |
| Claiming compliance from FL0806 Accepted status | Feature allocation is mistaken for implementation and performance evidence. | Require a separate compliance disposition and evidence reference. |
| Treating LH-SIG-105 as hardware MTBF without event agreement | Unsupported conversion can overstate or misrepresent the design obligation. | Agree the event population and keep metric evidence separate. |
| Excluding safe-dark or hardware-caused events without approval | Under-counting disturbances and misleading compliance reporting. | Record cause, safety status and KPI membership separately. |
| Ignoring common-cause disturbances | Multiple units can fail together; independent-event assumptions become invalid. | Evaluate environmental, supply, communication and systematic contributors. |
| Copying maximum replacement time as mean repair time | Maintainability requirement is weakened. | Define a maximum task duration and an approved demonstration procedure. |
| Treating 15 calendar years as 130,000 operating h | Intermittent use and calendar degradation are not properly addressed. | Separate operating-hour life, calendar ageing and product support. |
| Retaining legacy descopes as implicit customer waivers | Mandatory indicators or counters may remain unimplemented. | Obtain a controlled customer disposition or implement the requirement. |
| Using inconsistent blinking or temperature profiles | Prediction and lifetime evidence may not represent actual deployment. | Approve a single traceable profile per applicable variant. |
| Legacy small-light-point night minimum below customer minimum | Optical noncompliance and potential disturbance classification. | Resolve the 21 cd versus 40 cd discrepancy and verify lifetime margins. |

## Recommendations

**Do not mark LH-SIG-105 "not calculable", and do not claim it is fulfilled merely because FL0806 is Accepted.**

Recommended disposition:

> **Quantitative target understood; event classification, exposure definition and verification criteria unresolved; compliance not yet demonstrated.**

Keep distinct project requirements and evidence for:

1. Technical useful life and optical degradation.
2. Hardware MTBF.
3. Availability.
4. Maintainability and restoration.
5. Functional disturbance frequency.
6. Safety and fault-response obligations.

Baseline LH-SIG-105 only after agreeing the target interpretation, scope and event population. Do not declare numerical compliance until the agreed demonstration evidence is available.

## Required Evidence

- Controlled contractual requirement baseline and official customer clarification.
- Approved variant applicability and RAM boundary.
- Approved disturbance catalogue, event-counting specification and exposure definition.
- Approved mission and environmental profiles, including thermal modelling.
- RAM plan and customer-approved demonstration plan.
- Company-method hardware prediction, with component sources and failure-mode mapping.
- Optical degradation, lifetime and mechanical durability substantiation.
- Availability model with agreed downtime terms.
- Timed maintainability demonstration.
- Functional robustness and interface verification reports.
- FRACAS records, configuration-controlled exposure data and representative field evidence.
- Safety case and controlled THR allocations.
- German customer RAM and maintenance deliverables with complete bidirectional traceability.

## Actions

| Priority | Action | Responsible roles | Closure evidence |
| --- | --- | --- | --- |
| 1 | Confirm contractual LH baseline and applicability of the quoted OBB clarification. | Project / Requirements / Customer | Controlled baseline and clarification record. |
| 1 | Approve disturbance catalogue, counting rules and exposure basis. | RAM / Systems / Safety / Customer | Approved specifications with representative scenarios. |
| 1 | Agree acceptance semantics, feasible observation exposure and evidence strategy. | RAM / V&V / Customer | Approved RAM demonstration plan. |
| 2 | Separate useful life, MTBF, availability and disturbance-rate requirements. | RAM / Requirements | Reviewed requirement and evidence matrix. |
| 2 | Confirm minimum MTBF interpretation and any continuing 200,000 h product commitment. | Product / RAM / Requirements | Approved target allocation. |
| 2 | Resolve counter and indicator descopes and threshold rounding. | Product / Systems / Customer | Implementation plan or written customer disposition. |
| 2 | Define maximum 600 s exchange task and full restoration boundary. | Maintenance / V&V / Customer | Approved demonstration procedure. |
| 2 | Reconcile blinking and environmental profiles. | Engineering / RAM / Customer | Approved variant-specific profiles. |
| 2 | Resolve the small-light-point 21 cd versus 40 cd night-intensity discrepancy. | Product / Optics / Requirements | Approved optical specification and qualification evidence. |
| 2 | Check maintenance-free and dormant-use safety assumptions. | Maintenance / Safety / RAM | Approved maintenance concept and safety assumptions. |
| 2 | Obtain THR matrices and complete RAM evidence allocation. | Safety / RAM / V&V | Controlled allocations and evidence matrix. |
| 3 | Correct legacy origin references, including missing LH-SIG-94 origin in 0808 and erroneous LH-SIG-82 mounting reference. | Requirements / Product | Reviewed bidirectional traceability. |
| 3 | Reuse the agreed disturbance taxonomy, counting rules and demonstration approach in the review-comment library and RAM templates. | RAM process owner | Reviewed reusable guidance after customer agreement. |

## LH-SIG-105: Project Requirement Formulation and Fulfillment Strategy

**Added:** 2026-10-16. This chapter consolidates the proposed requirement and the practical fulfillment approach. It supplements the preceding analysis; it does not establish customer approval or demonstrated compliance.

The recommended approach is to formulate a **quantitative functional-disturbance requirement**, supported by an agreed verification specification, rather than another hardware MTBF requirement.

> The requirement specifies the permissible disturbance frequency. The verification specification defines what counts, how exposure is measured, and when the evidence is sufficient.

### Proposed Project Requirement

> **NGB-RAM-DST-105-01 - Zulässige funktionale Störungsrate**  
> Die funktionale Störungsrate des Signalgebers darf unter dem freigegebenen Einsatz- und Umgebungsprofil **0,001 Störungsereignisse je Signalgeberjahr** nicht überschreiten. Als Störungsereignisse gelten die im freigegebenen Störungskatalog für LH-SIG-105 definierten Ereignisse. Die Ermittlung der Exposition erfolgt gemäß der freigegebenen Nachweisspezifikation.

**Traceability:** LH-SIG-105 -> SE:FL:FEA:0806 -> NGB-RAM-DST-105-01.

This wording refines the same draft requirement identified earlier in this report; it is not a second independent requirement. It is a **proposed event-rate interpretation**, not an agreed contractual clarification. It must not silently replace the number of affected units with the number of events if the customer intended the former.

### Accompanying Event Definition

Based on the customer clarification quoted in S4, the following definition is proposed for approval:

> Ein LH-SIG-105-Störungsereignis liegt vor, wenn ein gültiger Schaltauftrag unter spezifizierten Betriebsbedingungen nicht zum geforderten funktionalen Verhalten des Signalgebers führt und das Ereignis dem vereinbarten, nicht-sicherheitsrelevanten Ereignisumfang zugeordnet ist.

**Example:** A valid switch-on command is issued, but the green light remains dark beyond the specified response time.

The response time must come from the applicable functional/interface specification. No new time limit is introduced by this definition.

| Topic | Decision required before baselining |
| --- | --- |
| Event scope | Only failed switching, or also flicker, temporary intensity deviations and other LH-SIG-10 disturbances? |
| Repetition | Does a persistent dark state count once, or does every unsuccessful command count? |
| Recovery | When does a recovered unit become eligible for a new event? |
| Exposure | Calendar in-service time, powered time or another agreed basis? |
| Attribution | How are external supply/interface disturbances and hardware-caused switching failures treated? |
| Applicability | Does the quoted LH4.0 clarification apply to this project? V1.1 assigns LH-SIG-105 to Conventional/SEA, not DSTW. |

Do not automatically exclude a disturbance because it is safe, self-recovering or hardware-caused.

### Three Layers of Fulfillment Evidence

| Evidence layer | Method | What it demonstrates |
| --- | --- | --- |
| **Design substantiation** | Failure-mode analysis, interface/timing review, diagnostic assessment and evaluation of common causes. | Relevant disturbance mechanisms have been identified and addressed. |
| **Functional verification** | Switching, startup/restart, blinking, dormant-use, supply-envelope, temperature and EMC tests. | Required behaviour is achieved under the tested conditions. |
| **Quantitative demonstration** | Representative field records or justified equivalent evidence, with complete exposure accounting. | Whether the numerical disturbance-frequency target has been demonstrated. |

**Passing functional tests alone does not establish a rate of 0.001 per Signalgeber-year.** A hardware MTBF calculation also does not cover all intermittent, software, timing and interface disturbances.

#### Required Event and Exposure Records

For each event, retain:

- Unit identity and hardware/software configuration.
- Command, expected response and observed response.
- Timestamp and operating conditions.
- Duration, recovery and corrective action.
- Event classification and attribution.

For the denominator, retain each unit's eligible observation period, including installation/removal and gaps in monitoring.

Allocate data collection between the Signalgeber, interlocking, service tools and FRACAS. The complete recording function need not be implemented inside the Signalgeber.

### Numerical Acceptance Example

#### Inputs and Assumptions

- Target: $r_D \leq 0.001$ events/(Signalgeber year).
- Illustrative acceptance criterion: **95% one-sided confidence**, not a contractual criterion.
- Homogeneous Poisson event process, representative exposure and complete observation.
- Independence and constant frequency require justification; common-cause events require special treatment.

#### Formula

The observed rate is:

$$
\hat r_D = \frac{K}{E}
$$

where $K$ is the number of qualifying events and $E$ is eligible exposure in Signalgeber-years.

For zero observed events, the upper confidence bound is:

$$
r_{D,U} = \frac{-\ln(0.05)}{E}
$$

#### Calculation

$$
E \geq \frac{-\ln(0.05)}{0.001}
= 2995.7\ \text{Signalgeber-years}
$$

#### Result

| Observation | Upper rate bound, events/(Signalgeber year) | Interpretation under the illustrative criterion |
| --- | --- | --- |
| Zero events in 100 Signalgeber-years | Approximately 0.02996 | Encouraging, but insufficient evidence. |
| Zero events in 1,000 Signalgeber-years | Approximately 0.002996 | Numerical target not demonstrated. |
| Zero events in 3,000 Signalgeber-years | Approximately 0.000999 | Numerical target demonstrated if the assumptions are valid. |

The customer must agree whether acceptance uses a confidence bound, a simple observed rate or a hard annual event ceiling. These are not equivalent.

### Practical Staged Verification Strategy

| Stage | Required activity | Result / permitted conclusion |
| --- | --- | --- |
| **Before design baseline** | Approve the event definition, exposure basis, applicability and acceptance method. | Requirement and verification basis agreed. |
| **Before product release** | Complete design substantiation and functional robustness tests; assess transferable evidence from previous products. | Design and tested behaviour substantiated; numerical compliance only where sufficient agreed evidence exists. |
| **During pilot/operation** | Accumulate representative exposure and perform the agreed statistical demonstration. | Numerical compliance assessed against the approved acceptance rule. |

Existing-product data may reduce the demonstration burden only after showing relevance to the new hardware, software, interfaces, mission profile and reporting completeness. Similar product names or a shared architecture alone are insufficient.

If sufficient exposure cannot be obtained before delivery, agree a **staged acceptance arrangement with the customer**. Do not substitute "tests passed" for numerical fulfillment without that agreement.

### Recommended Current Compliance Statement

The following wording is proposed for use when the stated supporting activities are actually in place; it does not assert that those activities have already been completed:

> Die Anforderung ist spezifiziert und wird durch konstruktive Maßnahmen sowie Funktions- und Robustheitsprüfungen unterstützt. Der quantitative Nachweis der zulässigen Störungsrate erfolgt gemäß dem mit dem AG abgestimmten RAM-Nachweisplan. Bis zum Vorliegen ausreichender repräsentativer Nachweisdaten bleibt der quantitative Erfüllungsnachweis offen.

**Conclusion:** The project can specify the requirement and verify the design against relevant disturbance mechanisms. Full numerical fulfillment requires an agreed demonstration method and sufficient representative evidence.

## Review Verification

The associated review register and calculation workbook were generated and reopened during the original analysis. Checks covered:

- 84 source entries and complete substantive RAMS chapter coverage.
- Eight separately derived LH-SIG-105 requirements.
- Twenty clarification/action entries.
- CSV structure and fully qualified legacy-feature ID existence.
- Numerical rate, exposure and simplified availability calculations.

These checks verify the review artefacts and calculations, **not actual product compliance**. Source documents were not modified.
