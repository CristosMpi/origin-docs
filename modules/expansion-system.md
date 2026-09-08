# Expansion System

The **ORIGIN Expansion System** defines the common rules that allow modules to attach to and extend ORIGIN Core without turning every deployment into a one-off prototype.

It is the architectural layer behind BITs, Aqua Base, Drone Mount, and future modules.

The long-term goal is simple: a module should be able to answer four questions clearly.

1. How does it attach?
2. How does it receive power, if required?
3. How does it exchange data, if required?
4. How does ORIGIN know what it is and whether it is healthy?

## Why a common expansion system is necessary

Without a shared interface, every module would need custom wiring, custom firmware assumptions, and custom mounting geometry.

That creates several problems:

- difficult maintenance;
- undocumented compatibility;
- fragile prototypes;
- repeated redesign of the Core;
- higher risk of wiring errors;
- unclear module identity;
- inability to support multiple hardware revisions cleanly.

The Expansion System is intended to replace that ad-hoc approach with a versioned contract between the Core and its modules.

## Four interface layers

The system can be understood as four related layers:

```text
Mechanical interface
        ↓
Electrical interface
        ↓
Communication interface
        ↓
Software / identity interface
```

A module may use only some of these layers. For example, a purely mechanical mount may not require power or data, but it should still have a defined mechanical revision and compatibility range.

## Mechanical interface

The mechanical interface defines how a module physically connects to ORIGIN Core.

It should eventually specify:

- attachment points;
- allowable envelope;
- insertion/removal direction;
- retention method;
- fastener type;
- load expectations;
- cable-routing zones;
- keep-out regions around sensors and antennas;
- environmental sealing requirements.

A key requirement already established during enclosure development is that module access must remain practical after installation. Expansion points should therefore not depend entirely on the bottom surface of the Core, because that region may be blocked by soil or a mounting base.

## Keep-out zones

The final mechanical standard should define keep-out zones for components that must remain unobstructed.

These can include:

- mmWave sensing faces;
- antennas;
- environmental-sensor openings;
- ventilation or pressure-equalization features;
- maintenance covers;
- solar-support geometry;
- primary mounting hardware.

A module that fits mechanically but occupies a keep-out zone is not compatible.

## Load classes

Not all modules place the same loads on the enclosure.

A useful future mechanical classification could distinguish between:

- **light accessory** — low-mass sensor or interface;
- **structural module** — base or support that transfers mounting loads;
- **dynamic module** — configuration exposed to vibration or acceleration, such as Drone Mount.

The final limits must be determined from real enclosure and material testing.

## Electrical interface

Active modules require a controlled way to receive power and, potentially, expose signals.

The electrical specification should eventually define:

- nominal supply rail(s);
- acceptable voltage range;
- maximum continuous current;
- transient/current-limit behavior;
- ground reference;
- connector family;
- pin assignment;
- reverse-polarity protection;
- ESD/transient expectations;
- whether hot-plugging is supported.

No pinout should be treated as final until it is confirmed against the released Rosetta hardware.

See [Rosetta → Interfaces](../rosetta/interfaces.md).

## Power budgeting

The Core must not assume unlimited expansion power.

For active modules, the system should maintain a power budget that considers:

- normal module current;
- startup current;
- multiple simultaneous modules;
- battery state;
- solar input conditions;
- regulator thermal limits;
- Core electronics demand.

A compatible connector does not guarantee that the power system can safely support every combination of modules.

## Communication interface

Where modules exchange data, the common interface should define how the Core distinguishes one module from another and how data integrity is handled.

The final implementation may use one or more buses already available through Rosetta. The exact choice should come from confirmed hardware and firmware.

Regardless of transport, the communication layer should support:

- module identity;
- initialization;
- capability discovery or configuration;
- health checks;
- error detection;
- recovery after disconnect;
- version compatibility.

## Module identity

The software should avoid relying only on physical connector position to determine module type.

A robust module record can include:

```text
module_family
module_revision
interface_version
serial_or_unit_id
capability_flags
firmware_requirement
configuration_profile
health_state
```

Some early modules may use manually configured identity rather than electronic discovery. That is acceptable as long as the configuration is explicit and traceable.

## Capability model

Rather than hard-coding every module name throughout the software, ORIGIN can also describe what a module contributes.

Example capability categories include:

```text
SENSOR
MOUNT
POWER_EXTENSION
DEPLOYMENT_ADAPTER
USER_INTERFACE
EXPERIMENTAL
```

A specific module can expose more than one capability.

This approach allows higher-level software to reason about the function of a module without depending exclusively on its marketing or project name.

## Initialization sequence

A future active module should follow a predictable startup sequence.

```text
Core starts
   ↓
Expansion interface initialized
   ↓
Module detected / configuration loaded
   ↓
Compatibility checked
   ↓
Module driver initialized
   ↓
Health verified
   ↓
Capability becomes available
```

