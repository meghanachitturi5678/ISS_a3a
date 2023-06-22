split=[]
rank=[]
import re
info= [dict()]#creating a list of dictionaries
del info[0]
#take number of students(given by user) as integer value of n
n=int(input("Enter number of students:"))

for i in range(0,n):
  j=0
  dic=dict()
  for j in range(0,2): #take student's Name(value of key Name) and Roll-Number(value of key Roll-Number) into dictionary
    data = input() 
    temp = data.split(':') 
    dic.setdefault(temp[0],temp[1])
  data=input()
  temp = re.split(':|,',data)
  k=0
  add=0
  pref1=0
  pref2=0
  while (k<6):
    dic.setdefault(temp[k],temp[k+1])#take subject-name(keys) and corresponding values(values) into dictionary
    temp[k+1]=(int)(temp[k+1])
    #finding median(2nd largest of 3 marks of a student)
    if(temp[k+1]>pref1-1):
        pref2=pref1
        pref1=temp[k+1]    
    elif(temp[k+1]<pref1)and (temp[k+1]>pref2):
        pref2=temp[k+1]
    add+=temp[k+1]   #finding sum of marks of a student
    k+=2
  rank.append(add) #adding sum of marks of a student to array rank
  dic.setdefault('mean',add/3)#adding mean(key) and mean value(value) to dictionary
  dic.setdefault('median',pref2)#adding median(key) and median value(value) to dictionary
  info.append(dic)
index=[]
temp=[]
for i in range(0,n):
      temp.append([rank[i],info[i]['Maths'],info[i]['CSE'],info[i]['Science'],info[i]['Roll-Number'],i])#adding list of values of keys rank,Maths,CSE,Science,Roll-Number and index i to list temp
#(created a list of lists temp)
temp.sort()#sorting lists in list temp based on priority order(high to low):sum of marks,Maths marks,CSE marks,Science marks,Roll-Number(dec order)
for i in temp:
      index.append(i[5])#creating a list index with updated indices of temp
for i in range(0,n):
  info[index[i]]['Rank']=n-i#finding rank of student

for i in range(0,n):#printing Roll-Number and Name of all students
    print(info[i]['Roll-Number'],end="")
    print(" : ",end="")
    print(info[i]['Name'])

#giving option to  user to type Roll-Number os student whose information he/she wants
k=input("Choose and type the Roll-Number whose information is required:")
i=0
#finding the student whose information user wants
while(info[i]['Roll-Number']!=k):
    i+=1
for keys,value in info[i].items():#printing info of required student
    print(keys,end="")
    print(":",end="")
    print(value)

  
  