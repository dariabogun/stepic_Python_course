dna = input()
dna_result = ""
i,j=1,1
while i <= len(dna):
    count = 1
    while i<=(len(dna)-1) and dna[i] == dna[i-1]:
        count = count + 1
        i+=1
    dna_result += (dna[i-1] + str(count))
    i+=1
print(dna_result)