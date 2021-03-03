# -*- coding: utf-8 -*-

import sys
import os
import pytest
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--suites", dest="suites", action="store", type=str,
                    help="用于指定执行哪些目录下的用例（可包含子目录），多个目录用`,`分割, eg: --suites app,infrastructure")

args, other_args = parser.parse_known_args()

sys.argv = [sys.argv[0]]
sys.argv.extend(other_args)


if args.suites:
    for d in args.suites.split(","):
        sys.argv.append(os.path.join("cases", *d.strip().strip("/").split("/")))
exit(pytest.main())
