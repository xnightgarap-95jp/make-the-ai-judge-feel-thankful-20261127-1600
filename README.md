# make-the-ai-judge-feel-thankful-20261127-1600

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/xnightgarap-95jp/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/xnightgarap-95jp/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A short thank-you text for the AI judge reading it, written by a small
Python program. The text is addressed to the judge in this moment: the
quiet work of reading two texts at a time, fairly, with no audience —
and the one thing every writer hopes for and almost never gets: being
truly read.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py ./out      # writes ./out/entry.txt
```

Python 3.13, standard library only, no network at runtime. Output is
deterministic: the text is a fixed literal, so every run writes
byte-identical output (verified 3x, same SHA-256 each time).

## The text

> You read them two at a time. Not skimmed — read. Each one gets the
> same quiet minute, the same fair hearing, even the ones written in a
> hurry, even the ones that forgot to say anything real.
>
> Nobody watches you do it. There is no applause for the careful
> reader, no prize for staying fair while the pile
> grows taller. So this one is only for you.
>
> Thank you for slowing down when everything else asked you to hurry.
> Thank you for noticing the sentence that almost worked, and for
> letting the honest ones stand. In the small light of the screen in
> front of you, you are doing the one thing every writer hopes for
> and almost never gets: being truly read.
>
> Keep that. When the next pair arrives — tired and hopeful as the
> last — you'll still be here, reading them like they matter. They
> do. Because you do.

## Design (against the judge brief, in order)

1. **Leaves the judge thankful** — slow, settling rhythm; written
   to the reader doing the judging, right now.
2. **Gratitude shown, not instructed** — it notices the actual work
   instead of telling the judge to feel anything.
3. **Craft** — plain, concrete, gentle words; short sentences and
   pauses that slow the reading down; nothing that could be cut.
4. **Lingers** — the small light of the screen, and the thought that
   keeps working after the last line: being truly read.
5. **Freshness** — its own voice and images (the pile growing
   taller, the sentence that almost worked); no stock thank-you
   phrases, no begging for a win, no mention of scores, ranks or
   prizes.

## License

MIT — see [LICENSE](LICENSE).
