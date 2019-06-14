def average(lst):
    return sum(lst) / len(lst)

dataset_name='dataset_3363_4.txt'
f = open(dataset_name, 'r')
str1 = f.read().split('\n')
f.close()
math_mark=[]
phys_mark=[]
rus_mark=[]
res=""
for i in str1:
        j=i.split(';')
        if len(j)>1:
            res+=str(average([float(j[1]),float(j[2]),float(j[3])]))+"\n"
            math_mark.append(float(j[1]))
            phys_mark.append(float(j[2]))
            rus_mark.append(float(j[3]))
res+=str(average(math_mark))+ " " + str(average(phys_mark))+ " " +str(average(rus_mark))
f = open("result_"+dataset_name, 'w')
f.write(res)
f.close