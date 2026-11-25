"""Monday Morning Punchlines - final entry.

A single original one-line joke about Monday mornings, written
to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
Standard library only; no network; deterministic output.
"""

import os

ENTRY = "Monday morning, my coffee took one look at my inbox and asked HR for a transfer to Friday."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
