# 연탄의 크기

import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().rstrip().split()))

# 연탄 사용이 가능한 최대 집의 수
answer = 0

for i in range(2, max(house)+1) :
    # 반지름이 i일때 사용가능한 집의 수
    tmp = 0

    for j in house :
        if j % i == 0 :
            tmp += 1
    answer = max(answer, tmp)

print(answer)