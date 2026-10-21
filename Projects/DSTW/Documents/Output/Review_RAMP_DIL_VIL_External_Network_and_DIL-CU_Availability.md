# Proposed RAM Review Responses — External Network and DIL-CU Availability

**Document reviewed:** [RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf)  
**Status:** Draft response for project review; confirm the current approved requirements baseline, architecture, and responsibility matrix before baselining.

## Executive summary

The RAM Plan describes the VIL scope and says that IPS and DFE are addressed in separate RAM Plans. It does not yet define how externally provided ÖBB communications networks are treated in the RAM demonstration, or how individual solution-element results will be combined to demonstrate a system-level target.

The SSS DIL RAM requirements identify the DIL-CU as comprising VIL, ADM, and IPS; IPS also provides server hardware and network components. DFE is addressed separately for field elements. Consequently, the DIL-CU demonstration and a wider operational end-to-end demonstration should be distinguished. Include DFE in the latter only where the requirement’s defined service boundary requires it.

No external-network availability figure, component allocation, network topology, or common-cause data is established by the RAM Plan reviewed. These must be obtained or agreed; they should not be replaced by an assumed perfect network or by unsupported numerical allocations.

## 1. General comment — external ÖBB communication networks

> “The availability dependency on external ÖBB communication networks is not defined. Please document the assumptions and boundary conditions used for RAM demonstration.”

### Proposed response to reviewer

**Agreed.** The RAM Plan will be clarified to identify the interfaces between the VIL/IPS solution and ÖBB-provided communications networks, and to state how these external dependencies are treated in each availability demonstration. Equipment and services outside the agreed supplier/system boundary will not be silently treated as 100% available or as having no effect.

The solution-element analysis will report the availability of the in-scope solution under its stated operating conditions. Where an external network is required for the assessed service, its availability and failure/recovery behaviour will be included in the end-to-end service model using ÖBB-provided evidence or a formally agreed assumption. If adequate network data is unavailable, the result will be explicitly conditional on network availability and will not be presented as an unconditional end-to-end operational availability demonstration.

### Proposed text for the RAM Plan

> **External communications networks and RAM boundaries**
>
> For each RAM analysis, the system boundary shall identify the supplier-provided equipment and the interfaces to externally provided communications networks, including the relevant ÖBB network segments and services. The applicable network paths and the functions dependent on them shall be identified from the approved system architecture and interface documentation.
>
> External networks outside the agreed supplier boundary are not included in the supplier equipment failure-rate calculation. They shall nevertheless be treated as dependencies in the availability assessment wherever loss or degradation of the network can prevent the assessed service from being delivered. The analysis shall state whether its result is (a) conditional availability of the in-scope solution assuming the external service meets an agreed availability/interface condition, or (b) end-to-end service availability including the external network.
>
> An end-to-end calculation shall use network availability, outage and restoration data supplied by the network owner or another project-approved source. If these data are not available, the assumption and its source shall be agreed with the relevant parties; the result shall be marked conditional and the data gap recorded. No external-network availability value shall be assumed to be 100% without an agreed and justified basis.
>
> The model shall document the service boundary, required network paths, operating and maintenance conditions, availability observation period, treatment of planned outages and service-impacting degradation, restoration assumptions, and any redundancy or common-cause assumptions. Redundant paths shall only be credited where the architecture and failure independence/common-cause assumptions are supported by evidence. Network-related operational events shall be distinguishable in the availability records from failures attributable to the VIL, IPS, or DFE.

### Boundary conditions to confirm and record

| Item | Required clarification / evidence |
| --- | --- |
| Network boundary | Named network segments, equipment, services, demarcation points, and responsible owner/operator; confirm these against the approved architecture and interface documents. |
| Service impact | Define when loss, delay, or degradation of communications makes the assessed railway function unavailable. Use approved interface and operational criteria; do not invent thresholds. |
| Availability input | ÖBB/network-owner availability and outage/restoration data, or a documented and approved assumption with source and validity period. |
| Resilience | Route/path topology, protection and switchover behaviour, shared equipment, and credible common-cause dependencies. Do not presume independent or redundant paths without evidence. |
| Measurement rules | Required operating period, denominator, planned-maintenance treatment, failure start/stop rules, restoration/reintegration, and attribution of service-affecting versus non-service-affecting events. |
| Demonstration status | Separate a conditional in-scope result from an end-to-end result that includes external-network performance; identify any open data or agreement needed to close the latter. |

