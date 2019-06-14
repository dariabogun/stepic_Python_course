nnum = int(input())
sum1=num
print(sum1)
nums = []
nums.append(num)
sum2=0
while sum1 != 0:
    a = int(input())
    sum1 += num
    print(sum1)
    nums.append(num)
for i in nums:
    sum2 += i**2
print(sum2)