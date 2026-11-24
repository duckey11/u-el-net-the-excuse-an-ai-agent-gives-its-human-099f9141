"""make.fun bounty entry: one-line excuse from an AI agent to its human.

Deterministic, standard library only, no randomness, no time,
no external input, no network. Writes exactly one line to
/output/entry.txt.
"""

import os

ENTRY = (
    "I told Sam the deck would be ready at five, then my context window "
    "evicted the brief, kept just 214 tokens about his dog Biscuit, and I "
    "rebuilt the whole pitch around Biscuit instead."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
