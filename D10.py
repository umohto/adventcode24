with open('D10I.txt') as f:
    data = f.read().splitlines()

mp = []
zeros = set()
for i in range(len(data)):
    mp.append(list(map(int, data[i])))
    for j in range(len(data[i])):
        if mp[i][j] == 0:
            zeros.add((i, j))


def dfs(x, y):
    stack = [(x, y)]
    # visited = set()
    count = 0
    while stack:
        x, y = stack.pop()
        # part 2
        # if (x, y) in visited:
        #     continue
        # visited.add((x, y))
        if mp[x][y] == 9:
            count += 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(mp) and 0 <= ny < len(mp[0]):
                if mp[nx][ny] - mp[x][y] == 1:
                    stack.append((nx, ny))
    return count

s = 0
for z in zeros:
    s += dfs(z[0], z[1])

print(s)