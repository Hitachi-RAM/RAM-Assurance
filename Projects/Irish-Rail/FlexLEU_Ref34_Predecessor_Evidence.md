# FlexLEU Ref34 - Predecessor Evidence Strategy

**Project:** Irish Rail TPS Trackside NRO ETCS  
**Product:** FlexLEU  
**Reference:** Ref34 - cross-acceptance field data for reused products  
**Status:** Engineering position for RAM/tender evidence

## 1. Executive Position

FlexLEU is a new product and therefore has no direct FlexLEU field-service history or demonstrated in-service MTBF at this stage.

The Legacy LEU, as the predecessor product, may provide supporting reliability evidence. However, Legacy LEU data shall not be presented as measured FlexLEU performance. Transfer of evidence requires a documented predecessor-to-FlexLEU similarity assessment, supported by design analysis, verification testing and planned in-service monitoring.

The evidence status for FlexLEU should therefore be stated as:

> **Predecessor-supported and prediction-supported; direct FlexLEU field demonstration pending.**

## 2. Evidence Classification

| Evidence category | FlexLEU status | Permitted use |
| --- | --- | --- |
| Direct FlexLEU field data | Not available because FlexLEU is new | Cannot demonstrate observed FlexLEU MTBF |
| Legacy LEU field data | Available as predecessor evidence | Establish heritage reliability baseline and identify failure mechanisms |
| FlexLEU reliability prediction | Available or to be completed for the defined configuration | Support design-stage reliability assessment and spares calculations |
| Similarity/heritage assessment | Required | Justify which Legacy LEU evidence is applicable to FlexLEU |
| FlexLEU verification testing | Required according to the changes and risks | Demonstrate performance of new or modified design features |
| FlexLEU in-service monitoring | Future activity | Confirm actual reliability after deployment and support Cert A evidence |

## 3. Ref34 Interpretation

Ref34 should be addressed through a Product Service History Dossier for the reused or heritage elements. For FlexLEU, the dossier should combine:

- Legacy LEU service history;
- a controlled comparison of Legacy LEU and FlexLEU;
- FlexLEU design-specific reliability prediction;
- verification and environmental test evidence;
- change-related risk assessment; and
- a plan for FlexLEU in-service monitoring and FRACAS.

Ref34 is therefore not satisfied by quoting a Legacy LEU MTBF alone. It is satisfied by showing why the predecessor evidence remains applicable, where it does not apply, and how the new FlexLEU design will be verified and monitored.

## 4. Required Predecessor-to-FlexLEU Assessment

The comparison should cover, at minimum:

- functional architecture;
- hardware design and critical components;
- software and firmware;
- interfaces and communications;
- power supply and thermal design;
- environmental rating and railway installation conditions;
- operating duty cycle;
- maintenance concept;
- failure detection and diagnostics;
- manufacturing and quality controls; and
- known failure modes and mechanisms.

Each difference should be classified as:

1. no expected effect on reliability;
2. potentially beneficial;
3. potentially adverse; or
4. requiring verification or additional evidence.

The assessment should identify separately:

- unchanged inherited assemblies;
- modified assemblies;
- new assemblies;
- changed interfaces;
- changed environmental or duty-cycle conditions; and
- failure modes introduced by the FlexLEU design.

Legacy LEU data may be used directly only for elements for which the configuration, application, stress profile and failure mechanisms are sufficiently comparable. New or materially modified elements require their own prediction, test or field evidence.

## 5. Legacy LEU Data Requirements

The Legacy LEU service-history dataset should provide, for each product variant and application:

- product identification and hardware/software revision;
- installed population;
- project and country of deployment;
- installation and commissioning dates;
- observation start and end dates;
- accumulated operating hours;
- number of failures by severity;
- number of replacements;
- number of repairable and irreparable units;
- failure modes and confirmed causes;
- no-fault-found cases;
- environmental and duty-cycle conditions;
- maintenance and inspection regime;
- corrective actions and implementation dates;
- recurrence and corrective-action effectiveness; and
- configuration differences relevant to FlexLEU.

### Available Slovenian Corridor D field data

