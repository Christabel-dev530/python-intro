#mr john took a loan of principal 500k for two years at the r8 of 5%
#write a python code  that will calculate the simple interest
def simple_interest():
    p=500000
    r=5
    t=2
    SI=p*r*t/100
    print("the simple interest is" ,SI)
simple_interest()

#Mr James just died and his properties  worth $108000  but he owe a debt of $10000, the balance was divided among his children in the ratio 1:3:4
#Write a python  function code that determines who got the highest and print it out
def properties():
    p=108000
    d=10000
    balance=p-d
    totalratio=1+2+4
    highest=3/totalratio*balance
    print(highest)
    lowest=1/totalratio*balance
    print(lowest)
properties()
