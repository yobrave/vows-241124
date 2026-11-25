"""vow6: vow binder. Validators fold over the line; a binder keeps the truth."""
import functools
import json
import os
import sys
from pathlib import Path

SLEEVE = 160


def plain(raw: str) -> str:
    return raw.strip()


def human(line: str) -> bool:
    return len(line) > 0 and not line.isspace()


def under_sleeve(line: str) -> bool:
    return len(line) <= SLEEVE


def bind(keep: dict, check) -> dict:
    keep[check.__name__] = check(keep["line"])
    return keep


def main():
    root = Path(__file__).resolve().parent
    bag = {"line": plain(root.joinpath("entry.txt").read_text(encoding="utf-8"))}
    keep = functools.reduce(bind, [human, under_sleeve], bag)
    good = keep["human"] and keep["under_sleeve"]
    if good:
        vault = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "vow6_vault")
        vault.mkdir(parents=True, exist_ok=True)
        (vault / "entry.txt").write_bytes(keep["line"].encode("utf-8"))
    print("VERDICT", json.dumps({"good": good, "chars": len(keep["line"]), "sleeve": SLEEVE, "checks": {k: v for k, v in keep.items() if k != "line"}}))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
