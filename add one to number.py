def plusOne(A):
    z=[str(y) for y in A]
    res = (int("".join(z))) + 1
    ans = [x for x in str(res)]
    return ans
print(plusOne([1,2,3]))