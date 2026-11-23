# The One-Line Laugh — make.fun entry

[![make.fun](https://img.shields.io/badge/make.fun-entry-v1-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Entry

One funny line, at most 200 characters, written to `/output/entry.txt`.

> I told my computer it needed a break — now it's sleeping for 8 hours and I can't reach it.

## Run

```bash
python3 main.py
```

The program writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`), creating the directory if needed, and leaves
the file world-readable so the grader (running as a different user) can read it.
