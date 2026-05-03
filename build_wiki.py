#!/usr/bin/env python3
"""
AIMA Wiki Builder - Processes chapter text files and generates wiki pages.
"""

import os
import re
from datetime import datetime
from pathlib import Path

WIKI_DIR = Path("/Users/fharook/Desktop/LLM-Wiki/wiki")
CHAPTERS_DIR = WIKI_DIR / "chapters"
TOPICS_DIR = WIKI_DIR / "topics"
ENTITIES_DIR = WIKI_DIR / "entities"
CONCEPTS_DIR = WIKI_DIR / "concepts"
SYNTHESIS_DIR = WIKI_DIR / "synthesis"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"
OVERVIEW_FILE = WIKI_DIR / "overview.md"
TODAY = datetime.now().strftime("%Y-%m-%d")

CHAPTERS = [
    (1, "Introduction"),
    (2, "Intelligent Agents"),
    (3, "Solving Problems by Searching"),
    (4, "Search in Complex Environments"),
    (5, "Constraint Satisfaction Problems"),
    (6, "Adversarial Search and Games"),
    (7, "Logical Agents"),
    (8, "First-Order Logic"),
    (9, "Inference in First-Order Logic"),
    (10, "Knowledge Representation"),
    (11, "Automated Planning"),
    (12, "Quantifying Uncertainty"),
    (13, "Probabilistic Reasoning"),
    (14, "Probabilistic Reasoning over Time"),
    (15, "Making Simple Decisions"),
    (16, "Making Complex Decisions"),
    (17, "Multiagent Decision Making"),
    (18, "Probabilistic Programming"),
    (19, "Learning from Examples"),
    (20, "Knowledge in Learning"),
    (21, "Learning Probabilistic Models"),
    (22, "Deep Learning"),
    (23, "Reinforcement Learning"),
    (24, "Natural Language Processing"),
    (25, "Deep Learning for Natural Language Processing"),
    (26, "Robotics"),
    (27, "Computer Vision"),
    (28, "Philosophy, Ethics, and Safety of AI"),
    (29, "The Future of AI"),
]

# Chapter-to-part mapping based on AIMA 4th edition structure
PARTS = {
    1: "Part I: Artificial Intelligence",
    2: "Part I: Artificial Intelligence",
    3: "Part II: Problem-Solving",
    4: "Part II: Problem-Solving",
    5: "Part II: Problem-Solving",
    6: "Part II: Problem-Solving",
    7: "Part III: Knowledge, Reasoning, and Planning",
    8: "Part III: Knowledge, Reasoning, and Planning",
    9: "Part III: Knowledge, Reasoning, and Planning",
    10: "Part III: Knowledge, Reasoning, and Planning",
    11: "Part III: Knowledge, Reasoning, and Planning",
    12: "Part IV: Uncertain Knowledge and Reasoning",
    13: "Part IV: Uncertain Knowledge and Reasoning",
    14: "Part IV: Uncertain Knowledge and Reasoning",
    15: "Part IV: Uncertain Knowledge and Reasoning",
    16: "Part IV: Uncertain Knowledge and Reasoning",
    17: "Part IV: Uncertain Knowledge and Reasoning",
    18: "Part IV: Uncertain Knowledge and Reasoning",
    19: "Part V: Learning",
    20: "Part V: Learning",
    21: "Part V: Learning",
    22: "Part V: Learning",
    23: "Part V: Learning",
    24: "Part VI: Communicating, Perceiving, and Acting",
    25: "Part VI: Communicating, Perceiving, and Acting",
    26: "Part VI: Communicating, Perceiving, and Acting",
    27: "Part VI: Communicating, Perceiving, and Acting",
    28: "Part VII: Conclusions",
    29: "Part VII: Conclusions",
}


def read_chapter_text(num):
    """Read extracted chapter text from temp directory."""
    safe_title = CHAPTERS[num - 1][1].replace(" ", "_").replace(",", "").replace("'", "")
    filepath = f"/tmp/chapters/ch_{num:02d}_{safe_title}.txt"
    with open(filepath, "r") as f:
        return f.read()


def extract_sections(text, chapter_num):
    """Extract section headings and their content from chapter text."""
    sections = []
    current_section = "Introduction"
    current_content = []

    # Pattern for section headers like "1.1 What Is AI?" or "1.1.1 Acting humanly"
    section_pattern = re.compile(rf'^{chapter_num}\.(\d+(?:\.\d+)?)\s+([A-Z][A-Za-z\s,\'\-:]+?)\s*$')

    for line in text.split("\n"):
        m = section_pattern.match(line.strip())
        if m:
            if current_content:
                sections.append((current_section, "\n".join(current_content)))
            current_section = f"{chapter_num}.{m.group(1)} {m.group(2).strip()}"
            current_content = []
        else:
            current_content.append(line)

    if current_content:
        sections.append((current_section, "\n".join(current_content)))

    return sections


