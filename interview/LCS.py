# LCS(Xm, Yn) = LCS(Xm-1, Yn-1) + Xm
A = 'abcdef'
B = 'acbcf'

a = [[0]*(len(A)+1) for j in range(len(B)+1)]
i = 0
j = 0
for j in range(1, len(A)+1):
    for i in range(1, len(B)+1):
        # 注意row, column循环内外层次序
        value1 = A[j-1]
        value2 = B[i-1]
        # print(i, j)
        if value1 == value2:
            # print(value1, value2)
            a[i][j] = a[i-1][j-1] + 1
        else:
            a[i][j] = max(a[i-1][j], a[i][j-1])
print('longest common sequence number is ', max(max(a)))
reverse_row = list(range(len(a)))[::-1]
reverse_col = list(range(len(a[0])))[::-1]
lcs = ['']*max(max(a))
# start from the right bottom
row, col, index = len(B), len(A), max(max(a))

while row > 0 and col > 0:
    print(row, col)
    value0 = a[row][col]
    value1 = a[row-1][col]
    value2 = a[row][col-1]
    value3 = a[row-1][col-1]
    #
    if A[col-1] == B[row-1]:
        lcs[index-1] = (A[col-1])
        row -= 1
        col -= 1
        index -= 1
    elif value1 > value2:
        row -= 1
    else:
        col -= 1
print('LCS: ', ''.join(lcs))
