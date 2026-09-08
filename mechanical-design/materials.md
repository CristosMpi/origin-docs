# Materials

Material selection for ORIGIN should follow the deployment environment and manufacturing process rather than defaulting to whichever filament or sheet is easiest to obtain.

The enclosure, brackets, solar supports, inserts, gaskets, fasteners, and protective windows each have different requirements. A single material is unlikely to be ideal for every mechanical function.

## Material-selection criteria

Every material choice should consider:

- outdoor temperature range;
- sunlight and UV exposure;
- moisture;
- mechanical load;
- impact and handling;
- printability or machinability;
- dimensional stability;
- electrical properties where relevant;
- radar interaction where the material is in front of a mmWave sensor;
- compatibility with sealants and gaskets;
- maintenance and replacement cost;
- appearance at the deployment site.

The selected material and manufacturing process should be recorded with each released CAD revision.

## 3D-printed enclosure materials

Additive manufacturing is currently an important fabrication method for ORIGIN prototypes and custom parts.

Common candidate material families include:

### PLA-family materials

PLA is useful for fast prototyping because it is easy to print and provides good dimensional quality on many machines.

It is suitable for:

- geometry validation;
- internal mock-ups;
- visual prototypes;
- low-risk test fixtures;
- early sensor-mount iterations.

Standard PLA should not automatically be selected for long-term outdoor structural parts without validating temperature and environmental behaviour for the intended site.

### PETG-family materials

PETG can be a practical candidate for outdoor-oriented prototypes because it generally provides more toughness and temperature tolerance than basic PLA while remaining accessible to print.

It may be suitable for:

- enclosure shells;
- brackets;
- cable guides;
- replaceable bezels;
- service parts.

Print settings, dimensional behaviour, and sealing still need to be validated on the actual equipment.

### ASA / outdoor-oriented polymers

ASA and similar materials may be appropriate when UV exposure and outdoor durability are priorities.

They can require more controlled printing conditions than PLA or PETG.

Before using them in a release design, Team Galene should verify:

- printer capability;
- warping;
- dimensional accuracy;
- layer adhesion;
- surface quality;
- fit with inserts and fasteners.

### Engineering polymers

More advanced polymers may be useful for high-temperature or highly loaded parts, but they should only be introduced when the added manufacturing complexity solves a real requirement.

Material sophistication is not a substitute for good geometry.

## Current sponsorship material

Team Galene has received support from filament manufacturers including eSUN. Sponsored materials can be valuable for prototyping and production, but the project should still document the exact material grade used for each released part rather than referring only to the manufacturer brand.

## Structural vs cosmetic parts

Different enclosure parts can use different materials.

For example:

- main shell: environmental and dimensional priorities;
- solar supports: stiffness and fatigue priorities;
- sensor bezel: dimensional accuracy and weather exposure;
- internal electronics tray: dimensional stability and heat resistance;
- decorative skin: appearance and low mass;
- module latch: toughness and repeated-cycle performance.

This avoids overengineering low-load parts or underengineering structural ones.

## Fasteners

External fasteners should be selected for the deployment environment.

Considerations include:

- corrosion resistance;
- galvanic compatibility with inserts or brackets;
- repeated service;
- strength;
- availability;
- standardisation across the product.

The final hardware list should identify exact screw, washer, nut, and insert specifications.

## Threaded inserts

Heat-set or mechanically retained inserts can improve repeated service of printed parts.

Their use should be validated for:

- pull-out strength;
- surrounding wall thickness;
- installation temperature;
- insert alignment;
- crack resistance;
- repeated screw cycles.

Insert installation should be treated as a manufacturing process with a defined tool and procedure.

## Gaskets and seals

Gasket material should be selected based on:

- compression behaviour;
- temperature;
- water resistance;
- UV exposure if external;
- chemical compatibility;
- recovery after repeated opening;
- adhesive backing, if used.

A gasket should be treated as a replaceable part when service access repeatedly compresses it.

## Cable materials

External cables should be suitable for the expected environment and should not become the weak point of an otherwise protected enclosure.

Mechanical design should account for:

- jacket flexibility;
- UV exposure;
- water exposure;
- bend radius;
- abrasion;
- temperature;
- connector strain relief.

## Sensor-window materials

Any material placed directly in front of a radar sensor requires special attention.

Mechanical transparency, visual appearance, and water resistance are not enough. The material must be tested with the **actual C4001 sensor** and final thickness/spacing.

Testing should compare:

- detection range;
- false detections;
- field-of-view changes;
- reflection effects;
- behaviour when wet;
- repeated environmental exposure.

Until such testing exists, a material should not be described as validated for the radar window.

## Internal insulation and spacers

Internal spacers, washers, or insulating barriers may be used where electronics require separation from conductive hardware or shell features.

These components should be included in the assembly BOM rather than added informally during construction.

## Adhesives

Adhesive use should be limited to roles where it offers a clear benefit.

Examples may include:

- secondary vibration control;
- gasket retention;
- cable management;
- decorative elements;
- non-serviceable low-load joints.

Adhesive should not replace a mechanical locating feature for critical sensors or structural parts.

Documentation should record the adhesive type and surface preparation if the joint is important.

## Coatings and finishes

Coatings can improve appearance, UV performance, sealing, or surface cleanability, but they also add process variation.

Potential finishes should be tested for:

- adhesion to the base material;
- cracking during flex;
- colour stability;
- interaction with gaskets;
- effect on radar-facing surfaces;
- repairability.

Paint should not be applied over radar windows without validation.

## Colour and thermal behaviour

ORIGIN's visual identity may use neutral or archaeology-inspired colours, but dark external surfaces can absorb more solar energy than light surfaces.

Where thermal loading matters, colour choice should be evaluated together with enclosure temperature tests.

Appearance and thermal performance are therefore connected design variables.

## Material traceability

For repeatable builds, manufacturing records should include:

- material manufacturer;
- material grade;
- colour;
- batch or spool identification where useful;
- drying requirements;
- print profile;
- post-processing;
- part revision.

If a different material is substituted, the change should be documented and critical mechanical/environmental tests repeated where appropriate.

## Material validation

Useful validation can include:

- tensile or bending coupons;
- insert pull-out tests;
- screw-cycle tests;
- drop/impact testing;
- water exposure;
- UV ageing where practical;
- thermal cycling;
- dimensional measurement after printing;
- outdoor exposure samples.

The purpose is not to generate material-science data for its own sake. It is to confirm that the selected material behaves acceptably in the actual ORIGIN geometry and manufacturing workflow.

## Related documentation

See:

- [Enclosure](enclosure.md)
- [Waterproofing](waterproofing.md)
- [Manufacturing](manufacturing.md)
- [CAD](cad.md)
- [Testing & Validation](../testing-validation/README.md)

Material selection should remain revision-specific. The public documentation can describe candidate materials and selection criteria, while the released manufacturing package should state exactly what each production part is made from.