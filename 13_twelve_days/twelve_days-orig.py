#!/usr/bin/env python3
"""
Author : michaellynton <michaellynton@localhost>
Date   : 2020-10-09
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days',
                        metavar='int',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if not 1 <= args.num <= 12:  # if mutations value is not between 0 and 1
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def verse(day):
    """Pass a number to get the verse for that day"""
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
               'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    gifts = ['And a partridge in a pear tree.',
             'Two turtle doves,',
             'Three French hens,',
             'Four calling birds,',
             'Five gold rings,',
             'Six geese a laying,',
             'Seven swans a swimming,',
             'Eight maids a milking,',
             'Nine ladies dancing,',
             'Ten lords a leaping,',
             'Eleven pipers piping,',
             'Twelve drummers drumming,'
             ]

    # For day 1, change the language of the first gift
    gifts[0] = 'A partridge in a pear tree.' if day == 1 else gifts[0]
    part1 = [f'On the {ordinal[day-1]} day of Christmas,',
             'My true love gave to me,']
    part2 = list(reversed(range(1, day + 1)))  # original
    
    return '\n'.join(part1+[gifts[c-1] for c in part2])



def test_verse():
    """Test the verse() function"""
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    verses = map(verse, range(1, args.num+1))
    args.outfile.write('\n\n'.join(verses) + '\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()

