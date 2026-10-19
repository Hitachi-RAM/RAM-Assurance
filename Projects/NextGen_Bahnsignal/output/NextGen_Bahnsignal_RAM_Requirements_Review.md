# NextGen_Bahnsignal - RAM Requirements Review

**Original analysis date:** 2026-10-15

**Revised:** 2026-10-19 - restricted to existing requirements and documented clarifications.

**Status:** Source-based engineering analysis. Not a new requirements specification, acceptance procedure or declaration of compliance.

**Subject:** Comparison of the Signalgeber customer specification with the previous Signal Element feature list; focus on LH-SIG-105.

**Parallel version:** [German report](./NextGen_Bahnsignal_RAM_Anforderungsreview_DE.md).

**Correction to the previous version:** Assistant-authored requirement drafts, additional evidence obligations and statistical acceptance criteria have been removed. They were not specified by the cited customer requirements. Chapter 16 records the withdrawal. The project source documents have not been changed.

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. Applied Skills](#2-applied-skills)
- [3. Sources and Review Scope](#3-sources-and-review-scope)
  - [3.1 Scope and Limitations](#31-scope-and-limitations)
- [4. Findings: RAM Requirements and Legacy Comparison](#4-findings-ram-requirements-and-legacy-comparison)
  - [4.1 Other RAM-Relevant Requirements](#41-other-ram-relevant-requirements)
  - [4.2 Important Distinctions](#42-important-distinctions)
- [5. LH-SIG-105: Sources and Interpretation](#5-lh-sig-105-sources-and-interpretation)
  - [5.1 Customer Specification](#51-customer-specification)
  - [5.2 Feature List](#52-feature-list)
  - [5.3 Documented Customer Clarification](#53-documented-customer-clarification)
  - [5.4 Annual Basis and Open Interpretation](#54-annual-basis-and-open-interpretation)
- [6. Distinction from Hardware MTBF](#6-distinction-from-hardware-mtbf)
- [7. Existing Requirement Rather Than New Requirements](#7-existing-requirement-rather-than-new-requirements)
- [8. Evidence Without Additional Acceptance Criteria](#8-evidence-without-additional-acceptance-criteria)
- [9. Availability and Maintainability Boundaries](#9-availability-and-maintainability-boundaries)
- [10. Missing Information](#10-missing-information)
- [11. Interpretation Risks](#11-interpretation-risks)
- [12. Requirements Analysis Result](#12-requirements-analysis-result)
- [13. Documented Evidence Requirements and Available Evidence](#13-documented-evidence-requirements-and-available-evidence)
- [14. Open Clarification Questions](#14-open-clarification-questions)
- **[15. LH-SIG-105: Annual Assessment of the Existing Requirement](#15-lh-sig-105-annual-assessment-of-the-existing-requirement)**
  - [15.1 Reference Requirement](#151-reference-requirement)
  - [15.2 Event Scope](#152-event-scope)
  - [15.3 What Tests Can Establish](#153-what-tests-can-establish)
  - [15.4 Readable Calculation Example for One Year](#154-readable-calculation-example-for-one-year)
    - [15.4.1 Example Inputs](#1541-example-inputs)
    - [15.4.2 Calculation Rule](#1542-calculation-rule)
    - [15.4.3 Calculation](#1543-calculation)
    - [15.4.4 Meaning and Limitations](#1544-meaning-and-limitations)
  - [15.5 Provisions Not Established by the Source](#155-provisions-not-established-by-the-source)
  - [15.6 Current Evidence Status](#156-current-evidence-status)
- [16. Correction Register and Document Checks](#16-correction-register-and-document-checks)

## 1. Executive Summary

**LH-SIG-105 contains a quantitative annual disturbance requirement. It is not inherently incalculable merely because it specifies neither MTBF nor availability.**

The sources distinguish:

- **LH-SIG-94:** availability at least **0.9999**.
- **LH-SIG-95:** MTBF **100,000 h**.
- **LH-SIG-105:** "Pro Jahr darf bei einem von 1000 Signalgebern eine Störung erfolgen."
- **SE:FL:FEA:0806:** at most **0.001 functional disturbances per element per year**.

The OBB answer quoted in S4 describes a non-safety-relevant failed switching operation, for example a green light remaining dark at switch-on. Its applicability to the project baseline is not established: the email refers to an unavailable LH4.0.

**The annual basis is retained.** This analysis does not replace it with a multi-year observation period or a statistical average across years. LH-SIG-105 and FL0806 do not, by themselves, fully define an acceptance test.

An observed annual rate can be calculated from suitable data. Accepted feature status or a hardware MTBF calculation alone does not establish the observed annual disturbance rate. Actual compliance evidence is not present in the supplied documents.

## 2. Applied Skills

The following repository methodologies informed the technical analysis:

- [Railway-RAM](../../../Skills/Railway-RAM.md): distinction between RAM measures and review of project sources.
- [REQ-Review](../../../Skills/REQ-Review.md): separation of requirements, interpretation and missing information.
- [RAM-Metrics](../../../Skills/RAM-Metrics.md): units and calculation of an observed disturbance rate.
- [Reliability-Prediction](../../../Skills/Reliability-Prediction.md): limits of comparison with hardware MTBF.

These methodologies do not create additional customer requirements. They are not used to impose a statistical confidence level on the project.

## 3. Sources and Review Scope

| Reference | Source | Use |
| --- | --- | --- |
| S1 | [715 LH Signalgeber DSTW V1.1_Kom_SS_20250704.pdf](../715%20LH%20Signalgeber%20DSTW%20V1.1_Kom_SS_20250704.pdf) | Customer requirements, IDs, binding attributes and applicability; especially p. 5 and pp. 17-22. |
| S2 | [LH Signalgeber V2.0 signed.pdf](../LH%20Signalgeber%20V2.0%20signed.pdf) | Conventional and SEA requirements; approved 8 May 2024. |
| S3 | [FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx](../FL_SignalElement_old_3BU_62200_1001_FLAPQ.docx) | Previous product features; 3BU 62200 1001 FLAPQ ED01, change log dated 8 October 2025. |
| S4 | [RE_ Aufklärungen durch ÖBB bei LED Ausschreibung.msg](../RE_%20Aufkl%C3%A4rungen%20durch%20%C3%96BB%20bei%20LED%20Ausschreibung.msg) | Internal thread dated 8 January 2026 quoting the answer of 12 December 2025; no separate official answer supplied. |
| S5 | [D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf](../D2.3_Teillastenheft_Allgemeine_Anforderungen_V1.3_Kom_SS_20250704.pdf) | Additional environmental and enclosure requirements where applicable. |
| S6 | [SSDD_iLED_01PD01.docx](../SSDD_iLED_01PD01.docx) | Architecture and diagnostic behaviour; refers to a separate RAM plan but supplies no quantitative LH-SIG-105 demonstration. |

[G-PRD_S06000_02_EN.pdf](../../../Knowledge/Process/RAM-Process/G-PRD_S06000_02_EN.pdf) and [Requirements_Lessons.md](../../../Knowledge/Lessons_Learned/Requirements_Lessons.md) provided process and review context. Process guidance and example lessons are not project-specific customer requirements or field data.

### 3.1 Scope and Limitations

- The comparison covers LH-SIG-84 through LH-SIG-116 and LH-SIG-139, plus selected RAM-relevant requirements outside the RAMS chapter. LH-SIG-83 and LH-SIG-117 are headings.
- Tables contain engineering summaries, not full verbatim transcriptions. Only explicitly identified quotations reproduce source wording.
- Binding attributes and applicability follow S1. S2 is a different document stream; version numbers alone do not establish contractual precedence.
- S4 refers to LH4.0 and feature-list identifier FLAPC. The available files are the listed LH versions and FLAPQ. The discrepancy remains unresolved.
- No separate approved project requirements specification defining a binding LH-SIG-105 demonstration method was identified among the six supplied project files. S6 is a system design description.
- No new requirement IDs, thresholds, test volumes, logging functions or acceptance procedures are specified.
- Info and Soll entries are not promoted to Muss requirements.
- This is not a complete functional, electrical, optical or safety requirements review.

## 4. Findings: RAM Requirements and Legacy Comparison

Feature numbers abbreviate **SE:FL:FEA:xxxx**. The final column records source comparisons and open points, not additional project requirements.

| LH requirement | Existing source content | Previous FL | Comparison / open point |
| --- | --- | --- | --- |
| **84, 88** | Installation and exchange with commercially available tools. | 1006; 0316/0317 | Corresponding intent. This comparison does not specify demonstration conditions. |
| **85** | Replace front optics, light source or electronics without housing removal or optical readjustment. | 1005 | Info in V1.1. LRU exchange is not necessarily separate component exchange. |
| **86-87** | Housing-independent light-point/indicator subsystem exchange without optical readjustment. | 1005 | Soll in V1.1; S2 uses stronger light-point wording. Applicability of 87 is blank in S1. |
| **89** | Exchange without changing physical or functional properties. | 1005 | Corresponding intent; actual implementation not demonstrated. |
| **90** | Installation/exchange maximum 10 min, labelled MRT. | 0811; 1005 | 0811 uses mean repair time and excludes preparation/follow-up; 1005 requires less than 10 min. Maximum and mean differ. 10 min equals 600 s, without creating a new target. |
| **91** | Visibility retained despite degradation, temperature and partial failures over useful life. | 0219; 0810 | Partial optical-lifetime coverage; feature text is not complete evidence. |
| **92** | Axial intensity range not undershot over useful life. | 0808/0810 | 0808 references the ID but its normative text specifies availability/MTBF rather than an explicit optical limit. |
| **93** | Technical useful life at least 130,000 operating hours. | 0810; 0808 comments | 15 calendar years are not equivalent to 130,000 operating hours for intermittent use. |
| **94** | Availability at least 0.9999 over life. | 0808 | Same numerical value as 99.99%. Availability class and downtime scope not defined by this wording. |
| **95** | "Ein Signalgeber muss eine MTBF von 100.000h aufweisen." | 0808: at least 200,000 h | FL explicitly states a minimum; LH wording does not. Comparison also depends on boundary, failure definition and profile. |
| **96** | Circuit measures to achieve useful life are permitted. | Design principles | Info/design freedom, not a separate numerical target. |
| **97** | Local operating-hour storage; SEA applicability. | 0407 | Records powered time, including dark time. |
| **98** | Usage visible at site without dismantling/additional systems. | 0633 | Descoped despite Muss in S1 for Conventional/SEA; no customer waiver evidenced. |
| **99** | Green to 68%, yellow 68.1-81.1%, red from 81.2% of useful life. | 0634 | Descoped. Treatment of values between stated boundaries not explained in the wording. |
| **100** | Indicator location agreed with customer. | 0633 | Customer agreement not established by feature status. |
| **101** | Wired readout after dismantling. | 0643 | CAN readout described; conventional applicability unresolved. |
| **102** | Wireless readout without dismantling. | 0644 | Soll in S1, Descoped in FL. Descope is not a documented customer waiver. |
| **103** | Useful-life boundary includes complete system from cable-side terminal, including full connector. | 0810 | Corresponding intent. The statement explicitly concerns useful life. |
| **104** | Average 300 activations/day or 100 blinking sessions/day of 2 min; continuous through very infrequent use. | 0810/0812/0813 | Different FL profiles include 300 x 2 min and 100 x 1 min. S1 marks this Info; an average is not a universal maximum. |
| **105** | Per year, a disturbance may occur in one of 1,000 Signalgeber. | 0806 | Annual normalisation of 0.001 functional disturbances per element-year present. Counting and demonstration method not fully described. |
| **106** | High-impedance interlocking interface on disturbance, Conventional. | 0805 | Related analogue fault response; no new impedance/time threshold from this review. |
| **107** | Disturbance disclosure at interface, DSTW/SEA. | 0805; 0406 | Diagnostic behaviour described; numerical compliance not established by feature text. |
| **108-109** | No required prescribed/periodic maintenance except external cleaning. | 1001 | Similar intent. Corrective intervention versus random-failure repair needs interpretation. |
| **110** | If necessary, maintenance/inspection interval at least 2 years. | 1004 | Ideally no recurring inspection does not explicitly reproduce the two-year limit. |
| **111** | At least 4 years as interval objective, Soll. | 1004 | No explicit four-year value identified. |
| **112** | Safety/application conditions cannot require interlocking activation/state changes for maintenance purposes. | 1003 | Not influencing safety/application conditions differs from prohibiting required activation. |
| **113** | SIL4 safety documented for approval. | 0801/0807 | Safety is distinct from disturbance rate and availability. |
| **114-116** | THR matrices for small/large light points and Signalgeber. | 0801 | A general FL scalar THR does not replace referenced matrix allocations without mapping. |
| **139** | Local illuminated-duration storage; Conventional. | 0407 | Powered operating hours, including dark time, are not illuminated duration. |

### 4.1 Other RAM-Relevant Requirements

| LH requirement | Source content / RAM relevance | Comparison / open point |
| --- | --- | --- |
| **5-9** | Signalgeber types and complete-system definitions. | Optics, interface, connector, mounting and housing form part of the applicable system definition. |
| **10-11** | Disturbance definition and unspecified optical behaviour. | Broader than the switching example in S4; relationship unresolved. |
| **12-13** | Disturbed state, dark/high impedance. | 0805 addresses non-recoverable faults; complete coverage and digital applicability not established. |
| **18** | Standards including EN 50126-1. | 0108/0701/0807 provide references, not a final contractual edition baseline. |
| **33, 35-36** | Alignment retention, exchange without readjustment, mass limits. | 0317/1005 and mass features correspond, sometimes with tighter product values. |
| **40-48** | Environment, snow, temperature, EMC, transport/storage, IP, pressure/suction. | 0703/0706/0707/0314/0803/0301 address these topics. FL IP65 versus LH IP54; temperature references and profiles differ. |
| **54-57, 63, 65** | Visibility, angles, distribution and intensity retention. | Functional disturbance/lifetime criteria, not additional MTBF targets. |
| **67-69** | Colour stability under ageing, temperature, voltage and phantom light. | 0220 addresses intent; informal colour deviations do not establish customer approval. |
| **71, 74, 81-82** | Fault disclosure, series operation, voltage behaviour, no flicker on single-pole disconnection. | Relevant to disturbance interpretation. 0317 incorrectly cites LH-SIG-82 for mounting. |
| **76-77** | 1 Hz, 1:1 duty ratio, tolerances. | 0502 is tighter; this does not establish an LH-SIG-105 counting rule for blink edges. |
| **118-120** | RAM evidence, German language, editable/noneditable digital formats. | 0904/0905/0807 partly correspond; generic English documents alone do not meet German delivery wording. |
| **121-123** | Manual, diagnostics, spares, measurement procedures and tools. | 0904/0905/1006 correspond; complete delivery not evidenced. |
| **124-126** | Identification and machine-readable information. | 0903; no automatic additional event-logging function follows. |
| **135** | Small light points: night range 40-300 cd. | 0619 nominally matches; 0624 permits 21 cd rather than 40 cd minimum. Variant-specific discrepancy. |
| **136-138** | Indicator intensity, angles and recognition. | 0218/0601/0602 correspond. Other customers' pixel-loss limits are not automatically OBB limits. |

### 4.2 Important Distinctions

- Accepted records feature acceptance, not demonstrated implementation or customer compliance.
- Descoped records a product decision, not demonstrated customer waiver.
- 30-year product support/product lifetime in 0809 is not 130,000 operating hours of technical useful life.
- The potentially applicable 30-year enclosure UV resistance in S5 does not automatically apply to every component.
- Ambient, external housing and internal component temperatures differ. S5 includes potentially applicable track-area ambient -40 to +70 degrees C; LH-SIG-42/43 concern the housing.
- A 20 degrees C FL assumption does not represent every environmental requirement.

## 5. LH-SIG-105: Sources and Interpretation

### 5.1 Customer Specification

**Verbatim S1, LH-SIG-105, p. 19:**

> Die zulässige Störungsrate ist wie folgt definiert und darf nicht überschritten werden:
>
> Pro Jahr darf bei einem von 1000 Signalgebern eine Störung erfolgen.

Binding: **Muss**. Applicability: **Konventionell, SEA**. DSTW is not listed for this row.

### 5.2 Feature List

**Verbatim S3, SE:FL:FEA:0806:**

> Die Störungsrate (Anzahl von Störungen je Element und Jahr) für Funktionsstörungen (fallweise Einschaltversagen, fallweise Toleranzüberschreitungen, etc.) eines Signalelements darf nicht mehr als 0.001 betragen.

The feature lists LH-SIG105 as its origin and Accepted as its status. It explicitly normalises per element per year and provides functional disturbance examples.

### 5.3 Documented Customer Clarification

The answer dated 12 December 2025, quoted in S4, describes a permitted non-safety-relevant failed switching operation among 1,000 Signalgeber; example: a green light remains dark at switch-on.

The answer calls LH-SIG-95 availability. The LH text instead specifies MTBF there; availability is separately specified by LH-SIG-94. The terminology discrepancy does not itself amend the requirement texts.

The answer is quoted in an internal email. Whether and with what precedence it clarifies the available LH versions is not established.

### 5.4 Annual Basis and Open Interpretation

"Pro Jahr" in the LH and "je Element und Jahr" in the FL establish the annual basis. No longer observation duration or averaging across years is derived from them.

Repeated disturbances of the same unit, fixed versus rolling years, changing fleets and observation gaps are not fully explained. These are open analysis questions, not additional provisions set by this report.

## 6. Distinction from Hardware MTBF

LH-SIG-95 specifies a time in hours. LH-SIG-105/FL0806 concern functional disturbance counts per element per year. Their event populations are not established as identical.

A hardware prediction alone does not provide an observed annual count of intermittent activation failures or tolerance exceedances. A switching failure is not automatically unrelated to hardware either.

This review derives **no hardware MTBF target, FIT target or per-switching failure probability** from LH-SIG-105. Previous conversions have been removed from the current analysis because they depended on additional exposure and event assumptions.

An actual FIDES, IEC 61709 or MIL-HDBK-217 prediction is outside this review.

## 7. Existing Requirement Rather Than New Requirements

The existing mapping is:

```text
LH-SIG-105 -> SE:FL:FEA:0806
```

No additional project requirement IDs or expanded shall-statements are introduced.

Previous obligations concerning an approved event catalogue, exposure specification, logging, statistical demonstration plan and test scenarios were assistant proposals. They are not contractual requirements established by LH-SIG-105 and have been withdrawn as requirement drafts.

Unclear terms can be recorded as clarification questions. They do not automatically require an additional customer document or device function.

## 8. Evidence Without Additional Acceptance Criteria

LH-SIG-105 and FL0806 state the annual basis and numerical target. Their quoted wording specifies no particular test fleet size, confidence level or complete acceptance procedure.

**Assessment of evidence, not an additional test requirement:**

| Available or possible evidence | Potential conclusion | What does not follow from it alone |
| --- | --- | --- |
| Feature text marked Accepted | Requirement is included in the FL. | Actual annual disturbance rate is met. |
| Functional test | Behaviour was checked under the recorded conditions. | Quantitative annual rate if results lack a traceable annual basis. |
| Switching/endurance test | Can provide event counts and test time or switching counts. | Automatic equivalence between cycles/laboratory hours and an operating year. |
| Annual operational record | Can provide an observed rate for the fleet and year considered. | Guarantee for other years or automatic formal customer acceptance. |
| Hardware MTBF prediction | Result for the modelled hardware reliability. | Complete evidence for every FL0806 functional disturbance. |

"Passing functional tests alone does not establish a rate of 0.001 per Signalgeber-year" describes a **limit of inference**, not an obligation to perform a particular extra test or achieve statistical confidence.

The binding project demonstration method is not conclusively identifiable from the supplied documents. This report does not invent one.

## 9. Availability and Maintainability Boundaries

- LH-SIG-94 specifies availability of at least 0.9999.
- LH-SIG-90 specifies maximum 10 min for installation/exchange.
- FL0811 describes mean repair time and excludes preparation/follow-up.

A maximum exchange activity is not mean complete downtime. The source comparison identifies this distinction without assigning additional downtime terms or budgets.

Previous illustrative MDT limits and availability calculations have been removed. They were model-dependent additions, not existing requirements.

## 10. Missing Information

| Item | Finding |
| --- | --- |
| Contractual precedence | Relationship between S1, S2 and the quoted LH4.0 clarification unresolved. |
| Disturbance scope | Broad LH-SIG-10 definition, FL examples and switching clarification not conclusively reconciled. |
| Repeated events | Event count versus affected-unit count not fully explained for repeated disturbances. |
| Year boundaries | Fixed or rolling year not explicitly specified. |
| Changing population | Partial years, replacements and reporting gaps not resolved by the wording. |
| Demonstration method | No complete project-specific acceptance rule identified in the supplied documents. |
| Performance evidence | No annual disturbance records or associated test results supplied for this assessment. |
| Other RAM evidence | Complete separate RAM plan, calculations, maintainability demonstration and controlled THR allocations unavailable in the reviewed file selection. |

These gaps identify missing review information, not necessarily missing project activities or noncompliance.

## 11. Interpretation Risks

| Risk | Potential incorrect conclusion |
| --- | --- |
| Adding statistical rules | Additional obligations are presented as customer requirements. |
| Replacing annual basis with multi-year averaging | An adverse year can be obscured by other years; source wording does not establish such averaging. |
| Confusing normalisation with test volume | Per 1,000 becomes exactly 1,000 mandatory test units without a source. |
| Inventing counting rules | Repeated disturbances are excluded or counted repeatedly without a basis. |
| Excluding every safe-dark reaction | Non-safety-relevant functional disturbances can be wrongly omitted. |
| Treating Accepted/Descoped as customer evidence | Compliance or waiver assumed without evidence. |
| Equating MTBF, useful life and disturbance rate | Different measures and event populations are conflated. |
| Ignoring existing FL differences | Maximum/mean time, counter types, inspection intervals and optical limits remain incorrectly mapped. |

## 12. Requirements Analysis Result

**Source-based conclusion:**

> LH-SIG-105 contains an annual disturbance requirement. FL0806 represents it as at most 0.001 functional disturbances per element per year. Counting and demonstration details are not fully described in the supplied documents. Actual compliance cannot be assessed from the supplied performance data.

The requirement is not inherently incalculable. The missing elements are the basis for a specific assessment and its evidence, not the numerical target.

This version contains no new requirement drafts or binding acceptance wording.

## 13. Documented Evidence Requirements and Available Evidence

| Source | Documented requirement / statement | Review evidence status |
| --- | --- | --- |
| LH-SIG-118 | Delivery documentation includes RAM evidence. | Does not establish a specific confidence level or test programme for LH-SIG-105. |
| LH-SIG-119 | German customer documentation. | Existing delivery requirement, not a review addition. |
| LH-SIG-120 | Editable and noneditable digital documentation. | Existing format requirement. |
| LH-SIG-121-123 | Manual, measurement/test documentation where measurements are required, and defined tools. | Subject to respective applicability; no blanket additional LH-SIG-105 test obligation. |
| S6 | Reference to a separate RAM plan. | Reference is not available quantitative compliance evidence. |
| S3, FL0806 | Requirement marked Accepted. | Establishes inclusion in FL, not achieved rate. |

The previous general Required Evidence list has been replaced with this source mapping. Other potentially useful RAM analyses are not declared additional customer deliverables.

## 14. Open Clarification Questions

These are **questions about existing requirements**, not newly assigned work packages or requirements.

| Source | Open question |
| --- | --- |
| S1/S2/S4 | Which document and customer clarification apply contractually to NextGen_Bahnsignal? |
| LH-SIG-10 / LH-SIG-105 / FL0806 | How does the broad disturbance definition relate to switching and tolerance examples? |
| LH-SIG-105 | How are repeated disturbances on one device counted? |
| LH-SIG-105 / FL0806 | Which year and fleet population govern a particular assessment? |
| LH-SIG-118 / S6 | Does an existing binding demonstration method appear in project documents not supplied here? |
| LH-SIG-90 / FL0811 | Has maximum exchange time versus mean repair time been resolved? |
| LH-SIG-93 / FL0810 | How is operating-hour versus calendar-year life treated for the actual use case? |
| LH-SIG-98-102 / FL0633/0634/0644 | Are documented decisions available for descoped indicators and readout options? |
| LH-SIG-104 / FL0812/0813 | Which of the differing profiles applies to each variant? |
| LH-SIG-135 / FL0624 | How is the 21 cd versus 40 cd discrepancy resolved for the relevant variant? |

## 15. LH-SIG-105: Annual Assessment of the Existing Requirement

This chapter replaces previous assistant-authored requirements and acceptance drafts. It explains only the existing requirement and its numerical normalisation.

### 15.1 Reference Requirement

The reference texts are LH-SIG-105 and SE:FL:FEA:0806 in Chapter 5. No additional shall-statement is created.

```text
LH:     Pro Jahr darf bei einem von 1000 Signalgebern eine Störung erfolgen.
FL0806: At most 0.001 functional disturbances per element per year.
```

The FL line above is a summary; section 5.2 contains its full original wording.

### 15.2 Event Scope

LH-SIG-10 describes loss of full functionality, including unacceptable optical properties, interface behaviour and flicker. FL0806 mentions intermittent activation failures and tolerance exceedances. S4 describes a non-safety-relevant failed switching operation.

No new definition with added response time, reset conditions or cause-based exclusions is formulated. The relationship between the statements remains an interpretation issue.

### 15.3 What Tests Can Establish

A functional test establishes the recorded behaviour under its test conditions. Whether it also substantiates the annual value depends on the available evidence and its relationship to the annual requirement.

The quoted LH-SIG-105/FL0806 wording specifies neither statistical confidence nor a particular endurance, switching, field or accelerated test. Such methods are not imposed here.

### 15.4 Readable Calculation Example for One Year

#### 15.4.1 Example Inputs

- **One year** is considered, retaining the source's annual basis.
- **1,000 Signalgeber** illustrate the numerical normalisation.
- For this example, all 1,000 units belong to the population for the year and the counted disturbances are known.
- These are calculation assumptions, not a prescribed sample size or acceptance procedure.

#### 15.4.2 Calculation Rule

```text
For the same population over one year:

Observed annual disturbance rate =
Number of counted functional disturbances in the year / Number of Signalgeber

Unit: disturbances per Signalgeber per year
FL0806 limit: at most 0.001
```

#### 15.4.3 Calculation

```text
0 disturbances among 1,000 Signalgeber in one year:
0 / 1,000 = 0

1 disturbance among 1,000 Signalgeber in one year:
1 / 1,000 = 0.001

2 disturbances among 1,000 Signalgeber in one year:
2 / 1,000 = 0.002
```

Three observation years are not needed to calculate these annual values. The previous statistical multi-year exposure calculation was not part of the customer requirement and has been removed.

#### 15.4.4 Meaning and Limitations

| Example annual observation | Comparison with the FL0806 number |
| --- | --- |
| 0 disturbances among 1,000 Signalgeber | Observed value below 0.001. |
| 1 disturbance among 1,000 Signalgeber | Observed value equals 0.001. |
| 2 disturbances among 1,000 Signalgeber | Observed value above 0.001. |

This is a numerical comparison for the year and assumed event scope. It does not replace an unresolved contractual acceptance rule or guarantee future-year rates.

No new conversion rule is established here for changing populations, partial years or unclear counting.

### 15.5 Provisions Not Established by the Source

The quoted wording alone does not establish:

- a mandatory test of exactly 1,000 units;
- a statistical confidence level or Poisson model;
- multi-year failure-free observation;
- a particular number of laboratory hours or switching cycles;
- additional Signalgeber logging;
- staged customer acceptance;
- a new hardware MTBF/FIT target or per-switching failure probability.

The annual basis exists. It is distinct from specifying how the demonstration is performed.

### 15.6 Current Evidence Status

**Established by the supplied documents:** The requirement is documented in the LH and FL0806.

**Not established:** The achieved annual rate of the project devices or whether an existing test report provides binding evidence of compliance.

This report does not assert that an agreed demonstration plan, ongoing tests or pilot programme already exist.

## 16. Correction Register and Document Checks

### Withdrawn Additions

The following quotations come from the previous report, not the customer specification. They identify specific corrected passages.

| Previous passage / exact quotation | Finding | Correction |
| --- | --- | --- |
| Chapter 7: "The RAM demonstration plan shall define the statistical model, confidence level, sample exposure, common-cause treatment and acceptance rule before compliance is claimed." | Assistant-derived shall-statement, not source wording. | Draft and assistant requirement IDs removed; questions do not impose new document obligations. |
| Chapter 15.4.1: "Illustrative acceptance criterion: **95% one-sided confidence**, not a contractual criterion." | Despite the caveat, elaborated as a demonstration basis and confused with the customer request. | Statistical acceptance example removed. |
| Chapter 15.4.4: "Numerical target not demonstrated." | Assessment concerned added confidence criterion, not solely the annual requirement. | Replaced with a numerical comparison of observed annual value against FL0806. |
| Chapter 15.5: "If sufficient exposure cannot be obtained before delivery, agree a **staged acceptance arrangement with the customer**." | Unsupported additional acceptance arrangement. | Removed as a prescribed course of action. |
| Chapter 15.6: "Der quantitative Nachweis der zulässigen Störungsrate erfolgt gemäß dem mit dem AG abgestimmten RAM-Nachweisplan." | Agreed plan and planned activities not evidenced. | Replaced with source-based information status. |
| Chapter 13: "Approved disturbance catalogue, event-counting specification and exposure definition." | Assistant document list under Required Evidence, not established by LH-SIG-105. | Chapter 13 now maps evidence requirements to sources. |

Additional hourly/FIT/per-demand conversions, model-based availability examples and general test/logging obligations have also been removed. Calculations use readable plain text.

### Correction Scope

- Both project Markdown reports have been aligned.
- Numbered chapters and a table of contents remain.
- Source comparison tables remain; assessments are not new requirements.
- Customer specifications, FL and other source documents were not changed.
- Earlier CSV/Excel artefacts outside these Markdown reports were not revised in this correction. Their assistant-authored requirement drafts and statistical criteria are likewise not customer requirements and must not be used as such.

These document checks do not certify product compliance. They correct the separation between source content, analysis and unsupported additions.
