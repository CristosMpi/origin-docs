# BITs

**BITs** are ORIGIN's attachable expansion elements. Their purpose is to extend the Core with additional capabilities without forcing those capabilities to be permanently integrated into the main enclosure or Rosetta board.

BITs are therefore part of ORIGIN's broader modular design philosophy: the Core remains stable, while smaller extensions can be added for a particular deployment, experiment, sensor requirement, or educational configuration.

## Role in the ORIGIN ecosystem

A BIT should behave as a defined extension of ORIGIN rather than as an unrelated accessory.

Depending on the specific BIT, it may provide an additional sensor; a different sensing position; a small external electronics function; a physical interaction point; deployment-specific functionality; and an educational or prototyping interface.

The long-term goal is to allow BITs to be developed independently while still following common ORIGIN rules for attachment, identification, power, data, health reporting, and version compatibility.

## Physical placement

An important design requirement identified during enclosure development is that BITs **must remain accessible after ORIGIN has been installed**.

A bottom-only attachment position is unsuitable for many deployments because the lower part of the Core may be inserted into soil, located very close to the ground, attached to a base, and blocked by a mounting structure.

For that reason, the mechanical architecture should prioritize side, upper-side, or otherwise externally reachable expansion positions.

This requirement is not cosmetic. It directly affects whether operators can install, replace, or inspect a BIT without removing the entire ORIGIN unit from the site.

## Mechanical interface goals

A BIT attachment should provide repeatable positioning; enough retention for the intended use; defined orientation; tool access where fasteners are used; cable clearance; strain relief; compatibility with the Core enclosure geometry; and minimal interference with the main sensors.

The final standard should also define whether a BIT is intended for repeated hot-swapping in the field or for installation during a maintenance session.

## Sensor interference

BIT placement must account for ORIGIN's built-in sensing system.

For example, an attached element should not block a mmWave sensor opening; create a large reflective object directly in a radar field; shade or obstruct another environmental sensor; interfere with an antenna region; and cover ventilation or protected sensing openings.

A mechanically successful attachment can still be a system-level failure if it degrades the Core's sensing performance.

## Electrical integration

Some BITs may be passive mechanical elements, while others may require power and communication.

For active BITs, the final electrical interface should define supply voltage; current limit; connector; polarity; communication method; logic levels; protection; startup behavior; and whether connection while powered is supported.

These values must come from the confirmed Rosetta/expansion hardware design. They should not be inferred from early prototype wiring.

## Software model

An active BIT should appear to the system as an identifiable capability rather than just another anonymous signal.

A useful software abstraction is:

```text
BIT
 ├── identity
 ├── revision
 ├── capability
 ├── health
 ├── configuration
 └── observations / actions
```

This allows firmware and higher-level software to determine not only that something is connected, but what that connected device is expected to do.

## Detection and initialization

A connected BIT should follow a predictable lifecycle:

```text
Connected
   ↓
Detected or configured
   ↓
Compatibility checked
   ↓
Initialized
   ↓
Health confirmed
   ↓
Active
```

If identification cannot be automated in the final hardware, configuration may initially be manual. Even then, the selected BIT type should be recorded explicitly in software configuration.

## Health states

BITs should use explicit health states wherever possible.

Recommended system-level states include:

| State | Meaning |
| --- | --- |
| `READY` | Module initialized and available |
| `ACTIVE` | Module operating normally |
| `DEGRADED` | Module operating with reduced capability |
| `FAULT` | Module detected but not functioning correctly |
| `DISCONNECTED` | Expected module no longer present |
| `UNSUPPORTED` | Module or revision is not compatible with current software |

A missing BIT should never silently become a valid zero reading.

## MakeCode / educational use

BITs have also been explored as a way to make parts of ORIGIN's hardware ecosystem more approachable for educational programming environments such as **Microsoft MakeCode**.

The educational goal is different from the production firmware goal.

Production ORIGIN software prioritizes reliability, diagnostics, traceability, and deployment behavior. A BIT-oriented educational interface can instead expose simplified inputs and outputs so students can experiment with sensing, logic, and hardware interaction without needing to understand the complete production stack first.

This educational layer should remain clearly separated from safety- or deployment-critical firmware.

## Example capability classes

The BIT concept can support several categories over time.

### Sensor BIT

Adds a new observation source.

Potential examples include environmental, proximity, or site-specific sensing, but only confirmed modules should be listed as supported hardware.

### Interface BIT

Provides a convenient connection, indicator, or user interaction point.

### Mechanical BIT

Changes how ORIGIN is positioned or connected to another object without adding electronics.

### Experimental BIT

Allows Team Galene to evaluate a new subsystem before deciding whether it belongs in a future Core revision.

This is particularly useful because experimental features can be tested without destabilizing the main Rosetta design.

## Versioning

BITs should eventually carry their own hardware revision identifiers.

A compatibility record might include:

```text
BIT family:      <name>
BIT revision:    <revision>
Core revision:   <supported range>
Interface:       <version>
Firmware:        <minimum version>
Status:          experimental / supported / deprecated
```

This becomes important once several physical revisions exist at the same time.

## Maintenance

BITs should be designed for replacement where practical.

A maintenance procedure should define:

1. whether the Core must be powered down;
2. how the BIT is mechanically released;
3. how any connector is disconnected;
4. how seals or covers are inspected;
5. how the replacement is identified;
6. how the system confirms normal operation after replacement.

If a BIT creates an enclosure opening, the maintenance procedure must also restore the required environmental protection.

## Testing

Each active BIT should be tested in isolation and as part of the complete system.

Tests should include attachment repeatability; connector retention; power behavior; communication recovery; removal/reconnection; Core sensor interference; environmental exposure appropriate to the module; firmware compatibility; and failure-state reporting.

## Development status

BITs are an evolving part of ORIGIN. The concept and mechanical accessibility requirements are established, while exact standardized pinouts, connector geometry, automatic identification methods, and the supported module catalog should be treated as revision-dependent until the final expansion interface is frozen.

The documentation should therefore distinguish between **BIT architecture** — the common design rules described here and **specific BIT implementations** — individual modules with confirmed hardware and software specifications.

## Related documentation

See [Modules](README.md); [Expansion System](expansion-system.md); [Rosetta → Interfaces](../rosetta/interfaces.md); [Mechanical Design](../mechanical-design/README.md); and [Software → Configuration](../software/configuration.md).
