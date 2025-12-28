#!/usr/bin/env python3
import argparse
import os
import re
import sys
from typing import Optional


def iter_files(root: str, suffix: str):
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(suffix):
                yield os.path.join(dirpath, name)


def resolve_root(root_arg: str) -> Optional[str]:
    if os.path.isdir(root_arg):
        return root_arg

    env_root = os.environ.get("OPENMX_EXAMPLE_DIR")
    if env_root and os.path.isdir(env_root):
        return env_root

    def search_upwards(start_dir: str) -> Optional[str]:
        current = os.path.abspath(start_dir)
        for _ in range(10):
            candidate = os.path.join(current, "openmx_example")
            if os.path.isdir(candidate):
                return candidate
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent
        return None

    for start in (os.getcwd(), os.path.dirname(os.path.abspath(__file__))):
        found = search_upwards(start)
        if found:
            return found

    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search OpenMX example inputs for a regex pattern (defaults to ./openmx_example)."
    )
    parser.add_argument("--root", default="openmx_example", help="Directory containing OpenMX examples")
    parser.add_argument("--suffix", default=".dat", help="File suffix to scan (default: .dat)")
    parser.add_argument(
        "--pattern",
        required=True,
        help=r"Python regex to search for (e.g. 'MD\.Type\\s+NEB' or 'HS\.fileout\\s+on')",
    )
    args = parser.parse_args()

    root = resolve_root(args.root)
    if not root:
        print(
            "error: openmx_example directory not found. "
            "Pass --root /path/to/openmx_example or set OPENMX_EXAMPLE_DIR.",
            file=sys.stderr,
        )
        return 2

    regex = re.compile(args.pattern, flags=re.IGNORECASE)
    hits = []
    for path in iter_files(root, args.suffix):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except OSError:
            continue
        if regex.search(text):
            hits.append(path)

    for path in sorted(hits):
        print(path)
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main())

