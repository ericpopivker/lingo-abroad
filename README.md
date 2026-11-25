# Lingo Abroad

> **Like a language podcast or audio course, but it talks back.** 7-minute voice lessons inside Claude: the polite phrases you'll say, what locals say back, and the signs you'll see.

Lingo Abroad is a travel language course that runs as a **Claude skill**: no app to install, no account, no tracking. Any language to any language. Level 1 (survival for a first trip) has six topics: Basics, Understanding & Getting Help, Transport, Sightseeing, Restaurant and Shopping, 3 lessons and a test each.

**Languages:** learn any language, explained in your own. By voice, it works best when both are among Claude's voice languages: currently English, Spanish, French, German, Italian, Portuguese (Portugal and Brazil), Chinese (Mandarin and Cantonese), Japanese, Korean, Hindi, Indonesian, Russian, Turkish and Ukrainian. In text, any language works.

Feedback and bugs: [Issues](https://github.com/ericpopivker/lingo-abroad/issues)

## Install and use (Claude)

### One-time setup

1. **Turn on files:** in Claude, **Settings → Capabilities → Create and edit files** (skills need it).
2. **Install the plugin:** **Customize → Plugins → Add marketplace** → `ericpopivker/lingo-abroad` → install **lingo-abroad** → turn on **Sync automatically**. Updates then arrive by themselves.
3. **Create a project named "Lingo Abroad"** (suggested) to keep your lesson chats together, and add it to your phone's home screen. Leave its **instructions empty**: project instructions make voice slow ("Let me check…" before every answer). Prefer plain chats? Skip this step; everything else is the same.
4. **First lesson:** **new chat** (in the project, if you made one) → pick **Opus** → type **"Start Lingo Abroad"** → when it says **"Lingo Abroad is loaded…"**, tap **Use voice mode** and say **"ready"** → answer the setup questions by voice.

### Every lesson, practice or test: new chat + paste your card

Pasting your **progress card** works best, with or without a project: it carries everything between chats, and Claude can't reliably find it by itself yet. Project or plain chats is up to you; the project is the suggested way.

1. Open a **new chat** (in your project, if you made one). Always a new one: faster and far fewer tokens than a long chat.
2. Pick **Opus**.
3. **Paste your latest progress card** and send it. For a test, type **"Basics test"** (or the topic you want) on a line below the card before sending, because tests can't be loaded once you're in voice. (Every lesson ends with the card printed in the chat; tap its **copy** button.)
4. When it says **"Lingo Abroad is loaded…"**, tap **Use voice mode** and say **"ready"** (or **"practice"**).

   ![Use voice mode inside an open chat: bottom left, next to the microphone](docs/img/voice-mode-in-chat.png)

   In an open chat, **Use voice mode** is the waveform icon at the bottom left; the microphone next to it is dictation only.

5. Do the lesson (~7 minutes), hands-free. Say **"wait"** if you need a moment.
6. At the end, **copy the new card** for next time. It also says what's next.

### If something's wrong

| What you see | What to do |
| :--- | :--- |
| No **"Lingo Abroad is loaded"**, or a general answer about the language | The skill didn't load. Check you're on **Opus**, start a new chat and paste the card again (its first line, "▶ Use skill: Lingo Abroad…", starts the skill). |
| "Let me check…" / "I'm working on it" before every answer | The chat is in a project with instructions. Empty the project's instructions and start a new chat. |
| It misheard you, or answers something else | Say it again, slowly. |
| In voice: "I need to load that first" | End the call and start again from step 1. |
| Lost your latest card | Start a new chat, type **"Lingo Abroad"** and say where you are: **"I finished Transport lesson 1, 7 of 18 lessons."** |
| Not sure you have the latest version | Say **"version"**: it answers "Lingo Abroad, version x.y.z". |

### Good to know

- **Opus is required.** Sonnet sometimes fails to load the skill or doesn't pick it up for the conversation, and then teaches without it. Haiku isn't supported.
- **Usage:** one new chat per lesson keeps usage down. (On Claude Free we measured roughly 1 lesson + 1 practice per 5-hour window, before Opus was required.)
- **Quick questions** ("plan", "stats", "how do I say…") are fine in the same chat; every new lesson, practice or test gets a new chat.
- **Tests:** pass = 8/10 and polite answers in the roleplay.
- **Optional progress sheet:** say **"log row"** after a lesson and paste the row into your own Google Sheet/Excel built from [templates/](templates/) (`progress-log.csv`, setup and formulas in `progress-sheet.md`).

## How it works

| Term | Meaning |
| :--- | :------ |
| **Level** | A course for one stage of travel. Level 1 = survival for a first trip (6 topics × 3 lessons = 18 lessons). |
| **Topic** | A subject area: Basics, Understanding & Getting Help, Transport, Sightseeing, Restaurant, Shopping. |
| **Lesson** | One 7-minute daily sitting: recall → speak & listen → read → roleplay → progress card. |
| **Topic test / Level final test** | Pass/fail checks (8/10 and 12/15, polite register required) that earn **Passed ✓**. |
| **Progress card** | A short text block Claude writes into the chat at the end of every lesson; the learner pastes it into a new chat to start the next lesson, practice or test (or a `trips/<destination>.md` file where the AI can write files). |

Every lesson has three parts: **Speak** (what you say, always polite), **Listen** (what locals say back) and **Read** (signs and menus). Review uses three buckets (**Weak / Learning / Solid**) ordered by list position only, so the AI never has to do date math.

## Learning science behind it

Lingo Abroad borrows proven pieces from six methods—trimmed down to fit a 7-minute voice lesson:

- **Pimsleur (Graduated-Interval Recall & Anticipation):** Model a new phrase slowly first, repeat it, then recall the one before the last one (~30–60s gap) and again in the roleplay—zero grammar lectures, polite register by default.
- **Atomic Habits (James Clear):** Habit-stacking cue (*"after morning coffee"*), visible trip countdown, a 2-minute **"quick one"** recall session for busy days, and **never miss twice** (easy win after a skipped day, zero guilt).
- **Anki / Leitner Spaced Repetition:** Retrieval-first prompts (answer before seeing/hearing the phrase), interleaving across topics, and an LLM-safe **3-bucket** queue (`Weak` → `Learning` → `Solid`)—plus Anki-style **again / easy** overrides in Practice mode.
- **Comprehensible Input (Krashen, *i+1*):** Every lesson trains **Listen** separately with realistic local replies slightly above what you produce, paired with a low-anxiety English safety net mid-roleplay.
- **Keyword Mnemonics:** Short, accurate memory tricks (word parts, cognates, or sound-alike pictures) tailored to the learner's own native language—or saved when the learner invents their own.
- **Shadowing (Voice Mode):** Light echo-repeat after hearing the tutor model each phrase aloud to build rhythm and mouth muscle memory.

## For maintainers

Requires Python 3 (standard library only).

```bash
python build.py          # check versions, build dist/lingo-abroad-claude.zip
python build.py --bump   # bump the patch version in plugin.json + marketplace.json, then build
```

Release: `python build.py --bump`, commit, push. Claude installs that have the marketplace with **Sync automatically** pick it up.
