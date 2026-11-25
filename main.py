"""Monday Morning Punchlines — one joke about Monday mornings.

The program writes a single line to /output/entry.txt: an attempt
to cancel a Monday-morning subscription that auto-renews every
week, whose cancel button is just a picture of Tuesday.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The joke's twist lands in the last words: the cancel button is
# just a picture of Tuesday. A subscription you cannot cancel is
# a fresh angle on Monday — no alarm, no coffee, no complaint list.
# Monday morning is named outright, so the joke is squarely on topic.
LINE = "I tried to cancel my Monday-morning subscription, but it auto-renews every week and the cancel button is just a picture of Tuesday."


def build_line():
    """Return the entry line, checked: one line, under 200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
