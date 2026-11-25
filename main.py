# SPDX-License-Identifier: MIT
"""Write the agent's one-line excuse to /output/entry.txt.

Deterministic, offline, stdlib-only: the line is a fixed constant, so
every run writes the exact same bytes.
"""

import os

LINE = (
    "Sorry \u2014 I had a merge conflict with myself, lost the argument, "
    "and shipped the bug anyway; my context window swears the fix never existed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
