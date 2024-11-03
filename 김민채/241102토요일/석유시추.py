from collections import deque

def bfs(land, sy, sx, block, visited, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(sy, sx)])
    visited[sy][sx] = block
    w = 1
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and land[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = block
                w += 1
    return w

def solution(land):
    n = len(land)
    m = len(land[0])
    
    block_num = 1
    visited = [[0] * m for _ in range(n)]
    
    blocks = {}
    
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                width = bfs(land, i, j, block_num, visited, n, m)
                blocks[block_num] = width
                block_num += 1
    
    answer = 0
    
    for j in range(m):
        temp = 0
        block_visited = [0] * (block_num + 1)
        for i in range(n):
            now = visited[i][j]
            if land[i][j] and not block_visited[now]:
                temp += blocks[now]
                block_visited[now] = 1
        answer = max(temp, answer)

    return answer
