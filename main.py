"""Sleeve Notes for the Frog Trio — album title + back cover blurb.

Writes one text (title followed by a short blurb, max 400 characters)
to /output/entry.txt. Pure Python stdlib, no network, deterministic.
"""

import os

TITLE = "Pond Standard Time"

BLURB = (
    "Milo on tenor, Bea on upright bass, Tad on brushes — three frogs "
    "who swing harder than bands twice their size. Cut live on a rainy "
    "Tuesday at the Lily Pad Club, where the reeds hum and the front row "
    "leans in. No gimmicks. Just standards, played low, loose, and right "
    "on the beat."
)

ENTRY = TITLE + "\n\n" + BLURB


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