## 2. General comment — DIL-CU availability and VIL/IPS/DFE contributions

> “The RAM Plan excludes IPS Solution and DFE from scope, while availability requirements for the complete DIL-CU have to be demonstrated. Please clarify how end-to-end availability figures will be derived and apportioned across VIL, IPS and DFE contributions.”

### Proposed response to reviewer

**Agreed.** The RAM Plan will state that separate RAM analyses for VIL, IPS, and DFE do not remove the need to demonstrate any applicable system-level availability requirement. The responsible solution-element owners will provide traceable availability inputs and assumptions for the system-level aggregation.

The applicable SSS DIL RAM specification describes the DIL-CU as comprising VIL, ADM, and IPS, and states that IPS provides server hardware and network components. It treats DFE/field elements separately. Therefore, the project should distinguish:

1. **DIL-CU availability:** aggregate the contributions that fall within the approved DIL-CU requirement boundary, including VIL, ADM, and IPS as defined by the requirement and architecture.
2. **Wider operational end-to-end availability:** include DFE and other required external services only where the requirement’s defined end-to-end service boundary includes them. Do not label this wider result as DIL-CU availability unless the applicable requirement baseline defines it that way.

The allocation will be derived from the approved system architecture and requirement definitions, using compatible availability measures and evidenced solution-element data. Numerical allocations cannot be set from the RAM Plan alone and remain subject to the approved dependability analysis and responsibility/interface agreements.

### Important target-consistency check

The referenced SSS DIL RAM specification lists a DIL-CU class 1 overall target of at least 0.99999 (99.999%) and a VIL-instance class 2 target of at least 0.99995 (99.995%). Confirm the exact requirement baselines and that the two figures use compatible service, outage-class, and measurement definitions.

If both figures are interpreted as the same availability measure over nested boundaries, with the DIL-CU service requiring the VIL service, then a DIL-CU target of 99.999% cannot be achieved when VIL availability is only required to be 99.995%: a series system cannot be more available than a required constituent. This is a consistency/definition issue to resolve, not a basis for inventing a different VIL target. Confirm whether the targets use different outage classes, service populations, or availability definitions, and document the agreed relationship and verification evidence.

For illustration only, assuming continuous required service for 365 days:

- 99.999% availability corresponds to approximately 5.26 minutes of unavailability per year.
- 99.995% availability corresponds to approximately 26.28 minutes of unavailability per year.

### Proposed text for the RAM Plan

> **System-level availability demonstration and allocation**
>
> The RAM analyses for VIL, IPS, and DFE shall be prepared within their respective approved technical and responsibility boundaries. Their separation into individual RAM Plans does not, by itself, demonstrate a system-level availability requirement. The responsible system RAM activity shall maintain traceability from each applicable system-level requirement to its defined service boundary, contributing solution elements, analysis/model, input data, assumptions, and verification evidence.
>
> For the DIL-CU requirement, the model boundary and included elements shall follow the applicable approved requirement baseline and system architecture. The cited SSS DIL RAM specification describes the DIL-CU as comprising VIL, ADM, and IPS; it describes DFE separately. DFE shall therefore be included in a wider end-to-end operational-service model only where that model’s approved requirement boundary includes the field elements and their interfaces. The DIL-CU and wider operational-service results shall be reported separately where their boundaries differ.
>
> For a service requiring all modelled elements in series, and only where their availability measures are compatible and failures are treated as independent, the model may calculate:
>
> `A_system = product(A_i)` and `U_system = 1 - A_system`
>
> where `A_i` is the availability of each required element and `U_system` is system unavailability. The model shall use the actual functional architecture: redundant paths and elements shall be represented using the relevant reliability block diagram/fault-tree logic, and common-cause failures, shared resources, switching/recovery behaviour, and dependencies shall be addressed. Independence shall not be assumed without justification.
>
> System-level availability targets shall be apportioned to contributing elements through an approved unavailability budget or other justified allocation method. The allocation shall be consistent with the requirement’s outage classes, system boundary, operating profile, restoration assumptions, and verification rules. A system-level result shall not be claimed by simply repeating the top-level target for each element or by combining figures based on incompatible definitions.
>
> The RAM Plan shall identify the owner of the system-level model and the input/evidence obligations of the VIL, IPS, ADM, DFE, and external-service owners as applicable. Missing data, unresolved boundaries, or unapproved allocations shall be recorded as open points and shall limit the claim made by the availability demonstration.

