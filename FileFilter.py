# coding=utf-8
import codecs
import datetime
import sys


def filter_file(src_file, dst_file, line_filter):
    print 'filter_file(%s, %s)' % (src_file, dst_file)

    in_file = codecs.open(src_file, 'r', 'utf-8')

    out_file = codecs.open(dst_file, 'w', 'utf-8-sig')
    lines = in_file.readlines()
    for line in lines:
        # print line
        if line_filter(line):
            out_file.write(line)

    out_file.close()

    in_file.close()
    pass


def line_filter_callback(line):
    pos = line.find(u"#")
    if pos  >= 0:
        return True
    return False


def main(argv):
    if len(argv) < 2:
        print "usage: $src_file, %dst_file"
    src_file = argv[0]
    dst_file = argv[1]

    filter_file(src_file, dst_file)
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
