def solution(friends, gifts):
    n = len(friends)
    arr = [[0] * n for _ in range(n)]
    score = [0] * n # 선물지수
    idx = {}
    
    for i in range(n):
        idx[friends[i]] = i
    
    for gift in gifts:
        a, b = gift.split()
        arr[idx[a]][idx[b]] += 1
        score[idx[a]] += 1
        score[idx[b]] -= 1
    
    result = [0] * n
    for i in range(n): # 주는사람
        for j in range(n): # 받는사람
            if i == j:
                continue
            if (arr[i][j] > arr[j][i]):
                result[i] += 1
            elif (arr[i][j] == arr[j][i]):
                if (score[i] > score[j]):
                    result[i] += 1
    print(result)
    return max(result)