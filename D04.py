with open('D04I.txt') as f:
    data = f.read().splitlines()

def check_xmas(i, j):
    c = 0
    if i >= 3 and j >= 3:
        if data[i][j] == 'X' and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
            c += 1
        if data[i][j] == 'S' and data[i-1][j-1] == 'A' and data[i-2][j-2] == 'M' and data[i-3][j-3] == 'X':
            c += 1
    if i >= 3 and j + 3 < len(data):
        if data[i][j] == 'X' and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
            c += 1
        if data[i][j] == 'S' and data[i-1][j+1] == 'A' and data[i-2][j+2] == 'M' and data[i-3][j+3] == 'X':
            c += 1
    if i >= 3:
        if data[i][j] == 'X' and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
            c += 1
        if data[i][j] == 'S' and data[i-1][j] == 'A' and data[i-2][j] == 'M' and data[i-3][j] == 'X':
            c += 1
    if j >= 3:
        if data[i][j] == 'X' and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
            c += 1
        if data[i][j] == 'S' and data[i][j-1] == 'A' and data[i][j-2] == 'M' and data[i][j-3] == 'X':
            c += 1

    return c

s = 0
for i in range(len(data)):
    for j in range(len(data)):
        s += check_xmas(i, j)

# 2560
print(s)

def check_mas(i, j):
    if data[i][j] != 'A':
        return False

    if (data[i-1][j-1], data[i+1][j+1]) in [('M', 'S'), ('S', 'M')] and (data[i-1][j+1], data[i+1][j-1]) in [('M', 'S'), ('S', 'M')]:
        return True
    
    return False

    
        
    
s = 0
for row in range(1, len(data)-1):
    for col in range(1, len(data)-1):
        if check_mas(row, col):
            s += 1

# 1910
print(s)