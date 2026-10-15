#prime umber
num=int(input())
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime numbers")
else:
    print("not prime number")

for i in range(1,11):
    if i==6:
         break
    print(i,end=" ")
print() 
for i in range(1,11):
    if i==6:
        continue
    print(i,end=" ")

if True and False:
    pass
else:
     print("javascript") 