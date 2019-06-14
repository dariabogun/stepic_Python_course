arr = [int(i) for i in input().split(" ")]
arr_res=[]
s=" "
if len(arr) == 1:
    print(arr[0])
else:
    for i in range(0,len(arr)):
        if i < len(arr)-1:
            arr_res.append(str(arr[i-1]+arr[i+1]))
        else:
            arr_res.append(str(arr[i-1]+arr[0]))
    print(s.join(arr_res))

