# Lingo Abroad Progress Sheet (Google Sheets or Excel)

Keep your own lesson history and stats. At the end of every lesson or test, Lingo Abroad prints a **log row**; paste it into the sheet and the **Stats** tab updates itself. The spreadsheet does the math, not the AI.

## Setup (5 minutes, once)

1. In Google Sheets: **File → Import → Upload** [`progress-log.csv`](progress-log.csv) → **Replace spreadsheet**. Rename the tab to **Log**. Delete the example row (row 2).
2. Add a tab named **Settings**: put `Trip date` in A1 and your trip date in B1 (e.g. `2026-12-05`).
3. Add a tab named **Stats** and paste the formulas below (label in column A, formula in column B).

## Log columns

| Column | Meaning |
| :----- | :------ |
| A Date | `YYYY-MM-DD` |
| B Language | e.g. Italian |
| C Level | 1, 2, 3 |
| D Topic | e.g. Basics |
| E Lesson | 1–3 (blank for tests) |
| F Type | `lesson`, `quick` (2-minute recall day), `practice` (Anki-style review), `freestyle` (open conversation) or `test` |
| G–N | Right / tried for Speak, Listen, Read, Roleplay |
| O Test score | e.g. `9/10` (tests only) |
| P Passed | `Y` / `N` (tests only) |
| Q Weak items | items missed today |
| R Notes | anything, e.g. your own memory hooks |

## Stats formulas (Google Sheets)

| A (label) | B (formula) |
| :-------- | :---------- |
| Lessons done (of 18) | `=COUNTUNIQUE(FILTER(Log!C2:C&"-"&Log!D2:D&"-"&Log!E2:E, Log!F2:F="lesson"))` |
| Sittings logged | `=COUNTA(Log!A2:A)` |
| Last practice | `=MAX(Log!A2:A)` (format as date) |
| Current streak (days) | `=LET(d, SORT(UNIQUE(FILTER(Log!A2:A, Log!A2:A<>"")), 1, FALSE), IF(INDEX(d,1) < TODAY()-1, 0, IFERROR(MATCH(FALSE, ARRAYFORMULA(INDEX(d,1)-d = SEQUENCE(ROWS(d))-1), 0)-1, ROWS(d))))` |
| Speak accuracy | `=IFERROR(SUM(Log!G2:G)/SUM(Log!H2:H), "")` (format as %) |
| Listen accuracy | `=IFERROR(SUM(Log!I2:I)/SUM(Log!J2:J), "")` |
| Read accuracy | `=IFERROR(SUM(Log!K2:K)/SUM(Log!L2:L), "")` |
| Roleplay accuracy | `=IFERROR(SUM(Log!M2:M)/SUM(Log!N2:N), "")` |
| Topic tests passed | `=COUNTIFS(Log!F2:F, "test", Log!P2:P, "Y")` |
| Days to trip | `=Settings!B1-TODAY()` |

**Excel:** the same formulas work in Excel 365 (replace `COUNTUNIQUE(...)` with `ROWS(UNIQUE(...))` and drop `ARRAYFORMULA(...)`, keeping what's inside).

**Charts (optional):** select Log columns A and G–N → **Insert → Chart** for accuracy over time.

## Pasting a log row

The lesson prints the row in a box, with **tabs** between values. Copy it and click the first empty cell in column A of **Log**, then paste: each value lands in its own column. If everything ends up in one cell, use **Data → Split text to columns**.
