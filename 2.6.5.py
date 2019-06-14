n=int(input())

table = [[0 for j in range(0, n)] for i in range(0, n)]

s=" "
level = 0
num = 1
def layer_calc(level, num, n, table):
    for i in range(level, n-level):
        table[level][i] = str(num)
        num += 1

    num -= 1
    for j in range(level, n-level):
        table[j][n-level-1] = str(num)
        num += 1

    num -= 1
    for i in range(n-level, level, -1):
        table[n-level-1][i-1] = str(num)
        num += 1

    num -= 1
    for j in range(n-level-1, level, -1):
        table[j][level]=str(num)
        num += 1
    return num
while level<=int(n//2):
    num=layer_calc(level, num, n, table)
    level+=1

for i in table:
    print(s.join(i))