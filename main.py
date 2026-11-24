"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence (110 chars) about a small moment of wonder in
everyday life to /output/entry.txt.
"""

ENTRY = (
    "My shadow arrived at the crosswalk half a step before I did, "
    "in a hurry to cross a street I hadn't chosen yet."
)


def main() -> None:
    import os

    # Gate self-check: 1-200 chars, a single sentence, not whitespace-only.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() and ENTRY.count(".") == 1, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
