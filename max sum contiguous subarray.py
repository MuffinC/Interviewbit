def maxSubArray(A):
    n = len(A)
    sumi = 0
    maxi = float('-inf')
    for x in range(0, n):
        sumi += A[x]
        maxi = max(maxi, sumi)
        if (sumi < 0): sumi = 0
    return maxi


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))