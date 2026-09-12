# Component Replacement

Component replacement is appropriate when diagnostics has isolated a fault to a replaceable part or when preventive service requires a controlled substitution.

Replacement is not complete when the new part is physically installed. ORIGIN must also preserve configuration, identity, calibration, sealing, traceability and validated system behavior.

## Replacement principles

Every replacement should be justified by evidence; electrically and mechanically compatible; documented before and after service; performed with power safely isolated; followed by the required calibration or recommissioning; and treated as a configuration/revision change when the replacement is not identical.

## Before replacement

Record unit ID; site ID; failed component; observed symptom; diagnostic conclusion; component revision or identifier; firmware/configuration state; calibration values relevant to the component; photographs if useful; and replacement part identity.

Preserve logs before disconnecting the system whenever possible.

## Compatibility check

Do not assume two visually similar parts are interchangeable.

Confirm compatibility across supply voltage; current requirements; connector and pinout; logic levels; communication protocol; firmware driver support; mechanical dimensions; mounting-hole geometry; sensing orientation; environmental suitability; and released hardware revision.

A substitute component that changes any of these characteristics may require engineering review and re-validation.

## Safe power isolation

Before manipulating powered components:

1. place the unit into maintenance state;
2. save logs/configuration;
3. disconnect external input or solar source as required;
4. isolate battery power according to the hardware procedure;
5. verify the expected unpowered state;
6. use appropriate ESD precautions for electronics.

## Rosetta PCB replacement

Replacing Rosetta is a major service event because the PCB anchors multiple system interfaces.

Before removal, record Rosetta hardware revision; firmware version; configuration version; unit identity/provisioning information; connected modules; sensor-channel mapping; storage state; and known calibration values.

After installing the replacement verify mounting; verify all connectors; confirm no cable is trapped or strained; load the approved firmware; restore only compatible configuration; confirm unit identity; verify every expected sensor and module; run power, storage and communication checks; and perform commissioning checks before returning to service.

See [Rosetta → Assembly & Bring-up](../rosetta/assembly-and-bring-up.md).

## mmWave sensor replacement

The current ORIGIN Core uses three DFRobot C4001 mmWave sensors in defined physical positions.

When replacing one:

1. record the logical channel being replaced;
2. mark or record the original orientation;
3. remove the sensor without changing neighboring mounts where possible;
4. install the replacement using the intended mounting holes;
5. confirm connector seating;
6. preserve channel identity;
7. confirm electrical communication;
8. repeat relevant calibration and coverage checks.

Because radar behavior depends on physical orientation and site geometry, a sensor replacement should not return directly to service without a controlled presence/coverage check.

## Environmental sensor replacement

After replacement verify correct exposure to ambient conditions; confirm any shield or membrane is restored; verify units and scaling; compare readings with a suitable reference where available; and check for plausible stabilization behavior.

Do not copy old calibration values to a different sensor unless the calibration scheme explicitly supports that practice.

## Battery replacement

Battery replacement requires special care.

Use a battery that matches the released electrical design and manufacturer requirements.

Before installation, inspect the new battery for physical damage.

After installation confirm polarity; secure the battery mechanically; prevent cable strain; verify charging behavior; verify power-management state; and monitor for abnormal heat during initial operation.

Never return a swollen, punctured, leaking or overheated battery to service.

## Solar-panel replacement

When replacing the panel or supports confirm panel electrical compatibility; restore the commissioned mechanical orientation; check all supports; verify the hollow third support cable path; prevent cable abrasion; inspect the enclosure cable entry; and verify charging behavior after reassembly.

A changed panel geometry or electrical rating should be treated as a design revision rather than an invisible service substitution.

## Cable and connector replacement

Replacement cables should match conductor requirements; connector type; environmental exposure; strain-relief method; routing constraints; and current/voltage requirements.

Route the replacement so it does not obstruct sensors; create a water path; contact sharp edges; carry structural load; and interfere with enclosure closure.

## Enclosure-part replacement

Replacing a shell, hatch, sensor face or mounting element can change sealing behavior; radar geometry; structural stiffness; cable routing; and module accessibility.

Use the correct CAD revision and material/process where possible.

After replacement, inspect fit, fasteners, sealing surfaces and sensor alignment.

## Seal or gasket replacement

Use the released seal geometry/material where specified.

Before fitting the new seal clean the mating surfaces; remove debris; inspect the groove or compression surface; verify the seal is not twisted; and ensure wiring does not cross the seal path.

Do not claim an IP rating after field seal replacement unless the complete configuration has been validated to that rating.

## Module replacement

For BITs, Aqua Base, Drone Mount or future modules confirm module identity; check compatibility version; verify mechanical engagement; verify power and data interface; confirm software detection; run module-specific functional checks; and ensure the Core remains healthy with the module attached.

## Storage replacement

Before storage replacement attempt to preserve recoverable data, record corruption or failure evidence, confirm the approved storage format and capacity requirements, and restore only known-good data/configuration.

After replacement, verify initialization, write/read behavior and local buffering.

## Firmware-related replacement state

Hardware replacement can require firmware changes, but service work should avoid opportunistic software upgrades unless planned.

Combining hardware replacement with unrelated firmware changes makes root-cause verification harder.

Where possible:

1. restore the system using the known-good software baseline;
2. validate the repair;
3. perform software updates separately under the normal update process.

## Replaced-part disposition

Failed components should be labeled with unit/site source; date removed; suspected fault; diagnostic reference; and whether further analysis is required.

Do not immediately discard a part if it may contain useful failure evidence.

## Post-replacement verification

At minimum, verify correct mechanical installation; no remaining loose hardware; correct electrical connection; normal startup; expected device identity; sensor/module health; storage; communication; no new warnings; and no visible environmental-protection defect.

Then perform the calibration or commissioning steps affected by the replacement.

## Replacement record

Record:

```text
unit_id
site_id
date
component_removed
removed_component_revision_or_id
reason
root_cause
replacement_component
replacement_revision_or_id
firmware_before
firmware_after
configuration_before
configuration_after
calibration_performed
validation_performed
final_health_state
technician
notes
```

## When replacement becomes a design change

Escalate to development when the new part differs materially in electrical behavior; dimensions; sensor characteristics; protocol; material; environmental specification; connector; and firmware requirement.

In that case, update the relevant design documentation and repeat the appropriate [Testing & Validation](../testing-validation/README.md) procedures before treating the new configuration as a released ORIGIN build.