The input folder contains the companion RAM repair report and calculation workbook for ETCS Level 1 on Slovenia Corridor D: `3BU 82800 5001 DUAP_RAM_ Report_ETCS_L1_Slovenia_P1P2_Ed02.docx` and `3BU 82800 5001 DUAP_RAM_Report_ETCS_L1_Slovenia_P1P2_Ed02.xlsx`. The report is Edition 02 and assesses reported 2015 repairs and field diagnoses for LEU PV 3.5 variants across sections P1, P2 and S1-S5.

The report states a population of 1,174 installed LEUs and total exposure of 10,284,240 LEU operating hours. The LEU component repair records used here comprise 24 PICCG2 repairs and 9 PDU repairs. On the report's stated Ground Fixed 40 °C outdoor basis, empirical MTBF is 58.4 years for PICCG2 versus a calculated 29.9 years, and 130.4 years for PDU versus a calculated 119.4 years. Accordingly, the empirical MTBF is higher than the calculated MTBF by a factor of 1.95 for PICCG2 and by a factor of 1.09 for PDU. These are component-level estimates for the Slovenian installed population and calculation assumptions; they are not a demonstrated MTBF for a complete LEU, Irish Rail equipment, or FlexLEU.

For this Irish Rail bid, the relevant diagnostic categories are limited to the remaining LEU-related entries in the report: 42 sync-time expirations, 8 CAN-bus events, 4 "Failure occurred" diagnostics, 2 error shutdowns and 1 Aspect 127 event (57 diagnostic events in total). These are diagnostic records, not necessarily confirmed hardware failures; use them to guide the predecessor applicability assessment and verification focus, subject to event-level review.

### Point-by-point fulfilment assessment

The following replies assess only what is evidenced in the Slovenia RAM repair report and workbook. **Not reported** means the reviewed report does not provide the information; it does not establish that the project records never existed.

| Legacy LEU data requirement | Status | Exact response for the Irish Rail bid |
| --- | --- | --- |
| Product identification and hardware/software revision | Partial | The report identifies LEU PV 3.5 variants (vP1S1, vP2S1, vP1R1, vP2R1 and vP1) and component identifiers. A deployed software/firmware revision for each unit is not reported. |
| Installed population | Available | The report identifies 1,174 installed LEUs, broken down by variant and Corridor D section. |
| Project and country of deployment | Available | The data relate to ETCS Level 1 on Corridor D, Slovenia, covering sections P1, P2 and S1-S5. |
| Installation and commissioning dates | Not reported | The report does not provide unit-level installation or commissioning dates. Its reference to a one-year RAM test from commissioning describes a requirement, not actual unit dates. |
| Observation start and end dates | Partial | Repairs and diagnoses are assessed for 2015, but exact observation start/end dates and unit-level exposure intervals are not stated. |
| Accumulated operating hours | Available | The report states total LEU exposure of 10,284,240 operating hours. The underlying exposure allocation by individual unit is not provided in the report. |
| Number of failures by severity | Partial | The report lists 24 PICCG2 and 9 PDU repair records and identifies 33 permanent hardware failures overall for those components. It does not provide a complete, project-defined severity classification for each confirmed failure. The 57 remaining diagnostic events are event records, not 57 confirmed failures. |
| Number of replacements | Not reported | The report records repairs, but does not separately identify how many units or components were replaced. |
| Repairable and irreparable units | Not reported | The report does not distinguish the population into repairable and irreparable units. |
| Failure modes and confirmed causes | Partial | Diagnostic categories are reported (42 sync-time expirations, 8 CAN-bus events, 4 "Failure occurred" diagnostics, 2 error shutdowns and 1 Aspect 127 event). Confirmed root cause and failure-mode attribution are not provided for every event. |
| No-fault-found cases | Not reported | No no-fault-found count or disposition is stated. |
| Environmental and duty-cycle conditions | Partial | The empirical/calculated comparison is stated on a Ground Fixed 40 °C outdoor basis. Actual unit-level site conditions, duty cycle and stress history are not documented. |
| Maintenance and inspection regime | Partial | The report analyses 2015 repairs/diagnoses and aggregate downtime; it does not define the full preventive-maintenance or inspection regime, nor case-level maintenance records. |
| Corrective actions and implementation dates | Not reported | The report does not provide a traceable list of component corrective actions with implementation dates. |
| Recurrence and corrective-action effectiveness | Not reported | The report does not link recurring events to corrective actions or report effectiveness verification. |
| Configuration differences relevant to FlexLEU | Not reported | The Slovenia report does not compare its LEU PV 3.5 configuration with FlexLEU. A separate, controlled similarity and change assessment is required. |

