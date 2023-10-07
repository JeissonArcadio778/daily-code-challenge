# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true


def birthday(s, d, m):
    ans = 0
    for i in range(n-m+1):
        if (sum(s[i:i+m]) == d):
            ans += 1
            
    return ans