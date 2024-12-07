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
    visited = []
    paved = []
    for i in range(len(m)):
        visited.append([0] * len(mp[i]))
        paved.append([' '] * len(mp[i]))
    while 0 <= c_x < len(mp) and 0 <= c_y < len(mp[c_x]):
        visited[c_x][c_y] += 1
        if mp[c_x][c_y] == '#':
            visited[c_x][c_y] -= 1
            paved[c_x][c_y] = '#'
            if direction == '^':
                c_x += 1
            elif direction == 'v':
                c_x -= 1
            elif direction == '>':
                c_y -= 1
            elif direction == '<':
                c_y += 1
            direction = next_dir(direction)
        paved[c_x][c_y] = paved[c_x][c_y].strip() + direction if paved[c_x][c_y] == ' ' else '+'
        if direction == '^':
            c_x -= 1
        elif direction == 'v':
            c_x += 1
        elif direction == '>':
            c_y += 1
        elif direction == '<':
            c_y -= 1
    
    return visited, paved

v, p = simulate(d, s_x, s_y, m)

s = 0
for r in v:
    for c in r:
        if 3 > c >= 1 :
            s += 1

# looks cool to print paved
with open('D06O.txt', 'w') as f:
    for r in p:
        f.write(''.join(r) + '\n')
    

print(s)
            
  

