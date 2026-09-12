# Introduction

Project ORIGIN is a student-led engineering initiative developed by **Team Galene** to explore how modern sensing, embedded systems, artificial intelligence, and modular robotics can support the protection of cultural heritage.

The project begins from a practical observation: important monuments, archaeological sites, museums, and historic environments cannot always be protected through occasional inspections alone. Conditions can change between visits, damage may develop gradually, and many risks become easier to manage when they are detected early.

ORIGIN is Team Galene's response to that challenge.

## Purpose

The purpose of ORIGIN is to create a flexible technological platform that can help monitor heritage environments continuously and provide useful information about changing conditions.

The project is not limited to a single sensor, installation type, or physical form. Instead, it is being developed as a modular system that can be adapted to different environments and expanded as new requirements appear.

At a high level, ORIGIN brings together environmental and presence sensing; custom embedded electronics; power and communication systems; local firmware and data processing; intelligent analysis through Centaurus AI; mechanical protection and field-ready mounting; modular extensions such as BITs, Aqua Base, and Drone Mount; and testing, diagnostics, maintenance, and deployment procedures.

## Why cultural heritage?

Cultural heritage connects communities with their history, identity, architecture, art, and collective memory. Protecting it is therefore not only a conservation problem; it is also an engineering, social, educational, and technological challenge.

Many preservation methods depend on specialists, scheduled inspections, fixed infrastructure, or equipment designed for a narrow task. These approaches remain essential, but technology can add another layer: continuous observation between inspections and a clearer record of how conditions change over time.

ORIGIN is designed to complement human expertise, not replace it. The goal is to provide better visibility, earlier warning, and more adaptable monitoring tools so that professionals can make informed decisions.

## A system, not a single device

The name ORIGIN refers to the complete project ecosystem.

A typical ORIGIN installation can include a central field unit, the Rosetta electronics platform, selected sensors, communications, software, intelligent processing, and optional modules. The exact configuration can vary depending on the site and the monitoring objective.

This system-oriented approach is important because the engineering challenges are interconnected. A sensor choice affects power consumption. Power constraints affect communications. Mechanical design affects sensor placement. Placement affects data quality. Data quality affects analysis. Maintenance requirements affect enclosure and mounting decisions.

ORIGIN is therefore developed by considering the full chain from physical environment to useful information.

## Project scope

ORIGIN covers several engineering disciplines:

### Electronics

The project includes **Rosetta**, Team Galene's custom electronics platform. Rosetta is developed to consolidate the control, power, interfaces, storage, and expansion requirements of ORIGIN into hardware that can evolve with the project.

### Embedded software

Firmware manages sensors, system state, communications, diagnostics, and device-level behavior. The software layer is designed to make the physical platform configurable and maintainable rather than hard-coded for one demonstration.

### Artificial intelligence and cybersecurity

**Centaurus AI** represents the project's intelligent analysis layer. Its role is to support interpretation of system data and to explore intelligent monitoring while treating security and system integrity as first-class design concerns.

### Mechanical engineering

ORIGIN must operate in environments where appearance, exposure, accessibility, mounting, water, heat, dust, and maintenance all matter. Mechanical design is therefore treated as a functional subsystem rather than simply an enclosure around electronics.

### Modular robotics

Modules such as **BITs**, **Aqua Base**, and **Drone Mount** extend ORIGIN beyond one fixed installation concept. They allow the project to explore different deployment scenarios using a common architecture.

## Development philosophy

ORIGIN is built through iteration. Designs are prototyped, tested, revised, and documented. Components may change as the team learns from fabrication, laboratory testing, deployment preparation, and real-world feedback.

The project therefore distinguishes between **system concepts**, which describe how ORIGIN is intended to operate, **current implementations**, which describe the hardware and software available in a specific version, and **future development**, which records planned improvements without presenting them as completed features.

This distinction is important throughout these docs. Where an implementation detail is version-dependent, the relevant technical page should be treated as authoritative.

## Who these docs are for

ORIGIN Docs are written for several audiences heritage and museum professionals evaluating the concept; engineers reviewing the system architecture; robotics teams and students learning from the project; partners and sponsors supporting development; Team Galene members maintaining and extending ORIGIN; and judges, educators, and researchers who need a structured technical reference.

The documentation aims to remain understandable at the system level while providing deeper technical sections for readers who need implementation details.

## Where to go next

Continue to [The Problem](the-problem.md) to understand the challenges ORIGIN is designed around, or jump directly to [Our Solution](our-solution.md) for the project's engineering approach.
