# Waterproofing

ORIGIN requires environmental protection, but the current mechanical design also includes dedicated openings for the three mmWave sensors. For that reason, the project should not describe the enclosure as fully waterproof unless a specific revision has been tested and certified to a defined ingress-protection level.

The current design philosophy is therefore **controlled water management**: identify likely ingress paths, reduce direct exposure, protect electronics, provide drainage where useful, and validate the complete assembly under representative conditions.

## Environmental protection goals

The enclosure should be designed to reduce risk from rain; splash; dripping water; dust and debris; condensation; wet cables; water travelling along supports or fasteners; and temporary outdoor exposure during deployment and service.

Exact protection requirements depend on the deployment environment and should be defined before a production enclosure is released.

## Main ingress paths

The current enclosure architecture has several likely weak points: radar openings; service-panel seams; solar cable entry; module interfaces; fastener penetrations; lower mounting joints; mating surfaces between printed parts; and any ventilation or pressure-equalisation feature.

These areas should receive more design attention than uninterrupted shell walls.

## Sensor openings

The three radar openings are the most obvious conflict between sensing and sealing.

Possible protection strategies include recessed sensor placement; external overhang or drip lip; sloped opening geometry; replaceable bezel; radar-transparent protective window; gasketed cover; membrane or thin barrier material; and drainage below the opening.

Any material placed in front of the C4001 must be tested for its effect on radar performance. A mechanically waterproof window is not useful if it creates unacceptable sensing loss or reflections.

## Avoid upward-facing openings

Where possible, cable entries, screw recesses, and service seams should not face directly upward.

Upward-facing pockets can collect water and maintain hydrostatic pressure against seals long after rain has stopped.

Geometry should encourage water to shed away from seams, run past openings rather than into them, leave recessed areas through drainage paths, and avoid pooling near cable penetrations.

## Labyrinth and overlap geometry

A seam does not always need to rely on one exposed gasket line.

Printed or machined parts can use overlapping edges or labyrinth paths so water must change direction before reaching the interior.

A conceptual joint may look like:

```text
outside
  ↓
 ┌───────┐
 │ cover └──┐
 │          │  ← overlap / labyrinth
 └────┐     │
      └─────┘
         ↓
       inside
```

The actual joint should be designed around print tolerance and service requirements.

## Gaskets

Where a service panel needs repeated opening, a compressible gasket can provide a more controlled seal than sealant applied manually each time.

Gasket design should define material; thickness; compression target; groove geometry; joint flatness; fastener spacing; and replacement procedure.

A gasket cannot compensate for badly warped mating surfaces or very uneven fastener pressure.

## Sealants

Sealant can be useful around permanent penetrations, but it should not replace good mechanical design.

If used, documentation should identify sealant type; compatible materials; cure requirements; preparation method; areas where it must not be applied; and service implications.

Permanent sealant should not trap a component that is expected to be replaced regularly.

## Solar cable entry

The hollow third solar support creates a protected cable route, but the transition into the enclosure still needs a defined seal.

The design should prevent water from travelling down the support and directly into the electronics cavity.

Possible strategies include cable gland; sealed bulkhead fitting; compression grommet; internal drip loop; offset entry with drainage below; and sealed support-to-enclosure interface.

The correct solution depends on the final cable diameter and connector strategy.

## Module interface protection

BITs and other expansion modules may require an external interface.

When no module is installed, the interface should remain protected by a cap, cover, shutter, or sealed blanking part where appropriate.

When a module is installed, the connection should avoid creating a channel that directs water into the Core.

A side-accessible interface is preferable to an underside interface for usability, but side placement still requires splash and runoff management.

## Fasteners

Fastener penetrations can become water paths.

The design should consider blind inserts rather than open through-holes where possible; washers or sealing washers where justified; screw recess geometry; whether water can follow threads into the enclosure; corrosion resistance; and drainage around external screw heads.

Fastener count should be sufficient for even gasket compression but not unnecessarily high.

## Printed-part porosity

3D-printed parts should not automatically be treated as watertight.

Leakage can occur through layer interfaces; under-extrusion; seams; thin walls; infill-connected cavities; screw holes; and poorly fused surfaces.

Watertightness therefore depends on the print process, geometry, material, and post-processing, not only the CAD model.

## Condensation

A sealed enclosure can still contain moisture.

Temperature cycling may cause condensation on internal surfaces even if rain never enters.

The design should consider initial trapped humidity; temperature swings; internal heat sources; pressure changes; desiccant where appropriate; breathable membrane vents if justified and validated; and conformal protection of electronics where appropriate.

The solution should match the actual deployment environment.

## Drainage

Some external cavities are easier to make drainable than perfectly sealed.

Drain holes or channels may be appropriate for sensor recesses, solar-support cavities, decorative outer shells, and lower mounting interfaces.

Drainage paths must not lead toward electronics or protected cable entries.

## Internal protection

Mechanical environmental protection can be supported by internal design features such as raised PCB mounting above the lowest internal surface; drip shields; separate wet and dry zones; cable entry below sensitive electronics; splash barriers; and replaceable internal covers.

If minor ingress occurs, the architecture should make it less likely that water immediately reaches the most sensitive components.

## Testing levels

Water testing should progress from low-risk inspection to more realistic exposure.

### Visual path inspection

Inspect all seams and openings and trace where water would flow.

### Local spray test

Expose one region at a time to controlled spray while monitoring the interior.

### Full assembly rain simulation

Test the complete enclosure in its normal installed orientation.

### Reassembly test

Open and close the enclosure, then repeat selected water tests to ensure the seal remains effective after service.

### Ageing test

Where practical, repeat after thermal cycling, UV exposure, or repeated use of service panels.

## Leak detection

Testing can use methods such as absorbent indicator paper; internal humidity logging; visual inspection; removable moisture indicators; and controlled mass comparison where appropriate.

Electronics should not be powered during early high-risk leak tests unless the procedure specifically requires it.

## Claims and IP ratings

ORIGIN documentation should not claim an IP rating unless the specific enclosure revision has been tested according to the relevant standard and conditions.

Instead, development documentation can state what has actually been validated, for example survived controlled splash test, no visible ingress after defined rain simulation, and sensor opening remained dry under a specified orientation.

These claims are more useful than an unsupported generic statement such as "waterproof."

## Failure handling

If water ingress is detected during field use, the maintenance process should include:

1. isolate power if safe to do so;
2. remove the unit from exposure;
3. inspect the ingress path;
4. dry and inspect electronics;
5. replace damaged seals or parts;
6. document the failure;
7. revise the design or installation method if needed;
8. retest before redeployment.

## Related documentation

See [Enclosure](enclosure.md); [Sensor Mounting](sensor-mounting.md); [Solar System](solar-system.md); [Materials](materials.md); [Testing & Validation](../testing-validation/README.md); and [Maintenance](../maintenance/README.md).

Environmental protection is a system property. A good ORIGIN enclosure should manage water deliberately, preserve sensor function, remain serviceable, and make only the protection claims that the actual hardware has earned through testing.
