def find_combinations(n):
    if (n < 1):
        return(0)
    elif (n == 1):
        return(1)
    elif (n == 2):
        return(3)
    sumTerms = {}
    new_terms = {}
    for i in range(1, 4):
        sumTerms[i] = 1
        new_terms[i] = 0
    for i in range(4, n + 1):
        sumTerms[i] = 0
        new_terms[i] = 0
    sumComb = sumTerms[n]
#    print(sumTerms)
    for level in range(n - 1):
        for i in range(1, n + 1):
            upperLimit = 4 if (i > 4) else i
            for k in range(1, upperLimit):
                new_terms[i] += sumTerms[i - k]
        for i in range(1, n + 1):
            sumTerms[i] = new_terms[i]
            new_terms[i] = 0
#        print(sumTerms)
        sumComb += sumTerms[n]
    return(sumComb)

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(find_combinations(n))
