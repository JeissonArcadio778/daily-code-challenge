"""
https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
"""

def bonAppetit(bill, k, b):
    print(bill, k, b)

    sum_foot_brian = 0
    for i in bill:
        if i == bill[k]:
            continue
        sum_foot_brian += i
    
    print(sum_foot_brian)

    total_bill = sum_foot_brian // 2

    if total_bill < b:
        return b - total_bill
    
    return total_bill


print(bonAppetit([3, 10, 2, 9], 1, 12))


def bonAppetit(bill, k, b):
    bill.pop(k)
    per_face = sum(bill) // 2
    print("Bon Appetit" if per_face == b else b - per_face)