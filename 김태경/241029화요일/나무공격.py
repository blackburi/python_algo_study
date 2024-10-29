# 나무 공격

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 각 행에 몇명이 있는지 확인하는 list
cnt = [0]
for _ in range(n) :
    lst = list(map(int, input().rstrip().split()))
    cnt.append(sum(lst))

for _ in range(2) :
    a, b = map(int, input().rstrip().split())
    for i in range(a, a+5) :
        if cnt[i] :
            cnt[i] -= 1

print(sum(cnt))