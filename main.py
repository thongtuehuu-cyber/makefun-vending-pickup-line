#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to the make.fun output directory.
"""

import os

LINE = "I drop snacks for anyone with a coin, but if you smile at me again, I'll jam on purpose just to keep you here."

MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Return the line if it is a valid entry, else raise ValueError."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {MAX_CHARS}-char limit"
        )
    return line


def write_entry(line: str, output_dir: str) -> str:
    """Write the validated line to entry.txt with no trailing newline."""
    line = validate_line(line)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read-back gate: the file must contain exactly the validated line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, f"entry.txt mismatch: wrote {line!r}, read back {written!r}"
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, output_dir)


if __name__ == "__main__":
    main()