def extract_key_entities(text):
    """Extract named entities and key people mentioned in text."""
    known_people = [
        "Alan Turing", "Aristotle", "Bertrand Russell", "Immanuel Kant",
        "John McCarthy", "Marvin Minsky", "Allen Newell", "Herbert Simon",
        "Claude Shannon", "Judea Pearl", "Thomas Bayes", "Andrey Markov",
        "Richard Bellman", "Andrew Barto", "Richard Sutton", "Geoffrey Hinton",
        "Yann LeCun", "Yoshua Bengio", "Jürgen Schmidhuber", "John von Neumann",
        "John Searle", "Kurt Gödel", "George Boole", "Ada Lovelace",
        "Charles Babbage", "Norbert Wiener", "Warren McCulloch", "Walter Pitts",
        "Frank Rosenblatt", "Donald Hebb", "Oliver Selfridge", "Seymour Papert",
        "John Haugeland", "Drew McDermott", "Patrick Winston", "Terry Winograd",
        "Rodney Brooks", "Hans Moravec", "Douglas Lenat", "Raj Reddy",
        "Tomas Lozano-Perez", "Peter Norvig", "Stuart Russell", "Ian Goodfellow",
        "Ilya Sutskever", "Alex Krizhevsky", "Demis Hassabis", "Fei-Fei Li",
        "Christopher Manning", "Dan Jurafsky", "Leslie Valiant", "Jitendra Malik",
    ]

    entities = set()
    for name in known_people:
        if name in text:
            entities.add(name)

    return sorted(list(entities))


def extract_algorithms(text):
    """Identify algorithm names mentioned in text."""
    algorithm_patterns = [
        r"[A-Z][a-z]*(?:\s+[A-Z][a-z]*)*\s+(?:Algorithm|algorithm|search|Search)",
        r"(?:A\*|BFS|DFS|IDS|UCS|Minimax|Alpha-Beta|Monte Carlo|Value Iteration|Policy Iteration|Q-Learning|Backpropagation|Gradient Descent)",
    ]

    algorithms = set()
    for pattern in algorithm_patterns:
        for m in re.finditer(pattern, text):
            name = m.group(0).strip()
            if len(name) > 3 and len(name) < 50:
                algorithms.add(name)

    return list(algorithms)[:10]


def create_chapter_page(num, title, text):
    """Generate a wiki chapter page."""
    sections = extract_sections(text, num)
    entities = extract_key_entities(text)
    algorithms = extract_algorithms(text)

    # Build key points from first few sections
    key_points = []
    for section_name, section_content in sections[:5]:
        # Get first meaningful paragraph
        paragraphs = [p.strip() for p in section_content.split("\n\n") if p.strip() and len(p.strip()) > 100]
        if paragraphs:
            first_para = paragraphs[0][:300]
            key_points.append(f"**{section_name}**: {first_para}...")

    # Build cross-references
    part = PARTS.get(num, "")
    cross_refs = []
    if num > 1:
        prev_num, prev_title = CHAPTERS[num - 2]
        cross_refs.append(f"- Previous: [[Chapter {prev_num} - {prev_title}]]")
    if num < len(CHAPTERS):
        next_num, next_title = CHAPTERS[num]
        cross_refs.append(f"- Next: [[Chapter {next_num} - {next_title}]]")

    part_chapters = [n for n, t in CHAPTERS if PARTS.get(n) == part]
    if len(part_chapters) > 1:
        cross_refs.append(f"- Part: {part}")

    # Entity links
    entity_links = [f"[[{e}]]" for e in entities[:5]]

    # Word count
    word_count = len(text.split())

    page = f"""---
type: chapter
tags: [aima, chapter, {title.lower().replace(" ", "-")}]
created: {TODAY}
updated: {TODAY}
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: {num}
---

# Chapter {num} - {title}

## Summary

Chapter {num} of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **{title.lower()}**. This chapter is part of {part}. The chapter contains approximately {word_count:,} words and covers foundational concepts, algorithms, and frameworks central to understanding {title.lower()} in the context of artificial intelligence.

## Key Points

{chr(10).join(f"- {kp}" for kp in key_points[:5])}

## Sections Overview

"""

    for section_name, section_content in sections:
        # Clean section content - remove page numbers, artifacts
        cleaned = re.sub(r'^\d+\s+Chapter\s+\d+', '', section_content, flags=re.MULTILINE)
        cleaned = re.sub(r'Section\s+\d+\.\d+\s+', '', cleaned)
        paragraphs = [p.strip() for p in cleaned.split("\n\n") if p.strip() and len(p.strip()) > 50]

        if paragraphs:
            page += f"### {section_name}\n\n"
            # Take first paragraph as summary
            page += f"{paragraphs[0][:400]}...\n\n"

    page += f"""## Key Entities Mentioned

{chr(10).join(f'- {e}' for e in entities) if entities else '- None identified'}

## Algorithms & Concepts

{chr(10).join(f'- [[{a}]]' for a in algorithms) if algorithms else '- To be identified on detailed review'}

## Cross-References

{chr(10).join(cross_refs)}

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter {num}. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
"""

    return page


