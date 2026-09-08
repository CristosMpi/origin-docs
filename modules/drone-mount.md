# Drone Mount

**Drone Mount** is an ORIGIN module intended for temporary aerial integration, allowing selected ORIGIN hardware or sensing functions to be carried by an unmanned aerial platform during inspection, mapping, or short-duration monitoring tasks.

It is an adaptation of ORIGIN for a fundamentally different operating environment: instead of remaining fixed at a site, the system is exposed to motion, vibration, changing orientation, weight limits, and flight-safety constraints.

For that reason, Drone Mount should be treated as a specialized deployment configuration rather than simply as another bracket.

## Intended role

Drone Mount is intended to support situations where an aerial perspective can provide useful context around a heritage site, for example when fixed ground placement cannot easily reach or observe a location.

Potential use cases include:

- temporary elevated sensing;
- inspection of hard-to-reach structures;
- collection of site-context data;
- short-duration environmental observations;
- evaluation of possible permanent sensor positions.

Only capabilities that have been actually tested on the selected aircraft should be described as supported.

## System boundary

The ORIGIN project must distinguish between:

- the **ORIGIN payload**;
- the **Drone Mount**;
- the **aircraft**;
- the **pilot/operator**;
- flight-planning and regulatory requirements.

The mount does not make ORIGIN itself an autonomous aircraft system, and ORIGIN software should not be assumed to control the drone unless a future explicitly documented integration provides that function.

## Mechanical architecture

The mount must securely connect the ORIGIN payload to the aircraft while respecting the aircraft's structure and center of gravity.

A conceptual stack is:

```text
      ORIGIN payload
            │
      Drone Mount
            │
   aircraft hard point
            │
          drone
```

The mechanical interface should be repeatable and should avoid improvised attachment methods during flight.

## Mass and center of gravity

Payload mass is one of the most important constraints in any aerial configuration.

A valid Drone Mount design must account for:

- payload mass;
- mount mass;
- aircraft payload rating;
- battery endurance reduction;
- center-of-gravity shift;
- moment arm from the aircraft center;
- effect on flight stability.

The mass limit should come from the actual aircraft manufacturer and the tested configuration. No generic ORIGIN payload rating should be assumed.

## Vibration

Flight introduces vibration from motors, propellers, airflow, and control corrections.

Vibration can affect:

- PCB connectors;
- fasteners;
- sensor readings;
- accelerometers;
- cable retention;
- solder joints;
- mechanical fatigue.

A mount should therefore provide positive retention and avoid loose cable loops or unsupported mass.

Where vibration isolation is used, it must not allow excessive movement of the payload.

## Orientation

Unlike a fixed ORIGIN Core, an aerial payload constantly changes orientation.

Software and analysis must therefore avoid assuming that:

- “up” remains constant;
- sensors remain level;
- detection zones remain fixed relative to the ground;
- distance readings have the same meaning as in a stationary deployment.

If orientation matters to interpretation, the system should record or receive sufficient attitude/context information to explain the observation.

## Sensor suitability

Not every ORIGIN sensor is automatically useful in flight.

Each sensor should be evaluated for:

- motion sensitivity;
- vibration sensitivity;
- field of view;
- airflow effects;
- required stabilization time;
- operating distance;
- interference from the aircraft;
- electromagnetic or mechanical interference.

For example, a sensor validated for stationary presence detection should not automatically be claimed to perform identically while the platform itself is moving.

## mmWave considerations

Aerial use of mmWave sensing requires specific validation because the sensor and target can both be moving relative to each other.

Potential complications include:

- aircraft velocity;
- rotation;
- changing distance to surfaces;
- reflections from the aircraft body;
- propeller or structural movement;
- rapidly changing beam orientation.

Therefore, Drone Mount documentation should not reuse stationary ORIGIN presence-detection claims without separate flight testing.

## Power

The ORIGIN payload may use its own power source or, in a future supported design, receive power from the aircraft.

The final configuration must define:

- power source;
- voltage range;
- connector;
- current requirement;
- electrical isolation;
- startup/shutdown procedure;
- effect on aircraft endurance.

Using the aircraft battery introduces an additional dependency and should not be assumed safe without a validated electrical interface.

