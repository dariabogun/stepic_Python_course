a,b,c,d = int(input()),int(input()),int(input()),int(input())
t=""
for i in range(c, d+1):
    t+=(str(i)+'\t')
print(t)

for j in range(a, b+1):
	t=""
	t+=(str(j)+ '\t')
	for i in range(c,d+1):
		t+=(str(i*j)+'\t')
	print(t)
