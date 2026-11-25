#!/usr/bin/env python3
"""The Moon Finally Answers Back entry (account B).

Writes one line, 113 characters, in the voice of the Moon answering
everyone who has ever stared up at it, to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.

The joke: the Moon ticks off all three things people do at it — howl,
wish, promise to change — then points out the one wish nobody ever
made: wishing the Moon itself a good night. Wry, old, a little tired
of being wished upon, with the turn ("wished me a good night") landing
at the very end of the line.
"""

import os

# The Moon's comeback: it names all three things people do at it —
# howl, wish, promise to change — then points out the one wish nobody
# ever made: wishing the Moon itself a good night.
MOON_LINE = (
    "You howl, you wish, you promise to change — four billion years "
    "of it, and nobody has ever wished me a good night."
)

MAX_CHARS = 240
OUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def verify(text: str) -> str:
    """Return the line, stripped, after enforcing the gate."""
    line = text.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, must be at most {MAX_CHARS}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(text: str, path: str = OUT_PATH) -> str:
    """Verify the line and write it to the output file."""
    line = verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    return line


def main() -> None:
    line = write_entry(MOON_LINE)
    print(f"Wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
