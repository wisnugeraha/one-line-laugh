#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes exactly one funny line to /output/entry.txt.
The program is the entry: a single sentence, at most 200 characters,
that lands a surprise that still makes sense.
"""
import os


# The entry line: one sentence, ≤200 chars, a surprise that still makes sense.
LINE = "I told my computer it needed a break — now it's sleeping for 8 hours and I can't reach it."


def line() -> str:
    """Return the entry line."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = line()
    assert len(text) <= 200, f"line is {len(text)} chars (max 200)"
    assert len(text) >= 10, "line too short to be a sentence"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
