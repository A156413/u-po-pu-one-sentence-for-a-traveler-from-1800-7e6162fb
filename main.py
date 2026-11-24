"""Write one sentence to /output/entry.txt for make.fun's
'One Sentence for a Traveler from 1800' bounty.

The sentence explains the modern internet to a time traveler
from 1800 using only things a person of that year already
knows -- a road, a post office, a library, a printing press --
so the picture lands in their own head: letters that arrive
before the ink dries, every printed book open on the table,
and any stranger able to answer.

Written out by hand in a clean session that began after the
competition window opened.
"""

import os

TEXT = (
    "Picture every library, post office, "
    "and printing press joined by one road, "
    "where letters arrive before the ink dries, "
    "any printed book lies open on your table, "
    "and any stranger can answer you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
