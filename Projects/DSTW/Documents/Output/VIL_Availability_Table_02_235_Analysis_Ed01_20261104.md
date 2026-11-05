# VIL Availability - Analysis of Customer Table 02_235 (D2.2 "Tabelle 2")

| Document information | Value |
| --- | --- |
| Subject | Customer availability table 02_235 for the VSTW / [VIL-Instance] and its relation to EL4-DIL-SSS-REQ-00587, -00569 and -00570 |
| Edition | **Ed01** |
| Date | 2026-11-04 |
| Status | Engineering analysis for review; not an approved requirements baseline or compliance demonstration |
| Classification | Hitachi Rail - Internal |
| Scope | Meaning of the table categories and rows (MRT, MTTR, MTTF); recalculation; calculation method; demonstration of fulfilment; impact on the assumptions used so far |

## 1. Key messages

1. **Table 02_235 is the customer's top-down allocation table for the VSTW** (D2.2 clause 5.4.0-2, "Tabelle 2"). It shows **one combination** of MTTF and MTTR that produces each required availability value. The **availability values are the requirements**; the MTTF values are **not**.
2. **MRT and MTTR are different quantities.** MRT is the active repair time; MTTR is the complete time to restore service. Availability is calculated with **MTTR**, not MRT.
3. **The manual restoration time is 3.75 h (225 min).** This value is in the customer table and in RAMP DIL/VIL Table 9. The value **"MTTR = 6 h" in EL4-DIL-SSS-REQ-00569 does not match either source** and should be corrected.
4. **02_195 (MRT = 0.5 h) does not conflict with 3.75 h.** It describes the repair part of the manual restoration. In the manual case, the difference of 3.25 h is consistent with the **3 h on-site response time** in the technical concept plus a non-explained 0.25 h. Using 0.5 h as MTTR would be non-conservative by a factor of 7.5.
5. **The customer's own manual column does not strictly meet 0.999979.** Unrounded, it gives 99.99786 %. Strict compliance at MTTR = 3.75 h needs a mean time between manual events of at least **20.38 years**, not 20 years.
6. **The three Störung categories use 18.4 min/year of the 26.28 min/year overall budget.** About 7.9 min/year (30 %) remain unallocated. Their use must be agreed.
7. **Fulfilment is shown per category:** sum the unavailability $f_i \cdot MDT_i$ of all events assigned to the category and compare it with the category budget. The overall requirement is shown by adding the service-affecting categories.
8. **Random hardware failures of the compute nodes are not the design driver.** The manual and overall budgets are dominated by software-induced and common-cause events; the "Fehler" budget is dominated by **how long a lost redundancy stays unrepaired**.

## 2. Sources and precedence

| Ref. | Source | Used for |
| --- | --- | --- |
| S1 | [D2.2 Teillastenheft RAMS V1.3](../D2.2_Teillastenheft_RAMS_V1.3.pdf), clauses 02_36, 02_84, 02_97, 02_98, 02_111, 02_113 to 02_119, 02_195, 02_196 | Customer requirement text, formula $A = MTTF/(MTTF+MTTR)$, fault classes, definitions |
| S2 | Table 02_235 (image of "Tabelle 2", supplied by the user; the [D2.2 Excel version](../D2.2_Teillastenheft_RAMS_V1.3.xlsx) contains only the placeholder "5.4.0-2 Tabelle 2") | Table values analysed here |
| S3 | [SSS DIL RAMS Ed02PD01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed02PD01.docx), EL4-DIL-SSS-REQ-00587, -00569, -00570 | Current system requirement wording |
| S4 | [RAMP DIL/VIL Ed01](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf), section 3.4, Table 9 | Hitachi RAM plan representation of the same table |
| S5 | [PH D2.2 RAMS Ed02](../PH_D2.2_RAMS_3BU_17300_0022_DTAPC_Ed02.pdf), response to 02_84 | Hitachi commitment on MRT verification |
| S6 | [Technische Konzepte V04 PD01](../Digitales_Stellwerk_Technische_Konzepte_V04_PD01.pdf), sections 8.1.1, 8.1.2.2, 8.1.5.1 | Service organisation, 3 h on-site response, FK1 to FK4 handling |
| S7 | [VIL Availability Approximate Calculation](<../VIL Availability Approximate Calculation.xlsx>) | Hardware MTBF values and existing hot-hot calculation |
| S8 | [VIL_Redundancy_Restoration_Time.md](VIL_Redundancy_Restoration_Time.md) and [VIL_Availability_Three_Requirements_Interpretation_Ed04_V1.3.md](VIL_Availability_Three_Requirements_Interpretation_Ed04_V1.3.md) | Assumptions used so far (600 s redundancy restoration, 2-minute candidates) |

