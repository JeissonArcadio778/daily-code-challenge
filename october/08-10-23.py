
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

def divisibleSumPairs(n, k, ar):
    res = 0
    print(k)
    for i in range(0, len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                print(i, j)
                res += 1
    return res