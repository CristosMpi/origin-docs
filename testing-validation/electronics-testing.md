# Electronics Testing

Electronics testing verifies that Rosetta and the supporting electrical system behave correctly before they are trusted inside the complete ORIGIN assembly.

The objective is not only to confirm that the board powers on, but also to verify power integrity, interfaces, startup behavior, fault visibility and repeatability.

## Scope

Electronics testing may include:

- PCB visual inspection;
- continuity and short-circuit checks;
- power-rail validation;
- battery and charging behavior;
- regulator behavior;
- ESP32 startup and reset;
- storage interfaces;
- sensor buses;
- external connectors;
- module connections;
- current consumption;
- communication interfaces;
- fault recovery.

## Pre-power inspection

Before applying power to a newly assembled Rosetta board, perform a visual inspection.

Check for:

- solder bridges;
- rotated components;
- missing components;
- damaged pads;
- incomplete joints;
- connector damage;
- debris;
- incorrect polarity;
- obvious footprint mismatch.

Where practical, compare the assembly against the schematic, PCB layout and BOM revision used for manufacturing.

## Continuity and short checks

Before first power-up, verify that major supply rails do not show an obvious short to ground.

Recommended checks include:

```text
Battery/input rail → GND
Regulated rail(s) → GND
USB/input power → GND
```

The expected resistance depends on the circuit and should not be reduced to a universal pass value. The objective is to identify an abnormal near-short before applying energy.

## Controlled first power-up

A bench supply with current limiting is preferred for initial bring-up where the design allows it.

Procedure:

1. disconnect optional external modules;
2. set the supply to the expected input voltage;
3. configure a conservative current limit;
4. apply power;
5. observe current draw;
6. check for unexpected heating;
7. measure main rails;
8. stop immediately if behavior is abnormal.

Record the supply settings and observed current.

## Power-rail validation

For each regulated rail, record:

- nominal target;
- measured voltage;
- test location;
- load condition;
- instrument used;
- pass/fail criterion.

A rail should be tested during more than one operating state where possible, such as:

- startup;
- idle;
- active sensing;
- communication activity;
- module load.

This helps identify droop or instability that is invisible during idle measurement.

## Power-management components

Rosetta v2 includes dedicated power-management circuitry, including the BQ24074 battery-management device and TPS63031 regulator architecture documented elsewhere in the Rosetta chapter.

Testing should verify the functions actually implemented on the tested revision rather than relying only on datasheet behavior.

Relevant tests may include:

- external input detection;
- battery operation;
- charging state;
- transition between input sources;
- regulated output stability;
- restart behavior after brownout;
- recovery after battery reconnect.

## Current consumption

Current consumption should be measured for representative operating states.

Suggested states:

| State | Purpose |
| --- | --- |
| Boot | startup peak behavior |
| Idle | baseline consumption |
| Sensors active | normal monitoring load |
| Communications active | transmission load |
| Storage write | local logging load |
| Expansion active | module-dependent load |

These measurements are needed before meaningful battery-life or solar-energy claims can be made.

## ESP32 bring-up

The controller test should verify:

1. stable boot;
2. firmware upload path;
3. serial/debug output where enabled;
4. reset behavior;
5. repeated restart behavior;
6. access to required buses and peripherals.

Repeat boot tests rather than relying on one successful start.

## Interface testing

Each external interface should be verified independently before complete system integration.

A useful record includes:

```text
Interface ID
Connector/reference
Supply voltage
Signal type
Connected device
Expected behavior
Observed behavior
Fault behavior
```

## Sensor-bus testing

For each attached sensor:

- confirm electrical connection;
- confirm device communication;
- confirm stable repeated reads;
- disconnect the sensor deliberately;
- verify the firmware reports a fault;
- reconnect and verify recovery.

The system must not convert a disconnected sensor into a valid-looking measurement.

## Storage testing

If local removable or onboard storage is used on the tested revision, test:

- detection;
- read/write;
- file or record integrity;
- restart with storage present;
- restart with storage absent;
- removal or failure behavior where safe.

Storage failure should be visible to the system.

## SIM / communications hardware

Where a SIM or cellular interface is present on the tested revision, electrical validation should be separated from network-service validation.

Electrical validation may include:

- connector/holder inspection;
- supply behavior;
- device detection;
- communication with the modem/interface.

Network registration and data transport belong partly under communications and field testing.

## Thermal observation

During extended operation, inspect for unexpected heating.

Potential methods include:

- touch only where safe;
- infrared thermometer;
- thermal camera;
- onboard temperature telemetry if appropriate.

Record ambient conditions because component temperature without ambient context can be misleading.

## Brownout and restart testing

Where safe, test behavior under controlled power interruption.

Verify that the system:

- does not corrupt persistent configuration;
- restarts predictably;
- reinitializes sensors;
- identifies missing devices;
- resumes logging/communication according to design.

## Connector durability and serviceability

Repeatedly connect and disconnect serviceable connectors during development to identify:

- weak solder joints;
- mechanical strain;
- poor retention;
- inaccessible connectors;
- cable-routing problems.

This is especially useful before the electronics are enclosed.

## Manufacturing-file verification

A fabrication package should be checked before ordering.

The Rosetta v2 Gerber export previously reviewed for the project contained copper, mask, silkscreen, profile and Gerber job data but **did not include Excellon drill files**. That export therefore must not be treated as a complete manufacturing package.

This is a useful example of why file-package validation is part of electronics testing and manufacturing QA.

Before release, verify at minimum:

- copper layers;
- solder mask;
- silkscreen;
- board outline;
- drill files;
- fabrication notes where required;
- correct revision identifier.

## Regression testing

Repeat affected electronics tests after changes to:

- PCB layout;
- component footprints;
- regulator design;
- battery circuitry;
- connector assignments;
- firmware pin assignments;
- sensor interfaces;
- component substitutions.

## Example electronics test matrix

| Test | Status |
| --- | --- |
| Visual inspection | To be recorded per assembly |
| Supply-to-ground precheck | To be recorded |
| Main rail voltage | To be recorded |
| ESP32 boot repeatability | To be recorded |
| Sensor interface communication | To be recorded |
| Sensor disconnect detection | To be recorded |
| Storage read/write | Revision-dependent |
| Power interruption recovery | To be recorded |
| Thermal observation | To be recorded |
| Manufacturing-package completeness | Drill-file issue identified in reviewed export |

## Evidence

Recommended evidence includes:

- photographs of board revision;
- multimeter readings;
- bench-supply screenshots/photos;
- boot logs;
- current measurements;
- fault logs;
- manufacturing-package manifest.

## Related documentation

See:

- [Rosetta](../rosetta/README.md)
- [Rosetta Power Management](../rosetta/power-management.md)
- [Assembly & Bring-up](../rosetta/assembly-and-bring-up.md)
- [Sensor Testing](sensor-testing.md)
- [Validation Results](validation-results.md)
