# Repository

The public ORIGIN documentation repository is the current source of truth for project documentation and GitBook navigation.

Repository:

`CristosMpi/origin-docs`

Default branch:

`main`

## Purpose

This repository exists to keep ORIGIN's technical documentation version-controlled, reviewable, and publishable. It is not yet a complete monorepo containing every hardware, firmware, AI, CAD, and manufacturing source file.

That distinction is intentional. Documentation may describe a subsystem before the editable engineering source for that subsystem is released publicly.

## Current top-level structure

The repository is organized by subsystem and lifecycle stage. Major directories include:

```text
overview/
origin-core/
rosetta/
software/
centaurus-ai/
modules/
mechanical-design/
installation-deployment/
testing-validation/
deployments/
maintenance/
development/
open-source/
partners-sponsors/
resources/
```

Repository-level GitBook files include:

```text
README.md
SUMMARY.md
.gitbook.yaml
gitbook-docs.yaml
```

## Documentation navigation

`SUMMARY.md` defines the documentation navigation order. It should be updated whenever pages are added, removed, renamed, or reorganized.

`.gitbook.yaml` configures the space-level GitBook content mapping.

`gitbook-docs.yaml` defines the site-level GitBook structure and should retain stable space keys once Git Sync is configured.

These files are part of the publishing system and should not be edited casually.

## Source-of-truth hierarchy

When documentation conflicts with engineering evidence, use the most authoritative source available.

A practical precedence order is:

1. validated, editable engineering source for the exact revision;
2. released fabrication/build outputs generated from that source;
3. measured validation records tied to the revision;
4. approved technical documentation;
5. design notes and historical discussions;
6. concepts, sketches, presentations, or memory.

For example, a PCB dimension extracted from a released Gerber job should take precedence over an older approximate value in a presentation.

## Revision coupling

Hardware, software, mechanical, and documentation revisions must not be treated as interchangeable.

A deployment record should identify, where practical:

- ORIGIN system revision;
- Rosetta hardware revision;
- enclosure/mechanical revision;
- firmware version;
- configuration version;
- Centaurus version or rules/model identifier if active;
- module revisions;
- documentation revision or commit.

This prevents a validation result for one build from being mistakenly applied to another.

## Recommended source layout for future releases

As more engineering files are published, Team Galene can either extend this repository or create dedicated repositories. Either approach is valid if ownership and version relationships remain clear.

A future source layout could include:

```text
hardware/
  rosetta/
  modules/
firmware/
centaurus/
mechanical/
manufacturing/
tests/
docs/
```

Alternatively, dedicated repositories can be linked from this documentation repository.

The important requirement is not the exact folder layout. It is that users can identify the authoritative source and compatible revision.

## Binary and generated files

Generated outputs should be distinguished from editable source.

Examples of generated files include:

- Gerbers;
- drill files;
- pick-and-place files;
- PDFs;
- STEP exports;
- STL exports;
- compiled firmware binaries;
- rendered diagrams;
- packaged releases.

Generated files should ideally be reproducible from source and associated with a version or release.

Do not replace editable source with only generated exports unless the source cannot legally or practically be published.

## Manufacturing packages

A manufacturing package should be treated as a release artifact rather than an arbitrary ZIP export.

For a PCB, a release package may include:

- Gerber copper and mask layers;
- board outline;
- Excellon drill files;
- BOM;
- centroid/pick-and-place data when assembly is intended;
- assembly drawings;
- fabrication notes;
- revision identifier;
- checksum or release tag.

The Rosetta v2 Gerber package inspected during documentation work was missing drill files. That package should therefore not be labeled a complete fabrication release.

## Documentation commits

Documentation changes should use meaningful commit messages. Good messages describe the engineering effect, for example:

- `Document Rosetta v2 manufacturing constraints`
- `Add field calibration procedure`
- `Record missing drill files in known issues`

Avoid messages such as `update`, `fix`, or `stuff` when the change affects engineering traceability.

## Branching and review

For substantial future contributions, a feature-branch and pull-request workflow is recommended.

Typical flow:

```text
main
  └── docs/update-radar-calibration
  └── hardware/rosetta-v2-fab-fix
  └── mechanical/enclosure-r3
```

The exact branch naming scheme is flexible, but changes should remain easy to understand and review.

Direct commits to `main` may still be appropriate for controlled maintainer work, especially while the project is small.

## Issues

GitHub issues can be used to track:

- documentation gaps;
- bugs;
- fabrication blockers;
- validation failures;
- feature proposals;
- deployment findings;
- compatibility problems;
- release tasks.

When an issue affects safety, field reliability, or a public technical claim, the relevant documentation should also be updated rather than relying only on the issue tracker.

## Releases

A future ORIGIN release should identify a coherent set of compatible artifacts rather than simply tagging the latest repository state.

A release record should state:

- version;
- date;
- release scope;
- included hardware/software/mechanical revisions;
- validation status;
- known limitations;
- required migration steps;
- source commit or tag;
- artifact checksums where appropriate.

## External source repositories

If firmware, Centaurus, CAD, or PCB sources are moved into separate repositories, this documentation repository should contain stable links to them and state which versions are compatible.

A documentation page must never silently imply that a linked repository is authoritative if it is only an experiment or archived prototype.

## Archiving obsolete work

Obsolete designs should not necessarily be deleted. Historical source can be useful for understanding decisions.

When retaining old work:

- mark it clearly as deprecated or archived;
- identify the last compatible system version;
- do not place it where new users will mistake it for the current release;
- retain important known issues and migration notes.

## Repository hygiene

Before committing, check for:

- credentials or secrets;
- private deployment details;
- personal data;
- temporary exports;
- editor backup files;
- duplicated binaries;
- proprietary third-party material;
- unverified technical claims.

## Documentation quality gate

A page should not be considered complete merely because it contains text. Before merging a significant update, confirm that:

- the title and navigation are correct;
- the page matches the current system state;
- current, planned, and conceptual behavior are distinguished;
- measurements are tied to evidence;
- links work;
- no sensitive data is exposed;
- known limitations are documented;
- the change does not contradict a more authoritative source.

## Repository principle

The repository should make it possible to answer a basic engineering question:

> **What exactly was built, what evidence supports it, and where is the source for that revision?**
