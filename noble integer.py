def solve(A):
    A=list(sorted(A))
    p=float('-inf')
    smallest=0
    for x in A:
        if x>0 and x>p:
            p=x
            break
    for y in A:
        if y>p:
            smallest+=1

    if smallest==p:
        return 1
    return -1


print(solve([3,2,1,3]))