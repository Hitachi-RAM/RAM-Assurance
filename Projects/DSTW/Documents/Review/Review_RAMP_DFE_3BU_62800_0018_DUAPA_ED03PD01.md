# Review – RAMP_DFE_3BU_62800_0018_DUAPA_ED03PD01

**Document under review:** [RAMP_DFE_3BU_62800_0018_DUAPA_ED03PD01.docx](./RAMP_DFE_3BU_62800_0018_DUAPA_ED03PD01.docx)  
**Scope of review:** Chapter 3, “Description of the system,” including the system overview, solution elements, DCA component versions, interface-converter cabinets, FES configuration and RAM Design Rules.  
**Conclusion:** The plan describes the principal Phase 1 DFE equipment, including DCA-based Field Element Stations (FES), FES M AzLM and IFC ZG62. However, the system overview lists IFC Sbl60 as utilized without identifying it as the Sbl60A converter planned for Phase 2 in the available SEMP. The Phase 1 boundary for the LCSI gateway also needs to be made clearer: Phase 1 includes supplier support and a prototype for initial tests, while integration into an FES is assigned to Phase 2. The DCA 3.x component list omits ICB-LS, which is included in the SEMP component breakdown, and the FES M maximum OC capacity is not stated. The statements are materially unchanged from the available Edition 02 RAM Plan; the Edition 03 change history records reference updates.

The proposed wording below is document-ready and describes the Phase 1 scope. Confirm any subsequent baseline changes before using it.

## Findings and recommended actions

| Topic | Finding | Recommended action |
| --- | --- | --- |
| 3.1 System scope and interface converters | The overview lists two converters, IFC ZG62 and “IFC Sbl60”, as utilized. The available SEMP defines IFC ZG62 1.0 as a Phase 1 deliverable and IFC Sbl60A as work contained in Phase 2. The RAM Plan’s section 3.4 lists only IFC ZG62 in the Phase 1 cabinet contents. The current overview therefore blends the overall EULYNX/product landscape with the Phase 1 scope and uses an incomplete converter designation. | Distinguish the Phase 1 RAM boundary from later-phase equipment. Identify ZG62 as the Phase 1 converter; mention Sbl60A only as a planned Phase 2 item unless the approved baseline has changed. |
| 3.2 Solution elements and LCSI gateway | Section 3.2 includes FES S IFC LCSI, says development starts in Phase 1 and finalization is in Phase 2, and notes supplier support. The SEMP further states that Phase 1 provides only a prototype for first tests; integration/qualification of the externally developed LCSI gateway and FES S IFC LCSI are Phase 2 work. | State explicitly that Phase 1 includes development support and a prototype for initial tests, not a fully integrated/qualified operational LCSI gateway. Retain FES S integration and qualification as Phase 2 scope. |
| 3.3 DCA 3.x component versions | The listed DCA-LS 3.1.0 components include ICB-O2 and ICB-IO but omit ICB-LS. The available SEMP lists both ICB-O2 and ICB-LS under DCA-LS 3.1.0, as well as ICB-IO. | Add the Interface Control Unit Light Signal (ICB-LS) under DCA-LS 3.1.0, subject to confirmation against the approved DCA configuration baseline. |
| 3.2 / 3.5 FES capacity | Section 3.2 says FES S supports up to two OCs and describes FES M only as having “extended capacity.” The SEMP gives capacities of up to two OCs for FES S and up to ten OCs for FES M. This sizing affects the defined station configurations and the RAM analysis boundary. | State both capacities explicitly and keep them consistent with the station configuration and the approved hardware baseline. |
| 3.6 RAM Design Rules | The section says RAM Design Rules “will be developed” and used as binding architectural conditions, while Section 3.6 already contains specific rule statements. It is unclear whether those rules are proposals or baselined design constraints. | Identify whether the listed rules are approved/baselined. Use “shall” for approved rules and describe unbaselined rules as proposed; map each approved rule to its applicable requirement(s). |

## Old and proposed wording

### 3.1 System Overview

| Old wording | Proposed wording |
| --- | --- |
| “As stated in [SP_DSTW], the EULYNX system definition defines following Object Controller (OC) level subsystems: Subsystem - Point; Subsystem - Light Signal; Subsystem - Generic I/O; Subsystem - Train Detection System (TDS); Subsystem - Level Crossing (LX). Additionally, two interface converters are utilized: IFC ZG62 (Blockconverter); IFC Sbl60 (Blockconverter).” | “The DFE Phase 1 scope comprises Field Element Stations (FES) for point, light-signal, generic-I/O and train-detection applications, together with the IFC ZG62 block interface converter. The Phase 1 scope also includes development support and a prototype of the Level Crossing System Interface (LCSI) gateway for initial tests; integration and qualification of the gateway in an FES are planned for Phase 2. The IFC Sbl60A is planned for Phase 2 and is not part of the Phase 1 equipment configuration.” |

