# Design Philosophy

ORIGIN's mechanical design follows one central idea: **the enclosure is part of the system, not packaging around it**.

The outer form determines sensor orientation, service access, environmental exposure, cable routing, mounting stability, thermal behaviour, and how confidently the device can be installed in the field. For that reason, Team Galene develops the mechanical system together with the electronics and sensing architecture rather than treating CAD as a final cosmetic stage.

## 1. Function before decoration

ORIGIN is intended to have a recognisable appearance, but visual identity cannot override sensing, maintenance, or structural requirements.

The preferred design direction is deliberately more architectural than a conventional rectangular enclosure. Tall, tapered, faceted, and pyramid-influenced forms are being explored because they can make ORIGIN visually distinctive while also creating useful directional faces for sensors and structural transitions.

However, every visual feature should justify itself through at least one of the following: sensor placement; structural stiffness; cable routing; service access; weather shedding; mounting; manufacturing; and product identity that does not interfere with function.

If a feature makes the device harder to build, seal, inspect, or validate without adding enough value, it should be simplified.

## 2. Height over unnecessary width

The current design preference is for a **taller, narrower product** rather than a low and bulky one.

This supports several project goals smaller ground footprint; better separation between lower mounting hardware and upper sensing regions; more useful vertical internal packaging; improved access to side-mounted module interfaces; a clearer visual identity; and easier use of multiple angled sensor faces.

A tall design still needs stability. The base, mounting method, mass distribution, and solar-panel loading must therefore be considered together.

## 3. Sensor-first geometry

Sensor performance is a primary mechanical constraint.

The current ORIGIN design integrates three DFRobot C4001 24 GHz mmWave sensors. Their orientation should be defined by the enclosure geometry, not improvised during assembly.

This means CAD must answer questions such as What direction does each radar face? What material lies in front of it? Is the opening large enough for the intended field of view? Can nearby fasteners or ribs influence the sensing region? Can the PCB be replaced without changing its angle? Can each radar be identified consistently in software and test documentation?

The sensor mounting system therefore becomes part of the calibration and validation process.

## 4. Serviceability is a design requirement

ORIGIN should be maintainable after deployment.

A design is not considered successful merely because all components fit inside it once.

The enclosure should allow technicians or team members to open the unit without destroying the shell; inspect Rosetta; reach connectors; replace a radar module; inspect cable strain relief; access fasteners with normal tools; replace a damaged external part without replacing the complete system; reconnect a module correctly; and close the enclosure again without relying on improvised sealing.

This is particularly important for a project intended for iterative field testing.

## 5. Accessible modularity

The BITs interface should remain reachable after ORIGIN is installed.

Placing the attachment point on the bottom of the enclosure is unsuitable when the device is inserted into soil, fixed close to the ground, or otherwise mounted in a way that blocks the underside.

The current mechanical philosophy therefore favours a **side or raised-access module interface**.

This principle generalises beyond BITs: expansion interfaces should be positioned based on real installation conditions, not only CAD symmetry.

## 6. Deliberate environmental trade-offs

A completely sealed enclosure is attractive from a waterproofing perspective, but the sensing system may require openings or carefully selected transmission windows.

ORIGIN therefore does not treat environmental protection as a marketing label. Instead, the design should identify the actual ingress paths and manage them deliberately.

For example, a sensor opening may be accepted if it improves validated radar performance, provided the surrounding geometry includes appropriate shielding, drainage, recesses, membranes, covers, or other protection strategies where needed.

The important requirement is that the trade-off is **documented and tested**.

## 7. Mechanical and electrical co-design

Rosetta v2 is approximately 105 × 100 mm, so its mounting pattern, connector orientation, and cable paths strongly affect the enclosure interior.

Mechanical design should be updated whenever an electrical change modifies board dimensions; mounting-hole positions; connector locations; antenna clearance; battery or power routing; sensor headers; SD/SIM access; and service requirements.

Likewise, mechanical constraints should feed back into PCB decisions where possible.

This prevents the common failure mode where a board and enclosure are each valid independently but difficult to assemble together.

## 8. Design for available manufacturing

The current project constraint is that no single manufactured object should exceed approximately **250 × 250 × 250 mm**.

Rather than treating this as a limitation to hide, ORIGIN should use it to encourage a modular mechanical architecture.

Large assemblies can be divided into central shells; removable covers; sensor bezels; solar supports; base components; module adapters; and service panels.

A multi-part assembly can be superior to a one-piece print when it improves orientation, strength, repairability, or surface quality.

## 9. Replaceable wear and exposed parts

External parts are more likely to suffer damage than protected internal electronics.

Therefore, components such as solar supports; external brackets; sensor covers; module latches; mounting feet; and cable guides.

Should be replaceable where practical.

This reduces maintenance cost and lets the system evolve without requiring a complete enclosure redesign.

## 10. Avoid hidden assembly traps

CAD models often look valid while containing practical assembly problems.

Every major revision should be checked for trapped screws; connectors blocked after another component is installed; cables that cannot be inserted after assembly; fasteners requiring impossible tool angles; covers that cannot be removed without disconnecting unrelated parts; parts that collide only during insertion; insufficient tolerance for printed parts; and inaccessible module latches.

An exploded assembly and a real assembly sequence should be maintained alongside the finished model.

## 11. Build for revision

ORIGIN is an evolving system.

The mechanical design should therefore make revision inexpensive.

Stable elements should be separated from likely-to-change elements. For example the central electronics volume can remain stable while sensor bezels evolve, a module interface can use an adapter rather than reshaping the entire shell, the solar panel can use a replaceable support assembly, and internal trays can be revised independently of the exterior skin.

This approach makes iteration faster and reduces the risk that one component change invalidates the entire design.

## 12. Heritage-site awareness

ORIGIN is intended for cultural-heritage environments, so the physical product should avoid unnecessary visual or physical intrusion.

Mechanical design should consider compact footprint; reversible installation where possible; minimal permanent intervention; clear distinction between modern equipment and historic fabric; low-maintenance mounting; cable management; safe edges and exposed hardware; and avoidance of unnecessary contact with protected surfaces.

Final installation methods must always be adapted to site requirements and approved procedures.

## 13. Validate, do not assume

Mechanical claims should come from tests.

Examples include whether a sensor opening affects water ingress; whether a solar support is stiff enough; whether a printed latch survives repeated use; whether the enclosure resonates or vibrates; whether radar coverage matches the intended geometry; and whether a part remains dimensionally stable after environmental exposure.

The design process is therefore:

```text
Requirement
   ↓
CAD concept
   ↓
Prototype
   ↓
Assembly test
   ↓
Functional test
   ↓
Environmental / field test
   ↓
Revision
```

## Summary

ORIGIN's mechanical design philosophy is based on five priorities:

**sensor performance, serviceability, modularity, manufacturability, and honest validation.**

The distinctive architecture is important, but it is valuable only when it helps create a better field system.

Continue with [Enclosure](enclosure.md) for the current physical architecture.
