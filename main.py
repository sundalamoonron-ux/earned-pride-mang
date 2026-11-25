#!/usr/bin/env python3
"""One Line of Earned Pride — u-mang-one-line-of-earned-pride-a0138557.

Writes a single line (1-240 characters) to /output/entry.txt: a quiet, earned
moment of pride for a twelve-year-old boy who spent six months carrying bricks
after school and finally sets the last one in the wall.
"""

import os

LINE = (
    'After six months of carrying bricks after school, twelve-year-old Milo '
    'set the last one in the wall, stood back with his hands on his hips, '
    'and said, "That\'s my house."'
)


def main() -> None:
    # The line is 168 characters: inside the 1-240 gate, single line, no
    # trailing newline — the file holds exactly the line and nothing else.
    assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
