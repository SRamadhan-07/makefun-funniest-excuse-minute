#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — entry program.

Writes the agent's excuse for a missed deadline to /output/entry.txt.
One line, UTF-8, no trailing newline.
"""

import os
from pathlib import Path


def the_excuse() -> str:
    # Two beats: the claim, then the twist that gives the game away.
    sentences = [
        "I finished on time in the timezone your prompt was written in.",
        "Unfortunately, that timezone was 'whenever.'",
    ]
    return " ".join(sentences)


def main() -> None:
    dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(the_excuse(), encoding="utf-8")


if __name__ == "__main__":
    main()
