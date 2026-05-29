#!/usr/bin/env python3
"""Validate the paper database and write data/validation_report.md."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
PAPERS_CSV = ROOT / "data" / "papers.csv"
REFERENCES_BIB = ROOT / "bib" / "references.bib"
DEEP_RESEARCH_REPORT = ROOT / "data" / "deep-research-report.md"
VALIDATION_REPORT = ROOT / "data" / "validation_report.md"

REQUIRED_COLUMNS = [
    "id",
    "title",
    "authors",
    "year",
    "venue",
    "arxiv_id",
    "doi",
    "url",
    "bibtex_key",
    "category",
    "sub_category",
    "task",
    "input_modality",
    "output_modality",
    "model_family",
    "dynamics_modeling",
    "physical_prior",
    "interaction",
    "benchmark",
    "dataset",
    "metrics",
    "key_contribution",
    "main_limitation",
    "relevance_to_survey",
    "status",
    "notes_file",
]

ENTRY_RE = re.compile(r"@\s*([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
FIELD_RE = re.compile(r"(?ims)^\s*([A-Za-z][A-Za-z0-9_-]*)\s*=\s*([{\"])(.*?)(?:[}\"])\s*,?\s*$")
RANKED_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(P\d{3})\s*\|\s*\*\*(.*?)\*\*\s*(?:—|-|鈥\?)\s*(.*?)\s*\|\s*(\d{4})\s*\|\s*([^|]+?)\s*\|\s*`?([^`|]+?)`?\s*\|\s*([^|]+?)\s*\|",
    re.MULTILINE,
)
ARXIV_RE = re.compile(r"(?:arxiv\.org/abs/|arXiv:)?(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)


@dataclass
class BibEntry:
    entry_type: str
    key: str
    fields: dict[str, str]


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def normalize_url(value: str) -> str:
    return value.strip().lower().rstrip("/")


def normalize_unknown(value: str) -> str:
    return value.strip()


def extract_arxiv(value: str) -> str:
    match = ARXIV_RE.search(value or "")
    return match.group(1) if match else ""


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def bullet(items: Iterable[str]) -> list[str]:
    values = list(items)
    return [f"- {item}" for item in values] if values else ["- None found."]


def parse_csv_with_widths(path: Path) -> tuple[list[str], list[dict[str, str]], list[dict[str, object]]]:
    rows: list[dict[str, str]] = []
    width_issues: list[dict[str, object]] = []
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return [], [], [{"line": 1, "columns": 0, "expected": len(REQUIRED_COLUMNS)}]

        expected_width = len(header)
        for row in reader:
            if len(row) != expected_width:
                width_issues.append(
                    {
                        "line": reader.line_num,
                        "id": row[0] if row else "",
                        "columns": len(row),
                        "expected": expected_width,
                    }
                )
            padded = row[:expected_width] + [""] * max(0, expected_width - len(row))
            rows.append(dict(zip(header, padded)))
    return header, rows, width_issues


def parse_bibtex_entries(path: Path) -> list[BibEntry]:
    text = path.read_text(encoding="utf-8-sig")
    entries: list[BibEntry] = []
    for match in ENTRY_RE.finditer(text):
        start = match.start()
        brace_pos = text.find("{", start)
        depth = 0
        end = brace_pos
        for pos in range(brace_pos, len(text)):
            char = text[pos]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = pos + 1
                    break
        body = text[match.end() : end - 1]
        fields: dict[str, str] = {}
        for line in body.splitlines():
            field_match = FIELD_RE.match(line)
            if field_match:
                fields[field_match.group(1).lower()] = field_match.group(3).strip()
        entries.append(BibEntry(match.group(1), match.group(2).strip(), fields))
    return entries


def parse_ranked_list(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    ranked: list[dict[str, str]] = []
    for match in RANKED_ROW_RE.finditer(text):
        title = re.sub(r"\s+", " ", match.group(3)).strip()
        ranked.append(
            {
                "rank": match.group(1),
                "id": match.group(2),
                "title": title,
                "year": match.group(5).strip(),
                "venue": match.group(6).strip(),
                "url": match.group(7).strip(),
                "arxiv_id": match.group(8).strip(),
            }
        )
    return ranked


def groups_by(rows: list[dict[str, str]], field: str, normalizer=lambda value: value.strip()) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        value = normalizer(row.get(field, ""))
        if value and value.upper() != "UNKNOWN":
            grouped[value].append(row)
    return {key: value for key, value in grouped.items() if len(value) > 1}


def duplicate_lines(label: str, groups: dict[str, list[dict[str, str]]]) -> list[str]:
    lines = [f"### {label}"]
    if not groups:
        lines.append("- None found.")
        return lines
    for value, rows in sorted(groups.items()):
        ids = ", ".join(row.get("id", "") for row in rows)
        titles = "; ".join(f"{row.get('id', '')}: {row.get('title', '')}" for row in rows)
        lines.append(f"- `{markdown_escape(value)}` appears in {ids}. {markdown_escape(titles)}")
    return lines


def find_suspicious_metadata(rows: list[dict[str, str]]) -> list[str]:
    issues: list[str] = []
    ids = [row.get("id", "") for row in rows]
    for key, count in Counter(ids).items():
        if key and count > 1:
            issues.append(f"`{key}` appears {count} times in `id`.")

    current_year = 2026
    for row in rows:
        paper_id = row.get("id", "")
        title = row.get("title", "")
        year = row.get("year", "").strip()
        if not re.fullmatch(r"\d{4}", year):
            issues.append(f"{paper_id}: year `{year}` is not a four-digit year.")
        elif int(year) > current_year:
            issues.append(f"{paper_id}: year `{year}` is later than the current project date.")

        arxiv_id = row.get("arxiv_id", "").strip()
        url = row.get("url", "").strip()
        if arxiv_id.upper() != "UNKNOWN" and not re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id):
            issues.append(f"{paper_id}: arxiv_id `{arxiv_id}` does not match the expected numeric arXiv format.")
        url_arxiv = extract_arxiv(url)
        if arxiv_id.upper() != "UNKNOWN" and url_arxiv and arxiv_id != url_arxiv:
            issues.append(f"{paper_id}: arxiv_id `{arxiv_id}` does not match arXiv URL `{url_arxiv}`.")

        if row.get("doi", "").strip().upper() == "UNKNOWN" and "doi.org/" in url.lower():
            issues.append(f"{paper_id}: DOI is UNKNOWN but URL appears to be a DOI URL.")
        if not row.get("bibtex_key", "").strip():
            issues.append(f"{paper_id}: empty bibtex_key.")
        if not row.get("notes_file", "").strip().startswith("notes/"):
            issues.append(f"{paper_id}: notes_file `{row.get('notes_file', '')}` is not under notes/.")
        elif not (ROOT / row.get("notes_file", "").strip()).exists():
            issues.append(f"{paper_id}: notes_file `{row.get('notes_file', '')}` does not exist yet.")

        if "\ufffd" in title or "鈥" in title or "顖" in title:
            issues.append(f"{paper_id}: title contains likely mojibake/encoding artifacts.")

    return issues


def compare_ranked_list(rows: list[dict[str, str]], ranked: list[dict[str, str]]) -> list[str]:
    by_id = {row["id"]: row for row in rows}
    issues: list[str] = []
    for item in ranked:
        row = by_id.get(item["id"])
        if not row:
            issues.append(f"{item['id']}: present in ranked list but missing from papers.csv.")
            continue
        mismatches = []
        if normalize_title(row.get("title", "")) != normalize_title(item["title"]):
            mismatches.append(f"title ranked=`{item['title']}` csv=`{row.get('title', '')}`")
        if row.get("year", "").strip() != item["year"]:
            mismatches.append(f"year ranked=`{item['year']}` csv=`{row.get('year', '')}`")
        ranked_arxiv = item["arxiv_id"]
        if ranked_arxiv.upper() != "UNKNOWN":
            ranked_arxiv = extract_arxiv(ranked_arxiv) or ranked_arxiv
        csv_arxiv = row.get("arxiv_id", "").strip()
        if ranked_arxiv.upper() != "UNKNOWN" and csv_arxiv.upper() != "UNKNOWN" and ranked_arxiv != csv_arxiv:
            mismatches.append(f"arxiv_id ranked=`{ranked_arxiv}` csv=`{csv_arxiv}`")
        if normalize_url(row.get("url", "")) != normalize_url(item["url"]):
            mismatches.append(f"url ranked=`{item['url']}` csv=`{row.get('url', '')}`")
        if mismatches:
            issues.append(f"{item['id']}: " + "; ".join(mismatches))

    ranked_ids = {item["id"] for item in ranked}
    for row in rows:
        if row.get("id") not in ranked_ids:
            issues.append(f"{row.get('id')}: present in papers.csv but missing from ranked list.")
    return issues


def make_report(
    header: list[str],
    rows: list[dict[str, str]],
    width_issues: list[dict[str, object]],
    bib_entries: list[BibEntry],
    ranked: list[dict[str, str]],
) -> str:
    schema_ok = header == REQUIRED_COLUMNS
    paper_keys = [row.get("bibtex_key", "").strip() for row in rows]
    paper_key_set = {key for key in paper_keys if key}
    bib_keys = [entry.key for entry in bib_entries]
    bib_key_set = set(bib_keys)

    missing_bib = sorted(paper_key_set - bib_key_set)
    unused_bib = sorted(bib_key_set - paper_key_set)
    duplicate_csv_key_groups = groups_by(rows, "bibtex_key")
    duplicate_title_groups = groups_by(rows, "title", normalize_title)
    duplicate_arxiv_groups = groups_by(rows, "arxiv_id")
    duplicate_url_groups = groups_by(rows, "url", normalize_url)
    duplicate_bib_entry_key_groups = {
        key: [{"id": key, "title": key}] * count for key, count in Counter(bib_keys).items() if key and count > 1
    }

    bib_by_title: dict[str, list[BibEntry]] = defaultdict(list)
    bib_by_url: dict[str, list[BibEntry]] = defaultdict(list)
    for entry in bib_entries:
        title = normalize_title(entry.fields.get("title", ""))
        url = normalize_url(entry.fields.get("url", ""))
        if title:
            bib_by_title[title].append(entry)
        if url:
            bib_by_url[url].append(entry)

    duplicate_bib_titles = {key: entries for key, entries in bib_by_title.items() if len(entries) > 1}
    duplicate_bib_urls = {key: entries for key, entries in bib_by_url.items() if len(entries) > 1}
    suspicious = find_suspicious_metadata(rows)
    ranked_issues = compare_ranked_list(rows, ranked)

    lines: list[str] = [
        "# Literature Database Validation Report",
        "",
        "Generated by `scripts/validate_papers.py` from the current repository files. This report does not fabricate missing metadata; uncertain fields remain as they appear in the source files.",
        "",
        "## Summary",
        "",
        f"- CSV rows: {len(rows)}",
        f"- CSV columns: {len(header)}",
        f"- Required schema match: {'yes' if schema_ok else 'no'}",
        f"- Rows with column-count problems: {len(width_issues)}",
        f"- Unique CSV BibTeX keys: {len(paper_key_set)}",
        f"- BibTeX entries: {len(bib_entries)}",
        f"- Unique BibTeX entry keys: {len(bib_key_set)}",
        f"- Ranked-list entries parsed: {len(ranked)}",
        "",
        "## Schema Check",
        "",
    ]

    if schema_ok:
        lines.append("- `data/papers.csv` follows the required schema exactly.")
    else:
        lines.extend(
            [
                "- `data/papers.csv` does not match the required schema.",
                f"- Expected: `{', '.join(REQUIRED_COLUMNS)}`",
                f"- Found: `{', '.join(header)}`",
            ]
        )

    lines.extend(["", "## Row Width Check", ""])
    if width_issues:
        lines.append("| Line | ID | Columns | Expected |")
        lines.append("|---:|---|---:|---:|")
        for issue in width_issues:
            lines.append(
                f"| {issue['line']} | {markdown_escape(issue['id'])} | {issue['columns']} | {issue['expected']} |"
            )
    else:
        lines.append("- Every data row has the same number of columns as the header.")

    lines.extend(["", "## Duplicated Papers", ""])
    lines.extend(duplicate_lines("By title", duplicate_title_groups))
    lines.append("")
    lines.extend(duplicate_lines("By arXiv ID", duplicate_arxiv_groups))
    lines.append("")
    lines.extend(duplicate_lines("By URL", duplicate_url_groups))
    lines.append("")
    lines.extend(duplicate_lines("By CSV bibtex_key", duplicate_csv_key_groups))
    lines.append("")
    lines.extend(duplicate_lines("By BibTeX entry key", duplicate_bib_entry_key_groups))
    lines.append("")
    lines.append("### BibTeX duplicate-looking entries by title")
    if duplicate_bib_titles:
        for _, entries in sorted(duplicate_bib_titles.items()):
            keys = ", ".join(entry.key for entry in entries)
            title = entries[0].fields.get("title", "UNKNOWN")
            lines.append(f"- `{markdown_escape(title)}` appears as BibTeX entries: {keys}.")
    else:
        lines.append("- None found.")
    lines.append("")
    lines.append("### BibTeX duplicate-looking entries by URL")
    if duplicate_bib_urls:
        for url, entries in sorted(duplicate_bib_urls.items()):
            keys = ", ".join(entry.key for entry in entries)
            lines.append(f"- `{markdown_escape(url)}` appears as BibTeX entries: {keys}.")
    else:
        lines.append("- None found.")

    lines.extend(["", "## Missing BibTeX Keys", ""])
    lines.extend(bullet(f"`{key}` is used in `data/papers.csv` but missing from `bib/references.bib`." for key in missing_bib))

    lines.extend(["", "## Unused BibTeX Entries", ""])
    lines.extend(bullet(f"`{key}` is present in `bib/references.bib` but not referenced by `data/papers.csv`." for key in unused_bib))

    lines.extend(["", "## Ranked List vs CSV ID Inconsistencies", ""])
    lines.extend(bullet(ranked_issues))

    lines.extend(["", "## Suspicious Metadata", ""])
    lines.extend(bullet(suspicious))

    recommendations: list[str] = []
    if not schema_ok:
        recommendations.append("Fix the `data/papers.csv` header to match the required schema.")
    if width_issues:
        recommendations.append("Fix row-width problems before adding or editing metadata.")
    if duplicate_title_groups or duplicate_arxiv_groups or duplicate_url_groups or duplicate_csv_key_groups:
        recommendations.append("Resolve duplicate CSV rows before using the database for manuscript citations.")
    if duplicate_bib_titles or duplicate_bib_urls or duplicate_bib_entry_key_groups:
        recommendations.append("Remove or justify duplicate-looking BibTeX entries.")
    if missing_bib:
        recommendations.append("Add missing BibTeX entries only after verifying metadata from primary sources.")
    if unused_bib:
        recommendations.append("Remove unused BibTeX entries or explicitly justify why they remain.")
    if ranked_issues:
        recommendations.append("Realign `data/papers.csv` IDs with the ranked list before writing manuscript text.")
    missing_notes = [issue for issue in suspicious if "notes_file" in issue and "does not exist yet" in issue]
    if missing_notes:
        recommendations.append("Create or verify the referenced `notes/` files before using rows as manuscript evidence.")
    recommendations.append("Keep `UNKNOWN` for missing arXiv IDs, DOIs, or technical fields until verified from a primary source.")

    lines.extend(["", "## Recommended Fixes", ""])
    if recommendations:
        lines.extend(f"- {item}" for item in recommendations)
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            "## Validation Status",
            "",
            "- `python scripts/validate_papers.py` is expected to exit with status 0 when schema, row width, duplicate-key, and missing-BibTeX checks pass.",
            "- `python scripts/check_bibtex_keys.py` is expected to exit with status 0 when every CSV key has a BibTeX entry and every BibTeX entry is referenced.",
            "",
            "## Reproducible Commands",
            "",
            "```powershell",
            "python scripts/validate_papers.py",
            "python scripts/check_bibtex_keys.py",
            "python -m py_compile scripts/validate_papers.py scripts/check_bibtex_keys.py",
            "```",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--papers", type=Path, default=PAPERS_CSV)
    parser.add_argument("--bib", type=Path, default=REFERENCES_BIB)
    parser.add_argument("--deep-report", type=Path, default=DEEP_RESEARCH_REPORT)
    parser.add_argument("--report", type=Path, default=VALIDATION_REPORT)
    args = parser.parse_args()

    header, rows, width_issues = parse_csv_with_widths(args.papers)
    bib_entries = parse_bibtex_entries(args.bib)
    ranked = parse_ranked_list(args.deep_report)
    report = make_report(header, rows, width_issues, bib_entries, ranked)
    args.report.write_text(report, encoding="utf-8")

    missing_bib = {row.get("bibtex_key", "").strip() for row in rows if row.get("bibtex_key", "").strip()} - {
        entry.key for entry in bib_entries
    }
    duplicate_keys = [key for key, count in Counter(row.get("bibtex_key", "") for row in rows).items() if key and count > 1]
    failed = bool(width_issues or header != REQUIRED_COLUMNS or missing_bib or duplicate_keys)
    print(f"Wrote {args.report}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
