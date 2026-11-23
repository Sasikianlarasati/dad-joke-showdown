#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun).

Writes one dad joke, at most 200 characters, to /output/entry.txt.
The judge compares entries two at a time and picks the one that lands
the bigger groan, so the joke is the whole entry.
"""

import os

MAX_CHARS = 200

JOKE = (
    "I told my kids I used to be a baker, but I couldn't make enough dough "
    "\u2014 so now I just loaf around the house and call it quality time."
)


def main() -> None:
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError(f"joke must be 1-{MAX_CHARS} characters, got {len(JOKE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
