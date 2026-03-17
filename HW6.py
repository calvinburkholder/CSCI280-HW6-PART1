import pytest_lazyfixture

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
    prev = memo[0]

    for i in range(3, n+1):
        memo[i] = q[i-1] + prev
        prev = max(prev, memo[i-2])

    return max(prev, memo[n-1], memo[n])

def test_best_quality_1():
    assert turnips([5,1,2,8]) == 13

test_best_quality_1()
