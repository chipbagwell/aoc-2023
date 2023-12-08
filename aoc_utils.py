from functools import reduce
from math import gcd  

def find_all(a_str, sub, overlap=False):
    """
    find all occurances of the substring 'sub' in the source string 'a_str'
    @params
    a_str:    source string
    sub:      target substring
    overlap:  True for overlapping matchs, False for non-overlapping matches
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += 1 if overlap else len(sub)


def lcm(vals: list[int]) -> int:
    """
    Least common multiple
    
    Parameters:
    vals list[int]: the list of integers as input

    Returns:
    int: the least common multiple of all inputs
    """
    return reduce(lambda a,b: a*b // gcd(a,b), vals)

