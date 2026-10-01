# Relays

## Description

Relays are electromechanical switching devices used for signal switching, isolation, control logic and safety functions in railway signalling systems.

Typical applications:

- Vital relay logic
- Interlocking systems
- Interface relays
- Power switching
- Status indication

---

## Failure Modes

- Stuck Open
- Stuck Closed
- Contact Resistance Increase
- Contact Bounce
- Coil Open Circuit
- Coil Short Circuit
- Welded Contacts
- Intermittent Contact
- Delayed Operation
- Failure to Operate
- Failure to Release

---

## Typical Causes

### Electrical

- Overcurrent
- Overvoltage
- Coil overheating
- Arcing

### Mechanical

- Wear
- Spring fatigue
- Mechanical obstruction

### Environmental

- Vibration
- Shock
- Humidity
- Corrosion
- Dust contamination

### Ageing

- Contact erosion
- Material degradation
- Insulation degradation

---

## Local Effects

- Output not energized
- Output permanently energized
- Intermittent operation
- Increased heating
- Unexpected switching

---

## Higher-Level Effects

- Loss of control function
- Incorrect signal state
- Communication interruption
- Equipment shutdown
- Spurious activation

---

## End Effects

- Loss of railway functionality
- Service disruption
- Reduced availability
- Delayed train operation
- Safety function unavailable

---

## Detection Methods

### During Operation

- Self-monitoring
- Current monitoring
- Voltage monitoring
- State feedback

### Maintenance

- Functional test
- Contact resistance measurement
- Insulation resistance measurement
- Visual inspection

---

## Preventive Measures

- Relay health monitoring
- Redundant architecture
- Contact monitoring
- Preventive replacement
- Environmental protection

---

## Reliability Considerations

Important ageing mechanisms:

- Contact wear
- Contact welding
- Coil degradation
- Spring fatigue

Key contributors:

- Switching frequency
- Load current
- Environmental conditions
- Maintenance intervals

---

## FMEA Guidance

Typical FMEA entries:

| Function | Failure Mode | Typical Cause | Typical Effect |
| ---------- | -------------- | --------------- | --------------- |
| Switch Output | Stuck Open | Coil Failure | Loss of Function |
| Switch Output | Stuck Closed | Contact Welding | Permanent Activation |
| Switch Output | Increased Resistance | Corrosion | Degraded Performance |
| Switch Output | Intermittent Contact | Vibration | Sporadic Failure |

---

## FRACAS Guidance

Typical root causes:

- Contact wear
- Corrosion
- Incorrect loading
- Manufacturing defect
- Mechanical damage
- Environmental exposure

---

## Lessons Learned

Capture project-specific lessons learned here over time.

Example:

- Irish Rail Project: Relay contact contamination caused intermittent circuit occupancy indication.
- DSTW Project: Coil failures associated with elevated cabinet temperatures.