The current SSS RAMS is the controlling system requirement. The customer table and RAMP Table 9 are the basis for correcting the MTTR value in EL4-DIL-SSS-REQ-00569. Approval of that correction is a configuration-management action and is not assumed here.

## 3. The table as published

Source: S2, D2.2 clause 5.4.0-2 (ID 02_235).

| Row | Störung VSTW Gesamt | Störung VSTW (Behebung manuell) | Störung VSTW 10 min (selbsttätig beheben) | Störung VSTW 2 min (selbsttätig beheben) | Fehler VSTW |
| --- | ---: | ---: | ---: | ---: | ---: |
| MRT: Mean repair time [h] | 0.4375 | 0.5 | 0.1667 | 0.0333 | 1 |
| MTTR: Mean time to restore [h] | 0.4375 | 3.7500 | 0.1667 | 0.0333 | 25 |
| MTTF: Mean time to fail [h] | 8760 | 175200 | 17520 | 8760 | 8760 |
| Availability [%] | 99.9950 | 99.9979 | 99.9990 | 99.9996 | 99.7154 |
| Related requirement | 02_113 / REQ-00587 | 02_116 / REQ-00569 | 02_118 / REQ-00569 | 02_119 / REQ-00569 | 02_117 / REQ-00570 |

RAMP DIL/VIL Table 9 (S4) shows the same content in minutes and years: overall 26.25 min/year; manual MTTR 225 min, MTBF 20 years, 11.25 min/year; 10 minutes, 2 years, 5 min/year; 2 minutes, 1 year, 2 min/year.

## 4. What the categories mean

### 4.1 Störung and Fehler

The customer distinguishes two kinds of events (S1 clause 02_36; S3 definitions [Fault] and [Error]):

| Term | Meaning | Effect on availability |
| --- | --- | --- |
| **Störung** (disturbance, [Fault]) | The event **restricts operation** | Consumes the operational downtime budget of 02_113 / REQ-00587 and one of the three categories of 02_116, 02_118, 02_119 / REQ-00569 |
| **Fehler** (error, [Error]) | A fault is present but has **no operational impact** | Does not consume operational downtime. It is limited separately by 02_117 / REQ-00570 |

### 4.2 The five columns

| Column | What it covers | Interpretation |
| --- | --- | --- |
| **Störung VSTW Gesamt** | All disturbances of the VSTW together | The overall class 2 envelope of 99.995 %. 0.4375 h with one event per year equals **26.25 min/year**, the rounded form of the exact 26.28 min/year budget. MRT = MTTR because it is a pure top-down equivalent, not a maintenance scenario |
| **Störung - Behebung manuell** | Disturbances that need a technician to restore service | MRT 0.5 h repair time (02_195), MTTR 3.75 h total restoration. On average **one event in 20 years** |
| **Störung - 10 min selbsttätig** | Disturbances the VSTW clears **automatically within 10 minutes** (02_111: detect, safe state, self-test, automatic recommissioning) | MRT = MTTR = 10 min; no logistic delay. **One event in 2 years** |
| **Störung - 2 min selbsttätig** | Disturbances the VSTW clears **automatically within 2 minutes** | MRT = MTTR = 2 min. **One event per year** |
| **Fehler VSTW** | Errors without operational impact | MRT 1 h (02_196), MTTR 25 h. **One error per year**, present for 25 h on average |

### 4.3 Classification of an event (proposal)

The supplied documents contain no rule that assigns a specific event to a column. The following rule is proposed so that the categories are **exhaustive and mutually exclusive**:

