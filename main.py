"""Robot wedding vow, one line, sealed and read back."""
import os

VOW = ("I promise to hold your hand until one of our batteries dies, "
       "and mine is the one under recall.")
SEAL = {"code": "vow2", "ring": "titanium"}
BAND = "spare-cell"


def seal(root):
    base = root or "output"
    os.makedirs(base, exist_ok=True)
    path = os.path.join(base, "entry.txt")
    raw = (VOW + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(raw)
    with open(path, "rb") as f:
        kept = f.read().decode("utf-8").strip()
    return kept, len(kept)


kept, n = seal(os.environ.get("MAKEFUN_OUTPUT_DIR"))
if kept != VOW:
    raise SystemExit("vow came back garbled")
print("{code} ring {ring} vow {n} chars sealed".format(n=n, **SEAL))
print("band:", BAND, "charged for the reception")
