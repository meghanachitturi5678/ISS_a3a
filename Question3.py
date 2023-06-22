a=[]
print("Enter 10 strings:")
for i in range(0,10):#taking input for list of 10 strings
    k=input()
    a.append(k)
#taking user choice(ascending/descending)
k=input("Enter your choice(ascending/descending):")
a.sort()#sorting 10 strings in list a  
#printing 10 strings depending on user's choice
if(k=="ascending"):
    for i in range(0,10):
      print(a[i])
elif(k=="descending"):
    a.reverse()
    for i in range(0,10):
      print(a[i])
#taking input of 1 more string from user
l=input("Add one more string:")
a.append(l)
a.sort()
#printing 11 strings depending on user's choice(taken earlier)
if(k=="ascending"):
    for i in range(0,11):
      print(a[i])
elif(k=="descending"):
    a.reverse()
    for i in range(0,11):
      print(a[i])

 