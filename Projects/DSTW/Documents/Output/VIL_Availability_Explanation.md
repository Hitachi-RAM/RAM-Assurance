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

## The six VIL availability requirements (short summary)

A detailed explanation of each requirement follows in "Detailed meaning of the requirements".

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
- **Meaning:** This covers faults that have **no operational impact**; the requirement's own comment names this defect class **FK4**. It limits how long the VIL may run with such a fault present (see the detailed section below).
- **Value:** `A >= 0.997154`

### 4. EL4-DIL-SSS-REQ-00573 — Minor SW/HW changes

- **Text:** Minor changes of VIL software or hardware shall be carried out **without operational restrictions**.
- **Meaning:** Patches and small hardware changes must not interrupt service.
- **Implication:** This is a lifecycle and maintainability requirement, not just a reliability number.

### 5. EL4-DIL-SSS-REQ-00574 — Operational downtime

- **Text:** The operational downtime shall not be longer than the restart time of the affected component, as well as the time for the re-integration into the overall system.
- **Meaning:** When a component is restarted (for example for a change), operation may be interrupted only for the technical restart and re-integration time, not longer. The requirement contains no numeric limit.

### 6. EL4-DIL-SSS-REQ-00818 — Major SW/HW changes

- **Text:** Major changes of the VIL software (upgrades), especially with safety impact, or of the hardware shall be carried out **during operational breaks**.
- **Meaning:** Major changes are not done while normal train operation continues; they are planned for periods without regular traffic. (It is not a "later release" requirement; its target release is DIL_OBB_1.0.x like the others.)
- The repository allocates it to lifecycle and CDS/NMR/J4S behavior.

## Detailed meaning of the requirements

This section explains what each of the six requirements means in practice, which customer wording it comes from, what the requirement does **not** define, and what it implies for the VIL design.

Sources: chapter 3.1.4.3.2 of SSS RAMS 3BU_17300_1257_DTAPA Ed02PD01 (requirement text, customer text "LH" and Hitachi response text "PH"); the DPR Requirements [VIL-Instance]; the RAM plan 3BU_17300_1209_DUAPA, section 3.4 (Table 9). Where this section **interprets** instead of quoting, it says so. Annual figures use a 365-day year (525,600 min) and continuous required service; the requirements themselves do not state an observation period.

### Vocabulary used by the requirements

| Term | Meaning here |
| --- | --- |
| VIL instance | One virtual interlocking running for one station, made of redundant nodes of the two components ELEKTRA Core and ECMUX (SSS_VIL section 3.1.2). |
| Availability A, unavailability U | A is the share of time the service is usable; U = 1 - A. |
| MTTR (mean time to restore) | Time from the loss of service until operation is resumed (the definition used in the RAM plan, taken from EN 50126-1). It includes detection and recovery, not only the repair work itself. |
| Automatic correction | The system clears the disturbance itself, without a technician. The DPR describes it as entering a safe state, self-test and automatic reintegration of the disturbed component. |
| Manual correction | A person has to intervene (for example replace a part). |
| Class 2 | The availability class that the customer assigns to every VIL (LH 5.4.0-3): 99.995 %. The whole DIL central unit is class 1: 99.999 % (RAM plan section 3.4, Table 9). |
| Operational break | A period without regular train traffic ("Betriebspause"). |
| FK4 | The customer defect class for faults without operational impact (named in the comment of EL4-DIL-SSS-REQ-00570). Its definition is not given in the chapter. |
| LH / PH | Lastenheft (customer specification text) and Pflichtenheft (Hitachi response text) shown with each requirement. |

### Facts common to all six requirements

- Status Accepted, priority Mandatory, scope System, target release DIL_OBB_1.0.x (EL4-DIL-SSS-REQ-00818 additionally IFC_BLOCK_1.0.0), originator Customer.
- EL4-DIL-SSS-REQ-00587, 00569 and 00570 have category DPR (availability figures). EL4-DIL-SSS-REQ-00573, 00818 and 00574 have category MCR (they govern changes).
- The verification field of every requirement still says "will be added in a later document edition": **no verification method is defined yet**.

