# Solar System

The solar assembly is both an energy subsystem and a mechanical structure. Its supports must carry the panel, protect the cable path, tolerate normal handling, and avoid transferring excessive loads into thin enclosure walls.

The current ORIGIN concept uses a **three-support solar structure**. The third support is intentionally designed to be hollow or internally routed so the solar cable can pass through it into the enclosure instead of remaining exposed outside the product.

## Mechanical objectives

The solar support system should provide:

- stable panel positioning;
- resistance to normal handling and transport loads;
- controlled cable routing;
- serviceable attachment to the enclosure;
- enough stiffness to prevent excessive panel movement;
- replaceable supports if one is damaged;
- compatibility with the manufacturing envelope;
- minimal interference with the radar sensors and service openings.

## Three-support architecture

A three-point or three-support concept can provide a stable connection while leaving room between supports for access and cable management.

The exact support geometry is not yet frozen, but each support should have a clear function.

A conceptual arrangement is:

```text
     Solar panel
  ───────────────
    |     |     |
    A     B     C
              cable path
                 ↓
           ORIGIN enclosure
```

Support C represents the cable-routing support in this simplified example. Final naming and position should follow the released CAD.

## Cable-routing support

The third support should include an internal passage large enough for the solar cable and connector strategy selected for the final design.

The passage must account for:

- cable outside diameter;
- connector size, if the connector must pass through the support;
- bend radius;
- strain relief;
- sealing at the enclosure entry;
- water drainage or exclusion;
- assembly sequence;
- cable replacement.

A channel that fits the cable in CAD but requires impossible bends during assembly is not acceptable.

## Protected cable entry

The point where the cable enters the main enclosure is a likely ingress path.

The mechanical design should therefore include a defined transition such as:

- cable gland;
- gasketed pass-through;
- sealed bulkhead fitting;
- labyrinth entry;
- compressive seal around a protected cable route.

The exact method depends on the final cable and enclosure revision.

The cable should not enter through an upward-facing unprotected hole where water can collect directly above the opening.

## Load path

Solar loads should be transferred into reinforced enclosure features.

Thin decorative walls should not carry the full bending load from the panel.

The CAD model should show a clear structural path from:

```text
Panel
  ↓
Support
  ↓
Reinforced attachment
  ↓
Main enclosure structure
```

Where possible, support loads should connect into ribs, thicker bosses, internal frames, or other reinforced geometry.

## Panel angle

The final panel angle should balance energy requirements, product architecture, drainage, and mechanical loading.

Mechanical documentation should not claim an optimum solar angle unless it is based on the deployment location and energy model.

From a mechanical perspective, the chosen angle affects:

- centre of pressure in wind;
- water shedding;
- overall height;
- centre of mass;
- support length;
- visibility;
- transport volume.

The solar-energy design and deployment documentation should determine the operational angle requirements.

## Wind and leverage

A panel can act as a lever above the enclosure.

Even a lightweight panel can generate significant bending moment when mounted away from the main body.

Testing should therefore consider:

- panel area;
- support height;
- support spacing;
- enclosure mounting strength;
- wind exposure;
- repeated oscillation;
- fastener loosening.

The unit should not be assumed wind-resistant until the complete assembly and site mounting method have been tested.

## Fasteners and joints

Panel supports should use repeatable joints.

Potential joint types include:

- screws into inserts;
- through-bolts with captive nuts;
- keyed printed interfaces with retaining screws;
- replaceable brackets.

The design should avoid relying on a friction fit alone where the solar panel could become loose during transport or outdoor exposure.

## Replaceability

Solar supports are exposed and therefore likely to experience more mechanical stress than internal components.

They should be individually replaceable where practical.

A modular support strategy allows:

- damaged parts to be replaced cheaply;
- revised panel geometry to use new adapters;
- transport with the panel removed;
- future solar upgrades without replacing the main enclosure.

## Cable strain relief

The solar cable should be secured on both sides of the enclosure transition so movement of the panel does not pull directly on the PCB or internal connector.

Strain relief should be located close to:

- the panel connector or cable exit;
- the enclosure entry;
- the internal termination point if needed.

Enough service slack should remain for disassembly.

## Water management

The solar structure can create new paths for water to travel toward the enclosure.

Design should avoid:

- channels that guide water directly into the cable opening;
- upward-facing cavities that remain full after rain;
- closed printed pockets with no drainage;
- support joints that depend on raw print surfaces alone for sealing.

Where a hollow support contains the cable, its geometry should either exclude water or provide a controlled drainage path that does not lead into electronics.

See [Waterproofing](waterproofing.md).

## Manufacturing constraints

Each support and solar-mount component should remain inside the project's approximate 250 × 250 × 250 mm single-object manufacturing envelope.

Small replaceable supports are generally easier to:

- orient for print strength;
- reprint after failure;
- revise;
- transport;
- test independently.

The panel itself is a purchased or separately fabricated component and should be represented in CAD using the real manufacturer dimensions before the mount is frozen.

## Print orientation

If supports are additively manufactured, layer orientation matters because the support experiences bending.

A support should not be printed in an orientation that places the primary tensile load entirely across weak inter-layer bonds without validation.

Different orientations should be compared for:

- bending strength;
- fastener pull-out;
- dimensional accuracy;
- surface quality at mating faces;
- support-material requirements.

## Assembly sequence

A representative assembly process is:

1. prepare the panel and cable;
2. route the cable through the hollow support;
3. install the support hardware;
4. attach the three supports to the panel or panel frame;
5. secure the supports to the enclosure;
6. complete the protected cable entry;
7. connect internal power hardware;
8. apply strain relief;
9. verify mechanical stability;
10. perform electrical and charging tests.

The final process should be updated to match the released design.

## Validation

The solar mechanical assembly should be validated for:

- static load;
- repeated handling;
- fastener retention;
- support flex;
- cable chafing;
- cable replacement;
- water exposure around the cable path;
- transport with panel attached and/or removed;
- interaction with enclosure service access.

The mechanical system should also be checked to ensure it does not obstruct the intended radar coverage.

## Related documentation

See:

- [Power System](../origin-core/power-system.md)
- [Enclosure](enclosure.md)
- [Waterproofing](waterproofing.md)
- [CAD](cad.md)
- [Manufacturing](manufacturing.md)

The third support's integrated cable path is a defining requirement of the current design. It should be developed as an engineered cable-management and structural feature, not as an empty decorative column.