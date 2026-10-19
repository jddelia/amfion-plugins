#!/usr/bin/env python3
"""Package only the OpenAI distribution; never infer review readiness."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


FILES = (
    "LICENSE",
    "README.md",
    "assets/icon.png",
    "assets/logo.png",
    "mcp.json",
    "plugin.json",
    "skills/front-desk-setup/SKILL.md",
    "skills/website-install/SKILL.md",
)
SUPERSEDED_DEMO = (
    "https://github.com/jddelia/amfion-plugins/releases/download/"
    "review-2026-10-15/amfion-chatgpt-demo-1.0.2.mp4"
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--review", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    plugin = root / "plugins" / "amfion"
    manifest = json.loads((plugin / "plugin.json").read_text())
    review = manifest["extensions"]["com.openai"]["review"]
    recording = review.get("demo_recording_url", "")
    if args.review:
        parsed = urlparse(recording)
        if parsed.scheme != "https" or not parsed.netloc:
            parser.error("A fresh, verified HTTPS demo_recording_url is required for review packaging.")
        if recording == SUPERSEDED_DEMO:
            parser.error("The 1.0.2 general-profile recording is not evidence for the OpenAI profile.")

    # Resolve every entry before writing so symlinks cannot smuggle other
    # workspace files into a distributable archive.
    payloads = {}
    for name in FILES:
        path = plugin / name
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(plugin.resolve()):
            parser.error(f"Missing or unsafe distributable file: {name}")
        payloads[name] = path.read_bytes()

    output = args.output.expanduser().resolve()
    if output.is_relative_to(root):
        parser.error("Write review artifacts outside the source distribution.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in payloads.items():
            entry = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data, compresslevel=9)
    output.chmod(0o600)
    print(json.dumps({
        "mode": "review" if args.review else "draft",
        "name": manifest["name"],
        "version": manifest["version"],
        "files": len(payloads),
        "bytes": output.stat().st_size,
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "output": str(output),
    }))


if __name__ == "__main__":
    main()
