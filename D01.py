with open('D01I.txt') as f:
    data = f.read().splitlines()

res = 0
left = []
right = []
right_count = {}
for r in data:
    f, s = r.split('   ')
    f, s = int(f), int(s)
    
    left.append(f)
    right.append(s)

for r in right:
    if r in right_count:
        right_count[r] += 1
    else:
        right_count[r] = 1

for l in left:
    if l in right_count:
        res += right_count[l] * l
    
print(res)

