# Field Testing

Field testing evaluates ORIGIN as a complete system in realistic operating conditions.

Bench tests are essential, but they cannot reproduce every effect of installation geometry, weather, radio conditions, visitor movement, power availability, reflections, mounting constraints and maintenance access. Field testing is therefore the point where subsystem assumptions are tested against reality.

## Objectives

Field testing should answer practical questions such as: Does the complete ORIGIN unit remain mechanically stable after installation? Do the sensors cover the intended zones from the installed position? Are false detections acceptable and explainable? Does the power system support the intended operating cycle? Is communication reliable enough for the deployment? Are failures visible to operators? Can the unit be serviced without disturbing the site? Does the system recover correctly after a power or network interruption?

## Field-test stages

A useful field program progresses through several stages.

### 1. Controlled outdoor test

Use a representative outdoor location where the team can freely reposition equipment and repeat tests.

This stage is useful for initial radar coverage mapping; solar/power observations; environmental exposure; network testing; mechanical stability; and service-access evaluation.

### 2. Representative-site test

Use geometry that resembles the final heritage environment.

For example, walls and corridors; stone surfaces; restricted approach paths; similar mounting height; and similar visitor movement.

### 3. Pilot deployment

Operate a released or pilot configuration at an approved real site under site-specific rules.

At this stage, changes to thresholds and geometry should be documented rather than made informally.

## Pre-deployment baseline

Before transporting the unit, perform and record a baseline functional test.

Recommended checks include successful boot, sensor health, storage and logging, communications, the known configuration, battery or power state, and a mechanical inspection.

This helps distinguish transport damage from site-specific problems.

## Installation record

For each field deployment, record:

```text
Site / test area
Date and time
Unit identifier
Hardware revision
Firmware/software version
Mechanical revision
Installed modules
Mounting method
Mounting height
Radar orientation
Power source
Communication method
Configuration profile
Operator(s)
```

Photograph the final installation from multiple directions.

## Coverage testing in the field

Repeat sensor-coverage validation after installation.

Do not assume that laboratory or open-area radar results transfer directly to a site with walls, stone, metal objects or constrained paths.

Test routes should include normal approach; departure; slow movement; stationary presence; movement near zone boundaries; and movement outside the intended monitored zone.

Record which radar or sensor responds at each location.

## Baseline environmental observations

Record relevant site conditions such as ambient temperature; humidity if available; sunlight/shade; wind; rain exposure; nearby moving objects; and site geometry.

These observations can help explain changes in sensor or power behavior.

## Communications testing

Field communication tests should include more than a single successful connection.

Verify startup connection; repeated transmissions; expected data arrival; local buffering when unavailable; recovery after network interruption; and timestamp/order behavior after reconnection.

If multiple communications paths exist, test each path relevant to the deployed configuration.

## Power testing

Observe the energy system over a representative operating period.

Record where available battery state or voltage; external/solar input; operating mode; significant loads; reboot events; and brownout indicators.

Long-term battery-life or energy-autonomy claims should only be made from data covering representative conditions.

## False-positive observation

A field deployment should record events that ORIGIN interprets as potentially relevant but that operators determine are benign.

Examples may include visitors outside the intended area; staff movement; reflections; environmental movement; and site activity.

Do not simply delete these events. Categorize them so the team can improve placement, thresholds or analysis.

## Missed-event observation

Where tests intentionally create known events, record whether ORIGIN detects them.

Known test events can include a person entering the intended zone, remaining still, and exiting; movement or disturbance of the unit where tamper sensing is implemented; and disconnection of a selected sensor.

Known test events should be timestamped so they can be compared with logs.

## End-to-end event validation

A field event should be traceable through the complete chain:

```text
Physical condition
      ↓
Sensor observation
      ↓
Rosetta/firmware event
      ↓
Local record
      ↓
Transmission
      ↓
Backend / processing
      ↓
Centaurus analysis where enabled
      ↓
Operator-facing result
```

Testing only the final alert does not show where a failure occurred if the alert is missing.

## Failure and recovery tests

Where safe and approved, field validation should deliberately test failures.

Examples:

### Network interruption

Temporarily remove connectivity and verify system remains operational where designed, local data is retained, network state is visible, and queued data is handled correctly after recovery.

### Power interruption

Perform a controlled restart and verify boot; configuration persistence; sensor reinitialization; communication recovery; and logging continuity.

### Sensor disconnect

Disconnect an accessible test sensor and verify the fault is reported.

Do not perform unsafe fault injection on installed equipment or heritage infrastructure.

## Mechanical field inspection

After installation and again after a defined period, inspect mounting stability; fastener movement; enclosure cracks; solar-support movement; cable strain; sensor orientation; dirt/water accumulation; and service-interface accessibility.

## Operator usability

A technical system may work but still be impractical to operate.

Field testing should therefore check whether operators can understand health status; distinguish an event from a fault; access required service points; restart or isolate the unit safely; identify the device and configuration; and understand when technical support is required.

## Long-duration observation

Short demonstrations cannot validate long-term behavior.

Where possible, collect data over extended periods to observe communication uptime; power trends; sensor drift; false-event frequency; restart frequency; environmental effects; mechanical loosening; and storage behavior.

The duration should be stated explicitly in any published result.

## Pilot deployment and Durrës

ORIGIN's deployment planning includes work connected with the **Archaeological Museum of Durrës, Albania**.

Any public pilot result should identify the actual deployed configuration, dates, number of units, test scope and limitations. Planned deployment activity should not be presented as a completed field-validation result until evidence exists.

## Acceptance categories

A field test can be classified as:

### Accepted for pilot use

The defined pilot criteria are met, with known limitations documented.

### Conditional

The system may continue in controlled use while specific limitations are monitored.

### Rework required

A problem affects reliability, safety, serviceability or the intended monitoring function.

### Test incomplete

Insufficient duration, evidence or site access prevents a conclusion.

## Evidence package

Recommended field evidence includes installation photos; site map; sensor coverage map; event log; known-event timestamps; false-positive log; power telemetry; communications log; environmental observations; maintenance notes; and configuration/revision record.

## Related documentation

See [Installation & Deployment](../installation-deployment/README.md); [Commissioning](../installation-deployment/commissioning.md); [Sensor Testing](sensor-testing.md); [Environmental Testing](environmental-testing.md); [Deployments](../deployments/README.md); and [Validation Results](validation-results.md).
