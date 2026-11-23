"""One-Line Laugh entry: writes a single funny line to /output/entry.txt.

Stdlib only, deterministic, no network.
"""

import os

LINE = "My alarm clock finally learned my snooze pattern and now just texts, 'See you in nine minutes, liar.'"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
