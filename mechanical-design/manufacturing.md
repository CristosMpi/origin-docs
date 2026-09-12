# Manufacturing

ORIGIN's mechanical manufacturing workflow should convert the CAD model into repeatable physical parts with known material, orientation, tolerances, hardware, and inspection requirements.

The current project uses additive manufacturing heavily, but the architecture should remain compatible with other processes where they provide an advantage, including laser cutting, CNC machining, sheet fabrication, and partner-manufactured parts.

## Manufacturing principles

A mechanical part is not ready for release simply because it can be exported from CAD.

A repeatable manufacturing release should define part revision; source CAD revision; material; manufacturing process; orientation; relevant process settings; inserts and hardware; post-processing; inspection criteria; and known limitations.

## Manufacturing envelope

The current ORIGIN development constraint is that no single manufactured object should exceed approximately **250 × 250 × 250 mm**.

This limit should be checked at CAD level before manufacturing files are released.

Where an assembly exceeds the limit, it should be split intentionally into parts such as main shell sections; service cover; internal electronics tray; sensor bezels; solar supports; base components; and module adapters.

Part splitting should improve assembly and serviceability rather than create weak arbitrary seams.

## Additive manufacturing

3D printing is well suited to ORIGIN because the enclosure uses custom geometry, sensor-specific mounting features, and relatively low production quantities during development.

Additive manufacturing is particularly useful for enclosure prototypes; internal carriers; radar mounts; solar brackets; cable guides; BIT adapters; assembly fixtures; and test coupons.

## Print orientation

Print orientation should be specified for structural parts.

Orientation affects layer strength; dimensional accuracy; surface quality; support requirements; insert installation; sealing performance; and print time.

A mechanically loaded support should be oriented so its most important load path does not depend unnecessarily on weak inter-layer separation.

The chosen orientation should also allow critical mating surfaces to print accurately or be post-processed.

## Layer and wall strategy

Exact print settings depend on the selected material and machine, so these values should be stored in the manufacturing profile rather than hard-coded in this overview.

Important parameters include layer height; perimeter/wall count; top/bottom thickness; infill type and percentage; extrusion width; nozzle diameter; print temperature; bed temperature; and chamber conditions where applicable.

Structural parts should be designed around **walls and geometry**, not only high infill percentage.

## Test coupons

Before manufacturing the full enclosure in a new material or profile, small test coupons can validate hole size; insert fit; screw clearance; sliding tolerance; gasket groove dimensions; layer adhesion; and surface sealing.

This reduces the cost of discovering process errors after a long print.

## Threaded inserts

Where heat-set inserts are used, the manufacturing package should specify insert type; target hole size; installation tool; installation temperature or process guidance; final depth; and alignment check.

Insert bosses should be inspected for cracking or deformation after installation.

## Support removal

Support material should not be placed where removal risks damaging sealing surfaces; sensor windows; cable passages; threaded features; and tight internal channels.

CAD should reduce unnecessary support through geometry where practical.

If support is unavoidable, the manufacturing instructions should identify how it is removed and which surfaces require cleanup afterward.

## Surface finishing

Post-processing may include deburring; sanding; support removal; insert installation; gasket installation; coating or painting; sealing treatment; and label application.

Surface finishing should not unintentionally alter critical dimensions.

For example, paint or coating on a tight sliding joint or gasket surface can change fit.

## Radar-facing surfaces

Any part or coating placed in front of the C4001 radars should be treated as a sensing-critical component.

Manufacturing variation in wall thickness; material; coating; moisture absorption; and surface geometry.

may affect radar performance.

Radar-facing parts should therefore be controlled by revision and validated after manufacturing changes.

## Cable passages

The hollow solar support and other cable channels require special inspection because long internal passages can be partially blocked by print defects or support material.

Inspection should confirm full passage clearance; cable can be inserted without damage; required bend radius is achievable; no sharp internal burrs or strings remain; and entry and exit geometry matches the seal design.

A physical cable-pull test is more useful than visual inspection alone.

## Watertight manufacturing

A watertight CAD model does not guarantee a watertight printed part.

