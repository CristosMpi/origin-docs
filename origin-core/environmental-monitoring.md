# Environmental Monitoring

Environmental monitoring is one of the ways ORIGIN can help provide context about the condition of a heritage site. The purpose is not to produce a generic weather station; it is to measure environmental variables that are relevant to the risks, material behavior or operating conditions of a specific deployment.

## Purpose

Environmental data can help operators understand whether changes around an object, structure or site are gradual, sudden, normal or potentially harmful.

Depending on the deployment, relevant variables may include:

- temperature;
- relative humidity;
- moisture-related conditions;
- air-quality or gas-related indicators;
- light exposure;
- vibration or movement;
- other site-specific environmental variables.

This list describes possible sensing categories, not a fixed specification for every ORIGIN Core.

## Deployment-specific sensing

Different heritage environments have different risks.

An outdoor archaeological site, an indoor museum, a coastal location and an underground space should not automatically use the same environmental-sensor configuration.

ORIGIN therefore treats environmental monitoring as configurable.

A deployment plan should answer:

1. What physical condition matters at this site?
2. What sensor can measure it reliably?
3. Where should that sensor be located?
4. What sampling interval is useful?
5. What range or rate of change is meaningful?
6. How will the system distinguish a real change from sensor error?

## Measurements are context, not conclusions

A single environmental reading rarely proves that damage is occurring.

For example, a humidity value can be useful evidence, but interpretation may depend on:

- how quickly it changed;
- how long the condition persisted;
- temperature at the same time;
- the location of the sensor;
- the material being protected;
- the known normal range for the site;
- whether the sensor itself is stable and calibrated.

ORIGIN should therefore preserve measurements in a way that allows trends and events to be examined rather than reducing every value to a simple safe/unsafe decision.

## Sampling strategy

Environmental variables often change more slowly than security-related events, so high-frequency sampling may waste power and storage without providing additional value.

A configurable sampling strategy can include:

- periodic measurements;
- temporary higher-rate sampling after a significant change;
- lower-rate sampling during energy-saving states;
- event-driven recording when thresholds are crossed.

The final interval should be chosen through deployment requirements and testing.

## Thresholds

Thresholds can be useful for alerts, but they need careful definition.

There are several possible threshold types:

### Absolute threshold

An alert occurs when a value exceeds a fixed boundary.

### Rate-of-change threshold

An alert occurs when a value changes unusually quickly even if the absolute value is still within a broad acceptable range.

### Persistence threshold

A condition becomes important only after it remains outside a range for a defined period.

### Combined condition

Multiple measurements are evaluated together.

The software should identify which model is being used so that operators know why an event was generated.

## Baselines

A site baseline is often more useful than a generic number copied from a datasheet.

During commissioning, ORIGIN may collect reference data to understand the normal behavior of the site under typical conditions.

A baseline can help identify:

- recurring daily cycles;
- normal seasonal variation;
- unusual spikes;
- sensor drift;
- changes following maintenance or relocation.

Baseline collection should not be confused with formal conservation limits, which should come from appropriate heritage professionals or site requirements.

## Sensor placement

Environmental sensors should be placed where they measure the condition of interest rather than simply wherever space is available inside the enclosure.

Placement questions include:

- should the sensor measure internal enclosure conditions or the external site?
- is airflow required?
- will direct sunlight bias the reading?
- can rain or condensation reach the sensing element?
- is the sensor too close to heat-producing electronics?
- does a protective membrane change response time?
- can the sensor be cleaned or replaced?

These questions create a direct link between environmental sensing and enclosure design.

## Internal vs external conditions

ORIGIN may need to distinguish the environment around the heritage asset from the environment inside the device.

For example:

```text
External environmental sensor
        → site condition

Internal temperature / diagnostic sensor
        → device condition
```

These measurements should not be mixed under the same label because they answer different questions.

## Data quality

Environmental data should include enough metadata to be interpreted correctly.

Useful fields include:

- sensor identity;
- timestamp;
- value;
- unit;
- validity state;
- calibration or configuration version where relevant;
- deployment identifier.

A measurement with no unit or uncertain sensor identity is not useful long-term documentation.

## Calibration and drift

Environmental sensors can drift over time.

Depending on the device and required accuracy, maintenance may involve:

- comparison with a reference instrument;
- offset correction;
- replacement after a defined interval;
- inspection after environmental exposure;
- re-baselining after relocation.

Calibration procedures should be recorded in the deployment and testing documentation.

## Sensor failure

Potential environmental-sensor failures include:

- disconnected sensor;
- impossible value;
- frozen/stale value;
- excessive noise;
- slow response caused by contamination;
- condensation;
- cable damage;
- drift outside acceptable tolerance.

ORIGIN should report these conditions separately from genuine environmental alerts.

## Combining environmental data with other events

Environmental measurements become more useful when correlated with the rest of the system.

Examples include:

- comparing environmental changes before and after a detected presence event;
- correlating power problems with internal temperature;
- checking whether a vibration event coincides with human presence;
- interpreting a moisture-related event alongside weather or deployment context.

Higher-level correlation belongs in [Centaurus AI](../centaurus-ai/README.md) or the wider software stack.

## Validation

A new environmental sensor should not be considered deployment-ready until it has been tested for:

- repeatability;
- reasonable agreement with a reference where applicable;
- response time;
- operation in the expected temperature/humidity range;
- enclosure effects;
- power consumption;
- communication reliability;
- long-duration stability.

The test plan should record the exact sensor model and firmware configuration used.

## Current status

The ORIGIN architecture supports environmental monitoring, but the exact final sensor set should be documented per hardware revision and deployment rather than implied by this general page.

As final environmental sensors are frozen, their model numbers, interfaces, calibration requirements and validated ranges should be added to the appropriate Rosetta, BOM and Testing pages.

## Related documentation

See:

- [Sensor System](sensor-system.md)
- [Testing & Validation](../testing-validation/README.md)
- [Installation & Deployment](../installation-deployment/README.md)
- [Maintenance](../maintenance/README.md)
- [Centaurus AI](../centaurus-ai/README.md)