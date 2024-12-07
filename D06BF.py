with open('D06I.txt') as f:
    data = f.read().splitlines()

def next_dir(inp: str):
    return {
        '^': '>',
        'v': '<',
        '>': 'v',
        '<': '^'
    }[inp]

m = []
s_x, s_y = 0, 0
d = ''
for i, r in enumerate(data):
    m.append(list(r))
    for c in range(len(r)):
        if r[c] in '><^v':
            s_x, s_y = i, c
            d = r[c]

def simulate(direction, x, y, mp):
    c_x, c_y = x, y
    visited_set = set()

    while 0 <= c_x < len(mp) and 0 <= c_y < len(mp[c_x]):
        current_state = (c_x, c_y, direction)
        if current_state in visited_set:
            return None

        visited_set.add(current_state)

        if mp[c_x][c_y] == '#':
            if direction == '^':
                c_x += 1
            elif direction == 'v':
                c_x -= 1
            elif direction == '>':
                c_y -= 1
            elif direction == '<':
                c_y += 1
            direction = next_dir(direction)
        else:
            if direction == '^':
                c_x -= 1
            elif direction == 'v':
                c_x += 1
            elif direction == '>':
                c_y += 1
            elif direction == '<':
                c_y -= 1

    return list(visited_set)


o_pairs = []

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '^' or m[i][j] == '#':
            continue

        m[i][j] = '#'
        if not simulate(d, s_x, s_y, m):
            o_pairs.append((i, j))
            print(i, j)
        m[i][j] = '.'

print(f'Obstacles: {len(o_pairs)}')
            
  

