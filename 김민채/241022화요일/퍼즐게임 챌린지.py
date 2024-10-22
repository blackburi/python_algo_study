def solution(diffs, times, limit):
    right = max(diffs)
    left = 1
    
    answer = max(diffs)
    while left <= right:
        mid = (left + right) // 2
        time = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid: # 안 틀림
                time += times[i]
            else: # 틀림
                level_diff = diffs[i] - mid
                time += (times[i - 1] + times[i]) * level_diff + times[i]
        if time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer