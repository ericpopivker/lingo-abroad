"""Build and release helper for the Lingo Abroad plugin.

Usage:
  python build.py              # check versions match, build dist/lingo-abroad-claude.zip
  python build.py --bump       # bump patch version (0.1.0 -> 0.1.1) in both manifests, then build

Auto-deploy: Claude syncs the plugin from GitHub (marketplace in .claude-plugin/).
Bump the version and push to main so Claude picks up the change.
Release: python build.py --bump, then commit BOTH plugin/.claude-plugin/plugin.json and
.claude-plugin/marketplace.json (e.g. `git add -A plugin .claude-plugin`) and push.
"""
import json
import pathlib
import re
import sys
import zipfile

root = pathlib.Path(__file__).resolve().parent
market_file = root / ".claude-plugin" / "marketplace.json"
plugin_file = root / "plugin" / ".claude-plugin" / "plugin.json"
skill = root / "plugin" / "skills" / "lingo-abroad"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def save(p, data):
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")


market, plugin = load(market_file), load(plugin_file)
entry = next(p for p in market["plugins"] if p["name"] == "lingo-abroad")

if "--bump" in sys.argv:
    major, minor, patch = (int(x) for x in plugin["version"].split("."))
    new = f"{major}.{minor}.{patch + 1}"
    plugin["version"] = entry["version"] = new
    save(plugin_file, plugin)
    save(market_file, market)
    print(f"version -> {new}")

if plugin["version"] != entry["version"]:
    sys.exit(f"Version mismatch: plugin.json {plugin['version']} vs marketplace.json {entry['version']}")
if not (skill / "SKILL.md").exists():
    sys.exit("Missing plugin/skills/lingo-abroad/SKILL.md")

# Keep the version line in SKILL.md in sync (the "version" command reads it).
skill_md = skill / "SKILL.md"
text = skill_md.read_text(encoding="utf-8")
new_text, n = re.subn(r"\*\*Skill version: [0-9.]+\*\*", f"**Skill version: {plugin['version']}**", text)
if n != 1:
    sys.exit("SKILL.md needs exactly one '**Skill version: x.y.z**' line")
if new_text != text:
    skill_md.write_text(new_text, encoding="utf-8", newline="\n")

dist = root / "dist"
dist.mkdir(exist_ok=True)
out = dist / "lingo-abroad-claude.zip"
files = sorted(f for f in skill.rglob("*") if f.is_file())
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(f, f"{skill.name}/{f.relative_to(skill).as_posix()}")

print(f"version {plugin['version']}  ->  {out.relative_to(root)} ({len(files)} files)")