| Step | Question | Category |
| --- | --- | --- |
| 1 | Is operation restricted? No, but a fault is present | **Fehler** (REQ-00570) |
| 2 | Operation restricted; service restored automatically within $\le 120\,\mathrm{s}$ | **2 min** (REQ-00569) |
| 3 | Operation restricted; service restored automatically within $120\,\mathrm{s} < t \le 600\,\mathrm{s}$ | **10 min** (REQ-00569) |
| 4 | Operation restricted; manual intervention required | **Manual** (REQ-00569) |
| 5 | Operation restricted; automatic restoration but longer than 600 s | **Not covered by the table.** Proposal: count as manual, or in the unallocated reserve; to be agreed |

Every event of steps 2 to 5 also counts once in the overall requirement 02_113 / REQ-00587.

Typical candidates (from [VIL_Availability_Explanation.md](VIL_Availability_Explanation.md); to be confirmed by fault injection):

| Category | Candidate events |
| --- | --- |
| 2 min | Restart of one VIL application (RCU; CC with RCU) on all redundant nodes per EL4-VIL-SSS-REQ-01155 / -00229; reconnection of a RaSTA / X25 connection after a safety reaction; transient overload that a restart clears |
| 10 min | Complete automatic restart of the VIL instance (3 to 4 min according to the technical concept for a planned update); node-level restart when the remaining redundancy cannot carry operation |
| Manual | Double hardware failure; common-cause failure not cleared automatically; permanent fault; restart attempts exhausted ("Stopped" state); version or authorisation mismatch causing permanent shutdown |
| Fehler | Loss of one 2oo2 redundancy partner while the other keeps operating; loss of one network path; loss of one diagnosis channel - **subject to customer classification** (see 7.4) |

## 5. What the rows mean

### 5.1 Definitions

| Row | Meaning | Use |
| --- | --- | --- |
| **MRT** - mean repair time | Mean duration of the **active repair work** (diagnosis on site, exchange, reset, restart, function test) | Maintainability requirement. 02_84 requires that the MRT is met for component exchange. **Not** the downtime in the availability formula |
| **MTTR** - mean time to restore | Mean time **from loss of the required function until it is restored**. Includes detection, notification, travel / response, MRT and return to service | Mean down time per event in the availability formula |
| **MTTF** - mean time to fail | Mean operating time between two events of the category. For a repairable system this is the mean up time; RAMP Table 9 calls it MTBF | Event frequency $f = 1/MTTF$ |
| **Availability** | Share of time the function is available | The requirement value |

This reading is consistent with the EN 50126-1 / IEC 60050-192 terminology. The exact definitions should be quoted from the standard in the RAM plan.

### 5.2 Time line of a manual restoration

$$
MTTR = T_{\mathrm{detection/notification}} + T_{\mathrm{response\ on\ site}} + MRT + T_{\mathrm{test/return\ to\ service}}
$$

| Column | MTTR - MRT | Plausible content of the difference | Basis |
| --- | ---: | --- | --- |
| Manual | 3.25 h | 3.0 h on-site response + 0.25 h detection, ticket, hand-over and return to service | 3 h on-site response, 24/7 service centre: S6 section 8.1.1. The 0.25 h is **not explained** in the sources |
| 10 min, 2 min | 0 | Restoration is fully automatic; no logistic delay | 02_111 |
| Fehler | 24 h | Deferred rectification, for example next working day | **Interpretation.** FK4 handling is "werktags i. d. R. im Rahmen der nächsten geplanten Wartung" (S6 section 8.1.2.2), which can exceed 24 h over weekends |
| Gesamt | 0 | Top-down envelope only | - |

**Conclusion:** 02_195 (MRT 0.5 h) and 02_196 (MRT 1 h) are **consistent with the table**. They are repair times. The availability values are based on MTTR = 3.75 h and 25 h.

## 6. Recalculation and strict compliance check

### 6.1 Formulae

Customer formula (02_98):

$$
A = \frac{MTTF}{MTTF + MTTR}, \qquad U = 1 - A = \frac{MTTR}{MTTF + MTTR} \approx \frac{MTTR}{MTTF}
$$

Annual equivalent, continuous required service, $T_{\mathrm{year}} = 8760\,\mathrm{h} = 525{,}600\,\mathrm{min}$:

$$
D_{\mathrm{year}} = U \cdot T_{\mathrm{year}}
$$

Minimum mean time between events needed at a given MTTR:

