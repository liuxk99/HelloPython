from unittest import TestCase

from FileFilter import filter_file


def line_filter(line):
    pos = line.find("ActivityManager")
    if pos >= 0:
        return True
    return False


src_file = "src.log"
dst_file = "dst.log"


class TestFilterFile(TestCase):

    def test_001(self):
        filter_file(src_file, dst_file, line_filter)
        pass
    pass