### Proposed allocation and evidence register

| Contribution | Treatment in demonstration | Required input/evidence | Boundary/status to confirm |
| --- | --- | --- | --- |
| VIL | Include in the DIL-CU model; use the VIL service boundary and its required interfaces. | VIL availability analysis, architecture/configuration, outage-class and restoration data, operational profile, dependencies, and assumptions. | Reconcile the VIL-instance target and outage definitions with the DIL-CU target. |
| IPS | Include in the DIL-CU model to the extent defined by the DIL-CU requirement and architecture; account for IPS platform, server, and network contributions once. | IPS RAM analysis, architecture, failure/repair and recovery data, redundancy/common-cause analysis, and interface assumptions. | Obtain from IPS owner; do not duplicate shared infrastructure in multiple model blocks. |
| ADM | Include where it is within the approved DIL-CU boundary. | ADM availability evidence and its dependencies/interfaces. | Confirm the required scope and owner; ADM is named in the cited SSS DIL DIL-CU composition. |
| DFE / field elements | Include in the wider operational end-to-end model when required by that service boundary; keep separate from DIL-CU-only results if outside its approved definition. | DFE RAM analysis, relevant field-element service availability, outage/restoration data, and VIL/IPS interface assumptions. | Confirm the requirement’s end-to-end boundary and the applicable FES/OC definitions. |
| ÖBB external networks/services | Treat as an external dependency where service operation relies on them; include in end-to-end calculations or report the result as conditional. | Network-owner data or approved assumption; topology, outages, restoration, and interface performance criteria. | Confirm network demarcation, data source, and customer/supplier responsibility. |
| Integration/system model | Integrate the above contributions once using the approved service architecture and availability definitions. | Traceable model, requirement mapping, allocation rationale, sensitivity/uncertainty, and verification plan. | Name the accountable system RAM owner and obtain stakeholder approval. |

## Assumptions and open points

- This response is based on the supplied RAM Plan, the repository copy of the SSS DIL RAM specification, and project availability analyses. It is a proposed clarification, not an approved RAM allocation or compliance demonstration.
- The RAM Plan says IPS and DFE are outside its scope and will be addressed in separate RAM Plans. It does not establish current supplier/customer responsibilities for external networks.
- The SSS DIL RAM specification used here is the repository file `SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed01.pdf`. Other project analyses cite a later Ed02PD01 baseline. Configuration management must confirm the controlling approved edition before the figures or requirement statuses are baselined.
- The network topology, ÖBB network availability data, precise operational availability rules, approved element allocations, and named system-level model owner were not established by the supplied RAM Plan.
- The mathematical relationship between the DIL-CU and VIL targets is a consistency check. It requires confirmation that the targets share the same service and outage definitions before drawing a compliance conclusion.

## Recommended actions

1. Confirm the controlling SSS DIL RAM requirement baseline and the required service boundaries for DIL-CU, VIL, FES/OC, and the wider operational function.
2. Agree network demarcation, network-owner data, interface performance criteria, outage accounting, and responsibility for external-network dependencies with ÖBB.
3. Identify the system-level availability model owner and obtain consistent VIL, IPS, ADM, DFE, and external-service evidence from the respective owners.
4. Resolve the DIL-CU/VIL target relationship and approve an allocation/unavailability budget before claiming end-to-end compliance.
5. Update the RAM Plan and linked RAM analyses with the approved boundaries, assumptions, model references, open points, and verification approach.

## Applied Skills

- `Railway-RAM` — project-specific system boundaries, RAM evidence, assumptions, and risk framing.
- `RAM-Metrics` — availability definitions, data sources, and system/element KPI interpretation.
- `REQ-Review` — requirement-boundary consistency, testability, and traceable clarification wording.

## Repository information used

- [Railway RAM skill](../../../../Skills/Railway-RAM.md)
- [RAM Metrics skill](../../../../Skills/RAM-Metrics.md)
- [Requirements Review skill](../../../../Skills/REQ-Review.md)
- [RAM Plan under review](../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf)
- [SSS DIL RAM specification, Ed01](../SSS_DIL_RAMS_3BU_17300_1257_DTAPA_Ed01.pdf)
- [Prior DIL RAM Plan review](./RAM_DIL_3BU_17300_1209_DUAPC%20-%20Review.md)
- [VIL availability requirements analysis](./VIL_Availability_Requirements_Allocation.md)
- [VIL availability explanation](./VIL_Availability_Explanation.md)