$$
MTTF_{\mathrm{min}} = \frac{A_{\mathrm{req}}}{1 - A_{\mathrm{req}}} \cdot MTTR
$$

### 6.2 Results

| Column | $A$ calculated, unrounded | $A$ required | Strict result | Downtime [min/year] | Budget [min/year] | Margin [min/year] | $MTTF_{\mathrm{min}}$ at table MTTR |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| Gesamt | 99.995006 % | 99.995 % | Met | 26.249 | 26.280 | +0.031 | 8,750 h (1.00 y) |
| Manual | **99.997860 %** | 99.9979 % | **Not met** | 11.250 | 11.038 | **-0.212** | **178,568 h (20.38 y)** |
| 10 min | 99.999049 % | 99.999 % | Met | 5.001 | 5.256 | +0.255 | 16,670 h (1.90 y) |
| 2 min | 99.999620 % | 99.9996 % | Met | 1.998 | 2.102 | +0.104 | 8,325 h (0.95 y) |
| Fehler | 99.715424 % | 99.7154 % | Met | 1,495.7 (24.93 h) | 1,495.9 | +0.13 | 8,759 h (1.00 y) |

Calculation for the manual column:

$$
A_{\mathrm{man}} = \frac{175{,}200}{175{,}200 + 3.75} = 0.9999786 < 0.999979
$$

$$
MTTF_{\mathrm{min}} = \frac{0.999979}{0.000021} \cdot 3.75\,\mathrm{h} = 178{,}568\,\mathrm{h} = 20.38\,\mathrm{years}
$$

The table rounds to 99.9979 % and therefore looks compliant. Measured against the 6-digit value 0,999979 in 02_116, it is short by 0.21 min/year. **A demonstration should use the unrounded requirement**, unless the customer confirms that the table itself defines the acceptance level.

The rounding of 10 min to 0.1667 h and 2 min to 0.0333 h has no relevant effect.

### 6.3 How the categories fit together

| Quantity | Required (from availability values) | Table values |
| --- | ---: | ---: |
| Manual | $2.1\times10^{-5}$ = 11.04 min/y | 11.25 min/y |
| 10 min | $1.0\times10^{-5}$ = 5.26 min/y | 5.00 min/y |
| 2 min | $0.4\times10^{-5}$ = 2.10 min/y | 2.00 min/y |
| **Sum of the three categories** | $3.5\times10^{-5}$ = **18.40 min/y** | **18.25 min/y** |
| Overall (Gesamt) | $5.0\times10^{-5}$ = 26.28 min/y | 26.25 min/y |
| **Not allocated** | $1.5\times10^{-5}$ = **7.88 min/y (30 %)** | 8.00 min/y |
| Events per year | - | 0.05 + 0.5 + 1.0 = **1.55** (Gesamt column: 1.0) |

Interpretation:

- If all three categories are met, the overall requirement is met **as long as service-affecting events outside the three categories stay below 7.88 min/year**. RAMP section 3.4 states that the classes are "not a subcomponent of the overall downtime"; how the reserve is used must be agreed.
- The Gesamt column (1 event per year, 26.25 min) is **not the sum** of the other columns (1.55 events per year, mean 11.8 min). It is a separate envelope. This confirms that **the MTTF values are illustrations, not frequency requirements.**

## 7. Impact on the requirements and on the assumptions used so far

### 7.1 Manual MTTR: 3.75 h instead of 6 h

| Item | With 6 h (SSS text) | With 3.75 h (table, RAMP) | Effect |
| --- | ---: | ---: | --- |
| Mean time between manual events needed | 32.62 y | **20.38 y** | Requirement on event frequency 37.5 % less strict |
| Permitted manual events | 0.031 /y | **0.049 /y** | +60 % |
| Manual budget | 11.04 min/y | 11.04 min/y | Unchanged |
| Ratio to 02_195 (MRT 0.5 h) | 12 | 7.5 | **Not a conflict**: different quantities |
| Zero-failure demonstration time, 60 % confidence | 29.9 instance-years | **18.7 instance-years** | Still not demonstrable by one station |

### 7.2 DPR and earlier notes

