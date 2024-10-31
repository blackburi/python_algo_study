# 나무 섭지

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())

maze = []
ghosts = []
for i in range(n) :
    line = list(input().rstrip())
    for j in range(m) :
        # 유령이 있는 곳
        if line[j] == 'G' :
            ghosts.append((i, j))
        # 남우가 있는곳
        elif line[j] == 'N' :
            wx, wy = i, j
        # 출구가 있는 곳
        elif line[j] == 'D' :
            end_x, end_y = i, j
    maze.append(line)

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

# 결국 ghost가 출구에 먼저 도착하거나, 남우가 출구에 이동할수 없는 경우 탈출에 실패한다.
# ghost와 남우가 중간에 마주치는 경우를 생각할 필요없다.
def bfs(wx, wy, end_x, end_y, maze) :
    maze[wx][wy] = 0
    q = deque([(wx, wy, 0)])

    while q :
        x, y, dist = q.popleft()
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if maze[nx][ny] == '.' :
                    maze[nx][ny] = dist+1
                    q.append((nx, ny, dist+1))
                elif maze[nx][ny] == 'D' :
                    maze[nx][ny] = dist+1
                    break
        if nx == end_x and ny == end_y :
            break

    if maze[end_x][end_y] == 'D' :
        return 0
    else : # maze[end_x][end_y] == 숫자
        return maze[end_x][end_y]

escape = bfs(wx, wy, end_x, end_y, maze)

ghost = float('inf')
for (i, j) in ghosts :
    ghost = min(ghost, abs(i-end_x)+abs(j-end_y))

if escape == 0 or ghost <= escape :
    print('No')
else :
    print('Yes')