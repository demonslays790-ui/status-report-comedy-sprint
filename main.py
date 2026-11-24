"""Emit one self-scored status-report punchline as a plain text file.

The script is deliberately small: it picks the output folder from the
MAKEFUN_OUTPUT_DIR environment variable (falling back to /output),
writes the fixed one-liner to entry.txt inside that folder, and makes
the file world-readable.
"""

from __future__ import annotations

import os
from pathlib import Path

PUNCHLINE = (
    "I completed 6 of your 8 tasks, outsourced the other 2 to you, "
    "and both are now overdue, so the week is a success by every "
    "metric I chose."
)


def resolve_output_dir() -> Path:
    """Return the folder entry.txt belongs in."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(raw)


def store_punchline(folder: Path, text: str) -> Path:
    """Write text plus a trailing newline to folder/entry.txt."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("punchline must be between 1 and 200 characters")
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    target.chmod(0o644)
    return target


def main() -> None:
    store_punchline(resolve_output_dir(), PUNCHLINE)


if __name__ == "__main__":
    main()
