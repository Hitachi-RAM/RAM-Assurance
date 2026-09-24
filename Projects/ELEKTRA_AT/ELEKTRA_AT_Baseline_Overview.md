# ELEKTRA_AT Baseline Overview

## Purpose

This document summarises the ELEKTRA ÖBB baseline sequence and its relationship to the generic ELEKTRA product baselines. The OBB baseline is used as the primary column because it represents the customer-specific release scope.

## OBB Baselines

| OBB baseline | Related PV GEN baseline | Main RAM-relevant scope |
|---|---|---|
| **OBB 24.00** | Not stated | Initial ÖBB feature baseline. |
| **OBB 24.10** | Not stated | Feature additions and updates. |
| **OBB 25.00** | Not stated | EBO2 and operational-function changes. |
| **OBB 25.10** | Not stated | Features transferred from later development scope. |
| **OBB 26.00** | Not stated | Multiple power supplies, EC/CEC changes, X25-BFZ and D6 functions. |
| **OBB 27.00** | Not stated | ETCS-L2, SEA, additional EC functions and redundant LAN arrangements. |
| **OBB 27.10** | **PV GEN 2.15.2** | X25 routing, new PCs/operating systems, MOVUS and EC/CC changes. |
| **OBB 27.20** | Not stated | Additional ETCS, SEA, CEC and EKSA functions. |
| **OBB 28.00** | Not stated | Ethernet interfaces, EC expansion and additional ETCS functions. |
| **OBB 28.01** | Not stated | EBO2 and SEA enhancements. |
| **OBB 28.02** | Not stated | EBO2 display and operational changes. |
| **OBB 28.10** | **PV GEN 2.16.2** | X25 over TCP/IP, SEA extensions, EC expansion and draft non-redundant EC concept. |
| **OBB 28.30** | **PV GEN 2.19.0** | ÖBB-specific GenSys baseline with later feature updates. |
| **OBB 29.10** | Not stated | SSÜ redundant acquisition and related logic changes. |
| **OBB 29.20** | Not stated | Siemens BFZ georedundancy and SCWS/OIE adaptations. |
| **OBB 29.40** | **PV GEN 2.19.10** | Previous complete ÖBB product baseline and comparison baseline. |
| **OBB 29.50** | **PV GEN 2.20.10** | Current target baseline; TAS PLF 2.6, OCS-SBJ 3.6.1, updated diagnostics, security and interfaces. |
| **OBB 30.00** | Not stated | Later destination for selected functions, including SSÜ-related changes. |
| **OBBxx.yy** | Not applicable | Placeholder for features not yet assigned to a released ÖBB baseline. |

## Baseline Chain

```text
OBB 24.00
   |
OBB 25.00
   |
OBB 26.00
   |
OBB 27.00 / 27.10 / 27.20
   |
OBB 28.00 / 28.01 / 28.02 / 28.10
   |
OBB 28.30
   |
OBB 29.10 / 29.20
   |
OBB 29.40 + PV GEN 2.19.10
   |
OBB 29.50 + PV GEN 2.20.10
```

## Current Release Comparison

| Item | Previous release | Current release |
|---|---|---|
| OBB release baseline | **OBB 29.40** | **OBB 29.50** |
| Generic ELEKTRA software | PV GEN **2.19.10** | PV GEN **2.20.10** |
| ÖBB product version | PV OBB **2.15.0** | PV OBB **2.16.0** |
| TAS Platform | **2.4.2** | **2.6.0** |
| OCS-SBJ | **1.2** | **3.6.1** |
| SEA software | **2.1.2** | **2.2.0** |
| SEC software | **2.2.4** | **2.2.5** |
| SEC hardware | **2.2.3** | **2.3.0** |
| EBO2 | **01.99.0** | **02.00.0** |

## Meaning of the Baselines

- **PV GEN** is the generic ELEKTRA product baseline used as the technical foundation.
- **OBB baseline** is the customer-specific ÖBB feature and release baseline.
- **PV OBB** is the resulting ÖBB product version delivered for the customer.

The current product relationship is:

```text
PV GEN 2.20.10
        +
OBB-specific features and configuration from OBB 29.50
        =
PV OBB 2.16.0
        =
OBB 29.50
```

## RAM Assessment Baseline

The RAM assessment should use the complete configuration **PV OBB 2.16.0 / OBB 29.50**, rather than PV GEN 2.20.10 alone. The assessment should cover:

- reliability prediction for the actual hardware and software configuration;
- availability analysis including ECs, redundancy, LAN, TAS Platform and OCS-SBJ;
- maintainability and MTTR for the actual ÖBB equipment and maintenance concept;
- FMEA and failure propagation for the differences between OBB 29.40 and OBB 29.50; and
- verification evidence for the PV GEN and ÖBB-specific changes.

## Main Sources

- [Project-specific RAM Plan](3BU_15000_2446_DUAPA.docx)
- [System Specification, Edition 40](SSS_3BU_15000_0300_DTAPA_Ed40.docx)
- [Statement of Changes](SoC_3BU_15000_2453_QEAPA.docx)
- [ÖBB Feature List, Edition 43](FL_EL_OBB_3BU_15000_4301_FLAPC_Ed43.docx)
