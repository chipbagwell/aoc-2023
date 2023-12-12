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

def pivot_2d_y_to_x(data):
    """
    Given a list of strings, return a new list of strings
    Where the first string is the concatenation of the first
    characters of each original string, the second string
    is the concatenation of the second characters of each 
    original string (reflection along the n,n diagonal)
    
    Parameters:
    data list[str]: the original list of strings as input
    
    Returns:
    list[str]: the return list of strings
    """
    return [''.join([d[l] for d in data ]) for l in range(len(data[0]))]

def manhatten_distance(x, y):
    """
    Given two complex numbers, calculate the 'manhatten' distance
    between the numbers as a whole non-unit number
    
    Parameters:
    x complex(): the first complex number
    y complex(): the second complex number
    
    Returns:
    int: the 'manhatten' distance
    """
    return abs(x[0]-y[0])+abs((x[1]-y[1]))