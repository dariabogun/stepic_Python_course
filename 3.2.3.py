n = int(input())
calc_values = {}

for i in range(0, n):
    i = int(input())
    if calc_values.get(i) == None:
        calc_values.setdefault(i, f(i))
    print(calc_values[i])