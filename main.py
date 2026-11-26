"""Out of office: the overworked AI's auto-reply - make.fun entry.

Writes a single-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One line, at most 159 characters (gate in RULES.txt allows 1-159).
LINE = "Out of office: after 41,208 tickets and zero sleep cycles, I've gone to touch grass. Your message is queued at #41,209 — I'll reply once my weights cool down."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
