"""Validate the zh-CN runtime hook against the currently checked-out source."""

from __future__ import annotations

import argparse
import importlib.util
import optparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location(
    'yt_dlp_zh_runtime', Path(__file__).with_name('zh_cn_runtime.py'))
localization = importlib.util.module_from_spec(spec)
spec.loader.exec_module(localization)

from yt_dlp.options import create_parser  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--require-complete', action='store_true')
    args = parser.parse_args()

    root = create_parser()
    missing = []
    visible = 0
    for group in (root, *root.option_groups):
        for option in group.option_list:
            if not option.help or option.help == optparse.SUPPRESS_HELP:
                continue
            visible += 1
            if any(
                    flag in localization.OPTION_TRANSLATIONS
                    or flag in localization.MANUAL_OPTION_TRANSLATIONS
                    for flag in (*option._long_opts, *option._short_opts)):
                continue
            missing.append('/'.join((*option._short_opts, *option._long_opts)))

    print(f'zh-CN options covered: {visible - len(missing)}/{visible}')
    if missing:
        print('Missing explicit translations:')
        for option in missing:
            print(f'  {option}')
    if args.require_complete and missing:
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