### How the six requirements fit together

| Requirement | Question it answers | Kind |
| --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 | How available must the VIL be in total? | Overall target (99.995 %) |
| EL4-DIL-SSS-REQ-00569 | How is that availability distributed over the ways a disturbance is cleared? | Three scenario targets (manual, 10 min, 2 min) |
| EL4-DIL-SSS-REQ-00570 | How much time may the VIL spend with a fault that does not affect operation? | Target for the FK4 (no operational impact) condition |
| EL4-DIL-SSS-REQ-00573 | May a patch or small hardware change restrict operation? | Process requirement: no restriction |
| EL4-DIL-SSS-REQ-00818 | How are major changes carried out? | Process requirement: only in operational breaks |
| EL4-DIL-SSS-REQ-00574 | How long may operation be interrupted when a component is restarted? | Relative limit: restart time plus re-integration time |

### EL4-DIL-SSS-REQ-00587 - Overall availability

- **Requirement:** class 2 overall availability of at least 99.995 %.
- **In plain terms:** the VIL of a station may be unavailable for at most **0.005 % of the time = 26.3 min per 365-day year (about 0.44 h)**.
- **Where it comes from:** customer clauses 5.4.0-1 (availability of the VSTW at least 0.99995) and 5.4.0-3 (every VSTW belongs to availability class 2).
- **Hitachi response (PH):** the VSTWs run hot-hot and are distributed evenly over the availability zones, so that the requirement is also met when a server fails.
- **What it implies:** it is a target for the whole service, so it applies jointly to Core and ECMUX and to everything the service needs (network, shared servers). It cannot be met by one component alone and must not be copied to each component.
- **Not defined in the requirement (interpretation / open points):**
  - What counts as "unavailable": complete loss only, or also a partial restriction of a station?
  - Whether the planned operational breaks for major changes (EL4-DIL-SSS-REQ-00818) count as downtime.
  - The observation period over which the percentage is measured.

### EL4-DIL-SSS-REQ-00569 - Availability distribution

- **Requirement:** the availability must correspond to class 2, in particular at least:

| Scenario | Customer clause | Required availability | Unavailability U | Equivalent downtime per 365 days |
| --- | --- | --- | --- | --- |
| Disturbance that needs **manual** correction (MTTR 6 h in the current requirement text) | 5.4.0-4 | 99.9979 % | 2.1e-5 | 11.0 min |
| Disturbance corrected **automatically within 10 min** | 5.4.0-6 | 99.999 % | 1.0e-5 | 5.3 min |
| Disturbance corrected **automatically within 2 min** | 5.4.0-7 | 99.9996 % | 4.0e-6 | 2.1 min |

- **In plain terms:** the overall budget is looked at separately for each kind of disturbance. Each figure limits the downtime caused by disturbances of that kind. The RAM plan states that the classes apply to different scenarios and are not subcomponents of one overall downtime.
- **Why the three figures differ although the shorter outages are less severe:** for a fixed availability, a shorter outage may happen more often. Using the stationary relation `A = MUT / (MUT + MTTR)`, i.e. `MUT = A x MTTR / (1 - A)` (MUT = mean up time between outages):

| Scenario | Assumed restoration time | Outage frequency that just meets the target |
| --- | --- | --- |
| Manual, current requirement text | 6 h | about once per 32.6 years |
| Manual, RAM plan Table 9 | 225 min | about once per 20.4 years (Table 9 shows 20 years) |
| Manual, DPR | 0.5 h | about once per 2.7 years |
| Automatic 10 min | 10 min | about once per 1.9 years (Table 9 shows 2 years) |
| Automatic 2 min | 2 min | about once per 0.95 years (Table 9 shows 1 year) |

  This is exactly what the requirement's comment says: "outages with MTTR = 2 min may occur more often per N years than outages with MTTR = 10 min". In practice **a 2-minute outage about once a year is tolerated, a 6-hour outage only about once in 33 years**. The comment speaks of "equal availabilities", but the three values are not equal.
