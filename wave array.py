def wave(A):
    #wave will always be high->low ->high->low
    A=list(sorted(A))
    flip=0
    res=[]
    while flip+1<len(A):
        res.append(max(A[flip],A[flip+1]))
        res.append(min(A[flip],A[flip+1]))
        flip+=2
    if len(A)%2==1:res.append(A[len(A)-1])
    return res

print(wave([5,1,2,3,4]))