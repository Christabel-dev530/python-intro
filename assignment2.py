# mr john took a loan of principal 500k for two years at the rate of 5%
p=500000
t=2
r=5
SI=p*t*r/100
print("This is the result" ,SI)

#Mr Thomas has four properties valued at 100000  each 

#his father gave him 50000 

#his mum gave him 150000 

#He bought a car at a value of  200000 

#he gave his wife 30000, 

# if the money in his account initially is 300000

p=4*100000
f=50000
m=150000
c=200000
w=30000
moneyinaccount=300000
expenses=c+w
income=f+moneyinaccount+m
amount=income-expenses
print("the amount in his account is" ,amount)


#The length of a house is 42m and the breath is 34m 

# calculate the perimeter and  the area (separately)



#Then add the perimeter and area together and print out the final results

#Formula: area = length *breadth

                 #Perimeter = (length +breadth)*2 


l=42
b=34
a=l*b
p=2*(l+b)
d=a-p 
print("the area of the house is" ,a)
print("The perimeter of the house is" ,p)
print("the difference between them is" ,d)

if d>100:
    m=d*3000
    print(m)
    print("the difference is greater")
else:
    m=d/3
    print(m)
    print("the difference is less")    