- **What "automatic" asks of the design:** the system must detect the fault, bring the affected part to a safe state, restart or reintegrate it and restore operation by itself within 2 or 10 minutes. This is a requirement on failure detection, restart and reintegration of the SW components, not only on hardware. The earlier separate requirements EL4-DIL-SSS-REQ-00571 (10 min) and 00572 (2 min) were merged into this one.
- **Interpretation:** if the redundancy hides a fault completely (the other node keeps the service running), no service is lost and the event belongs to EL4-DIL-SSS-REQ-00570 instead. EL4-DIL-SSS-REQ-00569 becomes relevant when service is actually interrupted: for example a restart of an application on all redundant nodes (EL4-VIL-SSS-REQ-01155) or a failure that affects both nodes.
- **Open points:**
  - The manual restoration time is 6 h in the requirement text, 0.5 h in the DPR and 225 min in the RAM plan. With one availability value the allowed outage frequency differs by a factor of 12 between 6 h and 0.5 h.
  - The three scenario budgets add up to about 18.4 min per year, less than the overall 26.3 min per year. The documents do not say how the remainder is used or whether the figures are meant to be added.
  - The table in the RAM plan appears to print 99.9999 % for the 10-minute case, but its own 5 min per year and 2-year MTBF correspond to 99.999 %. This looks like a typing error and should be corrected in the RAM plan.
  - Whether "within 2 / 10 minutes" is a maximum per event or an average is not stated; the customer wording ("within") suggests a maximum.

### EL4-DIL-SSS-REQ-00570 - Outages with no operational impact (FK4)

- **Requirement:** outages of a VIL instance with no operational impact shall have an availability of at least 99.7154 %; the comment identifies this as defect class FK4. Customer clause 5.4.0-5 gives 0.997154.
- **In plain terms:** the VIL may be in such a "fault but no operational effect" condition for at most **0.2846 % of the time = about 1,496 min = 24.9 h per year**. This is a limit on how long the system may run with a fault present, for example **with one redundant partner failed while the other keeps operating** (interpretation: this is the typical case of a fault without operational impact).
- **Example (workbook assumption, not a requirement):** the project RAM workbook assumes 8 h for the manual exchange of a faulty component "with no impact on operation". At 8 h per event, 24.9 h per year corresponds to about three such events per year.
- **What it implies:** it is not a service-loss figure and must not be mixed with the 99.995 %. It is the reason why failed redundancy must be detected, reported and restored in reasonable time: while one partner is out, the service has no protection against a second failure.
- **Open points:** FK4 itself is not defined in this chapter. When the condition starts and ends (detection or failure), and which events count (for example a node that is out for a planned patch), has to be agreed.

### EL4-DIL-SSS-REQ-00573 - Minor SW/HW changes

- **Requirement:** minor changes of the VIL software (patches) or the hardware shall be carried out **without operational restrictions**. The comment gives a security update as an example.
- **Customer wording:** planned service software upgrades and planned hardware exchange must have no effect on operation and availability; railway operation must continue without interruption and no operational downtime may occur (5.9.0-1). During the exchange of non-safety-relevant software, a redundancy must take over operation (5.4.0-10).
- **Hitachi response (PH):** patches that do not touch the safety-relevant parts (the configuration data), for example security patches, can be introduced without affecting operation: one redundancy partner is taken out of service, the new software is installed, it is reintegrated, and the same is repeated with the remaining partners.
- **In plain terms:** a **rolling update**: the VIL keeps running on the remaining partner(s) while one partner is updated.
- **Conditions stated in the PH text:** changes in the generic baseline and in the station data are excluded, to preserve replica determinism (all replicas must run identical software and data). Every change must pass a change-impact analysis with safety involvement.
- **What it implies for the SW components:** the VIL must keep working with one partner out; a patched partner must rejoin without service interruption (automatic reintegration, EL4-VIL-SSS-REQ-00221); version consistency between nodes must be checked (EL4-VIL-SSS-REQ-01459); patch and unpatched versions must be able to coexist during the update.
- **Caveat (interpretation):** during the update window the redundancy is reduced, so the system is exposed to a second failure; the duration of this window should be kept short and its risk assessed.

