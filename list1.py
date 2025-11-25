list1=[1,3,5,7,9,11,13,15,17,19,21]
#total=sum(list1)
#print(total)


total=0
for i in list1:
    #print(i)
    total=total+i
print(total)
if total>100:
   m=total*3
   print("total is greater than 100")
   print(m)
else:
   m=total-50
   print(m)
   
    


