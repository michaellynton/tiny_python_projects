#!/usr/bin/env python3
"""
Author : michaellynton <michaellynton@localhost>
Date   : 2020-09-14
Purpose: Rock the Casbah
"""

import argparse
import os



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u',
                                 'A', 'E', 'I', 'O', 'U'])

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args

# Replace vowels [a,e,i,o,u] with the given vowel (a is default)
# foobar --> faabar
# foobar --vowel i --> fiibir
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    vowel = args.vowel
    text = args.text

    lookup = {
        'a': args.vowel,
        'e': args.vowel,
        'i': args.vowel,
        'o': args.vowel,
        'u': args.vowel,
        'A': args.vowel.upper(),
        'E': args.vowel.upper(),
        'I': args.vowel.upper(),
        'O': args.vowel.upper(),
        'U': args.vowel.upper()
    }


#    if args.text.isupper():
#        print(args.text.upper().translate(str.maketrans(lookup)))
#    else:
#        print(args.text.translate(str.maketrans(lookup)))

    # str_translate
    #print(args.text.upper().translate(str.maketrans(lookup)) if args.text.isupper()
     #     else args.text.translate(str.maketrans(lookup)))

    # list comprehension
    print(''.join([lookup.get(char, char) for char in args.text]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
