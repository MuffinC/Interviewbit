def solve( A, B):

    #find the front sum
    total=0
    for x, y in enumerate(A):
        if x ==B: break
        total+=y
    count=1
    ans=total
    while count<=B-1:
        total=total-A[B-count]+A[-count]
        ans=max(ans,total)


        count+=1
    total = total - A[B - count] + A[-count]
    ans = max(ans,total)
    return ans



print(solve([5, -2, 3 , 1, 2],3))