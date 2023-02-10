def commonelements(a,b):

 x=set(a) 
 y=set(b)
 if(x&y):  
   print(x&y)
 else:
   print('No common elements') 

a=[1,2,3,4,5,7,8]
b=[5,6,8,9,11]
commonelements(a,b)