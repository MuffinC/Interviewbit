def largestNumber( A):
    # so we identify 9 as the highest and 0 as the lowest
    # code should start from len 1 first check if 9, weightage of a single digit will always be 3 => 33, 4 => 44, when comparing tens
    # 3 300 => 3 300 vs 3003 1 110 1101

    #find index combination, to rearrange
    hold=[]
    conver={}
    def get_key(val):
        for key, value in conver.items():
            if val == value:
                return key
    maxlen=len(str(max(A)))
    for x in A:
        if len(str(x))<maxlen:
            z=str(x)
            for u in range(0,maxlen-len(str(x))):
                z+=str(x)[0]
            z=int("".join(z))
            hold.append(z)
            conver[x]=z

        else:
            hold.append(x)
    hold=list(reversed(sorted(hold)))

    for x,y in enumerate(hold):
        if y in conver.values():
            k=get_key(y)
            hold[x]= k
            conver.pop(k)

    hold=[str(x) for x in hold]
    res="".join(hold)
    return int(res)



print(largestNumber([ 1,170, 480, 735, 896, 634, 844, 610, 446, 591, 935, 802, 383, 8, 443, 247, 124, 461, 317, 457, 48, 886, 420, 473, 973, 464, 203, 288, 785, 703, 935, 7, 987, 48, 692, 633, 597, 857, 139, 733, 692, 68, 434, 587, 489, 517, 305, 432, 577, 335, 586, 34, 659, 491, 310, 857, 256, 856, 257, 877, 209, 979, 653, 646, 2, 65, 858, 779, 372, 116, 404, 268, 364, 351, 866, 824, 947, 960, 91, 691, 492, 312, 609, 915, 579, 476, 248, 192 ]
))