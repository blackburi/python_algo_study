import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

nam_y, nam_x = -1, -1
ghosts = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'N':
            nam_y, nam_x = i, j
        elif arr[i][j] == 'G':
            ghosts.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]
visited[nam_y][nam_x] = 1

q = deque([(nam_y, nam_x)])
namwoo = float('inf')
while q:
    y, x = q.popleft()
    if arr[y][x] == 'D':
        namwoo = visited[y][x] - 1
        break
        
    for d in range(4):
        ny = dy[d] + y
        nx = dx[d] + x
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and arr[ny][nx] != '#':
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1
    
visited = [[0] * m for _ in range(n)]
for y, x in ghosts:
    visited[y][x] = 1

q = deque(ghosts)
ghost = float('inf')
while q:
    y, x = q.popleft()
    if arr[y][x] == 'D':
        ghost = visited[y][x] - 1
        break
    
    for d in range(4):
        ny = dy[d] + y
        nx = dx[d] + x
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1
            
if namwoo == float('inf') or namwoo >= ghost:
    print('No')
else:
    print('Yes')