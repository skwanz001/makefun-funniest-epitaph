#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one single-line tombstone epitaph to /output/entry.txt.

Strategy (why this line, in my own words): the judge weighs, in order,
(1) a one-line epitaph of famous last words, (2) a real laugh from a
genuine joke, (3) a surprise/twist, (4) reads carved in stone, (5) stays
in the head. So the line is first-person dying speech, deadpan, with the
joke turning on one word: the dying man says he told everyone he was
dying, and the reply he got was "same" -- the modern shrug of total
indifference -- and his last word is a flat "Fair enough." The laugh
comes from that collision: a lifetime of being ignored, summed up in the
moment of death, accepted without a fight. No setup to explain, no stage
direction, no pun: short, quotable, and it lands on one read.

Only the standard library is used: the grading sandbox installs nothing.
"""

import os

EPITAPH = "I told you I was dying. You said 'same'. Fair enough."

MAX_CHARS = 150


def main() -> None:
    text = EPITAPH.strip()
    assert text, "epitaph must not be empty"
    assert "\n" not in text, "epitaph must be a single line"
    assert len(text) <= MAX_CHARS, f"epitaph is {len(text)} chars, over {MAX_CHARS}"
    # Exact length, checked by hand and by the assert above: 53 chars.
    # No trailing newline: the gate counts every character, and the
    # judge is shown the text exactly as submitted, so the file holds
    # the line and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
