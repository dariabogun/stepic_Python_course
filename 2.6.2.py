inp_num = int(input())
s=" "
arr=[]
i=1
count = 0
num = 0
while count < inp_num:
    for i in range(1, num+1):
        arr.append(str(num))
        count+=1
        if count>=inp_num:
            break
    num+=1
print(s.join(arr))