# Mechanical Testing

Mechanical testing verifies that ORIGIN's enclosure, mounts, interfaces and support structures remain functional, serviceable and physically stable under realistic handling and deployment conditions.

The current mechanical concept includes a tall faceted enclosure, three mmWave sensor positions, Rosetta v2 packaging, a side-accessible BIT interface, soil/deployment mounting, and a solar structure with a hollow third support for cable routing. Each of these elements requires validation beyond visual appearance.

## Scope

Mechanical validation may include dimensional inspection; PCB fit; sensor fit and orientation; connector access; BIT access; enclosure assembly; fastener retention; cable routing; solar-support stiffness; mounting stability; repeated assembly/disassembly; impact and handling resistance; deformation; and environmental sealing interfaces.

## Revision control

Every mechanical test should identify the exact CAD/released part revision.

Record at minimum:

```text
Enclosure revision
Manufacturing process
Material
Print/manufacturing settings where relevant
Installed hardware
Fastener type
Test configuration
```

A result from one prototype should not automatically be applied to a later geometry.

## Dimensional inspection

Before assembly, compare manufactured parts with critical CAD dimensions.

Priority dimensions include Rosetta mounting features; internal clearances; radar mounting-hole positions; sensor openings; connector openings; BIT interface position; solar-support interfaces; base/mount geometry; and mating surfaces.

The current design constraint that a single manufactured object remain within **250 × 250 × 250 mm** should also be checked at CAD-release stage.

## Rosetta fit test

Install Rosetta v2 into the enclosure without forcing the PCB.

Verify mounting holes align; standoffs support the PCB correctly; no component contacts the enclosure unintentionally; connectors remain accessible; cables can be attached and removed; PCB removal is possible without destructive disassembly; and fasteners do not bend the board.

Record any interference before modifying the part.

## Radar mounting test

Each C4001 radar mount should be tested for hole alignment; repeatable seating; stable angle; no PCB bending; connector access; clearance from fasteners and walls; and unobstructed sensing face.

After mechanical fit is confirmed, sensor performance must be rechecked because mounting geometry can affect radar behavior.

## Sensor-opening inspection

The enclosure intentionally includes openings for the mmWave sensors.

Check opening is centered on the sensing face; edges do not obstruct the intended field; mounting tolerance does not shift the sensor behind a wall; opening remains structurally sound; and drainage/water-entry implications are understood.

The mechanical test does not prove sensing performance; it confirms physical alignment. Performance belongs under [Sensor Testing](sensor-testing.md).

## BIT interface access

Because a bottom-mounted BIT interface could become inaccessible when ORIGIN is installed in soil or on a base, the current design direction places service/expansion access away from the underside.

Test with the unit in its intended mounted position.

Verify that an operator can reach the BIT interface; attach/remove a BIT without removing ORIGIN from the site; identify orientation; avoid damaging adjacent cables; and close/protect the interface after use where applicable.

## Enclosure assembly test

Perform multiple complete assembly/disassembly cycles.

Observe thread wear; insert movement; cracked printed features; stripped fasteners; seal damage; cable pinching; increasing gaps; and loss of alignment.

A prototype that assembles successfully once may still have poor service life.

## Fastener retention

Check that fasteners remain secure after representative handling.

Where threaded inserts or captive hardware are used, inspect for rotation; pull-out; cracking; deformation; and over-tightening damage.

Torque values should only be published if actually defined and validated for the chosen hardware/material combination.

## Cable routing

Mechanical cable validation should verify no sharp bends beyond acceptable limits; no cable trapped between enclosure halves; strain is not transferred directly to PCB connectors; service loops do not enter sensing regions; cables do not interfere with fasteners; and solar wiring can pass through the hollow support as intended.

Photograph the final routing configuration.

## Solar-support testing

The solar structure includes three supports in the current design direction, with one support also used as a cable path.

Test for panel retention; support stiffness; twisting; cable clearance; cable abrasion risk; fastener retention; and assembly repeatability.

If the panel creates a significant wind-loaded area, field validation should include observation under representative outdoor conditions before long-term deployment.

## Static load testing

Where appropriate, apply a defined static load to mounting features or supports.

Record load; location; duration; fixture; initial displacement; final displacement; permanent deformation; and damage.

Do not apply arbitrary destructive loads at a heritage site.

## Handling and transport testing

ORIGIN will be transported, installed and maintained, so representative handling should be tested.

Check for loosened internal parts; cracked mounts; connector movement; panel/support damage; rattling; and changed sensor orientation.

A post-transport functional check should follow physical inspection.

## Mounting stability

Test the complete unit on the intended mounting method or representative fixture.

Evaluate tipping tendency; rotation; loosening; soil/base interaction where applicable; access to service points; and sensor orientation after installation.

The tall enclosure direction makes center-of-mass and base stability particularly important.

## Deformation and creep

For polymer parts, long-term load can produce creep even if a short test passes.

Inspect loaded supports and interfaces after extended periods where possible, particularly solar supports; threaded inserts; narrow arms; clamped seals; and mounting interfaces.

## Drop and impact testing

A formal drop rating should not be claimed unless a defined procedure is completed.

During development, controlled handling-impact tests may be useful for service robustness, provided they are safe and do not risk surrounding heritage assets.

Record height, orientation, surface and resulting damage if such tests are performed.

## Acceptance framework

Mechanical tests may use criteria such as all intended components fit without forced deformation; sensors retain defined orientation; connectors remain accessible; no cable is pinched; enclosure closes consistently; no cracking after defined assembly cycles; supports remain aligned after defined load; and unit remains stable on intended mount.

Exact numerical thresholds should be defined per released design rather than invented globally.

## Regression triggers

Repeat relevant tests after changes to enclosure shape; wall thickness; material; print orientation; fasteners; sensor mounts; solar geometry; base geometry; Rosetta revision; and module interface.

## Evidence

Recommended evidence includes dimensional table; CAD screenshots; photographs before/after assembly; load-test setup photos; video of access/service test; damage photos; and revision identifier.

## Related documentation

See [Mechanical Design](../mechanical-design/README.md); [Enclosure](../mechanical-design/enclosure.md); [Sensor Mounting](../mechanical-design/sensor-mounting.md); [Solar System](../mechanical-design/solar-system.md); [Environmental Testing](environmental-testing.md); and [Validation Results](validation-results.md).
