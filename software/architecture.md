# Software Architecture

ORIGIN software uses a layered architecture so hardware access, device logic, communications, data services, intelligent analysis, and operator-facing functions remain clearly separated.

## Hardware abstraction

The lowest software layer translates Rosetta interfaces and connected sensors into consistent software operations. Each device retains a stable logical identity even if the physical connection changes between hardware revisions.

## Device services

Device services schedule acquisition, validate observations, associate time and source identity, maintain subsystem health, create events, manage local records, and expose the active configuration.

## Communications

The communications layer handles the selected transport, delivery state, retries, buffering behavior, and connection health. A transport condition is kept separate from sensor state.

## Data services

Remote services receive structured ORIGIN records, preserve provenance, support storage and visualization, and provide data to Centaurus and operator-facing applications.

## Centaurus AI

Centaurus performs higher-level analysis such as correlation, anomaly interpretation, contextual reasoning, prioritization, and event explanation. It consumes structured observations rather than directly controlling the hardware.

## Operator layer

The operator layer presents health, events, configuration, deployment identity, and maintenance information in a form that can be understood without board-level knowledge.

## Design goals

The architecture prioritizes modularity, traceability, resilience, configuration-driven behavior, diagnostics, security, and clear separation of responsibility between local device control and higher-level analysis.