If any stage fails, the module should remain unavailable or degraded rather than being silently treated as operational.

## Health and fault isolation

Module failures should not unnecessarily take down the Core.

The Expansion System should aim for fault isolation so that one bad accessory does not automatically disable all monitoring.

Potential failures include:

- short circuit;
- over-current;
- corrupted communication;
- missing module;
- incompatible revision;
- invalid sensor output;
- repeated resets;
- damaged connector.

Where hardware allows, power or communication to the affected module can be disabled while the Core continues operating in a degraded state.

## Hot-plugging

Hot-plug capability must not be assumed.

If modules are intended to be connected while ORIGIN is powered, the interface must be designed and tested for:

- contact sequencing;
- inrush current;
- transient suppression;
- bus recovery;
- firmware detection;
- accidental partial insertion.

Until that support is explicitly validated, maintenance instructions should assume modules are attached or removed with the affected interface safely powered down.

## Environmental interface

A module changes more than electronics.

Every attachment can affect:

- ingress protection;
- thermal behavior;
- airflow;
- water paths;
- UV exposure;
- structural loads;
- sensor geometry.

The module standard should therefore define whether an unused interface requires a cover, cap, gasket, or other protection.

## Configuration profiles

Modules can also be represented through deployment configuration.

A configuration profile can describe:

- expected module family;
- revision;
- enabled driver;
- sensor role;
- installation orientation;
- calibration values;
- data-label mapping.

This makes the deployed configuration reproducible and prevents firmware from depending on undocumented physical knowledge.

## Version compatibility

The Expansion System itself should have a version.

A future compatibility matrix could look like:

| Module | Revision | Expansion interface | Core requirement | Status |
| --- | --- | --- | --- | --- |
| BIT example | A | v1 | Rosetta v2 + supported firmware | Experimental |
| Aqua Base | A | Mechanical v1 | Compatible enclosure revision | Prototype |
| Drone Mount | A | Mechanical v1 | Validated payload configuration | Prototype |

The values above are illustrative only; the real matrix should be generated from released hardware revisions.

## Backward compatibility

Once modules are used outside the development bench, unnecessary breaking changes should be avoided.

If a new Core revision changes an interface, the project should either:

- preserve compatibility;
- provide an adapter;
- clearly mark the old module unsupported;
- document the required upgrade path.

Silent incompatibility is the worst outcome because it can make a physically connected module appear functional when it is not.

## Development workflow for a new module

A new module should progress through a controlled process.

### 1. Define the use case

State what deployment problem the module solves.

### 2. Define the interface

Document mechanical, power, and data requirements.

### 3. Prototype independently

Test the module without risking a complete field unit.

### 4. Integrate with Core

Verify attachment, power, communication, and software identity.

### 5. Test failure modes

Disconnect it, misconfigure it, restart it, and verify the Core remains understandable.

### 6. Validate the combined system

Re-test Core sensors and environmental behavior with the module installed.

### 7. Freeze a revision

Only after validation should the module receive a supported hardware/interface status.

## Documentation requirements

Every supported module should eventually document:

- purpose;
- hardware revision;
- compatible Core revisions;
- mechanical installation;
- electrical requirements;
- communication requirements;
- firmware requirement;
- configuration;
- health states;
- maintenance;
- known limitations;
- validation results.

This makes the module ecosystem maintainable as Team Galene develops new hardware.

## Security considerations

An active module expands the trusted hardware/software boundary.

Module interfaces should therefore avoid allowing an untrusted or malfunctioning device to:

- overwrite configuration without authorization;
- impersonate another critical sensor without detection;
- destabilize the main communications stack;
- consume unlimited power;
- bypass update or integrity checks.

Security controls should be proportional to the real interface and deployment risk, but expansion should not mean unrestricted trust.

## Testing

The Expansion System should be validated using both normal and failure conditions.

Recommended tests include:

- repeated mechanical attachment;
- connector mating cycles;
- incorrect/absent module;
- power overload behavior;
- communication interruption;
- reboot with module attached;
- module removal;
- multiple-module combinations;
- Core sensor interference;
- configuration mismatch;
- environmental exposure.

## Current status

The ORIGIN expansion architecture is established conceptually, and current modules already shape important mechanical requirements such as accessible side attachment. However, the full standardized connector geometry, electrical pinout, automatic identity method, and compatibility matrix remain revision-dependent until the expansion interface is formally frozen.

That distinction should remain visible in public documentation: the **architecture is intentional**, while some exact implementation details are still under development.

## Related documentation

See:

- [Modules](README.md)
- [BITs](bits.md)
- [Aqua Base](aqua-base.md)
- [Drone Mount](drone-mount.md)
- [Rosetta → Interfaces](../rosetta/interfaces.md)
- [Software → Configuration](../software/configuration.md)
- [Mechanical Design](../mechanical-design/README.md)
- [Testing & Validation](../testing-validation/README.md)
