#!/usr/bin/env python3
"""
Normalize all markdown files for Obsidian compatibility.
- Fix [[links]] to use page names without directory prefixes
- Ensure consistent naming across all files
- Add MOC (Map of Content) page
"""

import os
import re
from pathlib import Path

VAULT_DIR = Path("/Users/fharook/Desktop/LLM-Wiki-obsidian")

def get_all_page_names():
    """Collect all page names from the vault."""
    pages = set()
    for subdir in ["chapters", "entities", "concepts", "topics", "synthesis"]:
        dirpath = VAULT_DIR / subdir
        if dirpath.exists():
            for f in dirpath.glob("*.md"):
                pages.add(f.stem)
    for f in VAULT_DIR.glob("*.md"):
        pages.add(f.stem)
    return pages

def normalize_links_in_file(filepath):
    """Fix [[links]] in a file to work in Obsidian."""
    with open(filepath, "r") as f:
        content = f.read()

    original = content

    # Fix [[directory/Page Name]] -> [[Page Name]]
    content = re.sub(r'\[\[(?:chapters|entities|concepts|topics|synthesis)/([^\]]+)\]\]', r'[[\1]]', content)

    # Fix [[Page Name]] -> [[Page Name]] (already correct, but ensure no underscores)
    # Replace underscores in links with spaces
    def fix_link(match):
        link_text = match.group(1)
        return f"[[{link_text.replace('_', ' ')}]]"
    content = re.sub(r'\[\[([^\]]+)\]\]', fix_link, content)

    if content != original:
        with open(filepath, "w") as f:
            f.write(content)
        return True
    return False

def normalize_filenames():
    """Rename files to use spaces instead of underscores."""
    renames = []
    for subdir in ["chapters", "entities", "concepts", "topics", "synthesis"]:
        dirpath = VAULT_DIR / subdir
        if dirpath.exists():
            for f in dirpath.glob("*.md"):
                if "_" in f.name:
                    new_name = f.name.replace("_", " ")
                    new_path = dirpath / new_name
                    f.rename(new_path)
                    renames.append((f.name, new_name))
    return renames

def create_moc():
    """Create a Map of Content page for Obsidian."""
    toc = """---
tags: [moc, index]
created: 2026-05-02
---

# AIMA Wiki - Map of Content

*Artificial Intelligence: A Modern Approach* (4th Edition) by Stuart Russell and Peter Norvig

## Reading

- [[overview]] — Book overview and reading status
- [[index]] — Full content catalog

## Chapters (29)

### Part I: Artificial Intelligence
- [[Chapter 1 - Introduction]]
- [[Chapter 2 - Intelligent Agents]]

### Part II: Problem-Solving
- [[Chapter 3 - Solving Problems by Searching]]
- [[Chapter 4 - Search in Complex Environments]]
- [[Chapter 5 - Constraint Satisfaction Problems]]
- [[Chapter 6 - Adversarial Search and Games]]

### Part III: Knowledge, Reasoning, and Planning
- [[Chapter 7 - Logical Agents]]
- [[Chapter 8 - First-Order Logic]]
- [[Chapter 9 - Inference in First-Order Logic]]
- [[Chapter 10 - Knowledge Representation]]
- [[Chapter 11 - Automated Planning]]

### Part IV: Uncertain Knowledge and Reasoning
- [[Chapter 12 - Quantifying Uncertainty]]
- [[Chapter 13 - Probabilistic Reasoning]]
- [[Chapter 14 - Probabilistic Reasoning over Time]]
- [[Chapter 15 - Making Simple Decisions]]
- [[Chapter 16 - Making Complex Decisions]]
- [[Chapter 17 - Multiagent Decision Making]]
- [[Chapter 18 - Probabilistic Programming]]

### Part V: Learning
- [[Chapter 19 - Learning from Examples]]
- [[Chapter 20 - Knowledge in Learning]]
- [[Chapter 21 - Learning Probabilistic Models]]
- [[Chapter 22 - Deep Learning]]
- [[Chapter 23 - Reinforcement Learning]]

### Part VI: Communicating, Perceiving, and Acting
- [[Chapter 24 - Natural Language Processing]]
- [[Chapter 25 - Deep Learning for Natural Language Processing]]
- [[Chapter 26 - Robotics]]
- [[Chapter 27 - Computer Vision]]

### Part VII: Conclusions
- [[Chapter 28 - Philosophy, Ethics, and Safety of AI]]
- [[Chapter 29 - The Future of AI]]

## Key Concepts

- [[Rational Agent]]
- [[Intelligent Agents]]
- [[Knowledge Representation]]
- [[Uncertainty]]
- [[Machine Learning]]
- [[Search Algorithms]]
- [[Ethics and Safety]]

## Key Algorithms & Topics

- [[A* Search Algorithm]]
- [[Minimax Algorithm]]
- [[Bayesian Networks]]
- [[Markov Decision Processes]]
- [[Neural Networks]]
- [[Natural Language Processing]]
- [[Computer Vision]]
- [[Robotics]]

## Key People

- [[Alan Turing]]
- [[John McCarthy]]
- [[Marvin Minsky]]
- [[Stuart Russell]]
- [[Judea Pearl]]
- [[Geoffrey Hinton]]
- [[Yann LeCun]]
- [[Yoshua Bengio]]
"""
    with open(VAULT_DIR / "00 - Map of Content.md", "w") as f:
        f.write(toc)

def main():
    print("Normalizing Obsidian vault...")

    # Step 1: Rename files with underscores
    renames = normalize_filenames()
    for old, new in renames:
        print(f"  Renamed: {old} -> {new}")

    # Step 2: Normalize links in all files
    fixed_count = 0
    for md_file in VAULT_DIR.rglob("*.md"):
        if normalize_links_in_file(md_file):
            fixed_count += 1
            print(f"  Fixed links in: {md_file.relative_to(VAULT_DIR)}")

    # Step 3: Create MOC
    create_moc()
    print("  Created: 00 - Map of Content.md")

    print(f"\nDone! Fixed links in {fixed_count} files.")

if __name__ == "__main__":
    main()
