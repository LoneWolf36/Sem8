def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2 + (y2 - y1)**2)**0.5)


X = [2, 4, 4, 4, 6, 6]
Y = [4, 6, 4, 2, 4, 2]
O = ['y', 'y', 'b', 'y', 'y', 'b']

d = []

px = 6
py = 6

ycount = 0
bcount = 0

n = 6
k = 3


def minimum():
    index = d.index(min(d))
    print(d)
    d[index] = 99999
    return index


for i in range(n):
    dist = distance(px, py, X[i], Y[i])
    # print(dist)
    d.append(dist)

for i in range(k):
    out = minimum()
    if(O[out] == 'y'):
        ycount += 1
    else:
        bcount += 1

if ycount > bcount:
    print("Class = Yellow")
else:
    print("Class = Blue")
