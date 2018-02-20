def number_needed(a, b):
    nRemove = 0
    # Remove uncommon letters
    aStrip = a
    bStrip = b
    for l in a:
        if (bStrip.count(l) == 0):
            aStrip = aStrip.replace(l, '')
            nRemove += 1
        while (aStrip.count(l) < bStrip.count(l)):
            inx = bStrip.index(l)
            bStrip = bStrip[0:inx] + bStrip[(inx + 1):]
            nRemove += 1
    for l in b:
        if (aStrip.count(l) == 0):
            bStrip = bStrip.replace(l, '')
            nRemove += 1
        while (bStrip.count(l) < aStrip.count(l)):
            inx = aStrip.index(l)
            aStrip = aStrip[0:inx] + aStrip[(inx + 1):]
            nRemove += 1
    return(nRemove)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
