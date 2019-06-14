dataset_name='dataset_3363_3.txt'
f = open(dataset_name, 'r')
str1 = f.read()
f.close()
s=" "
words={}
arr=s.join(str1.split("\n")).split(" ")
for i in arr:
    if words.get(i) != None:
        words[i] = words[i] + 1
    else:
        words.setdefault(i, 1)
res=max(words, key=words.get)+ " " + str(words[max(words, key=words.get)])
f = open("result_"+dataset_name, 'w')
f.write(res)
f.close