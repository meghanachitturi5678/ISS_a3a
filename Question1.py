a=input("Enter the number of stars at extreme lines:")#taking input of number of stars to be printed on first and last lines
i=(int)a#taking integer value of a as i
if (i%2==1) or (i==0):
    print("Invalid Input!!")#handling impossible cases
else:
   #printing upper half of design 
   while(i>1):
        k=(int)((a-i)/2)
        print(" "*(k)+"*"*i+" "*k)#printing required number of stars with required spaces at left and right on each line
        i=i-2
   i=2
   #printing lower half of design 
   while(i<a+1):
        k=(int)((a-i)/2)
        print(" "*(k)+"*"*i+" "*k)#printing required number of stars with required spaces at left and right on each line
        i=i+2
