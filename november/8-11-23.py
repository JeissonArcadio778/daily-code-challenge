"""
https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
"""
from collections import defaultdict

arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]


def migratoryBirds(arr_birds):
    dict_bird = defaultdict(int)

    for bird in arr_birds:
        dict_bird[bird] += 1

    max_count = 0
    min_id = None
    for bird_id, count in dict_bird.items():
        if count > max_count or (count == max_count and bird_id < min_id):
            max_count = count
            min_id = bird_id

    return min_id


print(migratoryBirds(arr))
