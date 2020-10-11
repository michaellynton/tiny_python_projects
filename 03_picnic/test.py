#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'{prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_without_oxford_comma():
    """user can choose not to print oxford comma """

    arg = 'bananas apples dates'
    out = getoutput(f'{prg} {arg} --comma')
    expected = ('You are bringing bananas, apples and dates.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_sorted_without_oxford_comma():
    """user can choose not to print oxford comma """

    arg = 'bananas apples dates'
    out = getoutput(f'{prg} {arg} --comma --sorted')
    expected = ('You are bringing apples, bananas and dates.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_separator():
    """more than two items with different separator"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"{prg} {arg} --sep ';' ")
    expected = ('You are bringing potato chips; coleslaw; '
                'cupcakes; and French silk pie.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_sorted_separator():
    """more than two items, sorted, with different separator"""

    arg = 'bananas apples dates'
    out = getoutput(f"{prg} {arg} --sorted --sep ';' ")
    expected = ('You are bringing apples; bananas; and dates.')
    assert out.strip() == expected