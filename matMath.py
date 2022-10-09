# Operaciones con matrices obtenidas de varias fuentes
import math


# https://stackoverflow.com/questions/40120892/creating-a-matrix-in-python-without-numpy
def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            # you need to increment through dataList here, like this:
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)

    return mat


# https://stackoverflow.com/questions/28253102/python-3-multiply-a-vector-by-a-matrix-without-numpy
def multMatrix(v, G):
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(G[0])):  # this loops through columns of the matrix
        total = 0
        for j in range(len(v)):  # this loops through vector coordinates & rows of matrix
            for k in range(len(v)):
                result[i][j] += v[i][k] * G[k][j]
    return result


# Function to print identity matrix
# https://www.geeksforgeeks.org/python-program-for-identity-matrix/
def identityMatrix(size):
    matrix = []
    for row in range(0, size):
        matrix.append([])
        for col in range(0, size):
            # Here end is used to stay in same line. Append instead of print
            if (row == col):
                matrix[row].append(1)
                #print("1 ", end=" ")
            else:
                matrix[row].append(0)
                #print("0 ", end=" ")
    return matrix


# https://stackoverflow.com/questions/35208160/dot-product-in-python-without-numpy
def dotMatrix(v1, v2):
    return sum([x*y for x, y in zip(v1, v2)])


# Simplemente multiplicar vectores
def vectMultMatrix(M, v):
    return [dotMatrix(r, v) for r in M]


# https://www.statology.org/cross-product-python/
def crossProductMatrix(A, B):
    result = [A[1]*B[2] - A[2]*B[1],
              A[2]*B[0] - A[0]*B[2],
              A[0]*B[1] - A[1]*B[0]]
    return result


# Transpose matrix
def transposeMatrix(m):
    return map(list, zip(*m))


# Tres funciones para poder hallar el determinante de una matriz sin numpy
# https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
def zerosMatrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M


def copyMatrix(M):
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 2: Create a new matrix of zeros
    MC = zerosMatrix(rows, cols)

    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def determinantMatrix(A, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    # Section 3: define submatrix for focus column and
    #      call this function
    for fc in indices:  # A) for each focus column, ...
        # find the submatrix ...
        As = copyMatrix(A)  # B) make a copy, and ...
        As = As[1:]  # ... C) remove the first row
        height = len(As)  # D)
        for i in range(height):
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:]
        sign = (-1) ** (fc % 2)  # F)
        # G) pass submatrix recursively
        sub_det = determinantMatrix(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det
    return total


# Substract
def subtractVectors(v1, v2):
    result = [i-j for i, j in zip(v1, v2)]
    return result


# Norm fuction
def normMatrix(list):
    dist = math.sqrt(((list[0] - list[1]) ** 2)
                     + ((list[1] - list[2]) ** 2)
                     + ((list[2] - list[0]) ** 2))

    return dist


# Magnitud
def magnitudeMatrix(m):
    b = 0
    a = 0
    for i in m:
        a = i**2
        b += a
    b = b**0.5
    return b


# Matrix inversion dos funciones
# https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def inverseMatrix(m):
    determinant = determinantMatrix(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * determinantMatrix(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
