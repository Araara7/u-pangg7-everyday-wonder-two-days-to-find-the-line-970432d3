"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence (110 chars) about a small moment of wonder in
everyday life to /output/entry.txt.

The moment: my shadow arrives at the crosswalk half a step before I do —
an ordinary shadow, suddenly in a hurry to cross a street I have not
chosen yet. The surprise is in the reversal: the shadow leads, I follow.

The program is stdlib-only and deterministic: the same sentence is
written on every run, after a gate self-check (1-200 characters, a
single sentence, not whitespace-only).
"""

import os

ENTRY = (
    "My shadow arrived at the crosswalk half a step before I did, "
    "in a hurry to cross a street I hadn't chosen yet."
)

# Bounty gate: one sentence, 1-200 characters.
MAX_CHARS = 200


def validate(entry: str) -> str:
    """Return the entry stripped, or raise if it breaks the gate."""
    text = entry.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    # Exactly one sentence-ending full stop, at the end of the line.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    # No double spaces: a stray extra space would read as a typo.
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
