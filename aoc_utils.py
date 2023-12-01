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
