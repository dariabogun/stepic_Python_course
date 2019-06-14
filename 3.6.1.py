from requests import get

dataset_name='dataset_3378_2.txt'
f = open(dataset_name, 'r')
str1 = f.read()
res= get(str1.strip())
print(len(res.text.splitlines()))