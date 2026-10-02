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

## 6. FlexLEU Reliability Prediction

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

## 7. Verification and In-Service Demonstration

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

## 8. Recommended Tender Wording

> Direct in-service MTBF data for FlexLEU is not yet available because FlexLEU is a new product. Reliability evidence is therefore based on a combination of Legacy LEU service history, a documented predecessor-to-FlexLEU similarity assessment, design-specific reliability prediction, verification testing and planned in-service monitoring. Legacy LEU data is treated as supporting heritage evidence and not as direct demonstrated FlexLEU MTBF. Direct FlexLEU field performance will be recorded through the project FRACAS and in-service reliability monitoring process following deployment.

## 9. RAM Risks and Limitations

| Risk or limitation | RAM impact | Required control |
| --- | --- | --- |
| Legacy LEU MTBF transferred without a similarity case | FlexLEU reliability claim may be unsupported | Controlled predecessor-to-FlexLEU comparison and applicability matrix |
| New or modified failure mechanisms not covered by Legacy LEU data | Missing contributors in the reliability assessment | Change-specific FMEA/FMECA, prediction and verification testing |
| Different environmental or duty-cycle conditions | Field MTBF may not represent Irish Rail operation | Demonstrate stress and mission-profile comparability |
| Mixed product variants or configurations | MTBF estimate may be statistically or technically invalid | Separate datasets by part number, revision and application |
| Small or incomplete failure dataset | High confidence uncertainty | Report exposure, failure definitions and confidence bounds |
| Predicted and observed values combined | Results become non-traceable | Maintain separate predicted, observed and demonstrated metrics |
| No direct FlexLEU field history | Ref34 evidence remains provisional before deployment | State direct demonstration as pending and define the monitoring plan |

## 10. Overall Assessment

FlexLEU can be supported for tender and cross-acceptance purposes using Legacy LEU evidence, but only as a **heritage and predecessor argument**. The evidence must be bounded by a similarity assessment and supplemented by FlexLEU-specific prediction, verification and in-service monitoring.

The technically defensible claim is not that FlexLEU already has the Legacy LEU MTBF. The defensible claim is that Legacy LEU service data provides relevant reliability evidence for comparable inherited elements, while FlexLEU-specific changes are controlled through analysis, testing and subsequent field monitoring.