def create_entity_page(name, chapter_refs, text_snippets):
    """Generate an entity page."""
    page = f"""---
type: entity
tags: [person, ai-researcher]
created: {TODAY}
updated: {TODAY}
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
---

# {name}

## Summary

{name} is referenced in *Artificial Intelligence: A Modern Approach* as a key figure in the development of AI concepts and methodologies.

## Appearances in AIMA

{chr(10).join(f"- [[{cr}]]" for cr in chapter_refs[:5])}

## Contributions

To be expanded on detailed review of source chapters.

## Cross-References

- See also: [[History of Artificial Intelligence]]
- Related: [[Philosophy, Ethics, and Safety of AI]]

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
"""
    return page


def update_index():
    """Generate the index.md file."""
    index = f"""# Wiki Index

_Last updated: {TODAY}_

## Chapters

"""

    for num, title in CHAPTERS:
        page_file = CHAPTERS_DIR / f"Chapter {num} - {title}.md"
        if page_file.exists():
            index += f"- [[Chapter {num} - {title}]] — {title}\n"

    index += """
## Topics

"""
    # Add topic pages if they exist
    for f in TOPICS_DIR.glob("*.md"):
        if f.name != ".gitkeep":
            index += f"- [[{f.stem}]]\n"

    index += """
## Entities

"""
    for f in ENTITIES_DIR.glob("*.md"):
        if f.name != ".gitkeep":
            index += f"- [[{f.stem}]]\n"

    index += """
## Concepts

"""
    for f in CONCEPTS_DIR.glob("*.md"):
        if f.name != ".gitkeep":
            index += f"- [[{f.stem}]]\n"

    index += """
## Synthesis

"""
    for f in SYNTHESIS_DIR.glob("*.md"):
        if f.name != ".gitkeep":
            index += f"- [[{f.stem}]]\n"

    return index


