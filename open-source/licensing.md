# Licensing

Licensing defines what other people are legally allowed to do with ORIGIN documentation, hardware designs, software, CAD, datasets, media, and other project material.

## Current status

> **No project-wide license has been adopted in this repository yet.**

As of the current documentation revision, `CristosMpi/origin-docs` does not contain a repository-level `LICENSE` file.

The repository is publicly readable, but public visibility should **not** be interpreted as permission to freely copy, modify, manufacture, redistribute, or commercially use the material.

Until Team Galene explicitly publishes licensing terms, users should treat reuse permissions as **not yet granted by a project license**.

## Why the license is not being guessed

Selecting a license is a project-governance and rights decision, not a documentation formatting choice.

The correct license depends on questions such as whether Team Galene wants commercial reuse to be allowed; whether modified hardware designs must remain open; whether software derivatives must publish source; whether documentation can be remixed; whether school/institutional ownership affects copyright; whether sponsor or partner agreements impose restrictions; whether all contributors have the right to license their contributions; and whether third-party components or assets carry separate terms.

For those reasons, this documentation records the current status without silently choosing a license on behalf of the project.

## ORIGIN contains multiple types of intellectual work

A single license may not be ideal for every part of ORIGIN.

The project includes or may include written documentation; diagrams and illustrations; PCB schematics and layouts; mechanical CAD; firmware; application/backend software; Centaurus AI code and configurations; datasets and test results; photos and videos; logos and branding; and third-party datasheets and libraries.

These categories can require different licensing treatment.

## Possible future licensing model

The following is a **candidate structure only**, not the current license.

| Material | Possible license family | Status |
|---|---|---|
| Documentation | Creative Commons attribution-style license | Not selected |
| Hardware design source | Open hardware license such as CERN-OHL family | Not selected |
| Software / firmware | Permissive or copyleft software license | Not selected |
| CAD | Open hardware license or explicit CAD terms | Not selected |
| Test data | Dataset-specific terms where appropriate | Not selected |
| Logos / branding | Separate trademark/brand policy | Not selected |

Team Galene should choose exact licenses only after confirming ownership and project goals.

## Documentation licensing

Documentation can be licensed separately from code and hardware.

A future documentation license should answer Can others redistribute the documentation?; Can they modify and translate it?; Is attribution required?; Must derivative documentation use the same license?; and Can it be used commercially?.

Creative Commons licenses are commonly used for documentation and educational content, but the exact variant must be deliberately selected.

## Hardware licensing

PCB and mechanical designs raise questions that ordinary software licenses do not always address clearly.

An open-hardware license can define rights related to design-document distribution; modification; manufacture of physical products; distribution of modified design sources; notices and attribution; and reciprocal sharing requirements.

If Rosetta, BITs, Aqua Base, Drone Mount, or enclosure sources are released as open hardware, the chosen license should be stated directly in or alongside those source directories.

## Software and firmware licensing

Software licensing should cover the authoritative source code, not just binaries or snippets in documentation.

The project should decide whether it prefers, for example a permissive model that allows broad reuse with notice requirements; or and a reciprocal/copyleft model that requires certain derivatives to remain open.

The exact choice should be made before public source release whenever practical.

## Centaurus AI licensing

Centaurus may involve multiple separately licensed elements Team Galene source code; external libraries; model weights; datasets; APIs/services; and evaluation material.

A source-code license does not automatically grant rights to third-party model weights or datasets.

Any Centaurus release should identify those dependencies explicitly.

## Third-party components

ORIGIN uses third-party components and may reference external libraries, datasheets, SDKs, CAD models, symbols, footprints, or software packages.

Their licenses remain separate from the ORIGIN project license.

Examples include DFRobot sensor documentation and hardware; semiconductor vendor datasheets; EDA libraries; open-source software dependencies; and manufacturer CAD models.

Do not copy third-party material into the repository unless redistribution is permitted.

Prefer linking to the authoritative source when redistribution rights are uncertain.

## Sponsor and partner material

Sponsorship does not automatically transfer intellectual-property rights.

Logos, brand names, supplied photos, product files, and partner documents may have usage restrictions separate from ORIGIN's own license.

Sponsor assets should therefore not be assumed to fall under any future ORIGIN open-source license.

## Team Galene branding

Even if ORIGIN source material becomes open source, that does not necessarily mean others may present modified projects as official Team Galene products.

A future release should distinguish copyright/license permissions for source material and trademark/branding permissions for names, logos, and identity.

This helps prevent forks from being confused with official ORIGIN releases.

## Contributor rights

Before accepting externally contributed work under a future project license, Team Galene should ensure contributors have the right to submit that work.

Contributors should not submit copied proprietary code; unlicensed CAD; copyrighted diagrams without permission; restricted datasets; confidential sponsor files; and assets taken from commercial products without redistribution rights.

## License headers and notices

Once licenses are chosen, a mature release should include a root `LICENSE` or clearly named license files; copyright notices where appropriate; SPDX identifiers where useful; a `NOTICE` or attribution file if required; per-directory license files when different subsystems use different terms; third-party license notices; and clear documentation of exceptions.

## Mixed-license repository

If ORIGIN uses different licenses for hardware, software, and documentation, the repository should make that obvious.

For example:

```text
LICENSES/
  documentation-license.txt
  hardware-license.txt
  software-license.txt

hardware/
  LICENSE
software/
  LICENSE
docs/
  LICENSE
```

The exact layout can differ; clarity is what matters.

## Release checklist for licensing

Before calling a subsystem formally open-source/open-hardware, confirm The copyright owner(s) are identified; Team Galene has authority to license the material; An explicit license has been selected; The license text is included; Third-party dependencies are documented; Restricted/confidential material has been removed; Required attribution is present; Branding/trademark rights are not accidentally granted; Source files needed for meaningful modification are included; and The documentation states which license applies to which material.

## What users may rely on today

Users may read and reference the public documentation through the repository and published documentation interfaces.

They should **not** rely on an assumed open-source license for reuse until explicit licensing terms are published.

## Next licensing action

The next formal step is for Team Galene to choose a licensing policy and then add the corresponding license files to the repository.

That decision should be made intentionally by the project owners. Once selected, this page should be updated from **status guidance** into a precise explanation of the adopted licenses.

## Principle

Open source is not created simply by making a repository public. A trustworthy open release requires **source availability, explicit permissions, clear ownership, reproducibility, and transparent limitations**.
