with open("D03I.txt", "r") as f:
    data = f.read()

s = 0
first = True
valid = True
l_i = 0
for i, c in enumerate(str(data)):
    if i >= len(str(data)) - 3:
        break
    if data[i:i+3] == 'mul':
        if data[i+3] == '(':
            inparan = data[i+4:data.find(')', i+5)]
            try:
                l, r = inparan.split(',')
                l = float(l)
                r = float(r)
                if not first:
                    do_found = data.find('do()', l_i, i)
                    dont_found = data.find("don't()", l_i, i)
                    if do_found != -1:
                        valid = True
                        l_i = i
                    elif dont_found != -1:
                        l_i = i
                        valid = False             
                    if valid:
                        s += l * r
                else:   
                    s += l * r
                first = False
            except ValueError:
                pass
print(s)
