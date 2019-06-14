count=int(input())
words = [input().lower() for i in range(0,count)]
count=int(input())
strings= [input().lower().split(" ") for i in range(0,count)]
res=[]
for string in strings:
    for word1 in string:
        flag=True
        for word2 in words:
            if word1==word2:
                flag = False
        if flag:
            if word1 not in res:
                res.append(word1)
for i in res:
    print(i)