Process quality can affect leakage through under-extrusion; poor layer bonding; thin walls; seam placement; warped mating surfaces; and inconsistent gasket compression.

If a release requires water resistance, manufacturing validation should include leak or spray testing of actual printed assemblies.

See [Waterproofing](waterproofing.md).

## Laser-cut parts

Laser cutting may be useful for flat panels; internal plates; templates; gaskets from suitable sheet material; alignment fixtures; and decorative or identification elements.

Flat-part drawings should define material thickness and tolerances.

If acrylic or another brittle sheet is used structurally, fastener stresses and cracking should be considered.

## CNC or machined parts

CNC machining may be appropriate for high-load brackets; precise mounts; metal base interfaces; repeatable production parts; and components requiring better dimensional accuracy than a printed prototype provides.

Machined parts should be released with drawings or STEP geometry and critical tolerances.

Sponsor or partner fabrication should still use controlled revision files.

## Hardware kitting

A mechanical build should have a hardware kit or BOM that includes screws; nuts; washers; threaded inserts; spacers; gaskets; cable glands/grommets; clips and strain-relief hardware; and adhesives or sealants where specified.

Missing hardware should not be substituted informally without checking fit and material compatibility.

## Incoming inspection

Manufactured parts should be inspected before final assembly.

Useful checks include correct revision marking; no major warping; critical dimensions within expected tolerance; holes clear; insert bosses intact; cable passages open; mating surfaces flat enough for assembly; sensor openings clean; no cracks around fasteners; and no severe layer separation.

## First-article assembly

The first part from a new revision or manufacturing process should receive a full assembly test before multiple copies are produced.

The first-article check should verify Rosetta fit; radar fit and screw alignment; cable routing; service cover closure; BIT interface access; solar support attachment; hollow cable support usability; base/mount fit; fastener access; and no assembly collisions.

## Process changes

A change in printer, filament, slicer profile, orientation, or post-processing can change the physical result even when the CAD file is identical.

Important process changes should therefore be documented.

Where the change affects critical features, selected validation tests should be repeated.

## Build records

For important prototypes and deployment units, a simple manufacturing record should capture unit identifier; mechanical revision; material; manufacturing date; machine/profile; operator; notable deviations; inspection result; and rework performed.

This helps connect field failures to manufacturing history.

## Assembly after manufacturing

A typical final mechanical assembly workflow is:

1. inspect all printed/fabricated parts;
2. remove supports and clean interfaces;
3. install inserts and captive hardware;
4. verify cable passages;
5. install radar mounts;
6. install internal electronics carrier;
7. route internal cables;
8. install module interface hardware;
9. install gaskets or seals;
10. assemble solar supports and cable route;
11. perform dry-fit closure;
12. install electronics;
13. complete electrical tests;
14. close the enclosure;
15. perform mechanical and environmental checks.

The actual released work instruction should match the final CAD revision.

## Quality gates

A mechanical unit should not move to deployment solely because assembly was possible.

Recommended quality gates include:

### Geometry gate

All critical parts fit and fasteners engage correctly.

### Sensor gate

All three radars are seated and correctly oriented.

### Cable gate

No cable is pinched, over-bent, or unsupported.

### Service gate

The required covers and module interfaces can be accessed.

### Structural gate

Solar supports and enclosure mount are secure.

### Environmental gate

Seals and known ingress points pass the required development test.

### Final functional gate

The complete ORIGIN system powers and passes the relevant bring-up checks.

## File release package

A manufacturing release should ideally include source CAD revision; STEP assembly; STL/3MF files for printed parts; drawings where useful; manufacturing notes; material list; hardware BOM; assembly instructions; revision history; and validation status.

This makes the mechanical design reproducible outside the original CAD workstation.

## Related documentation

See [CAD](cad.md); [Materials](materials.md); [Enclosure](enclosure.md); [Waterproofing](waterproofing.md); [Installation & Deployment](../installation-deployment/README.md); and [Testing & Validation](../testing-validation/README.md).

ORIGIN's manufacturing process should remain flexible enough for rapid student-led iteration while still adopting the documentation discipline needed for repeatable, field-ready hardware.
