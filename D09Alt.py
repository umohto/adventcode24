import copy

with open("D09I.txt") as f:
    data = f.read()

line = []
c = 0
numbers_count = {}
for i in range(len(data)):
    n = int(data[i])
    if i % 2 == 0:
        for j in range(n):
            line.append(str(c))
        numbers_count[str(c)] = (n, len(line) - 1)
        c += 1
    else:
        for j in range(n):
            line.append('.')

def find_next_non_dot(line, pos):
    for i in range(pos, len(line)):
        if line[i] != '.':
            return i
    return -1

srt = sorted(numbers_count.items(), reverse=True, key=lambda x: int(x[0]))
checked_numbers = set()
p_line = copy.deepcopy(line)
while True:
    for i in range(len(srt)):
        count, end_i = srt[i][1]

        if srt[i][0] in checked_numbers:
            continue

        print(f'Processing: {srt[i][0]} with index {i}')

        for j in range(len(line)):
            if line[j] != '.':
                continue

            if j > end_i:
                break

            next_non_dot = find_next_non_dot(line, j)

            if next_non_dot == -1:
                break

            if next_non_dot - j >= count:
                k = 0
                while k < count:
                    if j + k >= end_i:
                        break
                    line[j+k], line[end_i] = line[end_i], line[j+k]
                    k += 1
                    end_i -= 1

                checked_numbers.add(srt[i][0])
                break

    same = True
    for i in range(len(line)):
        if line[i] != p_line[i]:
            same = False
            break

    if same:
        break

    p_line = copy.deepcopy(line)

print(line)

s= 0
for i in range(len(line)):
    if line[i] == '.':
        continue

    s += int(line[i]) * i

print(s)