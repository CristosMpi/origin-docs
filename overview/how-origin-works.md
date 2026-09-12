# How ORIGIN Works

ORIGIN operates as a chain that begins in the physical environment and ends with information that people can use.

The exact hardware and software configuration can change between deployments, but the system-level workflow remains consistent: **observe, process, evaluate, communicate, maintain, and improve.**

## 1. Observe the environment

An ORIGIN installation begins with sensing.

Sensors are selected according to the risks and conditions relevant to the monitored site. Depending on the deployment, the system can include environmental sensing, presence detection, motion-related sensing, or other specialized inputs.

Sensor placement is treated as part of the measurement system. A sensor that is electrically functional but poorly positioned can produce data that is misleading or incomplete. For this reason, site assessment and mechanical design are closely connected to the sensing architecture.

## 2. Acquire and manage measurements

The ORIGIN electronics platform receives data from the installed sensors and coordinates device-level operation.

Rosetta provides the electrical foundation for this process. The embedded firmware manages measurement timing, interfaces, local state, and the services needed to keep the device operating consistently.

At this stage, ORIGIN is concerned not only with the measured value but also with the health of the system producing it. Diagnostics can help distinguish a real environmental change from a device, sensor, power, or communication problem.

## 3. Perform local processing

Not every raw measurement needs to be transmitted or treated as an event.

The software layer can perform local processing before data leaves the device. This may include organizing readings, validating expected behavior, attaching timestamps or system state, and preparing information for storage or communication.

Local processing can also reduce unnecessary dependence on a permanent external connection. The exact behavior is implementation-dependent and is documented in the relevant firmware and software pages.

## 4. Store and communicate information

ORIGIN is designed to preserve useful monitoring information and communicate it through the available system interfaces.

Communication requirements can vary significantly between sites, so the architecture separates communications from the core monitoring concept. A deployment should be designed around the infrastructure that is realistically available rather than assuming ideal connectivity.

When communications are temporarily unavailable, the wider system design should avoid treating a network interruption as equivalent to the loss of the monitored event itself. Storage, retry behavior, and diagnostics are therefore important parts of the implementation.

## 5. Analyze the data

Once measurements are collected and organized, the data can be evaluated for useful patterns and events.

Centaurus AI represents the intelligent analysis layer in the ORIGIN ecosystem. Its purpose is to support the interpretation of information produced by the monitoring system rather than simply present large volumes of raw data.

Possible analysis tasks include identifying unusual changes, comparing measurements over time, prioritizing events, and combining information from multiple inputs.

Any intelligent output must be interpreted in context. ORIGIN is designed to assist human decision-making, not to present AI-generated conclusions as unquestionable conservation decisions.

## 6. Surface useful information

The value of monitoring depends on whether the resulting information can be understood and acted upon.

ORIGIN therefore aims to separate three concepts **measurement** — what a sensor observed, **event** — a change or condition that the system considers significant enough to record or surface, and **decision** — what a person chooses to do with that information.

This separation is important because a measurement is not automatically a problem, and an automated event is not automatically an emergency.

## 7. Monitor the monitor

An unattended monitoring system must also observe itself.

ORIGIN's design includes system diagnostics because failures can otherwise create gaps that are difficult to notice. Relevant health information can include sensor availability, power state, storage status, communication behavior, and other implementation-specific checks.

The objective is to make degraded operation visible rather than allowing the system to fail silently.

## 8. Maintain and update the installation

ORIGIN is intended to be serviceable.

A deployment may require inspection, cleaning, calibration, replacement of components, firmware updates, or changes to the sensor configuration. Mechanical access and modularity therefore influence the system from the design stage.

The maintenance process is documented separately under [Maintenance](../maintenance/README.md).

## 9. Extend the system when needed

Not every deployment should use the same physical platform.

BITs, Aqua Base, Drone Mount, and future modules allow ORIGIN to expand into additional monitoring and inspection scenarios while keeping a relationship with the same project architecture.

This enables the project to evolve without turning every new requirement into an unrelated standalone prototype.

## Example information flow

A simplified ORIGIN data path can be represented as:

```text
Physical environment
        ↓
      Sensors
        ↓
 Rosetta electronics
        ↓
 Embedded firmware
        ↓
Local validation / storage
        ↓
 Communications layer
        ↓
 Data processing
        ↓
   Centaurus AI
        ↓
Events / insights / records
        ↓
   Human evaluation
        ↓
Conservation or operational action
```

The real implementation may contain additional paths, local decisions, buffers, modules, or external services. The diagram is intended to show the conceptual direction of information rather than define a specific protocol.

## A feedback loop, not a one-way pipeline

ORIGIN is also designed as an iterative system.

Information from testing and deployments can lead to changes in sensor selection, thresholds, firmware, mechanical design, data analysis, or maintenance procedures. A deployment therefore feeds knowledge back into the engineering process.

The complete cycle is:

```text
Design → Build → Test → Deploy → Observe → Learn → Improve
```

This cycle is central to Team Galene's development philosophy for ORIGIN.

Continue to [System Architecture](system-architecture.md) for the relationship between the major subsystems.