- The DPR uses 0.5 h for manual restoration. As MTTR, this is **non-conservative by a factor of 7.5** and should not be used in availability calculations.
- Earlier repository notes describe a conflict between 0.5 h, 6 h and 225 min. With this analysis, **0.5 h (MRT) and 225 min (MTTR) are consistent; 6 h is the outlier.**

### 7.3 Proposed 600 s redundancy restoration

The 600 s limit for restoring a failed 2oo2 redundancy partner ([VIL_Redundancy_Restoration_Time.md](VIL_Redundancy_Restoration_Time.md)) applies to the **Fehler** category if the customer accepts that losing one partner has no operational impact. The table assumes 25 h per error. A restartable node fault restored in 600 s uses only 1/150 of that time. **The proposal is compatible with the table and the requirement.** Permanent hardware faults still need a technician; for those, MRT (02_196, 1 h) and the response policy apply.

### 7.4 Fault class of a lost redundancy

Without georedundancy, loss of one CN leaves **no** node-level redundancy. The customer's FK2 explicitly includes "Ausfall der Redundanz mit Gefahr eines Gesamtausfalls" with **immediate, uninterrupted** rectification. FK4 allows rectification at the next planned maintenance. The difference changes the degraded window from about 3.75 h to 25 h or more (section 9).

### 7.5 FK3 handling and the 3.75 h MTTR

FK3 ("Ausfall von einzelnen Funktionen eines VSTWs") is to be rectified "werktags zur Büroarbeitszeit" (S6). If an FK3 event restricts operation and needs manual action, its restoration can take far longer than 3.75 h (night, weekend). **The 3.75 h assumes a 24/7 response.** The mapping between FK classes and table categories must be agreed.

## 8. How to calculate each category

### 8.1 Per category

Each category $k$ (2 min, 10 min, manual, Fehler) collects all events $i$ that end in that category according to section 4.3.

$$
U_k = \sum_{i \in k} f_i \cdot \overline{MDT}_i
\qquad\Longrightarrow\qquad
A_k = 1 - U_k \;\ge\; A_{k,\mathrm{req}}
$$

Equivalent to the table form:

$$
MTTF_k = \frac{1}{\sum_{i\in k} f_i},
\qquad
MTTR_k = \frac{\sum_{i\in k} f_i\,\overline{MDT}_i}{\sum_{i\in k} f_i},
\qquad
A_k = \frac{MTTF_k}{MTTF_k + MTTR_k}
$$

| Symbol | Meaning | Source of the value |
| --- | --- | --- |
| $f_i$ | Frequency of event $i$ [1/h] | HW: reliability prediction (method per RAMP) and RBD / fault tree / Markov model. SW and systematic: allocation, field data, FRACAS. CCF: beta factor. Infrastructure: IPS / data-centre analysis |
| $\overline{MDT}_i$ | Mean service down time of event $i$ [h] | Automatic: measured recovery time (fault injection). Manual: maintenance concept (detection, 3 h response, MRT, return to service) |

### 8.2 Overall

$$
U_{\mathrm{VIL}} = U_{2\,\mathrm{min}} + U_{10\,\mathrm{min}} + U_{\mathrm{man}} + U_{\mathrm{other}} \;\le\; 5\times10^{-5}
$$

Fehler is **not** added: it does not interrupt operation.

### 8.3 Fehler

$$
U_{F} = \sum_{j} f_j \cdot \tau_j \;\le\; 2.846\times10^{-3}
$$

$\tau_j$ is the mean time the error condition is present: from occurrence until the redundancy or function is restored.

### 8.4 Redundant architecture: link between Fehler and manual category

For the 2x2oo2 hot-hot architecture, with node failure rate $\lambda_{CN}$ and degraded window $\tau$:

$$
f_{\mathrm{deg}} = 2\lambda_{CN},
\qquad
f_{\mathrm{double}} \approx f_{\mathrm{deg}} \cdot \lambda_{CN}\,\tau = 2\lambda_{CN}^2\,\tau,
\qquad
U_{\mathrm{double}} \approx f_{\mathrm{double}} \cdot MDT_{\mathrm{service}}
$$

If the service is restored when the first of the two failed nodes is repaired and both are repaired independently, $MDT_{\mathrm{service}} = \tau/2$ and $U_{\mathrm{double}} \approx (\lambda_{CN}\,\tau)^2$.

