# Key Components

Rosetta v2 combines a focused set of components selected for embedded control, power management, sensing, storage, and expansion.

| Function | Component or subsystem |
| --- | --- |
| Embedded processing | ESP32-class controller |
| Motion/orientation sensing | LIS3DH three-axis accelerometer |
| Battery charging / power path | BQ24074RGT |
| Regulated conversion | TPS63031DSK |
| Battery connection | Dedicated battery interfaces |
| External sensing / expansion | Multi-pin sensor and module headers |
| Local storage | Removable/local storage interface |
| Communications support | Communications-related interface hardware |
| User interaction | Buttons and status/control signals |

## Why these components matter

The component set is organized around the needs of ORIGIN Core: reliable embedded control, field-oriented power handling, identifiable sensor channels, local data support, communications integration, and modular expansion.

## Service perspective

Users normally interact with Rosetta at subsystem level rather than component level. Maintenance documentation therefore refers to power, sensing, storage, communications, and expansion functions so a service procedure remains understandable across hardware revisions.
