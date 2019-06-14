def decode(count, symb):
    r=""
    for i in range(0,count):
        r+=symb
    return r
dataset_name='dataset_3363_2.txt'
f = open(dataset_name, 'r')
str1 = f.read()
f.close()
i = 0
res=""
count = 0
count_temp = ""
symbol = ""
flag = True
while i < len(str1):
    if str1[i].isdigit():
        count_temp += str1[i]
        if not str1[i+1].isdigit():
            flag=False
    else:
        symbol=str1[i]
    if not flag:
        res+=decode(int(count_temp),symbol)
        flag=True
        count_temp=""


    i+=1
f = open("result_"+dataset_name, 'w')
f.write(res)
f.close