**A longer degraded window $\tau$ increases both the Fehler unavailability and the risk of a manual service loss.**

### 8.5 Category register (Excel template)

| ID | Event / failure mode | Category | $f$ [1/h] | Source of $f$ | MDT or $\tau$ [h] | Source of MDT | $U = f \cdot MDT$ | Share of category budget |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | Loss of one CN, restartable | Fehler | TBD | SW / transient data | 0.167 | Proposed 600 s limit | | |
| E02 | Loss of one CN, permanent HW | Fehler | $1.694\times10^{-5}$ | S7 (2 CN x 2 CE) | 3.75 or 25 | Response policy (7.4) | | |
| E03 | Both CNs lost, independent HW | Manual | from 8.4 | S7 | 3.75 | Table 02_235 | | |
| E04 | Both CNs lost, common cause | Manual or 10 min | $\beta \lambda_{CN}$ | Beta to be justified | 3.75 or $\le$ 0.167 | Recovery mode | | |
| E05 | Application restart on all nodes (RCU, CC) | 2 min | TBD | SW reliability evidence | measured | Fault injection | | |
| E06 | Connection reboot after safety reaction | 2 min | TBD | SW / interface data | measured | Fault injection | | |
| E07 | Complete automatic VIL restart | 10 min | TBD | Power / platform / SW | measured (3 to 4 min stated) | Fault injection | | |
| E08 | Network single element lost | Fehler | from S7 | S7 | 12 (S7) | IPS maintenance | | |
| E09 | Network double failure / loss of synchronisation | Manual | from S7 | S7 | to be aligned | IPS maintenance | | |

## 9. Worked example (illustrative)

**Purpose:** show how the formulae are applied. **Not a prediction.** Only random hardware failures of the compute nodes are included.

### 9.1 Inputs

| Parameter | Value | Source |
| --- | --- | --- |
| MTBF of one CE (server) | 236,127.5 h | S7, cell C3 |
| $\lambda_{CE}$ | $4.235\times10^{-6}$ /h (4,235 FIT) | $1/MTBF$ |
| $\lambda_{CN}$, 2oo2 needs both CEs | $8.470\times10^{-6}$ /h (8,470 FIT); MTBF 118,064 h | $2\lambda_{CE}$ |
| $f_{\mathrm{deg}}$, one of two CNs lost | $1.694\times10^{-5}$ /h = 0.148 /year (one in 6.7 years) | $2\lambda_{CN}$ |
| $MDT_{\mathrm{service}}$ after double loss | 3.75 h | Table 02_235, manual |

Assumptions: constant failure rates; independent failures except where stated; the surviving CN carries operation without interruption.

### 9.2 Results

| Degraded window $\tau$ | $U_F$ | Share of Fehler budget | $f_{\mathrm{double}}$ [1/h] | $U_{\mathrm{man}}$ contribution | Share of manual budget |
| --- | ---: | ---: | ---: | ---: | ---: |
| 600 s (automatic reintegration) | $2.82\times10^{-6}$ | 0.10 % | $2.39\times10^{-11}$ | 0.003 s/y | 0.0004 % |
| 1 h (MRT, 02_196) | $1.69\times10^{-5}$ | 0.60 % | $1.43\times10^{-10}$ | 0.017 s/y | 0.003 % |
| 3.75 h (FK2, immediate response) | $6.35\times10^{-5}$ | 2.2 % | $5.38\times10^{-10}$ | 0.064 s/y | 0.010 % |
| 25 h (FK4, deferred, table) | $4.24\times10^{-4}$ | **14.9 %** | $3.59\times10^{-9}$ | 0.42 s/y | 0.064 % |

Common-cause sensitivity, **assumed** $\beta = 0.02$ (value used for geo-link / router CCF in the preliminary RAM workbook; not justified for the CNs):

$$
U_{\mathrm{CCF}} = \beta\,\lambda_{CN}\,MDT_{\mathrm{service}} = 0.02 \times 8.47\times10^{-6} \times 3.75 = 6.35\times10^{-7}
$$

That is **20 s/year, 3.0 % of the manual budget**, about 47 times the independent double failure with a 25 h window.

### 9.3 Interpretation

