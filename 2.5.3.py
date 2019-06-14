arr = [int(i) for i in input().split(" ")]
arr.sort()
s = " "
arr_res = []
i = 0
while i in range(0, len(arr)):
    if arr.count(arr[i]) > 1:
        arr_res.append(str(arr[i]))
        i = i+arr.count(arr[i])
    else:
        i += 1

print(s.join(arr_res))