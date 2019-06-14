lst = [int(i) for i in input().split(" ")]
x = int(input())
position = 0
positionition_in_lst = []
while position < len(lst):
    if x in lst:
        for i in lst:
            if i == x:
               positionition_in_lst.append(position)
            position+=1
    else:
        positionition_in_lst.append("Отсутствует")
        break
for i in positionition_in_lst:
    print(i, end=" ")