### EL4-DIL-SSS-REQ-00818 - Major SW/HW changes

- **Requirement:** major changes (upgrades), especially with safety impact, or hardware changes shall be carried out **during operational breaks**. Examples: enhancement or correction of the application software, update of the data preparation.
- **Hitachi response (PH):** during such an update there is a short period in which neither the VSTW nor its redundancy partners are operational, so no route protection with cleared signals exists. The update must therefore be done in a planned interval without regular train traffic. This period is limited to **3-4 min**: from the dispatcher's consent to the activation until the new VSTW has completed the general interrogation of the neighbouring systems and the outdoor elements, the operational data are set again and the VSTW can be operated again.
- **Customer wording:** during the exchange of safety-relevant software the redundancy **should** take over operation (5.4.0-9). This is a wish ("soll") and conflicts with the PH statement that nobody is operational during the switchover; the accepted requirement text only demands operational breaks.
- **In plain terms:** safety-relevant changes are not rolled without interruption; they happen in a planned break, but the break must be short and technically bounded (see EL4-DIL-SSS-REQ-00574).
- **What it implies for the SW components:** a controlled maintenance shutdown (EL4-VIL-SSS-REQ-01156), activation only after authorization, restart of all nodes with the new version, version checks (EL4-VIL-SSS-REQ-01458 to 01460) and fast recovery of the interfaces and operational state after the restart.
- **Open points:** whether the planned break counts against the 99.995 %; which of the customer wish and the PH statement applies; the exact start and end of the 3-4 min period.

### EL4-DIL-SSS-REQ-00574 - Operational downtime

- **Requirement:** the operational downtime shall not be longer than the restart time of the affected component plus the time for its re-integration into the overall system.
- **Hitachi response (PH):** the operational interruption normally equals the boot time of the affected component plus the time for its integration into the overall system; safety-relevant changes are excepted.
- **In plain terms:** when something has to be restarted, the interruption may consist of the technical restart and re-integration only. No additional waiting, manual steps or avoidable delays are allowed.
- **What it implies:** the downtime is determined by the slowest chain of the restart: the component restart (Core node, ECMUX node, application), the re-synchronisation of the redundant nodes, the re-establishment of the RaSTA connections to adjacent systems and object controllers, and the restoration of the operational data. Each of these steps needs a defined time limit.
- **Limitation:** the requirement is **relative**; it gives no number. As long as no restart time and re-integration time are defined, it cannot be verified: a very long restart would still "comply". The origin text deals with software updates; whether it also bounds failure recovery is not stated (interpretation).

### Questions that should be answered by the requirement owner

1. What is the exact definition of "service unavailable" (complete loss, partial restriction) and over which period is availability measured?
2. Do planned operational breaks (EL4-DIL-SSS-REQ-00818) and update windows count as downtime?
3. Which manual restoration time is authoritative: 6 h, 225 min or 0.5 h?
4. How do the three scenario figures of EL4-DIL-SSS-REQ-00569 relate to the overall figure: added, overlapping or independent?
5. What exactly is FK4, and when does an FK4 condition start and end?
6. Which numeric limits apply to restart and re-integration in EL4-DIL-SSS-REQ-00574?
7. Does the customer wish for redundancy takeover during safety-relevant updates (5.4.0-9) apply or the operational-break approach?

## Recommended modeling approach (summary)

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

## Available models for calculation of VIL availability (detailed explanation)

This section explains which calculation models exist for the VIL, what each one actually calculates, and what is still missing. "Available" means three different things, which are kept apart here:

1. **Calculations that exist in the repository** (sheets of the preliminary RAM workbook).
2. **Results that are quoted** (the table on page 6 of the DPR).
3. **Methods that would be needed** for a complete VIL calculation but do not exist yet.

