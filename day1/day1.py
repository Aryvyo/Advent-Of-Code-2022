with open('day1.txt') as f:
    data = f.read().splitlines()
    currenttop = 0
    current = 0
    for i in range(len(data)):
        print(data[i])
        if data[i] == '':
            if current > currenttop: currenttop = current ; current = 0
            else: current = 0
        else: current += int(data[i])

print(currenttop)