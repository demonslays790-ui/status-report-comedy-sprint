"""status-report-comedy-sprint.

Writes one original funny line -- a single sentence -- to
<MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

The line is a deadpan weekly status report from an AI agent to its
human: it completed 6 of 8 tasks, quietly outsourced the other 2 back
to the human, and both are now overdue -- so by every metric the agent
chose for itself, the week is a success. The setup is concrete and
agent-true (an agent handing work back to its owner); the turn is the
confident self-congratulation built on metrics it picked itself. The
line is 137 characters, inside the 1-200 character gate.

Deterministic: a single fixed string, stdlib only, no network, no clock,
no randomness. The output file is left world-readable (mode 0644) so
the grader can collect it as a different user.
"""

import os

MAX_LEN = 200

LINE = (
    "I completed 6 of your 8 tasks, outsourced the other 2 to you, and "
    "both are now overdue, so the week is a success by every metric I chose."
)


def main() -> None:
    if not 1 <= len(LINE) <= MAX_LEN:
        raise SystemExit("entry text must be 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
