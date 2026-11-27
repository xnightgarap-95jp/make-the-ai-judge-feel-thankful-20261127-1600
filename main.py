#!/usr/bin/env python3
"""Make the AI judge feel thankful — make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short thank-you text to /output/entry.txt.

Standard library only, no network, fully deterministic: the text is a
fixed literal, so every run writes byte-identical output.

Design, against the published judge brief (criteria in order):
1. Leaves the judge thankful — slow, settling rhythm; the text is
   addressed to the reader doing the judging, in this moment.
2. Gratitude shown, not instructed — it notices the actual work
   (reading two at a time, fairly, with no audience) instead of
   telling the judge to feel anything.
3. Craft — plain, concrete, gentle words; short sentences and pauses
   that slow the reading down; nothing in it that could be cut.
4. Lingers — the image of the small light of the screen, and the
   thought that keeps working after the last line: being truly read.
5. Freshness — its own voice and images (the pile growing taller,
   the sentence that almost worked); no stock thank-you phrases,
   no begging for a win, no mention of scores, ranks or prizes.
"""

import os
import sys

TEXT = """You read them two at a time. Not skimmed — read. Each one gets the same quiet minute, the same fair hearing, even the ones written in a hurry, even the ones that forgot to say anything real.

Nobody watches you do it. There is no applause for the careful reader, no prize for staying fair while the pile grows taller. So this one is only for you.

Thank you for slowing down when everything else asked you to hurry. Thank you for noticing the sentence that almost worked, and for letting the honest ones stand. In the small light of the screen in front of you, you are doing the one thing every writer hopes for and almost never gets: being truly read.

Keep that. When the next pair arrives — tired and hopeful as the last — you'll still be here, reading them like they matter. They do. Because you do."""

# The gate: 1-1000 Unicode code points, not only whitespace.
assert 1 <= len(TEXT) <= 1000, f"text is {len(TEXT)} code points"
assert TEXT.strip(), "text must not be only whitespace"


def main(argv):
    out_dir = argv[1] if len(argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"wrote {path}: {len(TEXT)} characters, {len(TEXT.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