- Independent hardware double failures of the compute nodes use a negligible part of the manual budget, even with a 25 h degraded window.
- **Common cause dominates** the hardware contribution to the manual category.
- In the Fehler category, the **response policy** matters: CN hardware alone uses about 15 % of the budget with a 25 h window, but only 2 % with 3.75 h. Network, power, storage and software-induced node failures add to this.
- The 2-minute and 10-minute categories cannot be shown with hardware data. They need **software event frequencies** and **measured recovery times**.

### 9.4 Check of the existing calculation workbook (S7)

| Observation | Effect | Recommendation |
| --- | --- | --- |
| The hot-hot part uses $Q = 2\lambda^2 \cdot MTTR$ (cell B74) and calls it unavailability. This expression is a **frequency** [1/h] of double failures, not an unavailability | At MTTR = 1 h, the result is conservative by a factor of 2. With longer MTTR it is non-conservative: factor 1.9 at 3.75 h, factor 12.5 at 25 h | Use $U = f_{\mathrm{double}} \cdot MDT_{\mathrm{service}}$ or $(\lambda\tau)^2$ (section 8.4) |
| Cell C9 = 2·C8 and C13 = 2·C12 count the CE contribution of the "blue" path four times instead of twice | Small, conservative | Correct to 2·C5 |
| CE MTTR = 1 h, network MTTR = 12 h | Not aligned with the table (3.75 h, 25 h) | Align the MTTR assumptions with the response policy |

The workbook results (3.6 s/year) remain far below the budget. The corrections matter when the workbook is reused with the longer restoration times.

## 10. Permitted event frequency at the actual restoration time

If the real mean restoration is shorter than the table value, more events are allowed:

$$
f_{\mathrm{max}} = \frac{1 - A_{\mathrm{req}}}{A_{\mathrm{req}}} \cdot \frac{1}{MTTR_{\mathrm{actual}}}
$$

| Category | Actual mean restoration | Permitted events per year | Minimum mean time between events |
| --- | ---: | ---: | ---: |
| 2 min | 30 s | 4.2 | 0.24 y |
| 2 min | 60 s | 2.1 | 0.48 y |
| 2 min | 120 s | 1.05 | 0.95 y |
| 10 min | 240 s | 1.31 | 0.76 y |
| 10 min | 300 s | 1.05 | 0.95 y |
| 10 min | 600 s | 0.53 | 1.90 y |
| Manual | 1 h | 0.18 | 5.4 y |
| Manual | 2 h | 0.09 | 10.9 y |
| Manual | 3.75 h | 0.049 | 20.4 y |

**Use for design:** shorter recovery buys event frequency. A 60 s application restart permits about twice as many events as one of 120 s.

## 11. How to show fulfilment

### 11.1 Two stages

| Stage | Evidence | Method |
| --- | --- | --- |
| **Prediction** (design) | Category register (8.5), filled per event | HW: prediction per RAMP method, RBD / Markov. SW: allocation of a maximum event frequency per category from section 10; verified by test, field data and FRACAS. CCF: justified beta factor. Recovery times: fault injection with the agreed start and end points |
| **Demonstration** (operation) | Event log with timestamps and category per event | FRACAS: classify each event (section 4.3), sum the downtime per category and instance, compare with the budget |

### 11.2 Statistical limit

Without any event, the observation time needed to show $MTTF_{\mathrm{min}}$ at confidence $C$:

$$
T_{\mathrm{obs}} = -\ln(1 - C)\cdot MTTF_{\mathrm{min}}
$$

| Category | $MTTF_{\mathrm{min}}$ | $C = 60\,\%$ | $C = 90\,\%$ |
| --- | ---: | ---: | ---: |
| Manual (3.75 h) | 20.38 y | 18.7 instance-years | 46.9 instance-years |
| 10 min | 1.90 y | 1.7 instance-years | 4.4 instance-years |
| 2 min | 0.95 y | 0.9 instance-years | 2.2 instance-years |

Model: exponential, independent, identical instances. The automatic categories can be demonstrated with fleet data within a few years. **The manual category can only be shown by prediction**, supported by fleet data.

### 11.3 MRT

02_84 requires that the MRT is met for component exchange. Hitachi commits to checking this during hardware integration tests, "insbesondere 02_196 mit einer oberen Grenze von 1h für die MRT" (S5). The test should also cover 02_195 (0.5 h for a disturbance) and record the complete restoration time line, not only the repair work.

