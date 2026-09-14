# Rosetta Diagnostics

This page helps users and technicians identify which Rosetta subsystem deserves attention when ORIGIN reports an abnormal condition.

## Unit does not start normally

Check the available power source, battery connection, external-energy input, and visible system status. If power is available but startup does not complete, record the reported health state before cycling power.

## One sensor is unavailable

Check the physical connector, cable routing, sensor identity, and whether the sensor is enabled in the active configuration. A single unavailable channel should remain distinguishable from the other healthy channels.

## Several sensors are unavailable

When several channels change state together, inspect shared power, Rosetta interfaces, configuration, and the software startup record before replacing individual sensors.

## Local storage is unavailable

Check that the storage medium is seated correctly and recognized by the system. ORIGIN reports storage separately from sensing so operators can understand whether data logging or buffering is affected.

## Communications are offline

A communications interruption does not automatically imply a Rosetta hardware problem. Check the selected transport, signal/network conditions, authentication status where applicable, and whether the device continues to report healthy local sensing.

## Unexpected resets

Review power state, recent configuration or software changes, peripheral initialization, and storage activity. Repeated resets should be treated as a service condition and investigated before returning the unit to unattended operation.

## Support record

When requesting technical support, provide the ORIGIN unit identifier, Rosetta revision, software version, configuration identity, observed status, and the time the condition was first noticed. This information is usually enough to narrow the issue to the correct subsystem.
