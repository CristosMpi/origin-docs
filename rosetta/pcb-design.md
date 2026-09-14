# PCB Design

Rosetta v2 uses a compact two-layer PCB architecture designed specifically for ORIGIN Core.

## Board format

The board occupies roughly **100 × 105 mm** and uses a nominal **1.6 mm FR-4** construction. This format balances connector access, enclosure integration, sensor routing, power distribution, and serviceability.

## Layer architecture

The PCB uses front and back copper with solder mask and silkscreen on both sides. Components and connectors are arranged so the board can be mounted inside the vertical ORIGIN enclosure while keeping important interfaces reachable.

## Layout priorities

The layout gives particular attention to short power paths, local decoupling, return paths, separation of switching circuitry from sensitive signals, connector orientation, mounting clearances, and readable silkscreen labeling.

## Mechanical integration

PCB design is coordinated with the enclosure. Mounting points, connector positions, cable bends, sensor paths, and service access are treated as shared electrical-mechanical requirements.

## Identification

Board revision information allows a technician to match the physical Rosetta board with the correct software, enclosure, and service documentation.
