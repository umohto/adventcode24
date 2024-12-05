with open('D05I.txt') as f:
    data = f.read().splitlines()


l_pairs = []
for r in data:
    if r == '':
        break
    
    l, r = r.split('|')
    l, r = int(l), int(r)
    
    l_pairs.append((l, r))
    
rows = []
for r in data:
    if '|' in r or r == '':
        continue
    
    numbers = r.split(',')
    numbers = [int(n) for n in numbers]
    rows.append(numbers)

def check(left, right):
    if (left, right) in l_pairs:
        return True
    return False

valid_rows = []
s = 0
for r in rows:
    v = True
    for i in range(0, len(r)-1):
        if not check(r[i], r[i + 1]):
            v = False
            break

    if v:
        s += r[int(len(r)/2)]
        valid_rows.append(r)

print(s)
s = 0
for r in rows:
    if r in valid_rows:
        continue
    for i in range(len(r)-1):
        for j in range(i+1, len(r)):
            if not check(r[i], r[j]):
                # swap
                r[i], r[j] = r[j], r[i]
    
    s += r[int(len(r)/2)]

print(s)