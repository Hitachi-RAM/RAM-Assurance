# VIL Availability Requirements — Explanation and Suggestions

This note summarizes the VIL availability requirements found in the RAM-Assurance repository and explains how they should be interpreted.

## Scope

The key source document is:

- `Projects/DSTW/Documents/Output/VIL_Availability_Requirements_Allocation.md`

That document analyses chapter **3.1.4.3.2 “VIL Availability”** and allocates the requirements to software components. Its main message is that the **numeric availability targets belong to the VIL instance**, not to each component individually.

## Main interpretation

The availability requirements are best understood as **service-level requirements**:

- the VIL service must remain available as a whole
- component allocations describe **which parts contribute to that availability**
- availability values should **not** simply be copied to each SW component
- the model must account for dependencies, recovery, and shared failure modes

## The six VIL availability requirements

The source document states that chapter 3.1.4.3.2 contains **six active requirements**.

### 1. EL4-DIL-SSS-REQ-00587 — Overall VIL availability

- **Text:** The VIL instance shall have **class 2 overall availability of at least 99.995%**.
- **Meaning:** This is the top-level availability target for the full VIL service.
- **Value:** `A >= 0.99995`

### 2. EL4-DIL-SSS-REQ-00569 — Availability distribution of the VIL instance

- **Text:** The availability of a VIL instance must correspond to class 2.
- The requirement gives example restoration-time cases:
  - **99.9979%** for **MTTR = 6 h**
  - **99.999%** for **MTTR = 10 min**
  - **99.9996%** for **MTTR = 2 min**
- **Meaning:** Availability is strongly dependent on the assumed restoration time.
- **Note:** The repository warns that source documents use different restoration assumptions, so the timing basis must be aligned before any compliance argument is made.

### 3. EL4-DIL-SSS-REQ-00570 — Outages with no operational impact

- **Text:** Outages of a VIL instance with no operational impact shall have an availability of at least **99.7154%**.
- **Meaning:** This appears to cover less severe outage classes, likely corresponding to FK4.
- **Value:** `A >= 0.997154`

### 4. EL4-DIL-SSS-REQ-00573 — Minor SW/HW changes

- **Text:** Minor changes of VIL software or hardware shall be carried out **without operational restrictions**.
- **Meaning:** Patches and small hardware changes must not interrupt service.
- **Implication:** This is a lifecycle and maintainability requirement, not just a reliability number.

### 5. EL4-DIL-SSS-REQ-00574 — Operational downtime

- **Text:** Operational downtime must be handled within the availability design.
- **Meaning:** Downtime is a service-level issue involving operations, update coordination, and dependent components.

### 6. EL4-DIL-SSS-REQ-00818 — later-release availability-related requirement

- **Meaning:** This requirement is tied to later release / lifecycle behavior rather than only to the base runtime.
- The repository allocates it to lifecycle and CDS/NMR/J4S behavior.

## Recommended modeling approach

The repository recommends modelling availability as a **service-loss problem**, not a simple per-component percentage split.

### Suggested model types

- **Union-of-events model**
  - Example concept:
    - service is unavailable if Core service is lost, ECMUX service is lost, a required interface is lost, or a shared dependency is lost

- **Fault tree or state model**
  - Should include:
    - redundant states
    - degraded states
    - service-lost and restarting states
    - maintenance states
    - partition and authorization effects
    - exposure to a second failure while recovering

- **Conservative budget model**
  - Can be used if a strict upper-bound argument is desired
  - This is useful when exact dependency data is not available yet

### Models that should be used carefully

- **Series product model**
  - Appropriate only for mutually independent series blocks
  - Not a substitute for the full common-cause model

- **1oo2 squared-unavailability illustration**
  - Useful as an example only
  - Not sufficient for the actual VIL availability argument

## Component allocation meaning

The allocation tables in the source document assign responsibilities to components such as:

- CC
- RCU
- DGP
- CAR-RED
- NMR
- CDS
- ECMUX
- J4S
- RaSTA
- lifecycle and update coordination

This does **not** mean each component receives the full availability target.

Instead:

- some components are marked **Lead**
- others are **Supporting**
- some are **Not allocated**

The goal is to define the function each component contributes to the VIL service and how it supports the overall availability target.

## Practical suggestions

### 1. Treat 99.995% as the master service target

Use EL4-DIL-SSS-REQ-00587 as the top-level requirement for the entire VIL service.

### 2. Use restoration time as a key sensitivity factor

EL4-DIL-SSS-REQ-00569 shows that availability depends heavily on restoration time. Before using any numeric argument, confirm:

- whether MTTR is manual or automatic
- whether it is elapsed downtime or active repair time
- which source document is authoritative for the recovery scenario

### 3. Treat change and downtime requirements as lifecycle obligations

EL4-DIL-SSS-REQ-00573 and EL4-DIL-SSS-REQ-00574 imply that:

- patching must be service-safe
- operational downtime must be controlled
- update and reintegration workflows matter as much as runtime reliability

### 4. Use a service-based model instead of a component-sum model

The best approach is to:

- define the required service precisely
- define service-loss criteria
- include shared dependencies
- account for common-cause failures
- verify the model against fault injection and recovery evidence

### 5. Reconcile timing assumptions before making compliance claims

The repository notes that the source documents do not fully agree on restoration timing. Before reusing the values, reconcile:

- RAM plan assumptions
- DPR assumptions
- requirement text
- actual operational recovery behavior

## Short conclusion

The repository’s position is that **VIL availability is a system/service-level requirement**, not a simple component-by-component percentage assignment. The best compliance argument should combine:

- clear service definition
- dependency-aware modelling
- consistent recovery timing assumptions
- traceable verification evidence

