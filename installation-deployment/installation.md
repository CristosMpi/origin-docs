# Installation

This page covers the physical installation of ORIGIN after the site assessment has been approved.

The installation phase should leave the unit mechanically secure, electrically safe, serviceable, correctly oriented, and ready for software setup. It should not yet be considered operational until calibration and commissioning are complete.

## Installation principles

A good installation should be:

- **reversible** where heritage constraints require it;
- **stable** under normal handling and weather conditions;
- **serviceable** without disturbing the protected site;
- **documented** well enough to reproduce or remove;
- **safe** for visitors, staff, and technicians;
- **consistent** with the approved site assessment.

## Pre-installation inspection

Before mounting the unit, inspect the device and deployment kit.

Confirm:

- enclosure panels are intact;
- fasteners are present and undamaged;
- sensor openings are unobstructed;
- radar modules are securely mounted;
- Rosetta v2 is fixed correctly inside the enclosure;
- internal wiring is restrained;
- solar support components are complete where used;
- seals and gaskets are correctly seated;
- cable glands or feed-throughs are undamaged;
- the correct unit identifier is visible in the deployment record.

Any shipping damage should be resolved before the unit is installed.

## Position and orientation

Place the unit according to the approved site map.

Record:

- final position;
- enclosure orientation;
- mounting height where relevant;
- radar-facing directions;
- solar-panel orientation;
- nearby reference features that make the installation position reproducible.

A small orientation change can significantly affect presence detection, so orientation should not be treated as cosmetic.

## Mounting the Core

The actual mounting method depends on the site and enclosure version.

Possible methods may include:

- freestanding base;
- soil or ground support;
- clamp-based support;
- bracket;
- approved wall or structural fixing;
- custom non-invasive heritage-site mounting hardware.

The mounting method should be the one approved during site assessment.

After fastening, check:

- no visible rocking or looseness;
- no excessive stress on the enclosure;
- no fastener interference with service panels;
- sufficient clearance for cables;
- sufficient clearance for BIT access where used;
- no obstruction of sensor openings;
- no sharp edges or protrusions accessible to visitors.

## Soil or ground installation

Where ORIGIN is mounted partly into soil or ground, the accessible interfaces must remain above the practical service line.

In particular, BIT attachment points should not be placed where the user must dig around the device to access them.

Ground installations should also consider:

- drainage;
- standing water;
- soil movement;
- corrosion or material degradation;
- cable protection;
- root growth or vegetation;
- accidental impact from maintenance equipment.

## Sensor installation check

The current Core concept contains three C4001 mmWave radar modules.

Verify each sensor:

- is attached using the intended mounting holes;
- has not rotated during transport;
- is aligned with its assigned direction;
- has a clear sensing face;
- has strain-free cabling;
- can be uniquely identified in software.

Do not perform final coverage adjustments purely by eye. Final validation occurs during calibration.

## Solar system installation

Where solar charging is used, install the panel and supports only after the main enclosure is stable.

The current mechanical concept includes a third solar-panel support that is also used as a protected cable route.

During installation:

1. mount the structural supports;
2. verify panel angle and orientation;
3. route the cable through the hollow support;
4. avoid sharp bends and pinch points;
5. provide strain relief before the cable enters the Core;
6. inspect all penetrations before closing the enclosure.

The solar cable route should not create a direct water path into the electronics compartment.

## Power connection

Before applying power:

- confirm expected supply type;
- inspect battery polarity and connectors where applicable;
- confirm no exposed conductors;
- check connectors are fully seated;
- verify cable strain relief;
- inspect for accidental short-circuit risks;
- confirm the enclosure is ready to be energized.

Initial power-up should be monitored rather than left unattended.

If abnormal heating, smell, current draw, repeated reset, or unstable power behavior appears, disconnect power and investigate before continuing.

## Communications hardware

If the deployment uses cellular, Wi-Fi, wired networking, or external antennas, complete the physical installation before software setup.

Check:

- antenna location;
- cable routing;
- connector seating;
- SIM or eSIM provisioning status where applicable;
- waterproofing around external penetrations;
- clearance from metal structures likely to affect radio performance.

Do not publish SIM identifiers, credentials, or private network information in public documentation.

## Module installation

Install only modules approved for the specific deployment.

For each module, verify:

- mechanical compatibility;
- electrical compatibility;
- connector orientation;
- required firmware support;
- correct module identity;
- suitable environmental protection;
- no interference with neighboring modules or sensor fields of view.

A physically attachable module should not automatically be treated as electrically or software-compatible.

## Cable management

Cables should be routed so they cannot:

- touch sharp edges;
- obstruct enclosure closure;
- cross sensor openings;
- pull directly on PCB connectors;
- rub against moving or removable parts;
- form uncontrolled water paths;
- become visitor trip hazards.

Use strain relief at both the enclosure and external mounting structure where necessary.

## Sealing inspection

Before final closure, inspect:

- gasket alignment;
- enclosure seams;
- cable penetrations;
- sensor openings;
- solar-support cable route;
- fastener torque consistency;
- any temporary workshop access holes.

ORIGIN should not be assigned a waterproof or IP claim solely from visual inspection. Protection must be supported by testing documented under [Testing & Validation](../testing-validation/README.md).

## Final physical inspection

After assembly and before software setup, confirm:

- unit is stable;
- orientation is documented;
- all panels are closed;
- cables are restrained;
- no tool or loose fastener remains inside;
- service access remains possible;
- labels and unit identification are visible;
- the installation does not interfere with visitors or heritage assets.

Take final installation photographs before moving to setup.

## Installation record

Record at minimum:

| Field | Value |
| --- | --- |
| Unit ID | Deployment identifier |
| Hardware revision | Rosetta / enclosure revision |
| Installation date | Date |
| Site | Location |
| Mounting method | Type |
| Orientation | Recorded direction |
| Radar A/B/C directions | Recorded |
| Power source | Solar / battery / wired / other |
| Modules installed | List |
| Physical issues | None or documented |
| Installed by | Personnel |

After the physical installation passes inspection, continue to [Setup](setup.md).