**Short answer:** the repository contains a preliminary **hardware** calculation of the redundant Core (a repairable 1oo2 pair of computing nodes plus network) and some comparison and split-brain sheets. It contains **no model of the complete VIL instance** (Core, ECMUX, interfaces, software behaviour, recovery) and no model for the three change requirements.

### Basics needed to read the models

| Term | Meaning | Formula |
| --- | --- | --- |
| Failure rate lambda | Failures per hour of one item | FIT = failures per 10^9 h, so lambda = FIT x 10^-9 per hour |
| MTBF | Mean time between failures | MTBF = 1 / lambda |
| MTTR | Mean time to restore the service | taken from the scenario (2 min, 10 min, 1 h, 8 h ...) |
| Availability | Share of time the service is up | A = MTBF / (MTBF + MTTR), approximately 1 / (1 + lambda x MTTR) |
| Unavailability | Share of time the service is down | U = 1 - A |

**2oo2 and 1oo2 are two different things.** The Core computing node (CN) is 2oo2: its two diverse software channels must agree, which is what makes hardware faults safely detectable. For **availability**, a 2oo2 node behaves like two items **in series**: if either part fails, the node stops. Availability comes from having **two such nodes in hot-hot operation (2x2oo2)**: the service continues if one node fails. At node level this is a 1oo2 arrangement. The ECMUX is 2x1oo1: two nodes with one channel each, also hot-hot (SSS_VIL EL4-VIL-SSS-REQ-00181 and 00227). This is why the DPR speaks of "2x2oo2 = 1oo2".

### Models found in the repository

Source: Prelim_RAM_Estimation_DSTW_Ed02_20260910.xlsx (folder Split Brain), and DPR Requirements [VIL-Instance], page 6.

| Model | What it calculates | Where it helps | Main limits |
| --- | --- | --- | --- |
| Sheet "4.1 Calculations 2x(2oo2)" | Failure rate, MTBF and availability of two hot-redundant Core nodes plus network, for restoration times of 2 min, 5 min, 10 min and 1 h (and scaled for several cells per site) | Closest to the specified basic Core architecture | Hardware only; see the detailed explanation below |
| Sheet "4.2 Calculations 2oo3_hot" | The same type of calculation for a hot 2-out-of-3 server arrangement | Comparison of alternative architectures (8 VSTW on 3 servers) | Not the specified VIL architecture; formulas use a different restoration time than the row label; a cached location 2 result shows #DIV/0! |
| Sheet "4.3 Calculations Warm_standby" | A master/slave warm-standby arrangement (8 VSTW on 2 servers) | Comparison of alternatives | Uses only the master failure rate; a note in the sheet says no switchover happens if the slave fails; failover time and failover success are not modelled |
| Sheet "Split_Brain_260910" | Probability of a network partition (split brain) from the double fault of a core router and a crossed top-of-rack switch, with a common-cause factor for the routers | A focused sub-model for one failure mode | Network only; budget taken from the IPS class 1 target, not from the VIL |
| DPR page 6 table | Result of "CN1+CN2 1oo2 hot + network" for 2 min to 4 h | Order-of-magnitude cross-check | The cited January workbook was not found; the 2 min, 5 min, 10 min and 1 h values match the Ed02 sheet 4.1 |

#### How sheet 4.1 calculates (the model behind the DPR table)

1. **Failure rate of one computing node (2oo2 = series):** `lambda_CN = lambda_CE1 + lambda_CE2 + lambda_ControlServer`. Each CE consists of a compute and a storage server. Result in the sheet: CN1 (master) 21,175 FIT, CN2 (slave) 1,058.75 FIT.
2. **Failure rate of the hot pair (1oo2 with repair):** the service is lost only if the second node fails while the first one is still being restored:
   `lambda_pair = 2 x lambda_CN1 x lambda_CN2 x MTTR`
   (the factor 2 because either node can fail first).
3. **Network in series:** `lambda_total = lambda_pair + lambda_network`, with the network (3 pairs of switches, each pair already 1oo2) at 4.4477 FIT.
4. **Availability:** `A = MTBF / (MTBF + MTTR)`.

