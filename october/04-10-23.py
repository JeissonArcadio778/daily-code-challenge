

# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true 

# Solution:


def kangaroo(x1, v1, x2, v2):
    print(x1, v1, x2, v2)
        
    if x1 > x2 and v1 > v2:
        return "NO"
    elif x2 > x1 and v2 > v1:
        return "NO"

    count = 0
    n = 1
    while (count < 10000):
        if (n * v1 + x1 == n * v2 + x2):
            return "YES"
        n += 1
        count += 1
    return "NO"
