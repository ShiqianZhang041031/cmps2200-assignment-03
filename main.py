# Shiqian Zhang
# assignment-03

# no other imports needed
from collections import defaultdict
import math


### PART 1: SEARCHING UNSORTED LISTS

# search an unordered list L for a key x using iterate
# return True or False
def isearch(L, x):
    return iterate(lambda found, item: found or item == x, False, L)


def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])


# search an unordered list L for a key x using reduce
# return True or False
def rsearch(L, x):
    matches = list(map(lambda item: item == x, L))
    return reduce(lambda a, b: a or b, False, matches)


def reduce(f, id_, a):
    print(a)
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                reduce(f, id_, a[len(a)//2:]))
        return res


def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(ureduce(f, id_, a[:len(a)//3]),
                 ureduce(f, id_, a[len(a)//3:]))


### PART 2: DOCUMENT INDEXING

def run_map_reduce(map_f, reduce_f, docs):
    # done. do not change me.
    """
    The main map reduce logic.

    Params:
      map_f......the mapping function
      reduce_f...the reduce function
      docs.......list of input records
    """
    pairs = flatten(list(map(map_f, docs)))
    groups = collect(pairs)
    return [reduce_f(g) for g in groups]


def doc_index_map(doc_tuple):
    """
    Params:
      doc_tuple....a tuple (docstring, docid)
    Returns:
      a list of tuples of form (word, docid), where token is a
      whitespace delimited element of this string.

    Note that the returned list can contain duplicates.
    """
    # done. do not change me.
    doc, docid = doc_tuple[0], doc_tuple[1]
    return [(token, docid) for token in doc.split()]


def dedup(a, b):
    """
    Return a concatenation of two lists without any duplicates.
    Assume that input lists a and b already sorted and deduplicated.
    This should be done in constant time (ignoring any time to create
    or concatenate lists).

    >>> dedup([1,2,3], [3,4,5])
    [1,2,3,4,5]
    """
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[-1] == b[0]:
        return a + b[1:]
    return a + b


def doc_index_reduce(group):
    """
    Return the unique list of document ids that this word appears in.

    >>> doc_index_reduce(['is', [0,0,1,2]])
    ('is', [0,1,2])
    """
    doc_lists = list(map(lambda docid: [docid], group[1]))
    return (group[0], reduce(dedup, [], doc_lists))


def collect(pairs):
    """
    Implements the collect function.
    """
    # done
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())


def plus(x, y):
    # done. do not change me.
    return x + y


def flatten(sequences):
    # done. do not change me.
    return iterate(plus, [], sequences)


### PART 3: PARENTHESES MATCHING

#### Iterative solution

def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    """
    return iterate(parens_update, 0, mylist) == 0


def parens_update(current_output, next_input):
    """
    Update the running parenthesis balance.
    """
    # Once the balance becomes negative, keep it negative so that
    # an unmatched right parenthesis cannot later be repaired.
    if current_output < 0:
        return current_output

    if next_input == '(':
        return current_output + 1
    elif next_input == ')':
        return current_output - 1
    else:
        return current_output


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using scan.
    This function makes one call each to scan, map, and reduce.
    """
    mapped = list(map(paren_map, mylist))
    prefixes, total = scan(plus, 0, mapped)
    minimum = reduce(min_f, 0, prefixes)

    return total == 0 and minimum >= 0


def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class.
    """
    return (
        [reduce(f, id_, a[:i+1]) for i in range(len(a))],
        reduce(f, id_, a)
    )


def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0


def min_f(x, y):
    """
    Returns the min of x and y.
    """
    if x < y:
        return x
    return y


#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses.
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left == 0 and n_unmatched_right == 0


def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution.

    Returns:
      tuple (R, L), where R is the number of unmatched right
      parentheses and L is the number of unmatched left parentheses.
    """
    if len(mylist) == 0:
        return (0, 0)

    if len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1)
        elif mylist[0] == ')':
            return (1, 0)
        else:
            return (0, 0)

    mid = len(mylist) // 2

    left_r, left_l = parens_match_dc_helper(mylist[:mid])
    right_r, right_l = parens_match_dc_helper(mylist[mid:])

    matched = min(left_l, right_r)

    unmatched_r = left_r + right_r - matched
    unmatched_l = left_l + right_l - matched

    return (unmatched_r, unmatched_l)