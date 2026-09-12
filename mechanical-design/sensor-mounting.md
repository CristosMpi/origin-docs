# Sensor Mounting

Sensor mounting is one of the most important parts of ORIGIN's mechanical design because the physical orientation of a sensor becomes part of the sensing system itself.

The current ORIGIN Core concept integrates **three DFRobot C4001 24 GHz mmWave sensors**. These modules include PCB mounting holes, so the enclosure should locate them using repeatable mechanical features rather than adhesive-only placement or free cable support.

## Why mounting accuracy matters

A radar can only be interpreted correctly if its position and orientation are known.

If the same sensor is installed at a different angle after maintenance, the monitored area changes even when the firmware configuration stays the same.

For that reason, the mount should define sensor position; sensor angle; sensor face direction; stand-off from the enclosure wall; connector orientation; and mechanical datum surfaces.

These values become part of deployment and validation documentation.

## Three-sensor architecture

The current concept uses three radar modules distributed around the upper enclosure.

Each should have a stable logical identity such as:

```text
RADAR_A
RADAR_B
RADAR_C
```

When final orientation is frozen, direction-based names may be more useful if they remain unambiguous during installation.

The mechanical drawing, firmware mapping, and test logs should all use the same identity scheme.

## Preferred mounting method

A suitable mount should include dedicated screw bosses or inserts aligned to the sensor PCB holes; a locating surface that prevents board rotation; controlled clearance behind the PCB; clearance around the connector; access for installation tools; a defined front opening or radar-transparent window; and enough space to remove the board without disassembling unrelated hardware.

The board should not be clamped in a way that bends it.

## Avoid adhesive-only mounting

Adhesive can be useful as secondary vibration control, but it should not be the primary method for defining radar orientation where repeatability matters.

Adhesive-only mounting can introduce angular variation between units; uncertain stand-off; difficult replacement; damage during removal; long-term creep; and surface-preparation dependence.

Mechanical location features provide a more reproducible reference.

## Opening geometry

The enclosure concept intentionally includes dedicated sensor openings.

The opening should be designed around the sensing face rather than simply cut to match the outline of the PCB.

Key considerations include obstruction of the field of view; opening depth; surrounding ribs; fastener heads; conductive inserts; decorative features; water shielding; and debris accumulation.

The opening should be validated with the complete sensor installed in the final enclosure material.

## Recessed mounting

Recessing the radar can protect it from direct contact and improve appearance, but excessive recess depth may narrow the effective field of view or create unwanted interaction with surrounding geometry.

A recessed design should therefore be evaluated through coverage testing.

Useful variables to record include recess depth; opening width; opening height; face angle; and sensor-to-opening distance.

## Fasteners

Fasteners should be selected to avoid damaging the PCB and to support repeated maintenance.

The design should consider screw diameter compatible with the mounting holes; non-interference with nearby components; washer use where needed; insert or captive-nut retention; access from the service side; and repeatable tightening without PCB distortion.

Exact screw dimensions should be released with the final sensor-mount drawing rather than inferred from this overview.

## Cable strain relief

The sensor connector and PCB should not carry cable tension.

Each radar cable should have a nearby strain-relief point so pulling or vibration is transferred into the enclosure rather than the sensor connector.

A good cable path should avoid sharp bends; avoid screw paths; remain clear of the sensing face; allow enough service slack to remove the board; and prevent the cable from rattling against the shell.

## Mechanical datum strategy

A repeatable mount benefits from simple datums.

For example one rear reference plane controls depth, one side feature controls rotation, screw holes retain the board, and the exterior face defines the sensing direction.

This is more reliable than locating the sensor only by two screws with oversized clearance holes.

## Alignment and assembly

The assembly process should include an orientation check.

A simple inspection can verify correct sensor identity; correct face direction; no flipped connector orientation; no obstruction in front of the sensor; cable secured; and board seated against its intended datums.

For repeated builds, photos or a simple assembly fixture can improve consistency.

## Replacement

Sensors should be replaceable without destroying the enclosure.

A replacement procedure should allow the technician to:

1. open the relevant service area;
2. disconnect the radar cable;
3. remove the sensor fasteners;
4. install the replacement against the same datums;
5. reconnect the cable;
6. verify sensor identity in software;
7. perform a functional and coverage check.

If replacement changes the orientation, the deployment may require recalibration or revalidation.

## Environmental protection around sensors

Sensor mounting and waterproofing are connected problems.

Potential strategies around a radar opening include a recessed face; an overhanging lip; labyrinth geometry; a replaceable protective window; a gasketed bezel; and drainage below the opening.

Any cover material placed in front of the radar must be tested for its effect on detection rather than assumed to be transparent.

See [Waterproofing](waterproofing.md).

## Cross-sensor consistency

With three sensors, small mounting differences can produce different coverage even when all electronics are identical.

Mechanical validation should therefore compare sensor A coverage; sensor B coverage; sensor C coverage; overlap zones; blind zones; and repeated assembly after removal and replacement.

The objective is not only to prove that each radar works, but to show that the **mechanical installation is reproducible**.

## Testing procedure

A practical mounting validation should include:

### Fit test

Confirm the PCB, screws, connector, and cable fit without interference.

### Orientation test

Measure or verify the intended face angle.

### Coverage test

Test presence and motion at known positions around the assembled enclosure.

### Reassembly test

Remove and reinstall the sensor, then repeat selected coverage points.

### Environmental inspection

Check whether the mount or opening traps water or debris.

### Vibration/handling test

Verify that normal handling does not loosen the sensor or change orientation.

## CAD requirements

The released CAD should show PCB reference geometry; hole locations; mount bosses; opening geometry; cable path; fasteners; sensor identity/orientation; and service access.

A decorative external model without the internal sensor interfaces is not sufficient engineering documentation.

## Related documentation

See [Presence Detection](../origin-core/presence-detection.md); [Sensor System](../origin-core/sensor-system.md); [Enclosure](enclosure.md); [CAD](cad.md); and [Testing & Validation](../testing-validation/README.md).

The sensor mount should be treated as a precision interface relative to the rest of the 3D-printed enclosure: simple to manufacture, easy to replace, and repeatable enough that software and field tests can trust its orientation.
