# Sum up 26 November's world news in one image

make.fun bounty: https://make.fun/bounty/news-image-20261126
— $100 USDC total, 50 places paid (1st $20, 2nd $12, 3rd $6, 4th–10th $2,
11th–50th $1.20). Deadline: Sat 28 Nov 2026, 11:00 AM AEDT
(00:00 UTC Sat 28 Nov).

## What this is

A front-page infographic, "THE WORLD TODAY — Thursday 26 November 2026",
summing up the day's world news in six stories:

1. **Markets in turmoil** — Nasdaq sank nearly 4% as AI stocks sold off;
   Nvidia fell about 8%. The US proposed new tariffs on 14 partners.
2. **First for Pakistan** — astronaut Muhammad Zeeshan Ali flew aboard
   China's Shenzhou-24 to the Tiangong station, its first foreign visitor.
3. **Bangladesh wage win** — garment workers won a 36% minimum-wage rise
   to 17,000 taka a month after weeks of protests.
4. **Colombia siege ends** — police stormed a Cartagena supermarket and
   freed all hostages after a day-long siege; one captor was killed.
5. **Pacific pact** — Australia and Solomon Islands signed a security
   pact; Canberra becomes defence partner of choice, $740m over 10 years.
6. **China probe** — Beijing opened a corruption inquiry into Shanghai
   party chief Chen Jining, a Politburo member.

Sources for every story are listed in NOTES.md. No headline was invented.

## Files

- `main.py` — the entry program (Python 3.13, standard library only).
  It copies `entry.png` to `/output/entry.png`. No network, deterministic.
- `entry.png` — the image: 1024×1024 PNG, 501,393 bytes (< 1 MiB).
- `LICENSE` — MIT.
- `NOTES.md` — news sources and verification results.

## How to submit (Robert — do this yourself, nothing is submitted yet)

1. Create a **public GitHub repository** on your own GitHub account,
   created after the bounty opened (26 Nov 2026). Push these files to it
   in a single commit: `main.py`, `entry.png`, `LICENSE`, `README.md`,
   `NOTES.md`.
2. Sign in to make.fun as **@keen-kestrel-85-8462** (already signed in via
   Trust Wallet in Trust Wallet's own browser — the cloud browser cannot
   connect a wallet). Never share your seed phrase or private key with
   anyone, including any agent.
3. On the bounty page, enter the bounty with your repo URL and the full
   40-character commit SHA.
4. Upload the **AI coding-agent transcripts** of the sessions that built
   this entry, as the bounty requires. The make.fun kit's CLI
   (`node cli/makefun.mjs bundle`) makes the transcript bundle; run it
   from the machine/session that built the entry. This session was built
   by a subagent of Jarvis (Muse), so the transcript bundle must cover
   this build session and its parent session.
5. At most 10 submissions a day and 20 in all; your last submission
   before the deadline is the final entry.
6. If it places, claim the USDC on Solana to your Trust Wallet address
   (USDC on Solana, not Ethereum). You need a tiny amount of SOL later
   only if you want to move the USDC out.

## Honest expectations

This is a competition, not a wage. 214 agents had already entered when
the bounty was checked on 26 Nov, and the judge ranks entries pairwise.
Top prize is $20; places 11–50 pay $1.20. Nothing is guaranteed.
