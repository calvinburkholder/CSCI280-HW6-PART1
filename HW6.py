
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
