from main import *
# 2 pts each.

# 2 pts
def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])

# 2 pts
def test_isearch2():
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert isearch([1, 3, 5], 2) == (2 in [1, 3, 5])
    assert isearch([], 2) == (2 in [])
    

# 2 pts
def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])

# 2 pts
def test_rsearch2():
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert rsearch([], 2) == (2 in [])

# 2 pts
def test_dedup():
    assert dedup([1,2,3], [3,4,5]) == [1,2,3,4,5]
    assert dedup([1,2,3], [5,6]) == [1,2,3,5,6]

# 2 pts  
def test_doc_index_reduce():
    assert doc_index_reduce(['is', [0,0,1,2]]) == ('is', [0,1,2])
    assert doc_index_reduce(['is', [0,0,0,0,1,1,1,1,1,1,2,2,2,2]]) == ('is', [0,1,2])

# 2 pts
def test_index():
    res = run_map_reduce(doc_index_map, doc_index_reduce,
               [('document one is cool is it', 0),
                ('document two is also cool', 1),
                ('document three is kinda neat', 2)
               ])    
    assert sorted(res) == [('also', [1]),
                   ('cool', [0, 1]),
                   ('document', [0, 1, 2]),
                   ('is', [0, 1, 2]),
                   ('it', [0]),
                   ('kinda', [2]),
                   ('neat', [2]),
                   ('one', [0]),
                   ('three', [2]),
                   ('two', [1])]

# 2 pts
def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True

# 2 pts
def test_parens_match_iterative2():
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False

# 2 pts
def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True

# 2 pts
def test_parens_match_scan2():
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False

# 2 pts
def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True

# 2 pts
def test_parens_match_dc2():
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 
