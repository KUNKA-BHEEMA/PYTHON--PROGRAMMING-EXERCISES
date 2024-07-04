#ADDITION OF 2 MATRICES

Mat1 = ()
row = int(input("Enter Row : "))
col = int(input("Enter Cols : "))
print("Matrix 1 : ")
for i in range(row):
    c=()
    for j in range(col):
      v=int(input("Enter Value {},{}:".format(i,j)))
      c+=(v,)
    Mat1 += (c,)


Mat2 = ()
print("Matrix 2 : ")
for i in range(row):
    c = ()
    for j in range(col):
        v = int(input("Enter Value {},{}:".format(i, j)))
        c += (v,)
    Mat2 += (c,)

print("Value of matrix 1 : ", end = " ")
print(Mat1)
print("Value of matrix 2 : ", end = " ")
print(Mat2)

sumMat = ()
print("Sum Matrix : ", end = " ")
for i in range(row):
    c=()
    for j in range(col):
        v = Mat1[i][j]+Mat2[i][j]
        c+=(v,)
    sumMat+=(c,)

print(sumMat)

