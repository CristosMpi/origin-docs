# Electronics Testing

Electronics testing verifies that Rosetta and the complete ORIGIN Core electrical system operate consistently before and during deployment.

## Visual and mechanical inspection

The board and connectors are inspected for assembly quality, secure mounting, clean interfaces, correct cable seating, and absence of visible damage or contamination.

## Power verification

Power checks confirm stable startup, regulated supply behavior, battery and charging operation where applicable, and normal operation with the expected sensors and communications hardware connected.

## Processor and storage

The embedded controller is checked for consistent startup, correct software identity, stable operation, and access to local storage where used by the configuration.

## Sensor interfaces

Each sensor channel is checked for communication, stable identity, valid data, and correct health-state reporting. A disconnected channel is shown as a service condition rather than being interpreted as a normal measurement.

## Communications

The selected communications path is checked independently from sensing so temporary remote connectivity conditions remain distinguishable from local device health.

## Integrated verification

The final electronics check is performed with Rosetta installed in ORIGIN Core so cable routing, enclosure integration, sensors, modules, power, and software can be evaluated together.

The result is a system-level quality check rather than a bare-board inspection.
