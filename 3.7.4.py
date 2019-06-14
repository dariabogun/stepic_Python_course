count=int(input())
commands = [input().split(" ") for i in range(0,count)]

move_dict = {"север": 1, "юг": -1, "восток": 1, "запад":-1}
x=0
y=0

for command in commands:
    if command[0]=="север" or command[0]=="юг":
        y+=move_dict[command[0]]*int(command[1])
    if command[0]=="восток" or command[0]=="запад":
        x+=move_dict[command[0]]*int(command[1])
print(str(x)+" "+str(y))