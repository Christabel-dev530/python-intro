# a man went to the market and bought 3 dozens of egg at 200 each.
# he sold all the egg at 250 per one. using python function, calculate
# his profile and percentage profile.
def eliminate():
    cp=36*200
    sp=36*250
    profit=sp-cp
    perprofit=profit/cp*100
    print("the percentage profit is" ,perprofit)
eliminate()    
    
# your maths teacher gave you a question to solve. he said a diameter of a
# circle is 10 meter if pie = 3.142, calculate the area of a circle
#nr2.
def diameter():
    print("Enter your diameter")
    d=float(input())
    p=3.142
    r=float(d/2)
    area_of_a_circle=p*r*r
    print("The area is" ,area_of_a_circle)
diameter()    