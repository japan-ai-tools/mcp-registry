"""Check servers/*/server.json before publishing (standard library only)."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREFIX = "io.github.japan-ai-tools/"


def check(root=ROOT):
    errors = []
    dirs = sorted(p for p in (root / "servers").iterdir() if p.is_dir())
    if not dirs:
        errors.append("no servers/*/ folders")
    for d in dirs:
        f = d / "server.json"
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            errors.append(f"{f}: {e}")
            continue
        if j.get("name") != PREFIX + d.name:
            errors.append(f"{f}: name must be {PREFIX}{d.name}")
        pkgs = j.get("packages") or []
        if not pkgs or pkgs[0].get("identifier") != d.name:
            errors.append(f"{f}: packages[0].identifier must be {d.name}")
        elif pkgs[0].get("version") != j.get("version"):
            errors.append(f"{f}: package version and server version differ")
    return errors


if __name__ == "__main__":
    errs = check()
    for e in errs:
        print("ERROR", e)
    print("OK" if not errs else f"{len(errs)} error(s)")
    sys.exit(1 if errs else 0)
