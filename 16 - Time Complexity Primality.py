p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    prime = True
    upper_limit = round(n**(0.5)) + 1
    for i in range(2, upper_limit):
        if (n%i == 0):
            prime = False
            break
    prime = prime & (n != 1)
    if (prime):
        print ('Prime')
    else:
        print ('Not prime')
