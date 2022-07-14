def solve(A, B):
    # you just need to check if it cover the front
    count = 0
    while True:
        if A[count] != 1:
            count += 1
        else:
            break

    if (count - B + 1) < 1:
        return -1
    else:
        front =(count - B + 1)
        back = (count + B - 1)




print(solve([ 0, 0, 0, 1, 0],3))