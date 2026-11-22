#!/usr/bin/env python3
"""Write the single-ingredient food picture to /output/entry.png.

Copies the bundled image (entry.png if present, else entry.jpg) from the
directory containing this script to $MAKEFUN_OUTPUT_DIR/entry.png
(fallback /output/entry.png). Deterministic: a plain byte copy, so two
runs produce identical bytes. Standard library only, no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def find_source():
    for name in ("entry.png", "entry.jpg", "entry.jpeg"):
        path = os.path.join(HERE, name)
        if os.path.isfile(path):
            return path
    raise FileNotFoundError("no entry image (entry.png/entry.jpg) next to main.py")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.png"
    if os.path.isdir(out_dir) or not out_dir.lower().endswith((".png", ".jpg", ".jpeg")):
        out_path = os.path.join(out_dir, "entry.png")
    else:
        out_path = out_dir
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    shutil.copyfile(find_source(), out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 - surface any failure plainly
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
