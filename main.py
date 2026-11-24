#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes the two-line explanation to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Standard library only; fully deterministic: the same text every run.

Line 1 explains a toaster to a 10-year-old through one concrete analogy
(a tiny sunbed for bread). Line 2 says honestly what that analogy maps
(the browning, the waiting) and what it leaves out (the pop).
"""

import os
from pathlib import Path

ENTRY = (
    "A toaster is a tiny sunbed for bread: two glowing walls tan each slice "
    "golden-brown as it stands between them.\n"
    "The sunbed explains the browning and the waiting, but it leaves out the "
    "pop \u2014 no sunbed ever launches its customer into the air when the "
    "timer rings.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
