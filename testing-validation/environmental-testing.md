# Environmental Testing

Environmental testing evaluates how ORIGIN behaves when exposed to the conditions expected outside a controlled laboratory environment.

The objective is not to assign an IP rating or environmental certification without the required formal testing. Instead, this section defines practical engineering tests for moisture, temperature, sunlight, condensation, dust exposure and outdoor operation.

## Scope

Environmental validation may include:

- rain and splash exposure;
- water-entry inspection;
- drainage behavior;
- condensation;
- temperature variation;
- solar heating;
- humidity exposure;
- dust and debris;
- corrosion risk;
- material aging;
- cable-entry behavior;
- sensor-opening behavior;
- power-system behavior outdoors.

## Important limitation

The current ORIGIN enclosure intentionally includes dedicated mmWave sensor openings to avoid relying on unverified radar transmission through enclosure walls.

Those openings create an environmental trade-off.

Therefore, ORIGIN must not be described as waterproof or assigned a formal ingress-protection rating unless a released enclosure is tested according to the applicable formal standard.

## Test configuration

Record:

```text
Enclosure revision
Material
Manufacturing process
Seal/gasket revision
Sensor opening geometry
Cable-entry configuration
Installed electronics
Test duration
Ambient temperature
Humidity where available
```

## Visual pre-inspection

Before environmental exposure, inspect and photograph:

- enclosure seams;
- fasteners;
- sensor openings;
- cable entries;
- solar cable path;
- drain features;
- seals/gaskets;
- existing cracks or gaps.

This establishes the pre-test condition.

## Controlled splash test

A practical development splash test may be used to identify obvious water-entry paths.

The test should define:

- water source;
- direction;
- distance;
- duration;
- enclosure orientation;
- whether the system is powered;
- inspection method.

Do not describe this as a formal IP test unless it actually follows the required standard and equipment.

After exposure:

1. inspect the exterior;
2. open the enclosure in a controlled dry area;
3. look for droplets, wet surfaces or water tracks;
4. inspect electronics and connectors;
5. record entry location;
6. dry the unit safely before reuse if moisture entered.

## Sensor-opening test

Because the radar openings are deliberate penetrations, test them independently.

Observe whether water can:

- enter directly;
- run along the sensor PCB;
- follow the cable into the enclosure;
- collect in a pocket;
- drain away harmlessly.

Possible design responses may include geometry changes, shields, labyrinths, drainage or secondary internal protection, but each change must be revalidated for sensor performance.

## Cable-entry test

Inspect all cable paths for capillary or gravity-driven water entry.

Relevant areas include:

- solar cable routing;
- external module connections;
- service interfaces;
- connectors.

A cable should not create an uncontrolled path that guides water toward electronics.

## Drainage behavior

If the design includes intentional openings or drainage paths, test the unit in realistic orientations.

Verify that water does not become trapped near:

- Rosetta;
- battery/power components;
- connectors;
- sensor PCBs;
- fastener inserts.

## Condensation testing

Condensation can occur even when rain does not enter the enclosure.

A practical test may involve moving a safely powered-off enclosure between controlled warm/humid and cooler conditions, then observing internal moisture.

Record:

- starting conditions;
- ending conditions;
- transition time;
- internal moisture;
- drying time.

Do not create unsafe thermal shock to batteries or electronics.

## Temperature testing

Temperature testing should evaluate both electronics and mechanical behavior.

Possible observations include:

- boot reliability;
- sensor initialization;
- regulator behavior;
- battery behavior;
- enclosure deformation;
- seal compression;
- display/indicator behavior if present;
- connector fit.

Test ranges should be based on intended deployment and component limits, not arbitrary extremes.

## Solar-heating test

Direct sunlight can raise internal temperature significantly above ambient.

For outdoor prototypes, record:

- ambient temperature;
- enclosure surface temperature where practical;
- internal temperature at representative location;
- solar exposure duration;
- system operating state.

A temperature result should always include the measurement location.

## Humidity exposure

High humidity may affect:

- connectors;
- exposed copper;
- fasteners;
- adhesives;
- printed materials;
- sensor readings.

After prolonged humid exposure, inspect for:

- condensation;
- corrosion;
- discoloration;
- swelling;
- loosened adhesives;
- degraded electrical behavior.

## Dust and debris

Outdoor and archaeological environments may include soil, fine dust and debris.

Development testing should examine whether these materials accumulate in:

- radar openings;
- seams;
- module connectors;
- drainage channels;
- solar-support joints;
- service interfaces.

Cleaning must also be considered. A design that works only when perfectly clean may require unrealistic maintenance.

## UV and material aging

Long-term sunlight can degrade some polymers and finishes.

Short project tests cannot prove multi-year UV durability, so material selection should rely on manufacturer data plus long-duration observations where available.

Track:

- discoloration;
- brittleness;
- cracking;
- warping;
- surface degradation.

## Corrosion review

Inspect metal hardware and exposed conductive surfaces after outdoor exposure.

Pay attention to:

- mixed metals;
- fasteners;
- threaded inserts;
- connector contacts;
- exposed PCB edges;
- moisture-trapping interfaces.

## Wind and weather stability

The solar panel and tall enclosure can create wind loading.

Field observations should record:

- visible vibration;
- rotation;
- mount loosening;
- solar-support movement;
- changes in radar alignment.

Formal wind-load claims require a defined engineering analysis or test and should not be inferred from casual outdoor use.

## Post-exposure functional test

After each environmental test, repeat a basic functional verification:

- boot;
- power rails/health;
- sensor communication;
- radar detection;
- connectivity;
- storage/logging;
- module health.

Environmental exposure is only meaningful if its effect on system function is checked.

## Failure criteria

Examples of environmental failure include:

- water reaching electronics;
- persistent condensation;
- sensor obstruction;
- enclosure cracking;
- seal displacement;
- cable-entry leakage;
- corrosion;
- inability to boot or communicate after exposure;
- permanent mechanical deformation.

## Current public status

Environmental procedures are defined here, but no universal waterproofing, IP-rating, temperature-range or outdoor-lifetime claim is made for the current ORIGIN revision.

Those claims require released hardware and documented evidence.

## Evidence

Recommended evidence:

- pre/post photographs;
- internal inspection photos;
- temperature logs;
- humidity records;
- exposure duration;
- water-entry map;
- post-test functional logs;
- material observations.

## Related documentation

See:

- [Mechanical Design → Waterproofing](../mechanical-design/waterproofing.md)
- [Materials](../mechanical-design/materials.md)
- [Mechanical Testing](mechanical-testing.md)
- [Field Testing](field-testing.md)
- [Validation Results](validation-results.md)
