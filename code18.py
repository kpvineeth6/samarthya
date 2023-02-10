l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number:'))
    l1.append(numbers1)
 
l2 = []
num2 = int(input('Enter size of list 2:'))
for n in range(num2):
    numbers2 = int(input('Enter any number:'))
    l2.append(numbers2)
 
union = list(set().union(l1,l2))
 
print('The Union of two lists is:',union)



def intersection(a, b):
    return list(set(a) & set(b))
 
def main():
    alist=[]
    blist=[]
    n1=int(input("Enter number of elements for list1:"))
    n2=int(input("Enter number of elements for list2:"))
    print("For list1:")
    for x in range(0,n1):
        element=int(input("Enter element" + str(x+1) + ":"))
        alist.append(element)
    print("For list2:")
    for x in range(0,n2):
        element=int(input("Enter element" + str(x+1) + ":"))
        blist.append(element)
    print("The intersection is :")
    print(intersection(alist, blist))
main()