# Development Setup

This page explains how to work with the ORIGIN documentation repository today and how future hardware, firmware, AI, and CAD source releases should be approached.

The current public repository is primarily a **documentation repository**. Do not assume that every subsystem described in the documentation already has public editable source in this repository.

## Prerequisites

For documentation work, you need Git, a GitHub account for contributions, a Markdown-capable editor, and a web browser for GitBook/GitHub review.

Optional tools depend on the subsystem being edited.

## Clone the repository

```bash
git clone https://github.com/CristosMpi/origin-docs.git
cd origin-docs
```

Check the current branch:

```bash
git branch --show-current
```

The default branch is `main`.

## Update before editing

Before starting work:

```bash
git pull --ff-only
```

If working on a larger change, create a dedicated branch:

```bash
git switch -c docs/short-description
```

Example:

```bash
git switch -c docs/update-rosetta-manufacturing
```

## Documentation files

Most content is Markdown. The key publishing files are `SUMMARY.md` — GitBook navigation, `.gitbook.yaml` — space-level GitBook configuration, and `gitbook-docs.yaml` — site-level GitBook mapping.

Do not change GitBook keys or structure fields without understanding their effect on Git Sync.

## Editing a documentation page

A good workflow is:

1. identify the authoritative source for the technical claim;
2. edit the relevant Markdown page;
3. update related pages if the change affects other subsystems;
4. check internal links;
5. review terminology and revision labels;
6. verify no secrets/private data were introduced;
7. commit with a descriptive message.

Example:

```bash
git add rosetta/manufacturing.md development/known-issues.md
git commit -m "Document Rosetta drill package requirements"
```

## Local Markdown review

Any editor with Markdown preview can be used. Check especially heading hierarchy; tables; code blocks; relative links; filenames and capitalization; long lines that may be hard to maintain; and status labels such as current, planned, or conceptual.

The rendered GitBook view should also be reviewed after syncing or publishing changes.

## GitBook relationship

The repository is structured for GitBook publication.

The intended content flow is:

```text
GitHub Markdown source
        ↓
GitBook Git Sync / import
        ↓
Rendered ORIGIN Docs site
```

GitHub remains valuable because it provides change history and source review. GitBook provides the reader-facing documentation experience.

## Hardware development environment

Rosetta development has involved KiCad and later EasyEDA Pro design work. Exact source-tool requirements should be tied to the authoritative board source once it is publicly released.

When editable Rosetta hardware source is released, the setup guide should identify the required EDA tool; tested tool version; project libraries; custom symbols and footprints; design rules; fabrication-output procedure; BOM generation procedure; assembly-data generation procedure; and any required plugins/scripts.

A Gerber archive alone is not enough to reconstruct the complete editable board design.

## Mechanical development environment

Mechanical work may involve native CAD plus exchange formats such as STEP.

A future reproducible CAD setup should document primary CAD package; tested version; native source format; assembly structure; units; reference-coordinate conventions; manufacturing exports; required fonts or external assets, if any; and compatibility between enclosure and electronics revisions.

Do not rely only on STL files for editable mechanical development.

## Firmware development environment

Once the authoritative firmware repository is public, this section should be expanded with exact commands.

A reproducible firmware setup should state target microcontroller/module; framework and version; compiler/toolchain version; dependency versions; board configuration; build command; flash command; serial/debug configuration; test command; and configuration/secrets handling.

Until those values are tied to actual source code, this documentation should not invent commands.

## Centaurus development environment

Centaurus AI documentation currently describes architecture, processing, decision logic, cybersecurity, and limitations. A future source release should specify runtime environment; language/framework versions; model or rules-engine dependencies; data schemas; test/evaluation procedure; development datasets or synthetic fixtures where safe; deterministic configuration/version identifiers; and security boundaries.

Sensitive deployment data must not be required for basic local development.

## Configuration and secrets

Never commit real secrets.

Use patterns such as:

```text
config.example.*
.env.example
sample-config.*
```

Examples should contain placeholders only.

Do not commit API tokens; Wi-Fi passwords; private keys; SIM PINs or credentials; production endpoints that should remain private; and deployment access credentials.

## Test before proposing a change

The required tests depend on the area changed.

### Documentation-only change

Check Markdown renders; navigation works; claims match current evidence; links are valid; and no contradiction is introduced.

### Electronics change

At minimum, future workflows should include ERC/schematic checks; DRC; footprint verification; board-outline verification; drill-output verification; BOM/CPL consistency checks; and release-package inspection.

### Mechanical change

Check assembly fit; sensor clearances; cable routing; fastener access; service access; print/manufacturing constraints; and the 250 × 250 × 250 mm single-part limit where it applies.

### Software change

Check build success; configuration validation; sensor/interface behavior; failure handling; backward compatibility where required; and update/rollback behavior when relevant.

## Commit discipline

Keep each commit understandable. A commit should ideally represent one coherent engineering change.

Prefer:

```text
Add radar coverage calibration procedure
Fix Rosetta manufacturing package checklist
Clarify Durrës pilot status
```

Avoid:

```text
changes
update files
final final
```

## Pull requests

For external or substantial contributions, use a pull request.

A useful pull request description should answer What changed?; Why was it changed?; Which ORIGIN revision/subsystem is affected?; How was it tested?; Does it alter a public technical claim?; Does it introduce a compatibility change?; and Are documentation updates included?.

## Reproducibility rule

Do not describe a development environment as reproducible until another person can follow the documented steps from a clean environment and reach the expected result.

## Next steps

As Team Galene publishes authoritative hardware/software/CAD repositories, this setup page should be expanded with exact tool versions and commands rather than generic placeholders.