Result for MTTR = 2 min: 4.449 FIT, MTBF about 25,658 years, availability 99.99999999 %.

**What this result really says:**

- The redundancy term (the pair of nodes) is only **0.0015 FIT**. The **network contributes 4.4477 FIT, i.e. 99.97 %** of the total. The result is almost independent of the restoration time (4.449 FIT at 2 min, 4.493 FIT at 1 h).
- So the table shows that the **hot-redundant node pair is very reliable**. It says very little about the VIL as a whole.

**Points to check before reusing it** (observations from the sheet, not corrections):

| Point | Observation | Effect |
| --- | --- | --- |
| Restoration time of the network | The sheet gives the network its own 8 h restoration time in its own row, but the 2 min scenario applies 2 min to the whole rate, network included | With 8 h the network unavailability is 3.6e-8 (0.019 min per year) instead of 1.5e-10, a factor of 240. The 99.99999999 % is overstated; the conclusion "large margin for this hardware path" is not changed |
| Slave failure rate | The slave node is set to **5 % of the master's failure rate** (documented as an estimate). In the specified hot-hot design both nodes run synchronously | With equal rates the pair term rises from 0.0015 to 0.030 FIT: still negligible here, but the assumption needs a justification |
| Source of the server rates | The workbook states that the server failure rates are estimates; the switch rates are taken from an earlier analysis (RAM ANA BFZ) | The RAM plan names EN 50126-1 with the MIL-HDBK-217F based Alcatel standard as the prediction basis; the estimates are not evidence of that method |
| Ideal failover | The formula assumes the second node takes over immediately and always | No failover time, no failure to switch over, no failure of reintegration |
| Independence | The two nodes are assumed independent | No common cause (shared storage, power, network, software, configuration) |
| Software | Only hardware failure rates are used | Software failures, application restarts and recovery times are not represented |
| Spreadsheet quality | Defined names "Network" and "proc" point to #REF!; the file recalculates on opening; the fraction and percent conventions are mixed between rows | Cached values may be stale; recalculate and check before use |

### Methods needed for the VIL, explained

None of these methods is implemented for the VIL in the repository. They are listed with what they would add.

| Method | Plain description | What it gives for the VIL |
| --- | --- | --- |
| Reliability block diagram (RBD) | A drawing of the blocks the service needs (Core, ECMUX, network, shared services) and how they are connected: in series (all needed) or in parallel (one needed). Availabilities are combined accordingly. | A clear overview of the service structure and a transparent first estimate. Only valid for independent blocks and does not show repair or failover timing. |
| Fault tree | Starts from the top event (service lost, or FK4 condition) and breaks it down into combinations of lower events (AND/OR). | Finds the combinations that cause the loss (cut sets), shows shared causes such as common servers, network, deployment service, software or configuration. Does not show time behaviour by itself. |
| Repairable-state (Markov) model | Describes the system as states (both nodes up, one node up, service lost) with transition rates (failure, repair, failover, reintegration). | Calculates availability with repair, detection, failover and reintegration times. This is what is needed for the 2 min / 10 min recovery requirements. |
| Event-based / operational calculation | Adds up the real downtime of recorded or tested events per category and compares the totals with the limits. | Suited for the requirements on changes and restart time and for verification with fault injection and field data (FRACAS). |
| Simulation (Monte Carlo / discrete event) | Runs the behaviour many times with random failure and repair times. | For complex timing or dependencies, if the closed-form models are insufficient. Not needed until the simpler models are in place. |

#### Example of the repairable 1oo2 model

States: **S2** = both nodes up, **S1** = one node up (service still available, redundancy lost), **S0** = no node up (service lost). Each node fails with rate lambda. The restoration rate is mu = 1 / MTTR.

```text
S2 --(2 x lambda)--> S1 --(lambda)--> S0
S2 <--(mu)---------- S1 <--(mu)------ S0        (one repair at a time)

Steady state:  U = P(S0) is approximately 2 x (lambda / mu)^2 = 2 x (lambda x MTTR)^2
Rate of entering S0:  lambda_pair is approximately 2 x lambda^2 x MTTR
```

