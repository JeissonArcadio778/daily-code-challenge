
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

scores = [
    17, 45, 41, 60, 17, 41, 76, 43, 51, 40, 89, 92, 34, 6, 64, 7, 37, 81, 32, 50
]

def breakingRecords(scores):
    score_max = scores[0]
    score_min = scores[0]
    count = [0, 0]
    
    for i in range(1, len(scores)):

        if scores[i] < score_min:
            count[1] += 1
            score_min = scores[i]
        elif scores[i] > score_max:
            count[0] += 1
            score_max = scores[i]
        print(scores[i], score_min, score_max, count)
    
    return count

breakingRecords(scores=scores)
  

