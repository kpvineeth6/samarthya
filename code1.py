def sumofeven(b,sum):
   for j in b:
    if(j>0):
        if(j%2==0):
          sum=sum+j
   return sum
n=int(input("Enter the number of elements to be in the list:"))
b=[]
sum=0
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
    sumofeven(b,sum)
    print("Sum of all even numbers",sum)



