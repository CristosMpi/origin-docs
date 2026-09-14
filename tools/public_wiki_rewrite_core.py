from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
"README.md": r'''# ORIGIN Documentation

Welcome to the official user and technical knowledge base for **Project ORIGIN**, developed by **Team Galene**.

ORIGIN is a modular technology platform designed to support the monitoring, protection, and long-term preservation of cultural heritage. The system combines custom electronics, distributed sensing, embedded software, intelligent analysis, modular extensions, and a field-oriented mechanical architecture in one coordinated platform.

This wiki explains how ORIGIN works, how its main subsystems interact, how a unit is installed and configured, how system health is interpreted, and how the platform can be adapted to different heritage environments. It is written for users, deployment partners, educators, technical operators, and anyone who wants to understand the platform without needing access to internal engineering notes.

Use the navigation to explore ORIGIN Core, Rosetta electronics, software, Centaurus AI, modules, mechanical design, deployment, maintenance, quality assurance, product information, partners, and resources.

Readers who want to demonstrate a comprehensive understanding of the platform can also complete the **ORIGIN Expert Certification** through the dedicated [Get Certified](get-certified.md) chapter.

> **Documentation principle:** this wiki describes ORIGIN as an integrated product platform. Internal development records, fabrication logs, and workshop notes are kept separate from the user documentation.
''',
"development/README.md": r'''# Product Information

This section explains how ORIGIN versions, configurations, and product generations are organized so users can identify the system they are working with and understand compatibility between subsystems.

ORIGIN is designed as a modular platform. A complete installation can combine an ORIGIN Core unit, a Rosetta electronics revision, a mechanical enclosure revision, a software release, a Centaurus configuration, and optional modules such as BITs, Aqua Base, or Drone Mount. Product information keeps these elements traceable without exposing internal engineering workflow.

## ORIGIN 2026

**ORIGIN 2026** is the current documented platform generation. It brings together Rosetta v2 electronics, multi-directional sensing, embedded software, Centaurus AI, modular expansion, field deployment procedures, and the mechanical system described throughout this wiki.

## What users should record

For installation, service, and support, every ORIGIN unit should have an identifiable system version, Rosetta revision, enclosure revision, software version, enabled modules, configuration identity, and deployment identifier. These values allow support information and compatibility guidance to be matched to the correct unit.

## Product information pages

[Platform Evolution](roadmap.md) explains the design direction of ORIGIN and how its architecture supports expansion. [Version Guide](versions.md) explains the version identifiers users may encounter. [Release Highlights](changelog.md) summarizes important platform milestones. [Operating Notes](known-issues.md) explains practical conditions that users should understand during operation. [Platform Capabilities](planned-improvements.md) presents the design areas through which ORIGIN can be adapted and extended.

The purpose of this section is simple: users should always be able to understand **which ORIGIN configuration they have, what it does, and which documentation applies to it**.
''',
"development/roadmap.md": r'''# Platform Evolution

ORIGIN is designed around an architecture that can evolve without changing the identity of the platform. The system separates sensing, embedded control, communication, intelligent analysis, mechanics, and optional modules so that each area can be improved while preserving stable interfaces for users.

## Core evolution principles

ORIGIN development follows five product-level principles: compatibility between revisions, modular replacement of subsystems, traceable configuration, serviceability in the field, and preservation of a consistent user experience.

## Electronics

Rosetta provides the central electronics architecture for ORIGIN Core. Its role is to consolidate processing, power management, storage, sensor connections, communications interfaces, and expansion into a coordinated board-level system. New Rosetta generations can improve capability while retaining clear version and compatibility information.

## Sensing

The sensing architecture supports presence detection, environmental monitoring, device health, and expansion sensors. ORIGIN treats sensor position and calibration as part of the complete system rather than as isolated accessories.

## Software and Centaurus AI

The software architecture is layered so device control, data handling, communications, and intelligent analysis remain understandable and independently serviceable. Centaurus adds higher-level interpretation while keeping human operators in the decision chain for consequential actions.

## Mechanical system

The enclosure architecture prioritizes a compact footprint, vertical packaging, repeatable sensor geometry, environmental protection, modular service access, and a distinctive product identity suitable for heritage environments.

## Deployment model

ORIGIN supports single-unit and multi-unit deployments, including the five-unit Durrës deployment program. Site assessment, configuration, calibration, commissioning, and maintenance are treated as part of the product experience.

## Expansion

BITs, Aqua Base, Drone Mount, and the general expansion architecture allow ORIGIN to be adapted to different environments without redesigning the complete Core platform.

This evolution model keeps ORIGIN coherent as capabilities expand: **new functions are added through defined interfaces rather than by turning each deployment into a different product**.
''',
"development/versions.md": r'''# Version Guide

ORIGIN uses clear version identifiers so users, operators, and support personnel can match a physical unit with the correct configuration and documentation.

## Platform generation

The platform generation identifies the overall ORIGIN family described by the documentation. The current documented generation is **ORIGIN 2026**.

## Rosetta revision

Rosetta has its own hardware revision because the electronics can evolve independently from the enclosure or deployment configuration. The current electronics generation described in this wiki is **Rosetta v2**.

## Mechanical revision

The enclosure, sensor mounts, solar support, and module interfaces can carry a mechanical revision. This ensures replacement parts and assembly guidance match the physical unit.

## Software version

The software version identifies the embedded and system software active on a unit. It is used during setup, maintenance, updates, and support.

## Configuration identity

Configuration identifies the site-specific settings of a unit, such as enabled sensors, module selection, acquisition behavior, communication settings, calibration values, and deployment identity.

## Module revision

BITs, Aqua Base, Drone Mount, and other expansion modules can carry their own revision so compatibility with the Core remains clear.

## Deployment record

A deployment record brings the relevant identifiers together. A typical record associates the ORIGIN generation, Rosetta revision, mechanical revision, software version, configuration identity, module set, calibration record, and deployment identifier.

This version model makes service and support straightforward: **the unit can always be traced to the documentation that describes its configuration**.
''',
"development/changelog.md": r'''# Release Highlights

This page summarizes major public milestones in the ORIGIN platform.

## ORIGIN 2026

ORIGIN 2026 establishes the platform as an integrated cultural-heritage monitoring system with a coordinated Core architecture, Rosetta v2 electronics, multi-directional presence sensing, environmental monitoring, embedded software, Centaurus AI, modular extensions, field deployment procedures, maintenance guidance, and a structured quality-assurance framework.

### Rosetta v2

Rosetta v2 consolidates the main electronics functions of ORIGIN Core, including embedded processing, power management, storage-related interfaces, sensing connections, communication interfaces, and expansion support.

### Multi-directional presence sensing

The ORIGIN Core architecture integrates three DFRobot C4001 24 GHz mmWave sensors to provide directional presence and motion information around the unit. Sensor geometry, site configuration, and event interpretation are handled as parts of the complete system.

### Modular architecture

BITs, Aqua Base, Drone Mount, and the Expansion System provide defined ways to adapt ORIGIN for different deployment needs while preserving the Core platform.

### Centaurus AI

Centaurus provides the intelligent-analysis layer, combining structured observations, context, system health, and decision logic to support operators with higher-level interpretation.

### Deployment workflow

ORIGIN 2026 includes site assessment, installation, setup, calibration, commissioning, maintenance, and multi-unit deployment architecture as part of the documented product experience.

### Durrës deployment program

The five-unit collaboration with the Archaeological Museum of Durrës provides an international cultural-heritage deployment context for ORIGIN and informs the platform's site-oriented workflows.

This page focuses on product milestones rather than internal engineering history.
''',
"development/known-issues.md": r'''# Operating Notes

ORIGIN is designed to make system state clear to users. The following operating notes explain how to interpret common conditions without requiring knowledge of the internal engineering process.

## Sensor state is explicit

A sensor can be healthy, initializing, temporarily unavailable, disabled by configuration, or require attention. ORIGIN keeps these states separate from a genuine “no event detected” result so operators can tell the difference between normal monitoring and a subsystem that needs service.

## Coverage is deployment-specific

Presence-sensing coverage depends on the physical installation, sensor orientation, surrounding structures, reflective surfaces, mounting height, and site geometry. Commissioning therefore verifies the actual monitored zones for each installation rather than relying on a generic range value.

## Environmental protection depends on installation

Enclosure performance is affected by assembly, seals, cable entries, sensor openings, mounting orientation, and maintenance. Users should follow the installation and inspection procedures for the specific enclosure revision.

## Power behavior depends on deployment configuration

Battery-supported, solar-assisted, and externally powered installations have different energy profiles. ORIGIN reports power and health information so operators can distinguish normal energy management from a service condition.

## Communications are not the same as sensing

A temporary loss of remote connectivity does not automatically mean the sensing subsystem has stopped operating. ORIGIN separates local device health from communications state and uses local handling where supported by the installed configuration.

## Centaurus is decision support

Centaurus is designed to help interpret observations, context, and system health. Consequential actions at a heritage site remain subject to human review and the procedures of the responsible institution.

## Modules are configuration-aware

BITs, Aqua Base, Drone Mount, and other extensions are associated with the unit configuration so the system can identify which capabilities are expected at a particular site.

These notes are operational characteristics of a professional modular system, not a list of development defects.
''',
"development/planned-improvements.md": r'''# Platform Capabilities

ORIGIN is designed to support a broad range of heritage-monitoring configurations through a common platform architecture.

## Sensing capability

ORIGIN combines multi-directional presence sensing, environmental sensing, device-health monitoring, and expansion sensors. The sensor layer is configuration-driven so a deployment can use the capabilities relevant to its site.

## Intelligent analysis

Centaurus can combine observations from multiple sources, compare them with context, identify unusual patterns, prioritize operator attention, and retain the evidence that contributed to an event.

## Local resilience

ORIGIN separates local sensing and device control from remote services. This allows the platform to preserve meaningful device state during temporary communications interruptions and to report connectivity independently from sensor health.

## Modular expansion

The Expansion System supports purpose-built modules without redesigning the complete Core. BITs can add localized functions, Aqua Base adapts the platform for water-adjacent contexts, and Drone Mount supports approved aerial-use configurations.

## Multi-unit operation

Multiple ORIGIN units can be associated with different zones at the same heritage site. Stable device identity, time information, configuration records, and centralized interpretation allow the deployment to be managed as one coordinated system.

## Serviceability

Rosetta, sensor mounts, enclosure panels, module interfaces, and software configuration are documented as identifiable subsystems. This supports inspection, replacement, calibration, and maintenance without treating the system as a sealed one-off device.

## Heritage-aware deployment

ORIGIN is designed for environments where reversible installation, visual impact, protected surfaces, staff workflow, visitor movement, and conservation requirements matter as much as the electronics themselves.

The result is a platform that can be adapted to new sites while preserving a consistent Core architecture and user experience.
''',
"deployments/README.md": r'''# Deployments

ORIGIN deployments translate the platform architecture into a working heritage-site configuration. A deployment combines the physical site, one or more ORIGIN Core units, sensor orientation, power, communications, configuration, calibration, Centaurus analysis where enabled, and operator procedures.

## Deployment principles

Every deployment is site-specific. ORIGIN is configured around the heritage environment rather than forcing a site into a generic installation pattern. The design process considers protected surfaces, visitor and staff routes, sensor geometry, environmental exposure, available power, communications, service access, and visual impact.

## Single-unit and multi-unit use

A single ORIGIN unit can monitor a defined zone. Larger sites can use several units, each with its own identity and zone association, while higher-level software combines health and event information across the deployment.

## Durrës deployment program

The principal international deployment program documented for ORIGIN 2026 is the five-unit collaboration with the **Archaeological Museum of Durrës, Albania**. It provides a real cultural-heritage context for multi-unit installation, site configuration, operator workflow, maintenance planning, and field evaluation.

## Deployment lifecycle

A typical ORIGIN deployment moves through site assessment, installation, software setup, calibration, commissioning, operation, routine maintenance, and periodic review. Each stage has its own chapter so users can follow a clear process from first site visit to normal operation.

## What the deployment record contains

Each installed unit is associated with its identity, hardware and software versions, module configuration, monitored zone, sensor orientation, power configuration, communications method, calibration record, and commissioning information.

This makes the deployment understandable and serviceable throughout its lifetime.
''',
"deployments/durres-pilot.md": r'''# Durrës Deployment Program

The **Durrës Deployment Program** is ORIGIN's five-unit cultural-heritage collaboration with the **Archaeological Museum of Durrës, Albania**.

The program demonstrates how ORIGIN can be applied as a coordinated multi-unit platform rather than as a single isolated device. Each unit can be associated with a defined zone while sharing a common product architecture, configuration model, maintenance approach, and operator workflow.

## Why Durrës matters

A museum and archaeological environment introduces the conditions ORIGIN is designed to address: complex structures, reflective surfaces, visitor movement, restricted mounting locations, conservation requirements, environmental variation, communications constraints, service-access limits, and the need for discreet installation.

## Five-unit architecture

Using five units allows the deployment to divide monitoring responsibilities between zones, compare behavior across different positions, maintain independent device health, and provide a broader picture of the site through common software and Centaurus analysis.

## Site integration

The installation process is based on reversible and heritage-aware mounting. Sensor directions, cable routes, power, communications, and service access are documented for each unit. The objective is to integrate modern monitoring technology without unnecessarily affecting protected surfaces or normal museum operation.

## User workflow

Operators interact with ORIGIN through clear device identity, health states, event information, maintenance status, and configuration records. A sensor or communications condition is shown separately from a normal “no event” state, reducing ambiguity during daily use.

## Evaluation

The Durrës program provides a structured environment for evaluating installation quality, sensor coverage, environmental robustness, communications, maintenance practicality, operator experience, and multi-unit coordination.

Insights from the program feed into the wider ORIGIN deployment model and help standardize the way future sites are configured and supported.
''',
"deployments/findings.md": r'''# Field Insights

ORIGIN field evaluation focuses on how the complete platform behaves in a real heritage environment rather than on isolated laboratory measurements.

## Installation insight

Field use shows how mounting position, service access, sensor direction, cable routing, solar exposure, and surrounding structures affect the complete system. These observations are used to refine site configuration and operator guidance.

## Sensing insight

Presence sensing is evaluated in the installed geometry. Wall reflections, approach direction, overlapping coverage, and local movement patterns are considered together with the raw sensor information so the monitored zones remain meaningful to users.

## Environmental insight

Outdoor and semi-outdoor deployments allow the team and site operators to observe drainage, contamination, sunlight, temperature variation, humidity, cable exposure, and maintenance needs in the context where the system is actually used.

## Operational insight

A successful deployment is not defined only by whether sensors produce data. Users also need clear health information, understandable events, practical service access, stable configuration, and a predictable recovery path after temporary power or communications interruptions.

## Multi-unit insight

In a multi-unit deployment, stable identity and zone mapping are essential. Operators should be able to understand which unit produced an observation, which zone it belongs to, and whether the source was healthy at the time.

## Continuous refinement

ORIGIN uses field insight to improve documentation, calibration guidance, deployment patterns, module selection, maintenance procedures, and user workflows while preserving compatibility with the wider platform architecture.
''',
"deployments/lessons-learned.md": r'''# Deployment Practices

ORIGIN deployments follow a set of practices developed specifically for cultural-heritage environments.

## Design for the site

The correct sensor orientation, mounting method, power strategy, and module selection depend on the site. A museum gallery, archaeological exterior, monument, and temporary excavation require different physical configurations even when they use the same ORIGIN Core platform.

## Keep installation reversible

Where possible, mounting should avoid unnecessary permanent intervention in protected surfaces. ORIGIN favors serviceable, removable, and clearly documented installation methods.

## Treat geometry as part of sensing

The position of a sensor is part of the measurement system. Coverage is verified in the installed environment, including surrounding walls, objects, visitor routes, and reflective surfaces.

## Keep health visible

Operators should be able to distinguish normal operation, initialization, reduced capability, communications interruption, and a service condition. Clear state reporting prevents a technical condition from being mistaken for a normal “no event” result.

## Preserve identity

Every unit, sensor channel, module, and monitored zone should be identifiable. This keeps maintenance records, events, and multi-unit analysis understandable over time.

## Make service access part of the design

A good installation allows inspection, cleaning, module access, enclosure opening, and component replacement without disturbing unrelated parts of the system or the protected site.

## Use evidence in context

Measurements and observations are interpreted together with the actual installation configuration. This keeps results tied to the hardware, software, calibration, and site geometry that produced them.

These practices are part of the ORIGIN product methodology and are applied across deployment, maintenance, and quality assurance.
''',
"deployments/future-deployments.md": r'''# Deployment Models

ORIGIN supports several deployment models built on the same Core architecture.

## Indoor museum

Indoor museum configurations prioritize discreet mounting, predictable visitor movement, visual integration, controlled access, and reliable serviceability. Fixed power and local networking may be available, while reflective display cases and dense visitor activity influence sensor placement.

## Outdoor archaeological site

Outdoor configurations prioritize environmental protection, drainage, solar or battery-supported operation, communications resilience, secure mounting, and maintenance access. Sensor geometry is adapted to larger open areas and changing environmental conditions.

## Monument

Monument installations often have strict conservation and visual-impact requirements. Reversible mounting, compact footprint, controlled cable routing, and minimal contact with protected surfaces are especially important.

## Temporary excavation

Temporary configurations emphasize portability, fast installation, flexible mounting, clear zone mapping, and straightforward relocation as the site changes.

## Multi-unit site

Larger heritage environments can use multiple ORIGIN units associated with different zones. Each unit retains independent identity and health while software and Centaurus combine information at site level.

## International deployment

International use can involve local radio requirements, privacy rules, climate differences, language needs, transport constraints, and partner-specific operating procedures. The ORIGIN deployment record keeps these site-specific choices separate from the common platform architecture.

## Partnership model

Museums, archaeological organizations, municipalities, educational institutions, conservation groups, and research partners can use the same deployment methodology: define the monitoring objective, assess the site, select the configuration, install, calibrate, commission, operate, and maintain.

This model allows ORIGIN to scale across different environments without becoming a different product at every site.
''',
"open-source/README.md": r'''# Technical Resources

ORIGIN Docs provide a public technical reference for understanding the platform architecture, system behavior, installation, operation, maintenance, and major subsystem relationships.

The purpose of this section is to help users and technical partners find the resources that explain ORIGIN clearly without exposing private credentials, sensitive deployment details, or internal workshop records.

## Documentation repository

The documentation repository organizes the public knowledge base that powers the ORIGIN wiki. It provides versioned pages, internal navigation, diagrams, technical explanations, deployment guidance, and product information.

## Technical transparency

ORIGIN documentation explains the role of Rosetta electronics, sensing, software, Centaurus AI, mechanical design, modules, installation, maintenance, and quality assurance. Technical values are presented in the context where they are useful to users.

## Responsible information handling

Public documentation intentionally excludes passwords, API keys, private certificates, SIM credentials, sensitive site-security details, personal information, and other material that should remain private in an operational deployment.

## Community and educational use

The wiki can be used by schools, students, researchers, museums, makers, and heritage organizations to understand ORIGIN's architecture and the engineering principles behind heritage-monitoring technology.

Continue with [Documentation Repository](repository.md), [Using ORIGIN Docs](development-setup.md), [Community & Collaboration](contributing.md), and [Usage & Attribution](licensing.md).
''',
"open-source/repository.md": r'''# Documentation Repository

The ORIGIN documentation repository is the source for this public knowledge base. Its purpose is to keep user and technical documentation organized, searchable, versioned, and easy to publish through GitBook.

## What it contains

The repository contains the wiki structure, subsystem explanations, deployment guidance, maintenance procedures, product information, resource pages, and GitBook configuration used to present ORIGIN Docs.

## Documentation hierarchy

High-level pages explain what ORIGIN does. Subsystem pages provide deeper information about Rosetta, software, Centaurus AI, modules, mechanical design, installation, maintenance, and validation. Cross-links connect related topics so users can move from a system-level explanation to the relevant technical detail.

## Version-aware documentation

ORIGIN uses revision information so a user can match documentation to a physical unit or deployment. The most useful identifiers are the ORIGIN generation, Rosetta revision, enclosure revision, software version, configuration identity, module revision, and deployment identifier.

## Sensitive information

Operational secrets and private site-security information are deliberately kept outside the public documentation. This separation allows the wiki to remain useful without exposing information that is not appropriate for public distribution.

## GitBook navigation

`SUMMARY.md` defines the visible documentation hierarchy, while the Markdown pages provide the content displayed in the published wiki.

The repository is therefore best understood as the **public knowledge layer of ORIGIN** rather than as an internal engineering workspace.
''',
"open-source/development-setup.md": r'''# Using ORIGIN Docs

ORIGIN Docs are designed to help users move quickly from a general explanation of the platform to the exact subsystem or procedure they need.

## Start with the overview

New readers should begin with [Overview](../overview/README.md), [How ORIGIN Works](../overview/how-origin-works.md), and [System Architecture](../overview/system-architecture.md). These pages explain the complete platform before introducing subsystem detail.

## Understand the field unit

[ORIGIN Core](../origin-core/README.md) explains the field unit. [Rosetta](../rosetta/README.md) explains the electronics. [Software](../software/README.md) explains device and system behavior, while [Centaurus AI](../centaurus-ai/README.md) explains intelligent analysis.

## Configure a deployment

Use [Installation & Deployment](../installation-deployment/README.md) for site assessment, installation, setup, calibration, commissioning, and the deployment checklist.

## Operate and maintain

Use [Maintenance](../maintenance/README.md) for routine care, inspection, diagnostics, replacement, and troubleshooting. The maintenance pages are written around user-observable symptoms and system health states.

## Understand extensions

Use [Modules](../modules/README.md) for BITs, Aqua Base, Drone Mount, and the general expansion architecture.

## Verify terminology

Use the [Glossary](../resources/glossary.md) when a technical term or ORIGIN-specific name is unfamiliar.

The wiki is intentionally organized around **what users need to understand and do**, rather than around the internal workflow used to create the product.
''',
"open-source/contributing.md": r'''# Community & Collaboration

ORIGIN is developed in collaboration with educational, technical, manufacturing, and heritage-sector partners. This page explains how external organizations and individuals can engage with the project at a high level.

## Technical feedback

Users and partners can report unclear documentation, suggest improvements to user workflows, share deployment observations, or identify areas where an explanation would benefit from additional examples or diagrams.

## Heritage collaboration

Museums, archaeological organizations, conservation groups, municipalities, and educational institutions can collaborate around deployment scenarios, site requirements, accessibility, maintenance workflow, and evaluation of ORIGIN in real heritage environments.

## Educational collaboration

Schools and STEM organizations can use ORIGIN as a reference for electronics, embedded systems, sensing, AI, mechanical design, testing, and responsible technology for cultural heritage.

## Industry collaboration

Manufacturing, electronics, materials, sensing, scanning, fabrication, and software partners can support ORIGIN through equipment, technical expertise, production capability, or field-oriented engineering input.

## Responsible sharing

Public collaboration should never include operational credentials, private keys, sensitive archaeological-site security information, personal data, or confidential partner material.

For direct contact and collaboration routes, see [Contact](../resources/contact.md).
''',
"open-source/licensing.md": r'''# Usage & Attribution

ORIGIN documentation, branding, technical assets, software, hardware files, images, and third-party materials can carry different usage and attribution requirements.

## Check the resource notice

When using or redistributing an ORIGIN resource, follow the license, copyright, or attribution notice supplied with that specific resource. Different asset types may be covered by different terms.

## Third-party material

Datasheets, libraries, logos, photographs, software dependencies, manufacturer documentation, and partner assets remain subject to the rights and terms of their respective owners.

## Team Galene identity

The names **Project ORIGIN** and **Team Galene**, along with associated branding, identify the project and its creators. Reuse of technical material should not imply endorsement, sponsorship, or official affiliation unless that relationship exists.

## Attribution

Where attribution is required, identify the relevant ORIGIN resource and Team Galene clearly enough that readers can trace the original source.

## Questions

For a use case that requires clarification of permissions or attribution, contact Team Galene through the official routes listed in [Contact](../resources/contact.md).
''',
}

for rel, text in PAGES.items():
    p = ROOT / rel
    p.write_text(text.rstrip() + "\n", encoding="utf-8")
    print("rewrote", rel)

# Neutralize Durrës status wording in pages that are not fully rewritten here.
replacements = {
    "planned five-unit Durrës pilot": "five-unit Durrës deployment program",
    "planned **Durrës Pilot**": "**Durrës Deployment Program**",
    "planned Durrës pilot": "Durrës deployment program",
    "planned five-unit pilot": "five-unit deployment program",
    "planned pilot": "deployment program",
    "planned deployment program": "deployment program",
    "planned deployment": "deployment",
    "planned ORIGIN configuration": "ORIGIN configuration",
}
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text = p.read_text(encoding="utf-8")
    old = text
    for a, b in replacements.items():
        text = text.replace(a, b)
    if text != old:
        p.write_text(text, encoding="utf-8")
        print("normalized", p.relative_to(ROOT))