def main():
    print("=" * 60)
    print("AIMA Wiki Builder")
    print("=" * 60)

    created_chapters = []
    all_entities = {}

    # Process each chapter
    for num, title in CHAPTERS:
        print(f"\nProcessing Chapter {num}: {title}...")

        text = read_chapter_text(num)
        page_content = create_chapter_page(num, title, text)

        # Write chapter page
        filename = f"Chapter {num} - {title}.md"
        filepath = CHAPTERS_DIR / filename
        with open(filepath, "w") as f:
            f.write(page_content)

        created_chapters.append((num, title))

        # Extract entities for later
        entities = extract_key_entities(text)
        for e in entities:
            if e not in all_entities:
                all_entities[e] = []
            all_entities[e].append(f"Chapter {num} - {title}")

        print(f"  -> Created: {filename}")
        print(f"  -> Entities found: {len(entities)}")

    # Create entity pages
    print("\n" + "=" * 60)
    print("Creating entity pages...")
    print("=" * 60)

    for name, refs in sorted(all_entities.items()):
        # Check if entity already exists
        safe_name = name.replace(" ", "_")
        filepath = ENTITIES_DIR / f"{safe_name}.md"
        if not filepath.exists():
            entity_page = create_entity_page(name, refs, [])
            with open(filepath, "w") as f:
                f.write(entity_page)
            print(f"  -> Created: {filepath.name}")

    # Create key concept pages
    print("\n" + "=" * 60)
    print("Creating concept pages...")
    print("=" * 60)

    concepts = {
        "Rational Agent": "The core paradigm of AIMA - agents that act to achieve the best expected outcome",
        "Intelligent Agents": "Entities that perceive their environment and take actions to achieve goals",
        "Knowledge Representation": "How AI systems represent and reason about the world",
        "Uncertainty": "Handling incomplete or noisy information in AI systems",
        "Machine Learning": "Systems that improve their performance through experience",
        "Search Algorithms": "Fundamental problem-solving strategies in AI",
        "Ethics and Safety": "Considerations around responsible AI development and deployment",
    }

    for concept, desc in concepts.items():
        filepath = CONCEPTS_DIR / f"{concept}.md"
        if not filepath.exists():
            page = f"""---
type: concept
tags: [aima, core-concept]
created: {TODAY}
updated: {TODAY}
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
---

# {concept}

## Summary

{desc}. This is a foundational concept throughout *Artificial Intelligence: A Modern Approach* (4th Edition).

## Key Points

- Central to the rational agent paradigm
- Appears across multiple chapters and problem domains
- Evolves in sophistication throughout the book

## Details

To be expanded as chapters are ingested and cross-referenced.

## Cross-References

- Related: [[Rationality]]
- See also: [[Intelligent Agents]]

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
"""
            with open(filepath, "w") as f:
                f.write(page)
            print(f"  -> Created: {filepath.name}")

    # Create key topic pages
    print("\n" + "=" * 60)
    print("Creating topic pages...")
    print("=" * 60)

    topics = [
        ("A* Search Algorithm", "Informed search using heuristic function"),
        ("Minimax Algorithm", "Adversarial search for two-player games"),
        ("Bayesian Networks", "Probabilistic graphical models for reasoning under uncertainty"),
        ("Markov Decision Processes", "Framework for sequential decision making under uncertainty"),
        ("Neural Networks", "Foundation of deep learning and representation learning"),
        ("Natural Language Processing", "Computational approaches to understanding human language"),
        ("Computer Vision", "Enabling machines to interpret visual information"),
        ("Robotics", "Intelligent physical agents interacting with the world"),
    ]

    for topic, desc in topics:
        filepath = TOPICS_DIR / f"{topic}.md"
        if not filepath.exists():
            page = f"""---
type: topic
tags: [aima, algorithm]
created: {TODAY}
updated: {TODAY}
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
---

# {topic}

## Summary

{desc}. Covered in detail in *Artificial Intelligence: A Modern Approach* (4th Edition).

## Key Points

- Fundamental algorithm/framework in AI
- Detailed treatment in AIMA with pseudocode and analysis
- Connects to multiple chapters and problem domains

## Details

To be expanded as relevant chapters are processed in detail.

## Cross-References

- Related: [[Search Algorithms]]
- See also: [[Rational Agent]]

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
"""
            with open(filepath, "w") as f:
                f.write(page)
            print(f"  -> Created: {filepath.name}")

    # Update index
    print("\n" + "=" * 60)
    print("Updating index.md...")
    print("=" * 60)

    index_content = update_index()
    with open(INDEX_FILE, "w") as f:
        f.write(index_content)
    print("  -> Updated: index.md")

    # Append to log
    print("\n" + "=" * 60)
    print("Updating log.md...")
    print("=" * 60)

    log_entry = f"""
## [{TODAY}] ingest | AIMA 4th Edition - Full Book Ingest

Processed all 29 chapters from *Artificial Intelligence: A Modern Approach* (4th Edition).
- Created {len(created_chapters)} chapter summary pages
- Created {len(all_entities)} entity pages
- Created {len(concepts)} concept pages
- Created {len(topics)} topic pages
- Updated index.md with all new pages
"""

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    print("  -> Appended to log.md")

    # Update overview
    print("\n" + "=" * 60)
    print("Updating overview.md...")
    print("=" * 60)

    overview_update = f"""
## Reading Status (Updated {TODAY})

| Metric | Value |
|--------|-------|
| Chapters Ingested | {len(created_chapters)} / 29 |
| Wiki Pages | {len(created_chapters) + len(all_entities) + len(concepts) + len(topics) + 3} |
| Last Updated | {TODAY} |
| Current Status | Initial ingest complete |
"""

    # Read existing overview and update, or create if missing
    if OVERVIEW_FILE.exists():
        with open(OVERVIEW_FILE, "r") as f:
            overview = f.read()

        overview = re.sub(
            r"## Reading Status\n\n\| Metric.*?\| Current Status \|.*?\|",
            overview_update.strip(),
            overview,
            flags=re.DOTALL
        )
    else:
        overview = f"""---
type: overview
tags: [book, ai, textbook]
created: {TODAY}
updated: {TODAY}
---

# Artificial Intelligence: A Modern Approach

## Overview

**Title:** Artificial Intelligence: A Modern Approach (4th Edition)
**Authors:** Stuart Russell, Peter Norvig
**First Published:** 1995 (4th Edition: 2020)

The definitive textbook on artificial intelligence.

{overview_update.strip()}
"""

    with open(OVERVIEW_FILE, "w") as f:
        f.write(overview)
    print("  -> Updated overview.md")

    print("\n" + "=" * 60)
    print("Wiki build complete!")
    print(f"Total pages created: {len(created_chapters) + len(all_entities) + len(concepts) + len(topics)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
