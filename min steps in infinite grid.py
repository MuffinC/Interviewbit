def coverPoints(A, B):
    steps = 0
    for i in range(len(A) - 1):
        x = abs(A[i] - A[i + 1])
        y = abs(B[i] - B[i + 1])

        steps += max(x, y)

    return steps

print(coverPoints([0,1,1],[0,1,2]))