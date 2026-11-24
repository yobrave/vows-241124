"""Emits the robot wedding vow for One-Line Robot Wedding Vows (160 chars max)."""
import json
import os


class Vow:
    line = ("I promise to hold your hand until one of our batteries dies, "
            "and mine is the one under recall.")

    @classmethod
    def write(cls, folder):
        os.makedirs(folder, exist_ok=True)
        out = os.path.join(folder, "entry.txt")
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(cls.line + "\n")
        return out


def receipt(path):
    return {"path": path, "chars": len(Vow.line)}


print(json.dumps(receipt(Vow.write(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")), ensure_ascii=False))
