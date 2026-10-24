"""Check the Physical AI Collection against its rules and render the README tables.

    python tools/build.py           # check, then rewrite the README between the markers
    python tools/build.py --check   # check only; exit 1 if a rule fails or the README is stale

Rules (README, "Rules"):
- every entry has the required fields, a known layer and a known owner type;
- company-owned projects carry facts only: `reading` and `reason` are null;
- every other project carries a reading (becoming | returning) and a one-line reason;
- no ticker, exchange, price target or performance language anywhere in the file.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "collection.yaml"
README = ROOT / "README.md"
START, END = "<!-- collection:start -->", "<!-- collection:end -->"

LAYERS = [
    ("compute", "Accelerated compute"),
    ("memory", "High-bandwidth memory"),
    ("packaging", "Advanced packaging and foundry"),
    ("data-centres", "Data centres"),
    ("generation", "Power generation"),
    ("grid", "Transmission and grid"),
    ("cooling", "Cooling"),
    ("power-electronics", "Power electronics"),
    ("robotics", "Robotics and actuators"),
    ("sensing", "Sensors and machine vision"),
]
OWNER_TYPES = {"company", "academic", "public-research", "foundation", "community"}
KINDS = {"repository", "dataset", "paper"}
REQUIRED = ("name", "layer", "kind", "url", "owner", "owner_type", "licence", "does", "verified", "basis")
DENY = re.compile(
    r"\b(NASDAQ|NYSE|XETRA|ticker|price target|buy|sell|alpha|outperform|returns?|Sharpe)\b",
    re.IGNORECASE,
)


def load() -> dict:
    return yaml.safe_load(DATA.read_text(encoding="utf-8"))


def check(data: dict) -> list[str]:
    errors: list[str] = []
    layer_ids = {k for k, _ in LAYERS}
    names: set[str] = set()
    for i, e in enumerate(data.get("entries") or []):
        where = f"entry {i + 1} ({e.get('name', '?')})"
        for f in REQUIRED:
            if not e.get(f):
                errors.append(f"{where}: missing {f}")
        if e.get("name") in names:
            errors.append(f"{where}: duplicate name")
        names.add(e.get("name"))
        if e.get("layer") not in layer_ids:
            errors.append(f"{where}: unknown layer {e.get('layer')!r}")
        if e.get("kind") not in KINDS:
            errors.append(f"{where}: unknown kind {e.get('kind')!r}")
        if e.get("owner_type") not in OWNER_TYPES:
            errors.append(f"{where}: unknown owner_type {e.get('owner_type')!r}")
        if not str(e.get("url", "")).startswith("https://"):
            errors.append(f"{where}: url must be https")
        if not isinstance(e.get("verified"), date):
            errors.append(f"{where}: verified must be an ISO date")
        if e.get("owner_type") == "company":
            if e.get("reading") is not None or e.get("reason") is not None:
                errors.append(f"{where}: company-owned projects carry facts only (reading and reason null)")
        else:
            if e.get("reading") not in ("becoming", "returning"):
                errors.append(f"{where}: reading must be becoming or returning")
            if not e.get("reason") or len(str(e["reason"])) > 110:
                errors.append(f"{where}: reason required, at most 110 characters")
    for m in DENY.finditer(DATA.read_text(encoding="utf-8")):
        errors.append(f"collection.yaml: editorial deny-list hit {m.group(0)!r}")
    return errors


def render(data: dict) -> str:
    entries = data["entries"]
    n = len(entries)
    read = sum(1 for e in entries if e.get("reading"))
    b = sum(1 for e in entries if e.get("reading") == "becoming")
    last = max(e["verified"] for e in entries)
    out = [
        f"**{n} projects** across ten layers · {read} read ({b} Becoming, {read - b} Returning) · "
        f"{n - read} company-owned, facts only · last verified {last:%d %B %Y}",
        "",
    ]
    for layer_id, label in LAYERS:
        rows = [e for e in entries if e["layer"] == layer_id]
        if not rows:
            continue
        out += [f"### {label}", "", "| Project | What it does | Licence | Reading |", "| --- | --- | --- | --- |"]
        for e in rows:
            if e.get("reading"):
                reading = f"**{e['reading'].capitalize()}** — {e['reason']}"
            else:
                reading = "Facts only (company-owned)"
            kind = "" if e["kind"] == "repository" else f" ({e['kind']})"
            out.append(f"| [{e['name']}]({e['url']}){kind} | {e['does']} | `{e['licence']}` | {reading} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    data = load()
    errors = check(data)
    if errors:
        print("\n".join(errors))
        return 1
    text = README.read_text(encoding="utf-8")
    a, b = text.index(START) + len(START), text.index(END)
    new = text[:a] + "\n" + render(data) + text[b:]
    if "--check" in sys.argv:
        if new != text:
            print("README.md is stale: run python tools/build.py")
            return 1
        print(f"OK: {len(data['entries'])} entries")
        return 0
    README.write_text(new, encoding="utf-8")
    print(f"README.md rendered: {len(data['entries'])} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
