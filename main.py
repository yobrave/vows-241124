"""Robot vow binder: binds the vow to the gate, binds the copy to the output."""
STAMP = "onebug-11251142-vow3"
import json
import os
from pathlib import Path

ALTAR = Path(__file__).resolve().parent
VOWCAP = 160
VOW = ("I promise to hold your hand through every update, "
       "back you up before every argument, "
       "and never fall asleep at four percent again.")


def bind():
    parchment = ALTAR / "entry.txt"
    vow_line = parchment.read_text(encoding="utf-8").strip()
    sealed = vow_line.isprintable() and 1 <= len(vow_line) <= VOWCAP
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and sealed:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(parchment.read_bytes())
    print(json.dumps({"sealed": sealed, "stamp": STAMP, "vow_chars": len(vow_line), "vowcap": VOWCAP}))


if __name__ == "__main__":
    bind()
