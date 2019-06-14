def average(lst):
    return sum(lst) / len(lst)

dataset_name='dataset_3380_5.txt'
f = open(dataset_name, 'r')
str1 = f.read().split('\n')
f.close()
h_list=[]
res=""
for i in range(0,12):
    h_list.append([])

for i in str1:
    if len(i)>1:
        i1=i.split("\t")
        h_list[int(i1[0])].append(float(i1[2]))
for i in range(1,len(h_list)):
    if(len(h_list[i])<1):
        print(str(i)+" -")
        res+=str(i)+" -"+"\n"
    else:
        print(str(i)+" "+str(average(h_list[i])))
        res += str(i)+" "+str(average(h_list[i])) + "\n"



f = open("result_"+dataset_name, 'w')
f.write(res)
f.close