### 3.2 Solution Elements

| Old wording | Proposed wording |
| --- | --- |
| “According to [IPP_DSTW], the Solution Element contains five work packages: (see also [SEMP_DFE])” followed by the IFC ZG62, FES M AzLM, FES S DCA, FES M DCA and FES S IFC LCSI descriptions. | “For Phase 1, the DFE Solution Element comprises the following work packages: IFC ZG62 hardware and software; FES S DCA; FES M DCA; FES M AzLM; and development support for the FES S LCSI gateway. The FES S LCSI work in Phase 1 includes support to the external supplier and a prototype for initial tests. Integration and qualification of the LCSI gateway in an FES are planned for Phase 2.” |
| “FES S DCA (FES S (up to 2 OC))” / “FES M DCA” / “Same as FES S DCA, with extended capacity” | “FES S DCA supports up to two Object Controllers (OCs). FES M DCA supports up to ten OCs.” |

### 3.3 DCA 3.x Component Versions

| Old wording | Proposed wording |
| --- | --- |
| “DCA-LS 3.1.0: Interface Control Unit Output – ICB-O2; Interface Control Unit Generic IO – ICB-IO” | “DCA-LS 3.1.0: Interface Control Unit Output – ICB-O2; Interface Control Unit Light Signal – ICB-LS; Interface Control Unit Generic IO – ICB-IO.” |

### 3.5 FES Configuration

| Old wording | Proposed wording |
| --- | --- |
| “Station Size S: Equipped exclusively with DCA 3.x units (LCSI Gateway in phase 2). Station Size M: Equipped with DCA 3.x units and AzLM units for TDS. Interface Converters (ZG62): Equipped with SCA and DCA 2.x for communication with neighboring interlockings.” | “In Phase 1, Station Size S is equipped with DCA 3.x Object Controllers and supports up to two OCs. The LCSI gateway is not integrated into the FES in this phase; Phase 1 provides a prototype for initial tests, with FES integration planned for Phase 2. Station Size M is equipped with DCA 3.x Object Controllers and AzLM units for train detection and supports up to ten OCs. The IFC ZG62 cabinet contains the SCA computing board, DCA 2.x IOC and relay group for communication with neighbouring interlockings. IFC Sbl60A is planned for Phase 2.” |

### 3.6 RAM Design Rules

| Old wording | Proposed wording |
| --- | --- |
| “In order to ensure that the availability requirements (stated in section 6.2) are met, a series of rules, the so-called ‘RAM Design Rules’, will be developed and used as binding conditions for architectural design decisions. Note that each of these RAM Design Rules will also be explicitly mapped to one or more specific system requirement(s), ensuring traceability and compliance throughout the development lifecycle.” | “The RAM Design Rules listed in this section define the DFE design constraints applicable to the RAM assessment. Each baselined rule shall be traced to the applicable system requirement(s). Any rule not yet baselined shall be identified as proposed and shall not be treated as an approved design constraint.” |

## Sources reviewed

- [SEMP_DFE_3BU_62800_0000_DPAPA_Ed02.docx](../SEMP_DFE_3BU_62800_0000_DPAPA_Ed02.docx) – Phase 1 scope, station configurations and component versions; identifies IFC ZG62 and the LCSI gateway prototype in Phase 1, and IFC Sbl60A and LCSI integration in Phase 2.
- [SafetyConcept_DFE_3BU_62800_1001_DUAPC_Ed01_Pd01_Work.docx](../SafetyConcept_DFE_3BU_62800_1001_DUAPC_Ed01_Pd01_Work.docx) – broader DFE architecture and subsystems, including FES sizes S, M and L-XXL; block-interface converters ZG62 and Sbl60A; LCSI interfaces; DCA3 and AzLM OCs.
- [SSS_Field_Element_Controller_and_Stations_3BU_17300_1256_DTAPA_Ed02PD01.docx](../SSS_Field_Element_Controller_and_Stations_3BU_17300_1256_DTAPA_Ed02PD01.docx) – DFE field-element requirements specification referenced for the subsystem and controller architecture.
- [RAMP_DFE_3BU_62800_0018_DUAPA_Ed02.pdf](../RAMP_DFE_3BU_62800_0018_DUAPA_Ed02.pdf) – previous available RAM Plan edition; the Chapter 3 scope and component-list statements are materially the same as in the reviewed edition.

## Limitations and open confirmations

1. The SEMP is the source used here for the Phase 1/Phase 2 allocation. Confirm against the approved project configuration baseline before release.
2. The SEMP lists DCA-LS ICB-LS under the DCA-LS 3.1.0 component set. Confirm the exact ICB configuration against the released DCA BOM and product baseline.
3. The Safety Concept describes a broader DFE architecture than this Phase 1 RAM Plan. The proposed text deliberately distinguishes the overall architecture from the equipment and integration scope addressed by this Phase 1 plan.