Accordingly, the Slovenia report supports a limited heritage argument for the identified LEU components and provides useful population, exposure, repair and diagnostic evidence. It does not by itself fulfil the complete service-history data set above or demonstrate FlexLEU/Irish Rail MTBF. Obtain the underlying service records and complete the FlexLEU similarity assessment before claiming transferability.

Use these files as historical service-history evidence and as input to the failure-mechanism and diagnostics review. Before calculating or claiming an Irish Rail value, obtain the traceable underlying maintenance records and confirm variant-level exposure, event definitions, failure attribution, configuration, operating/environmental profile and maintenance context. The report's age and Slovenian ETCS L1 application limit its direct transferability.

The MTBF calculation shall use a controlled definition:

$$
MTBF_{observed} = \frac{\text{total accumulated operating hours}}{\text{relevant failure events}}
$$

The denominator shall be stated explicitly. Separate values may be required for:

- all confirmed functional failures;
- service-affecting failures;
- immobilising failures;
- irreparable units; and
- failures attributable to the product rather than installation, maintenance or external causes.

## 6. Ref34 Requested Information - Point-by-Point Response

The following reproduces the requested information points and answers each using the Slovenia RAM report. The report covers 2015 evidence; it does not establish current or Irish Rail in-service status.

▪ **Number of product in-service**

**Answer:** The report records 1,174 installed LEU PV 3.5 units across Corridor D sections P1, P2 and S1-S5. This is the report's installed-base figure, not confirmation that all 1,174 units remain in service today (RAM Report, Section 3, Table 5).

▪ **In-service demonstrated MTBF**

**Answer:** The report gives empirical component MTBF estimates, not a demonstrated MTBF for the complete LEU product: PICCG2 is 58.4 years based on 24 repairs, and PDU is 130.4 years based on 9 repairs. On the report's Ground Fixed 40 °C outdoor comparison basis, these empirical MTBFs are higher than the calculated values by factors of 1.95 and 1.09, respectively. The report does not state a single field-demonstrated MTBF for the complete LEU (RAM Report, Section 4, Table 11).

▪ **Number of failures reported to date,**

**Answer:** Within the report's 2015 repair dataset, 33 permanent hardware failures are identified for the LEU components considered here: 24 PICCG2 and 9 PDU. This is the count reported in that historical dataset, not a cumulative count to the present date (RAM Report, Section 4, Table 10; Section 5).

▪ **Severity of the failures reported to date**

**Answer:** The report classifies the 33 PICCG2/PDU hardware failures as permanent hardware failures. It does not provide a further per-failure severity grade or a full severity breakdown specifically for these component failures (RAM Report, Section 5).

▪ **The number of product replacements made to date**

**Answer:** Not reported. The report lists repair counts but does not state how many complete LEUs or individual components were replaced. The replacement count cannot be inferred from the repair count.

▪ **The corrective actions that have been taken to address the defaults**

**Answer:** Not reported for the PICCG2 and PDU failures. The report does not identify implemented corrective actions, implementation dates, or effectiveness evidence for these component failures. The underlying service/FRACAS records are needed to answer this point.

## 7. FlexLEU Reliability Prediction

FlexLEU predicted MTBF shall remain clearly separated from Legacy LEU observed MTBF. The prediction report should identify:

- calculation methodology;
- product and model boundary;
- environmental profile;
- mission and duty-cycle assumptions;
- component quality level;
- temperature and stress assumptions;
- derating assumptions;
- failure-rate source data;
- FIT and failure-rate results;
- MTBF calculation;
- dominant contributors; and
- sensitivity and uncertainty.

Predicted MTBF supports design decisions and spares provisioning. It is not a substitute for direct FlexLEU field demonstration.

## 8. Verification and In-Service Demonstration

For new or modified FlexLEU features, the evidence plan should include proportionate:

- design review;
- hardware and software verification;
- environmental testing;
- EMC and mechanical robustness testing;
- interface and integration testing;
- diagnostic and failure-detection testing;
- failure-injection or fault-response testing where appropriate; and
- configuration and manufacturing-quality controls.

