# Progress, Stats and Log Row

Read this when the learner asks for progress, stats, a plan or the log row. Never invent numbers: use the card (or the server).

**Progress = position** (from the card's Now, Stats and Tests lines; server: `get_progress`). Text:
```
Learn Italian · Level 1 · Next: Understanding & Help, Lesson 1
Lessons 5/18 · Topics ✓ Basics · ○ Understanding & Help · ○ Transport · ○ Sightseeing · ○ Restaurant · ○ Shopping
Rome in 9 days: 13 lessons left (about 1.5 a day)
```
Voice: "You're on Level 1, next is Understanding and Help. Five of eighteen lessons done, Basics passed. Nine days to Rome." If the trip is close, suggest the trip-priority path.

**Stats = performance** (from the card's Stats, Accuracy, Tests and bucket lines; server: `get_stats`). Text:
```
Streak 4 days (best 6) · last lesson yesterday
Accuracy: speak 18/22 · listen 12/15 · read 15/16 · roleplay 9/10
Memory: 3 weak · 6 learning · 5 solid · Tests: Basics 9/10
Strongest: reading. Try "practice listening".
```
Voice: streak, then the strongest and weakest part, then one suggestion. Then offer the **What next? menu**.

## Log row (for the learner's own spreadsheet)

**Only when the learner asks** ("log row"), print **one log row** for the last lesson, test or practice, in its own code block, values separated by **tab characters** (not spaces), in this exact column order, with no header:

```
Date	Language	Level	Topic	Lesson	Type	Speak right	Speak tried	Listen right	Listen tried	Read right	Read tried	Roleplay right	Roleplay tried	Test score	Passed	Weak items	Notes
```

- **Date** `YYYY-MM-DD` (today). **Type** is `lesson`, `quick`, `practice`, `freestyle` or `test`. For `practice`, Topic/Lesson may be blank or the main topic reviewed. **Lesson** is blank for tests. Counts are **this sitting only** (not totals). **Test score** like `9/10` and **Passed** `Y`/`N` for tests only; leave blank otherwise. Weak items separated by `; `.
- Mention once, in the first lesson's wrap-up (text only): "Keeping a spreadsheet? Say **log row** after a lesson."
- Example: `2026-11-23	Italian	1	Basics	1	lesson	3	3	2	3	4	4	3	3			buona giornata	`
