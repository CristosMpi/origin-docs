# Calibration

Calibration adapts ORIGIN to the real behavior of the installation site. It is the stage where sensor orientation, thresholds, baselines, timing, and event interpretation are checked against known conditions rather than assumed from bench tests.

Calibration should be repeatable and documented. Values should not be adjusted until the system “looks right” without recording what changed and why.

## Calibration objectives

Calibration should establish which sensors are operating correctly; what the local baseline looks like; whether the three radar directions match the intended monitored zones; whether environmental readings are plausible for their placement; what thresholds are appropriate for the site; whether overlapping sensor behavior is acceptable; whether false detections or blind zones exist; and whether configuration changes improve performance without creating new failure modes.

## Baseline period

Before changing thresholds, observe the installed system under normal site conditions.

Record a baseline that includes, where practical empty/quiet periods; normal visitor movement; normal staff activity; typical environmental variation; expected communications interruptions; and day/night or open/closed operating states.

The baseline should be long enough to capture realistic site behavior. A few minutes of quiet testing is not sufficient evidence for long-term deployment behavior.

## Presence-detection calibration

The current Core design uses multiple C4001 mmWave radars. Each radar should be calibrated and validated independently before evaluating multi-sensor logic.

For each radar, define test positions and perform repeatable passes.

Test at least approach toward the sensor; departure from the sensor; lateral movement; slow movement; stationary or near-stationary presence where supported; targets near the expected coverage edge; and areas expected to remain outside the monitored zone.

Record which radar reports each event and whether the result matches the expected zone.

## Coverage map

Create a simple site coverage map.

For each test point, record:

| Test point | Radar A | Radar B | Radar C | Expected result | Notes |
| --- | --- | --- | --- | --- | --- |
| P1 | Detect / no detect | Detect / no detect | Detect / no detect | Expected | Notes |

This makes blind zones and overlap visible instead of relying on intuition.

The coverage map should be updated whenever the unit orientation, mounting height, enclosure geometry, or radar configuration changes.

## False-detection testing

Calibration should intentionally test likely sources of unwanted detections.

Examples include movement outside the target zone; doors opening; people passing behind a wall or barrier; moving vegetation; mechanical equipment; reflective surfaces; nearby traffic; and other expected environmental motion.

Where a false detection is found, the response may involve changing orientation; changing mounting position; changing a threshold; changing event logic; marking a known site limitation; and excluding a region from the intended monitoring claim.

## Environmental-sensor calibration

Environmental sensors should be checked for both plausibility and placement effects.

Where reference equipment is available, compare readings under stable conditions.

For each channel, document reference instrument used; reference uncertainty where known; ORIGIN reading; difference; test duration; location; and whether an offset or calibration correction is applied.

Do not publish a calibration correction as universal if it was derived from only one unit or one condition.

## Baseline vs threshold

A threshold should be justified relative to the observed baseline and the monitoring objective.

For example, an environmental alert threshold may depend on normal site range; rate of change; duration above/below a value; repeated excursions; and site-defined conservation limits.

Similarly, a presence event may depend on persistence; sensor identity; time of day; agreement between multiple sensors; distance trend; and site operating mode.

Avoid reducing complex site behavior to a single unexplained threshold.

## Multi-sensor correlation

After validating individual sensors, test the combined logic.

Useful cases include one radar detects while others do not; two radars detect the same moving target; simultaneous but unrelated detections; a target moving from one radar zone to another; one radar temporarily unavailable; and disagreement between sensor state and higher-level event logic.

The system should preserve sensor provenance so later analysis can show which inputs contributed to an event.

## Centaurus AI calibration boundary

Centaurus AI should not be “calibrated” by simply changing outputs until they agree with desired conclusions.

If AI or anomaly-analysis behavior is used during deployment, document model/rule version; input channels; thresholds or confidence settings; expected classes/events; evaluation dataset or field cases used; known failure modes; and operator review procedure.

Any tuning should remain traceable to a versioned configuration or model release.

## Recalibration triggers

Recalibration should be considered after moving the unit; changing radar orientation; changing enclosure geometry; replacing a sensor; changing firmware that affects sensor processing; changing thresholds; changing site layout; adding a module that affects sensing or power; and observing a sustained change in false positives or missed events.

## Calibration record

A calibration record should contain unit ID; site; date; firmware version; configuration version; sensor inventory; radar orientation; test positions; baseline observations; threshold changes; reference equipment used; identified blind zones; identified false-detection sources; unresolved limitations; and person responsible.

## Calibration acceptance

Calibration is complete when expected sensors respond consistently; sensor directions match the site plan; major blind zones are understood; obvious false-detection sources have been tested; environmental channels are plausible; thresholds and event rules are documented; unresolved limitations are recorded; and no critical sensing fault remains hidden behind a normal state.

The system can then proceed to [Commissioning](commissioning.md).
