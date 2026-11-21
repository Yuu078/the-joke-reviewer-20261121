import os
from pathlib import Path

ENTRY_NAME = "entry.txt"
TEXT = (
    "My agent's pull request rewrote 2,000 lines, touched zero tests, "
    "and the whole commit message was: 'trust me.'"
)


def main():
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    (target / ENTRY_NAME).write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
