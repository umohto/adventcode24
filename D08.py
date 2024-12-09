with open('D08I.txt') as f:
    data = f.read().splitlines()

def read(ant: dict, different_ant: dict):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.':
                ant[(i, j)] = data[i][j]
                if data[i][j] not in different_ant:
                    different_ant[data[i][j]] = [(i, j)]
                else:
                    different_ant[data[i][j]].append((i, j))



def find_anti(ant: dict, different_ant: dict, possible_locations: list, c: str):
    counter = 0
    for i in range(len(different_ant[c])):
        for j in range(len(different_ant[c])):
            if i == j:
                continue

            d_x, d_y = different_ant[c][i][0] - different_ant[c][j][0], different_ant[c][i][1] - different_ant[c][j][1]

            n_x, n_y = d_x + different_ant[c][i][0], d_y + different_ant[c][i][1]

            while 0 <= n_x < len(data) and 0 <= n_y < len(data[0]):
                if (n_x, n_y) not in possible_locations and (ant.get((n_x, n_y), '@') != '@' or c != '#'):
                    counter += 1
                    possible_locations.append((n_x, n_y))
                    different_ant['#'].append((n_x, n_y))

                n_x += d_x
                n_y += d_y

    return counter


def find_all(ant: dict, different_ant: dict):
    counter = 0
    possible_locations = []
    for c in different_ant:
        if c == '#':
            continue
        counter += find_anti(ant, different_ant, possible_locations, c)

    counter += find_anti(ant, different_ant, possible_locations, '#')
    return counter

ant = {}
different_ant = {'#': []}
read(ant, different_ant)
counter = find_all(ant, different_ant)

print('count', counter)
