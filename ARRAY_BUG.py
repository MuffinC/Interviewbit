def rotateArray(a, b):
    ret = []
    """
    for i in xrange(len(a)):
        ret.append(a[i + b])
    """

    if len(a) == 1: return a
    z = b
    while z > len(a):
        z = z - len(a)
        if z%len(a)==0: return a

    ret = a[z:] + a[:z]
    return ret

print(rotateArray([ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ],56))