from requests import get

dataset_name='dataset_3378_3.txt'
f = open(dataset_name, 'r')
str1 = f.read()
res= get(str1.strip())
flag=True


while flag:
    res=get("""https://stepic.org/media/attachments/course67/3.6.3/"""+res.text.strip())
    if res.text[0]=="W" and res.text[1]=="e":
        print(res.text)
        flag=False