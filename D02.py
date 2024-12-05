from typing import List

with open("D02I.txt", "r") as f:
    data = f.read()

def check(n: List[int]):
    safe = True
    wrong_index = -1
    increasing = False
    for i in range(1, len(n)):
        if i == 1:
            if n[i] >= n[i - 1]:
                increasing = True
            else:
                increasing = False
        if abs(n[i] - n[i - 1]) > 3:
            safe = False
            wrong_index = i
            break

        if (n[i] == n[i - 1]) or (n[i] > n[i - 1] and not increasing) or (n[i] < n[i - 1] and increasing):
            safe = False
            wrong_index = i
            break
    
    return safe, wrong_index

data = data.split('\n')
count = 0
for r in data:
    numbers = r.split(' ')
    numbers = [int(i) for i in numbers]
    
    s, i = check(numbers)
    if s:
        count += 1
    else:
        if check(numbers[1:])[0]:
            count += 1
        else:
            num = numbers.copy()
            num.pop(i)                
            if check(num)[0]:
                count += 1
            else:
                numbers.pop(i-1)
                if check(numbers)[0]:
                    count += 1
print(count)