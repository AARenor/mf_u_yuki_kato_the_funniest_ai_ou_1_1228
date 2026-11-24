"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
Python 3.13, standard library only, no network access.
"""

import os
import sys

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1-280 characters, got {len(text)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
