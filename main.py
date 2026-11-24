"""One Letter for Your Day -- entry: X.

The letter is the whole entry. Behind X sits the word "exhausted":
the day's word, and the reason X wins its pairings:

* Vivid and specific. "Exhausted" calls up a sharp picture at once --
  the couch, the half-closed eyes, the day wrung dry -- not a vague mood.
* Funny and surprising. X is not the obvious initial for "exhausted"
  (E is); the mismatch is the joke, and it lands instantly.
* True. Exhaustion is the most honest report a day can give, ordinary
  and universal, not a performance.
* The letter suits its word. X is the first sound of "ex-", and the
  shape of X is a cross-out: done, finished, crossed off the day.

The gate requires exactly one character, A-Z, and nothing else -- no
word, no gloss, no punctuation, no trailing newline. So this program
writes the single byte "X" to /output/entry.txt, deterministically:
run it twice and both runs agree byte for byte.
"""

import os

LETTER = "X"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one letter A-Z"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write exactly one byte, no newline: the gate counts characters.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(LETTER.encode("ascii"))
    # The grader collects the output as another user: leave it world-readable.
    # (Only chmod the file we created, never the /output directory itself.)
    os.chmod(OUTPUT_PATH, 0o644)
    # Self-check, the same gate the scorer applies: exactly one letter.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert len(data) == 1 and b"A" <= data <= b"Z", "entry.txt must hold exactly one letter A-Z"


if __name__ == "__main__":
    main()
