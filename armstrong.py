num=int(input("enter the number"))
temp=num
sum=0
l=len(str(num))

while num>0:
 rem=num%10
 num=num//10
 sum=sum+(rem**l)
print(sum)
if sum==temp:
    print("yes")
else:
    print("No")  
