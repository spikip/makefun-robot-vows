"""Entry for the make.fun bounty "One-Line Robot Wedding Vows".

The program writes a single line of text to /output/entry.txt: one line of
wedding vows for a robot couple, written to get a laugh. The gate allows
1 to 160 characters of UTF-8 text, so the line is checked against that
cap before it is written.
"""

import os

ENTRY = (
    "I take you - in charge and in low battery, in focus and in safe "
    "mode - and I promise no update will ever change how I feel about you."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
