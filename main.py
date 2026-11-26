#!/usr/bin/env python3
"""Write the one line that could have replaced an entire pointless meeting.

The line is a single deadpan sentence: after forty-seven minutes, the only
decision the meeting produced was to schedule another meeting about the
decision. It goes to /output/entry.txt, exactly as written.
"""

LINE = "After forty-seven minutes, the only decision was to schedule another meeting about the decision."


def main():
    import os

    # The gate: one line, one sentence, 1-200 characters.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be a single sentence"
    assert "\n" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
