# Installation

Software installation prepares an ORIGIN Core unit for its assigned deployment and confirms that the device is running the correct software and configuration.

## 1. Identify the unit

Confirm the ORIGIN unit identifier, Rosetta revision, enclosure revision, and intended deployment profile.

## 2. Load the approved software

Install the ORIGIN software package appropriate to the Rosetta revision and deployment. Software identity is checked after startup so the active version can be recorded.

## 3. Apply configuration

Load the site-specific configuration, including unit identity, sensor selection, module configuration, communication settings, acquisition behavior, calibration values, and deployment metadata.

## 4. Verify hardware discovery

Confirm that the expected sensors, local storage, communications hardware, and modules appear with the correct logical identities.

## 5. Verify health

Check that required subsystems initialize normally and that the device reports a clear state for any optional subsystem that is intentionally disabled.

## 6. Test restart behavior

Restart the unit and confirm that configuration, identity, storage, sensor discovery, and communication state are restored consistently.

## 7. Continue to calibration

After software setup is complete, proceed to [Calibration](../installation-deployment/calibration.md) and then [Commissioning](../installation-deployment/commissioning.md).

This workflow keeps software installation focused on the user's unit and deployment rather than on internal programming tools.
