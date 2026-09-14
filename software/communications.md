# Communications

The communications subsystem connects ORIGIN Core with higher-level software while preserving clear separation between local device operation and network state.

## What is transmitted

Communications can carry sensor observations, structured events, device health, configuration information, software identity, timestamps, and maintenance-related state.

## Transport abstraction

ORIGIN software is designed so the data model is not tied to one transport. A deployment can use the communications method appropriate to the site while preserving the same higher-level record structure.

## Offline tolerance

When remote connectivity is interrupted, the device can continue local sensing and maintain local state. Where local storage is enabled, records can be queued according to the installed configuration and synchronized when connectivity returns.

## Message identity

Records include enough identity and timing information to distinguish current data from delayed or repeated delivery and to associate every observation with the correct device and sensor.

## Health reporting

Connectivity is represented as its own system state. Users can therefore distinguish a remote-network condition from a sensor or power condition inside ORIGIN Core.

## Security

Credentials and sensitive connection details are stored separately from the public documentation and from ordinary user-facing configuration. Only the information required for operation is exposed to the relevant subsystem.
