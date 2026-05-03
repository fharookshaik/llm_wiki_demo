# LLM-Wiki: AIMA Knowledge Base

A persistent, compounding wiki for **Artificial Intelligence: A Modern Approach (4th Edition)** by Stuart Russell and Peter Norvig — built and maintained by an LLM agent.

## The Idea

Instead of treating documents as static files to be retrieved at query time (RAG), this project uses an LLM to **incrementally build and maintain a structured wiki** that grows richer with every source added. The wiki is a persistent artifact — cross-references accumulate, contradictions get flagged, and synthesis reflects everything ingested.

The pattern is generalizable to any domain: research, reading notes, business documentation, personal knowledge management.

## Architecture

```
├── raw/                    # Immutable source documents (PDFs, etc.)
├── wiki/                   # The working wiki (LLM-owned)
│   ├── index.md            # Content catalog
│   ├── log.md              # Append-only activity log
│   ├── overview.md         # Book overview and reading status
│   ├── chapters/           # Chapter-by-chapter summaries
│   ├── topics/             # Algorithms and technical topics
│   ├── entities/           # Key people and frameworks
│   ├── concepts/           # Themes and recurring ideas
│   └── synthesis/          # Analyses and deep-dive essays
├── AGENTS.md               # Schema — instructions for the LLM agent
├── RULES.md                # High-level pattern description
├── build_wiki.py           # Script to extract and build wiki from raw sources
└── normalize_obsidian.py   # Script to export wiki to an Obsidian vault
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- An LLM agent (Claude Code, Codex, opencode, etc.)

### Quick Start

```bash
# Install dependencies
uv pip install pdfplumber

# Build wiki from raw sources
uv run python build_wiki.py

# Export to Obsidian
uv run python normalize_obsidian.py
```

### Using with an LLM Agent

1. **Place source documents** (PDFs, notes, articles) into the `raw/` directory
2. **Ask your LLM agent** to process them following the `AGENTS.md` schema
3. **The agent will** read the source, update chapter pages, create entity/concept pages, update the index, and log the activity

### Workflows

#### Ingest — Processing a New Source

1. Drop a new file into `raw/`
2. Ask the LLM to process it
3. The LLM reads, discusses key takeaways, creates/updates wiki pages, updates `index.md`, appends to `log.md`

#### Query — Asking Questions

1. Ask the LLM a question about the material
2. The LLM reads `index.md`, finds relevant pages, synthesizes an answer
3. If the answer is substantive, it gets saved as a new page in `wiki/synthesis/`

#### Lint — Health-Checking

Periodically ask the LLM to check for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Missing cross-references
- Important concepts without their own page

## Obsidian Export

The wiki can be exported as a ready-to-use Obsidian vault:

```bash
uv run python normalize_obsidian.py
```

This creates `LLM-Wiki-obsidian/` with all files formatted for Obsidian, including:
- `00 - Map of Content.md` — Entry point with organized links
- `.obsidian/app.json` — Pre-configured settings
- All `[[wiki links]]` normalized for Obsidian resolution

Open the exported folder in Obsidian via **File → Open Folder as Vault**.

## File Conventions

### YAML Frontmatter

Every wiki page includes frontmatter:

```yaml
---
type: chapter | topic | entity | concept | synthesis
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["source reference"]
chapter: N  # only for chapter/topic pages
---
```

### Naming

- **Chapters**: `Chapter N - Title`
- **Algorithms**: `Algorithm Name` (e.g., `A* Search Algorithm`)
- **Concepts**: `Concept Name` (e.g., `Rational Agent`)
- **People**: `Full Name` (e.g., `Stuart Russell`)
- **Cross-references**: `[[Page Name]]` with Title Case

## Current State

| Metric | Value |
|--------|-------|
| Chapters | 29 / 29 |
| Wiki Pages | 73 |
| Entity Pages | 29 |
| Concept Pages | 7 |
| Topic Pages | 8 |

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions, maintaining consistency. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a link, and can touch 15 files in one pass.

The human's job is to curate sources, direct analysis, ask good questions. The LLM handles everything else.

## License

This project is a personal knowledge management system. The AIMA source material is copyrighted by its authors and Pearson.
