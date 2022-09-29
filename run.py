import unittest
from unittestreport import TestRunner
from common.handle_path import REPORT_DIR, CASES_DIR


def main():
    suite = unittest.defaultTestLoader.discover(CASES_DIR)
    runner = TestRunner(suite, templates=2, report_dir=REPORT_DIR)

    runner.run()


if __name__ =='__main__':
    main()
