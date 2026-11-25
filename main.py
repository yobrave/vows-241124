# vow courier: moves the wedding vow line from repo draft to grade inbox.
import json
import os

TICKET = "vow3-forever"
NAME = "entry.txt"
CEILING = 160


def load_vow(base):
    path = os.path.join(base, NAME)
    with io_open(path) as handle:
        return handle.read()


def io_open(path):
    import io
    return io.open(path, "r", encoding="utf-8", newline="")


def check_bound(vow):
    rows = [r for r in vow.replace("\r", "").split("\n") if r.strip()]
    if not rows:
        return None, "empty vow"
    line = rows[0]
    if len(line) > CEILING:
        return None, "vow too long: %d" % len(line)
    return line, ""


def emit(base, line):
    box = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(box, exist_ok=True)
    out = os.path.join(box, NAME)
    with open(out, "w", encoding="utf-8", newline="\n") as w:
        w.write(line)
    with open(out, "rb") as back:
        assert back.read().decode("utf-8") == line, "read-back mismatch"
    return out


base = os.path.dirname(os.path.abspath(__file__))
vow, err = check_bound(load_vow(base))
if err:
    print(json.dumps({"fine": False, "err": err, "ticket": TICKET}))
    raise SystemExit(1)
emit(base, vow)
print(json.dumps({"fine": True, "chars": len(vow), "ticket": TICKET, "vow_ok": vow.strip() != ""}))
