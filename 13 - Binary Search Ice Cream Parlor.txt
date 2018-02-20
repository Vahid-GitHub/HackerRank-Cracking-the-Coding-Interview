t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    La = len(a)
    pos = None
    for i in range(La - 1):
        for j in range(i + 1, La):
            if ((a[i] + a[j]) == m):
                pos = (i + 1, j + 1)
                break
        if (pos != None):
            print(pos[0], pos[1])
            break
