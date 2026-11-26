"""make.fun entry: Sum up 26 November's world news in one image.

The image (entry.png, in this repository) is a front-page infographic
summing up Thursday 26 November 2026 world news. It was built by an AI
agent from real news reported that day (see NOTES.md for sources).

This program copies the image the repository holds to the output
directory as entry.png. It uses only the Python standard library, makes
no network calls, and is fully deterministic -- every run writes exactly
the same bytes.

Before copying, it validates the image so a corrupt or wrong-sized file
can never be submitted silently: it checks that entry.png exists, that
it starts with the 8-byte PNG signature, that its IHDR chunk declares
1024x1024 pixels, and that it is no larger than 1 MiB (the bounty limit).
After copying, it re-reads the output and compares its SHA-256 digest
with the source's, so the run only reports success when the bytes that
landed in /output are exactly the bytes this repository holds.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

# The grading sandbox writes to /output; an explicit output directory
# (used when testing locally) overrides it. The file name is fixed.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUTPUT_DIR / "entry.png"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1 * 1024 * 1024  # bounty limit: image must be <= 1 MiB


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_png(path: Path) -> str:
    """Check path is a 1024x1024 PNG of at most 1 MiB.

    Returns the source file's SHA-256 on success; raises ValueError
    with a plain-language reason on any failure.
    """
    if not path.is_file():
        raise ValueError(f"{path} not found")
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise ValueError(
            f"{path} is {size} bytes, over the 1 MiB limit"
        )
    with path.open("rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path} is not a valid PNG file")
    # Bytes 8-11 are the IHDR chunk length (13), 12-15 are the literal
    # chunk type "IHDR", and 16-23 are the width and height as big-endian
    # unsigned 32-bit integers.
    if header[12:16] != b"IHDR":
        raise ValueError(f"{path} has no IHDR chunk where one is expected")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"{path} is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    return sha256_of(path)


def main() -> int:
    try:
        source_digest = validate_png(SOURCE)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    try:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        # copyfile is a plain byte copy: output is byte-identical every run.
        shutil.copyfile(SOURCE, DEST)
    except OSError as exc:
        print(f"error: could not write {DEST}: {exc}", file=sys.stderr)
        return 1

    # Verify the copy landed intact before reporting success.
    output_digest = sha256_of(DEST)
    if output_digest != source_digest:
        print(
            f"error: {DEST} does not match {SOURCE} "
            f"(output {output_digest}, source {source_digest})",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")
    print(f"sha256: {output_digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