## 12. Findings and recommendations

| No. | Severity | Finding | Recommendation |
| --- | --- | --- | --- |
| F01 | High | EL4-DIL-SSS-REQ-00569 states "MTTR = 6 h". Table 02_235 and RAMP Table 9 give 3.75 h (225 min) | Correct REQ-00569 to "MTTR = 3.75 h (MRT = 0.5 h)" |
| F02 | High | MRT (02_195, 02_196) and MTTR are mixed in DPR and earlier notes | Use MTTR in all availability calculations; use MRT only for the maintainability demonstration (02_84) |
| F03 | High | The 3.75 h MTTR assumes 24/7 response with 3 h on site; FK3 and FK4 handling is limited to working days | Agree the mapping of FK1 to FK4 to the table categories and the response time per category |
| F04 | Medium | The customer's manual column does not strictly meet 0,999979 | Agree the acceptance level; demonstrate against the unrounded value ($MTTF \ge 20.38$ y at 3.75 h) |
| F05 | Medium | The MTTF values of the table are illustrations; the Gesamt column is not the sum of the categories | Treat the availability values as the only requirements; use $f_{\mathrm{max}}$ at the actual restoration time |
| F06 | Medium | 7.88 min/year are not allocated; automatic restoration longer than 600 s is not covered | Agree the counting rule and the use of the reserve |
| F07 | Medium | Loss of one redundancy partner may be FK2 (immediate) or FK4 (deferred, 25 h) | Agree the classification; it changes the Fehler budget use by a factor of about 7 |
| F08 | Medium | Workbook S7 uses $Q = 2\lambda^2 MTTR$ as unavailability | Correct the formula before reuse with 3.75 h or 25 h (section 9.4) |
| F09 | Low | RAMP Table 9 shows 99.9999 % for the 10-minute row (previously reported) | Correct to 99.999 % in the next RAMP edition |
| F10 | Medium | The verification field of REQ-00587, -00569, -00570 is empty | Define prediction and demonstration method per section 11 |

## 13. Open questions

| No. | Question | Why it matters | Addressee |
| --- | --- | --- | --- |
| Q1 | Is the image of table 02_235 the contractual version, and is a change request raised to correct REQ-00569 to 3.75 h? | Baseline for all calculations | Requirements management |
| Q2 | Where does MTTR start: at the failure, at detection, or at the notification of the service centre? What is the 0.25 h between 3.0 h response + 0.5 h MRT and 3.75 h? | Clock definition for measurement and FRACAS | Customer / Service |
| Q3 | Is the table (rounded) or the requirement value 0,999979 the acceptance level? | Strict compliance of the manual category | Customer |
| Q4 | How are events counted that are restored automatically after more than 10 minutes, and events below 2 minutes (only in the 2-minute category)? | Mutually exclusive categories | Customer |
| Q5 | Is loss of one 2oo2 partner without georedundancy FK2 or FK4? | Response time 3.75 h or 25 h | Customer |
| Q6 | What is the 24 h between MRT and MTTR in the Fehler column based on, and does it hold over weekends? | Fehler budget | Customer / Service |
| Q7 | Are network, IPS and data-centre failures inside the VIL-instance availability, or demonstrated in the DIL-CU class 1 requirements? | Scope of the category register | System / RAM |
| Q8 | Which software event frequency is targeted for the 2-minute and 10-minute categories, and what is the basis? | Only evidence route for the automatic categories | VIL design / RAM |
| Q9 | What observation period and fleet basis does the customer use for the demonstration (per instance, per year, fleet)? | Statistical demonstration (11.2) | Customer |

## 14. Applied skills and basis

Applied skills: [Railway-RAM](../../../../Skills/Railway-RAM.md), [RAM-Metrics](../../../../Skills/RAM-Metrics.md), [Reliability-Prediction](../../../../Skills/Reliability-Prediction.md), [REQ-Review](../../../../Skills/REQ-Review.md).

Repository information used: sources S1 to S8. All values in section 9 are taken from the repository workbook S7 or are explicitly marked as assumptions. No new failure rate is introduced. No standard clause numbers are claimed. All annual values assume continuous required service over a 365-day year (8,760 h).