The last line is the formula that sheet 4.1 uses, so the sheet is a first-order version of this model.

**Why common cause matters (illustration using the requirement itself, not project data):**

- EL4-DIL-SSS-REQ-00587 needs U of at most 5e-5. With two **independent** nodes and a perfect switchover, `U = u^2`, so each node would only need `u <= sqrt(5e-5) = 7.07e-3`, i.e. a node availability of 99.29 %.
- If a common-cause share beta of the node unavailability hits both nodes together, `U is approximately (1 - beta)^2 x u^2 + beta x u`. The common cause term decides the result:

| beta (share of common-cause failures) | Node unavailability that still meets 5e-5 | Node availability needed |
| --- | --- | --- |
| 0 (independent) | 7.07e-3 | 99.293 % |
| 1 % | 3.68e-3 | 99.632 % |
| 2 % | 2.26e-3 | 99.774 % |
| 5 % | 9.8e-4 | 99.902 % |

The value 2 % is only the factor the workbook uses for the router pair in the split-brain sheet; it is shown as a sensitivity and is **not** a VIL value. The conclusion is that a simple independent calculation can be far too optimistic.

### Which model fits which requirement

| Requirement | Suitable models | Comment |
| --- | --- | --- |
| EL4-DIL-SSS-REQ-00587 Overall | Block diagram for the service structure, fault tree for shared causes, Markov model for redundancy and recovery | Needs the full service boundary |
| EL4-DIL-SSS-REQ-00569 Distribution | Markov model with detection, restart and reintegration times; measured recovery times from fault injection | The 2 min and 10 min limits are time limits of the SW recovery, not only hardware rates |
| EL4-DIL-SSS-REQ-00570 FK4 | State model: time spent in the one-partner-out state; repair and exchange times | The result depends mainly on the restoration time of failed redundancy |
| EL4-DIL-SSS-REQ-00573 Minor changes | Procedure and timeline analysis, test with rolling update | No prediction model; it is a pass/fail behaviour with a measured reduced-redundancy window |
| EL4-DIL-SSS-REQ-00818 Major changes | Timeline analysis of the activation, measured duration | Planned break; also decides whether it counts as downtime |
| EL4-DIL-SSS-REQ-00574 Operational downtime | Critical-path timing of restart plus re-integration, measured | Needs numeric restart and re-integration limits |

### What is missing to build the VIL model

| Input | Status in the supplied files |
| --- | --- |
| Definition of "service unavailable", observation period, treatment of planned breaks | Not defined |
| Definition of FK4 and its start and end | Not defined in the chapter |
| Authoritative manual restoration time (6 h, 225 min, 0.5 h) | Conflicting |
| Failure rates of the ECMUX nodes and of the interface/connection paths | Not found |
| Mapping of Core and ECMUX nodes to servers and availability zones | Described only in general terms |
| Probability that automatic recovery succeeds within 2 min / 10 min (coverage) | Not found |
| Failover and reintegration times; numeric detection limits (EL4-VIL-SSS-REQ-01462 to 01464 are TBD) | Not found |
| Common-cause factors for the VIL (shared servers, network, software, configuration) | Only for routers in the split-brain sheet |
| Software failure scenarios (all replicas restart together, EL4-VIL-SSS-REQ-01155) | Not modelled; no software failure rates should be invented |

### Recommended next steps

1. Correct and revalidate the workbook (restoration time per block, slave failure rate, named ranges, units) and rerun it; keep it as the hardware input.
2. Agree the service definition and the open points of the requirements (see the questions above).
3. Build a simple block diagram of the VIL service (Core, ECMUX, network, shared services) and a fault tree for the shared causes.
4. Build a repairable-state model for the Core and the ECMUX with the recovery times as parameters; obtain these times from fault-injection tests.
5. Treat software failures as defined fault scenarios supported by tests and field data, not as invented failure rates.
6. Use the event-based approach for the change and restart requirements.

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

