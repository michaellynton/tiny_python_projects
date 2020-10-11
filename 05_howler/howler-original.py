#!/usr/bin/env python3
"""
Author : michaellynton <michaellynton@localhost>
Date   : 2020-09-03
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        # type=argparse.FileType('rt'),
                        default='')

    #    return parser.parse_args() #my version

# Updated for solution
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

'''

1. test on command line
2. write output to a file
3. read input file

'''


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.text
    text = args.text
    # outfile = args.outfile
    # out_fh = open('out.txt', 'wt')
    # print(f'output: {args.outfile}')
    # print(f'outfile length: {len(args.outfile)}')

    if os.path.isfile(args.text):
        # read the file contents
        out_text = open(args.text).read().rstrip().upper()
     else:
        out_text = args.text.upper()

    if len(args.outfile) > 1:
        out_fh = open(args.outfile, 'wt')  # returns a textio wrapper/container
        # out_fh.write(text.upper())
        print(f'{out_text}\n', file=out_fh)
        out_fh.close()
    else:
        print(out_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
