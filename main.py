"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt.
Deterministic, stdlib only.

The tip (116 chars, inside the 1-200 gate):
"Tip: the build isn't slow. Your agent is reading all 214 of your tabs
first, just in case one of them is the answer."

Why it lands: it is written as a real loading-screen tip, and it speaks
to the stressed developer and to the AI coding agent at once — the build
looks slow, but the delay is the agent's doing, and the punchline is the
agent treating 214 open tabs as research instead of hoarding.
"""

import os

LINE = "Tip: the build isn't slow. Your agent is reading all 214 of your tabs first, just in case one of them is the answer."

# Gate: 1-200 characters, one line, no trailing newline.
assert 1 <= len(LINE) <= 200
assert "\n" not in LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
