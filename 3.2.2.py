str = input().lower().split(" ")
words={}

for i in str:
    if words.get(i) != None:
        words[i] = words[i] + 1
    else:
        words.setdefault(i,1)

for key, value in words.items():
    print(key, value)