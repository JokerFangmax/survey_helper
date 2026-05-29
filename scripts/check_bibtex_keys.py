#!/usr/bin/env python3
"""Check BibTeX key coverage between data/papers.csv and bib/references.bib."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS_CSV = ROOT / "data" / "papers.csv"
REFERENCES_BIB = ROOT / "bib" / "references.bib"


ENTRY_RE = re.compile(r"@\s*([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


def read_paper_keys(path: Path = PAPERS_CSV) -> list[str]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "bibtex_key" not in reader.fieldnames:
            raise SystemExit(f"{path}: missing required 'bibtex_key' column")
        return [(row.get("bibtex_key") or "").strip() for row in reader]


def read_bibtex_keys(path: Path = REFERENCES_BIB) -> list[str]:
    text = path.read_text(encoding="utf-8-sig")
    return [match.group(2).strip() for match in ENTRY_RE.finditer(text)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--papers", type=Path, default=PAPERS_CSV)
    parser.add_argument("--bib", type=Path, default=REFERENCES_BIB)
    args = parser.parse_args()

    paper_keys = read_paper_keys(args.papers)
    bib_keys = read_bibtex_keys(args.bib)
    paper_key_set = {key for key in paper_keys if key}
    bib_key_set = set(bib_keys)

    missing = sorted(paper_key_set - bib_key_set)
    unused = sorted(bib_key_set - paper_key_set)
    duplicate_csv_keys = sorted(key for key, count in Counter(paper_keys).items() if key and count > 1)
    duplicate_bib_keys = sorted(key for key, count in Counter(bib_keys).items() if key and count > 1)

    print(f"CSV rows with BibTeX keys: {len([key for key in paper_keys if key])}")
    print(f"Unique CSV BibTeX keys: {len(paper_key_set)}")
    print(f"BibTeX entries: {len(bib_keys)}")
    print(f"Unique BibTeX keys: {len(bib_key_set)}")

    if missing:
        print("\nMissing BibTeX entries for CSV keys:")
        for key in missing:
            print(f"- {key}")
    else:
        print("\nMissing BibTeX entries for CSV keys: none")

    if unused:
        print("\nUnused BibTeX entries:")
        for key in unused:
            print(f"- {key}")
    else:
        print("\nUnused BibTeX entries: none")

    if duplicate_csv_keys:
        print("\nDuplicate bibtex_key values in CSV:")
        for key in duplicate_csv_keys:
            print(f"- {key}")

    if duplicate_bib_keys:
        print("\nDuplicate BibTeX entry keys:")
        for key in duplicate_bib_keys:
            print(f"- {key}")

    return 1 if missing or unused or duplicate_csv_keys or duplicate_bib_keys else 0


if __name__ == "__main__":
    raise SystemExit(main())