## Communications

Aerial use may change communication conditions significantly.

Potential factors include:

- greater distance from the operator or gateway;
- changing orientation of antennas;
- interference from aircraft electronics;
- temporary loss of connectivity;
- higher mobility.

The system should therefore preserve local buffering where possible and avoid treating network loss as data validity.

## Data provenance

Aerial observations must be distinguishable from fixed-site observations.

Useful contextual metadata can include:

```text
mount_type: drone_mount
flight_id: <identifier>
payload_revision: <revision>
platform_id: <aircraft identifier>
observation_mode: aerial
```

Where available, position and orientation metadata can significantly improve later interpretation.

The exact schema should come from the real software system.

## Attachment security

A failed attachment in flight can damage the aircraft, payload, property, heritage material, or people below.

Mechanical retention should therefore use a deliberate primary attachment and, where appropriate, a secondary retention strategy.

Inspection should verify:

- fastener engagement;
- locking features;
- cracks;
- cable retention;
- clearance from propellers and moving parts;
- absence of loose components.

## Pre-flight procedure

A Drone Mount deployment should include a dedicated pre-flight checklist.

At minimum:

1. confirm legal and site authorization;
2. inspect the aircraft;
3. inspect the mount;
4. verify payload mass and configuration;
5. secure all fasteners and cables;
6. power and initialize ORIGIN;
7. verify local logging/communications;
8. confirm no component can enter a propeller path;
9. perform a short low-risk hover test when permitted;
10. confirm system health before the mission.

## Post-flight procedure

After flight:

- power down safely;
- inspect mount and payload;
- check for loosened fasteners;
- inspect connectors;
- download or verify recorded data;
- record the flight configuration;
- note any unexpected vibration, instability, or sensor behavior.

## Flight safety and regulations

Drone operation is regulated and location-dependent.

The ORIGIN documentation must not imply that a technically successful mount authorizes flight.

The operator remains responsible for:

- aircraft-category requirements;
- registration where applicable;
- pilot competency requirements;
- geozone restrictions;
- maximum altitude and distance rules;
- site permission;
- privacy requirements;
- heritage-site restrictions;
- safe separation from people and property.

Flight procedures should always follow the requirements applicable to the actual country, aircraft, site, and mission.

## Heritage-site considerations

Heritage sites can add restrictions beyond normal flight rules.

Drone use should avoid:

- contact with protected structures;
- downwash near fragile surfaces or loose archaeological material;
- disturbing visitors or conservation work;
- unnecessary close approach;
- interference with other site operations.

The module is intended to improve access to information, not increase physical risk to the asset being protected.

## Validation

Drone Mount should be validated progressively.

### Static fit test

Confirm mechanical attachment without powering the aircraft.

### Ground vibration test

Operate the aircraft on the ground where safe and evaluate connector/mount stability.

### Low-risk hover test

Test basic retention and payload behavior in a controlled environment.

### Sensor validation

Compare selected sensor outputs between stationary and aerial conditions.

### Mission validation

Only after earlier stages should the configuration be used for a real heritage-site task.

## Failure modes

Important failure cases include:

| Failure | Consequence |
| --- | --- |
| Mount loosens | Payload movement or loss |
| Payload shifts | Center-of-gravity change |
| Cable enters moving area | Aircraft damage |
| Power interruption | Lost observations or reboot |
| Communication loss | Delayed data transfer |
| Excess vibration | Invalid data or hardware fatigue |
| Sensor misinterpretation | False conclusions from moving platform |

These risks justify separate validation from ground deployments.

## Development status

Drone Mount is a specialized ORIGIN module. Its exact geometry, compatible aircraft, payload mass, sensor set, and operating procedures should be revision-specific and based on tested hardware.

Until a specific aircraft/mount combination is validated, the documentation should describe Drone Mount as a **temporary aerial integration concept and module**, not a universally compatible drone payload.

## Related documentation

See:

- [Modules](README.md)
- [Expansion System](expansion-system.md)
- [Mechanical Design](../mechanical-design/README.md)
- [Software → Data Pipeline](../software/data-pipeline.md)
- [Testing & Validation](../testing-validation/README.md)
