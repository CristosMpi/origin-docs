# Sponsors

Project ORIGIN is supported by technology and manufacturing companies that contribute tools, fabrication capability, materials, equipment, or technical resources to Team Galene's development process.

The current official sponsor lineup is **Xometry**; **AISLER**; **eSUN**; **SCULPFUN**; **EasyEDA**; **JLCPCB**; and **Matter and Form**.

This page describes the role of each sponsor at a project level. It intentionally does not publish confidential voucher codes, private commercial terms, personal contact information, or internal correspondence.

## Xometry

**Xometry** supports ORIGIN in the manufacturing and prototyping part of the development process.

Industrial fabrication becomes important when a design moves beyond simple workshop prototypes and begins to require more repeatable manufacturing methods, tighter tolerances, or processes that are not practical to perform in-house.

For ORIGIN, this type of support is relevant to areas such as mechanical prototyping; manufactured enclosure or mounting components; CNC-oriented design workflows; fabrication planning; and design-for-manufacturing review.

The exact manufacturing process used for any ORIGIN part should still be recorded in the corresponding Mechanical Design or manufacturing documentation rather than inferred from the sponsorship itself.

## AISLER

**AISLER** supports the electronics development workflow around PCB manufacturing.

This is directly relevant to **Rosetta**, ORIGIN's custom electronics platform, where design files must move through fabrication, assembly preparation, inspection, and revision.

AISLER support contributes to the team's ability to work with professional PCB production processes, including prototype fabrication and the surrounding manufacturing workflow.

This sponsorship does not mean every Rosetta revision is automatically production-ready. Fabrication readiness remains governed by the release checks documented under [Rosetta Manufacturing](../rosetta/manufacturing.md).

## eSUN

**eSUN** supports ORIGIN with **3D-printing materials** used in mechanical development and prototyping.

Additive manufacturing is central to ORIGIN because the project requires repeated iteration of enclosure concepts; sensor mounts; brackets; internal supports; module interfaces; cable-routing features; fit-check parts; and demonstration hardware.

Material sponsorship helps the team iterate quickly, but final material selection for field deployment must still follow the requirements documented under [Materials](../mechanical-design/materials.md) and [Environmental Testing](../testing-validation/environmental-testing.md).

A prototype printed successfully is not, by itself, evidence that the material is suitable for long-term outdoor deployment.

## SCULPFUN

**SCULPFUN** supports Team Galene with laser-based fabrication and workshop capability.

Laser equipment can contribute to ORIGIN development through activities such as rapid fabrication of flat parts; templates and fixtures; engraving and labeling; workshop organization; prototype panels; manufacturing aids; and presentation and demonstration materials.

Laser fabrication is one of several processes available to the project and should be selected based on the actual material, tolerance, structural, and safety requirements of the part being produced.

## EasyEDA

**EasyEDA** supports the electronic design workflow used around ORIGIN PCB development.

The project has used professional PCB-design tooling while developing and revising Rosetta. This includes the practical work of schematic organization; PCB layout; footprint management; design-rule review; manufacturing-output preparation; component/library management; and design revision.

Software tooling assists the engineering process, but it does not replace schematic review, electrical validation, design-rule checking, manufacturing review, or first-article testing.

For the current state of Rosetta, see [Rosetta v2](../rosetta/rosetta-v2.md).

## JLCPCB

**JLCPCB** supports the PCB manufacturing and electronics prototyping ecosystem used by Team Galene.

Its relevance to ORIGIN includes the transition from PCB design data toward fabricated or assembled electronics.

ORIGIN Docs deliberately preserve manufacturing problems as part of the engineering record. In particular, the reviewed Rosetta v2 fabrication export documented in this repository lacked drill data and was therefore treated as an incomplete production package.

That issue is not hidden by the sponsorship relationship; it is documented because sponsor support and engineering validation are separate.

See [Rosetta Manufacturing](../rosetta/manufacturing.md), [Known Issues](../development/known-issues.md), and [Electronics Testing](../testing-validation/electronics-testing.md).

## Matter and Form

**Matter and Form** supports ORIGIN through **3D scanning technology**.

3D scanning can assist the project where a physical object, prototype, interface, or reference geometry needs to be captured digitally for analysis or design work.

Potential ORIGIN workflows include recording prototype geometry; comparing manufactured parts with intended geometry; creating digital references for mechanical design; supporting fit and interface work; documenting physical development stages; and assisting workflows where existing geometry must be understood before designing around it.

A scan should be treated as measurement/reference data whose accuracy depends on the scanner, setup, object surface, calibration, processing, and intended use. Critical mechanical dimensions should still be verified with appropriate measurement methods before manufacture.

## Sponsor-to-workflow map

| Sponsor | Primary ORIGIN development area |
|---|---|
| Xometry | Manufacturing and mechanical prototyping |
| AISLER | PCB fabrication and electronics manufacturing workflow |
| eSUN | 3D-printing materials and additive prototyping |
| SCULPFUN | Laser fabrication and workshop prototyping |
| EasyEDA | PCB design workflow |
| JLCPCB | PCB manufacturing / electronics prototyping |
| Matter and Form | 3D scanning and physical-to-digital reference workflows |

The table describes each sponsor's relevance to ORIGIN at a high level. It is not a substitute for the detailed engineering record of which process, material, tool, or revision was used for a specific part.

## Sponsorship does not equal certification

The following statements should **not** be inferred from inclusion on this page that a sponsor designed ORIGIN; that a sponsor certified ORIGIN; that a sponsor validated ORIGIN's performance; that a sponsor accepts responsibility for Team Galene's engineering decisions; that every sponsor product is used in the final deployed configuration; and that the sponsor endorses every statement in ORIGIN Docs.

Technical responsibility remains with Team Galene.

## Public disclosure policy

When describing sponsor support, Team Galene may publish information such as sponsor name; general type of support; equipment or manufacturing category; public project outcomes created using that support; and publicly agreed acknowledgement content.

The team should not publish private coupon or voucher codes; account numbers; private email addresses; personal telephone numbers; confidential quotations; unpublished shipping data; and contract terms not intended for public release.

## Brand assets

All sponsor names, logos, and trademarks belong to their respective owners.

The official ORIGIN sponsor graphic should remain consistent with the current approved sponsor list. If the sponsor lineup changes, both the graphic and this documentation should be updated together.

## Keeping this page current

Before adding or removing a sponsor, maintainers should confirm the relationship status and update:

1. this page;
2. the Partners & Sponsors overview;
3. Team Galene's official sponsor graphic;
4. relevant website/social sponsor listings where applicable;
5. acknowledgements when the change affects project credits.

The purpose is to maintain a single consistent public record rather than allowing different channels to show conflicting sponsor lists.
