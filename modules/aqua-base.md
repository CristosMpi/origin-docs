# Aqua Base

**Aqua Base** is an ORIGIN module intended for deployments where water, splash exposure, shoreline geometry, or water-adjacent placement changes how the system must be mounted and protected.

It should be understood as a **deployment adaptation layer**, not as a claim that the standard ORIGIN Core is automatically waterproof, submersible, or suitable for unattended aquatic use.

The purpose of Aqua Base is to let the project explore water-oriented heritage monitoring without redesigning every internal subsystem of the Core.

## Intended role

A standard ground or structure-mounted ORIGIN unit assumes relatively conventional mechanical support. Water-adjacent environments introduce different constraints, including:

- splash and spray;
- high humidity;
- condensation;
- unstable or soft ground;
- changing water level;
- corrosion;
- stronger environmental contamination;
- more difficult maintenance access;
- additional cable-sealing requirements.

Aqua Base is intended to provide a mechanical and deployment framework that addresses these conditions around the Core.

## What Aqua Base is not

The module should not be interpreted as automatically providing:

- full submersion capability;
- a certified ingress-protection rating;
- marine-grade corrosion resistance;
- buoyancy certification;
- safe operation in arbitrary currents or waves;
- permission to deploy hardware in protected aquatic environments.

Any such capability must be supported by explicit design, testing, and—where relevant—external requirements.

## Deployment architecture

Conceptually, Aqua Base sits between ORIGIN Core and the deployment environment:

```text
        ORIGIN Core
             │
      mechanical interface
             │
         Aqua Base
             │
    deployment environment
   water-adjacent / shoreline
```

The Core should remain removable so that maintenance and electronics servicing do not require replacing the entire base.

## Mechanical priorities

Aqua Base should provide:

- a stable support geometry;
- repeatable Core attachment;
- resistance to tipping under expected loads;
- protection for cable transitions;
- drainage where water can collect;
- access for inspection and removal;
- minimal obstruction of Core sensors;
- materials appropriate to the intended environment.

If the base is intended to contact water directly, all submerged or wetted components need separate material and sealing consideration.

## Stability

Water-adjacent deployments can experience forces not present in indoor or dry-ground installations.

Potential loads include:

- wind;
- accidental contact;
- moving water;
- buoyancy forces;
- debris impact;
- shifting soil or sediment;
- vibration.

The design should therefore be evaluated as a physical system, not only as a 3D-printed shape that holds the Core upright.

## Water paths

One of the most important design questions is not simply whether water reaches the outside surface, but **where water can travel**.

Possible ingress paths include:

- fastener holes;
- module interfaces;
- cable openings;
- seams;
- sensor cutouts;
- ventilation features;
- capillary paths between assembled parts.

Aqua Base should avoid creating a low point that channels water directly toward the Core enclosure.

Where cables pass upward into ORIGIN, routing should include appropriate strain relief and, where suitable, drip-loop or sealed-entry concepts.

## Drainage and condensation

A sealed-looking enclosure can still accumulate moisture through condensation.

Aqua Base design should consider:

- whether trapped cavities can drain;
- whether water can remain around fasteners;
- whether evaporation paths exist where appropriate;
- whether temperature changes can create internal condensation;
- whether seals are inspectable.

The correct solution may vary by deployment; sealing every cavity is not automatically superior to providing controlled drainage in a non-electronic region.

## Materials

Material selection should consider more than printability.

Relevant factors include:

- UV exposure;
- moisture absorption;
- corrosion of metallic hardware;
- galvanic interaction between metals;
- long-term creep;
- temperature range;
- brittleness;
- chemical exposure from the local environment.

Prototype materials can be useful for geometry testing, but prototype success does not establish long-term outdoor durability.

## Electrical separation

Aqua Base should not unnecessarily place electrical connections near the lowest or wettest region of the assembly.

Electrical design should aim to:

- keep connectors accessible and protected;
- avoid exposed conductors;
- prevent water from following cables into the enclosure;
- isolate faults where possible;
- detect degraded power or sensor behavior rather than masking it.

Exact connector and supply specifications belong to the confirmed expansion-interface design.

## Sensor effects

The module must not compromise ORIGIN's sensing geometry.

Aqua Base should be checked for:

- radar obstruction;
- large reflective surfaces near mmWave sensors;
- altered sensor height;
- changed sensor orientation;
- interference with environmental sampling;
- vibration transferred into the Core.

If Aqua Base changes the mounting height or angle of ORIGIN, the validated sensing coverage should be re-measured for that configuration.

## Software configuration

Aqua Base may eventually correspond to a deployment profile rather than requiring unique firmware.

A deployment profile can record contextual information such as:

```text
mount_type: aqua_base
site_environment: water_adjacent
orientation: <configured>
maintenance_class: <configured>
module_revision: <revision>
```

The exact schema should come from the real software configuration system.

The important requirement is that data collected from an Aqua Base deployment remains identifiable as coming from that physical configuration.

## Installation workflow

A safe installation procedure should include:

1. site assessment;
2. verification that deployment is permitted;
3. inspection of the base and fasteners;
4. installation of the base without the Core where practical;
5. stability check;
6. Core attachment;
7. cable and seal inspection;
8. power-up and health verification;
9. sensor validation in the installed orientation;
10. documentation of the final position and configuration.

## Maintenance

Water-adjacent environments justify more frequent visual inspection than protected indoor environments.

Maintenance should check:

- corrosion;
- loosened fasteners;
- cracks;
- accumulated water;
- debris;
- seal condition;
- cable damage;
- movement of the installation;
- sensor openings;
- unexpected biological growth or contamination.

The maintenance schedule should be based on actual environmental exposure rather than a universal interval.

## Failure modes

Potential Aqua Base failures include:

| Failure | Possible consequence |
| --- | --- |
| Base movement | Sensor coverage changes |
| Water accumulation | Increased ingress/corrosion risk |
| Seal damage | Moisture reaches Core |
| Fastener corrosion | Reduced structural retention |
| Cable damage | Communication or power fault |
| Material cracking | Loss of stability or protection |

These failure modes should be visible in inspection procedures and, where possible, reflected by system health monitoring.

## Validation

Aqua Base validation should progress in stages.

### Dry mechanical testing

Verify geometry, retention, assembly, and Core access before adding water exposure.

### Controlled water exposure

Evaluate splash paths, drainage, seams, and material behavior in a controlled environment.

### Stability testing

Apply representative loads without risking electronics.

### Integrated system testing

Install the real Core and confirm:

- sensor performance;
- power stability;
- communication;
- mounting repeatability;
- environmental behavior.

### Field pilot

Only after controlled tests should the complete configuration be evaluated in a representative water-adjacent site.

## Heritage-site considerations

Water-oriented heritage environments can be especially sensitive.

Installation must avoid:

- damaging archaeological material;
- introducing contaminants;
- obstructing visitor or staff access;
- creating trip or entanglement hazards;
- disturbing protected natural areas;
- using anchors or adhesives without site approval.

The module is intended to support heritage professionals, not override site conservation requirements.

## Development status

Aqua Base remains a module whose detailed geometry, materials, sealing approach, and environmental limits depend on the current mechanical revision and test program.

Until those limits are validated, documentation should describe it as a **water-adjacent deployment concept/module**, not as a certified waterproof or marine product.

## Related documentation

See:

- [Modules](README.md)
- [Expansion System](expansion-system.md)
- [Mechanical Design → Waterproofing](../mechanical-design/waterproofing.md)
- [Installation & Deployment](../installation-deployment/README.md)
- [Testing & Validation](../testing-validation/README.md)
