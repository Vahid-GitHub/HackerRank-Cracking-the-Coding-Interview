def ransom_note(magazine, ransom):
    possible = True
    magazineWords = {}
    for w in magazine:
        magazineWords.setdefault(w, 0)
        magazineWords[w] += 1
    for w in ransom:
        if (not(magazineWords.get(w))):
            possible = False
            break
        magazineWords[w] -= 1
    return(possible)
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
