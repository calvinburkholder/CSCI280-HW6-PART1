def turnips(q):
    n = len(q)
    if n == 0:
        return 0
    memo = [0]*(n+1)

    memo[0] = 0
    if n >= 1:
        memo[1] = q[0]
    if n >= 2:
        memo[2] = q[1]

    for i in range(3, n+1):
        memo[i] = q[i-1] + max(memo[:i-2])

    return max(memo)

def test_best_quality_1():
    assert turnips([5,1,2,8]) == 13

def test_best_quality_2():
    assert turnips([]) == 0

def test_best_quality_3():
    assert turnips([5]) == 5

def test_best_quality_4():
    assert turnips([3,3,3,3]) == 6

def test_best_quality_5():
    assert turnips([5,3,2,1]) == 6

def test_best_quality_6():
    assert turnips([1,2,3,4,5,6,7,8,9,10]) == 22

def test_best_quality_7():
    assert turnips([1,2]) == 2

#Output:
# @calvinburkholder ➜ /workspaces/CSCI280-HW6-PART1 (main) $ pytest HW6_tests.py
# ======================================= test session starts =============================================================================
# platform linux -- Python 3.12.1, pytest-9.0.1, pluggy-1.6.0
# rootdir: /workspaces/CSCI280-HW6-PART1
# plugins: anyio-4.11.0
# collected 7 items                                                                                                                                                             

# HW6_tests.py .......                                                                                                                                                    [100%]

# ======================================== 7 passed in 0.04s ==============================================================================
# @calvinburkholder ➜ /workspaces/CSCI280-HW6-PART1 (main) $ 