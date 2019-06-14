key = input()
code = input()
encode = input()
decode = input()


encode_dict={}
decode_dict={}


for i in range(0,len(key)):
    encode_dict[key[i]]=code[i]
    decode_dict[code[i]] = key[i]


for i in encode:
    print(encode_dict[i],end="")
print()

for i in decode:
    print(decode_dict[i],end="")
print()