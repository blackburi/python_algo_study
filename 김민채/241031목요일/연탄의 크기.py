import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

answer = 0
for r in range(2, max(arr) + 1):
    cnt = 0
    for x in arr:
        if x % r == 0:
            cnt += 1
    answer = max(cnt, answer)
print(answer)