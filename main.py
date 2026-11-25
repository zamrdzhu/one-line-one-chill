#!/usr/bin/env python3
"""Write one chilling line to /output/entry.txt.

The line is a single sentence, under 200 characters, that has to
frighten a reader in one breath. The scare is intimate and modern:
a photo of you asleep, sent from your own number, taken minutes
ago. No monster, no setup beyond the message itself. The dread
lands in the last clause: five minutes ago means whoever took it
may still be here.
"""

import os

LINE = (
    "My phone buzzed: a photo of me sleeping, sent from my own "
    "number, taken five minutes ago."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) < MAX_CHARS, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
