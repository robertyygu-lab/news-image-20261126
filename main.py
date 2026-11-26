"""make.fun entry: Sum up 26 November's world news in one image.

The image (entry.png, in this repository) is a front-page infographic
summing up Thursday 26 November 2026 world news. It was built by an AI
agent from real news reported that day (see NOTES.md for sources).

This program is the simplest form the bounty allows: it copies the image
the repository holds to /output/entry.png. It uses only the Python
standard library, makes no network calls, and is fully deterministic --
every run writes exactly the same bytes.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST = Path("/output/entry.png")


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    DEST.parent.mkdir(parents=True, exist_ok=True)
    # copyfile is a plain byte copy: output is byte-identical every run.
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