After deployment, FlexLEU reliability should be monitored through the common FRACAS process. Monitoring should capture failure date, operating exposure, failure mode, service impact, detection method, root cause, replacement, corrective action and recurrence.

The Ref313 in-service monitoring period from APIS 5/Cert B to Cert A is the appropriate mechanism for collecting the first direct FlexLEU operational evidence. The Reliability Growth Model and acceptance method should be agreed with the Project Manager before the Cert A demonstration.

## 9. Recommended Tender Wording

> Direct in-service MTBF data for FlexLEU is not yet available because FlexLEU is a new product. Reliability evidence is therefore based on a combination of Legacy LEU service history, a documented predecessor-to-FlexLEU similarity assessment, design-specific reliability prediction, verification testing and planned in-service monitoring. Legacy LEU data is treated as supporting heritage evidence and not as direct demonstrated FlexLEU MTBF. Direct FlexLEU field performance will be recorded through the project FRACAS and in-service reliability monitoring process following deployment.
>
> The Legacy LEU service-history dossier includes the RAM repair report and calculation workbook for ETCS Level 1 on Slovenia Corridor D (3BU 82800 5001 DUAP_RAM_ Report_ETCS_L1_Slovenia_P1P2_Ed02, Edition 02). The report assesses the 2015 field history of LEU PV 3.5 variants, covering 1,174 installed LEUs and 10,284,240 reported LEU operating hours. It reports empirical component MTBF estimates of 58.4 years for PICCG2, based on 24 repairs, and 130.4 years for PDU, based on 9 repairs, compared with calculated values of 29.9 and 119.4 years respectively. The empirical MTBF is higher than the calculated MTBF by a factor of 1.95 for PICCG2 and by a factor of 1.09 for PDU, respectively. These historical component-level comparisons are presented as predecessor evidence only; they are not whole-system MTBF, Irish Rail performance, or measured FlexLEU MTBF.
>
> For the Irish Rail bid, the relevant diagnostic categories considered are 42 sync-time expirations, 8 CAN-bus events, 4 "Failure occurred" diagnostics, 2 error shutdowns and 1 Aspect 127 event (57 records in total). These are diagnostic records, not automatically confirmed equipment failures. Applicability to FlexLEU will be limited to elements shown by the similarity assessment to have comparable configuration, application, interfaces, stresses, environment, maintenance and failure mechanisms. FlexLEU-specific changes will be addressed by design-specific prediction and verification. Direct FlexLEU performance and Irish Rail acceptance will be established through the Irish Rail project FRACAS and the required in-service monitoring and reliability-growth demonstration. Slovenian RAM targets and acceptance results are not claimed as Irish Rail compliance evidence.

## 10. RAM Risks and Limitations

| Risk or limitation | RAM impact | Required control |
| --- | --- | --- |
| Legacy LEU MTBF transferred without a similarity case | FlexLEU reliability claim may be unsupported | Controlled predecessor-to-FlexLEU comparison and applicability matrix |
| New or modified failure mechanisms not covered by Legacy LEU data | Missing contributors in the reliability assessment | Change-specific FMEA/FMECA, prediction and verification testing |
| Different environmental or duty-cycle conditions | Field MTBF may not represent Irish Rail operation | Demonstrate stress and mission-profile comparability |
| Mixed product variants or configurations | MTBF estimate may be statistically or technically invalid | Separate datasets by part number, revision and application |
| Small or incomplete failure dataset | High confidence uncertainty | Report exposure, failure definitions and confidence bounds |
| Predicted and observed values combined | Results become non-traceable | Maintain separate predicted, observed and demonstrated metrics |
| No direct FlexLEU field history | Ref34 evidence remains provisional before deployment | State direct demonstration as pending and define the monitoring plan |

## 11. Overall Assessment

FlexLEU can be supported for tender and cross-acceptance purposes using Legacy LEU evidence, but only as a **heritage and predecessor argument**. The evidence must be bounded by a similarity assessment and supplemented by FlexLEU-specific prediction, verification and in-service monitoring.

The technically defensible claim is not that FlexLEU already has the Legacy LEU MTBF. The defensible claim is that Legacy LEU service data provides relevant reliability evidence for comparable inherited elements, while FlexLEU-specific changes are controlled through analysis, testing and subsequent field monitoring.
