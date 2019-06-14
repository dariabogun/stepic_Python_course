matrix = []
delim=' '
while True:
    n = str(input())
    if n == 'end':
        break
    matrix.append([int(s) for s in n.split()])
matrix_result = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

column_count = len(matrix)
str_count = len(matrix[0])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
	matrix_result[i][j]=int(matrix[i-1][j]) + int(matrix[(i+1)%column_count][j]) + int(matrix[i][j-1]) + int(matrix[i][(j+1)%str_count])

res=[]
for i in range(len(matrix_result)):
    for j in range(len(matrix_result[i])):
        res.append(str(matrix_result[i][j]))
    print(delim.join(res))
    res=[]