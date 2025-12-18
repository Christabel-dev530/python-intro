#The radius of circle is 5cm, if pie =3.142. 
# Write a python code that will calculate the 
# double the area of the circle and the one third of the 
# circumference of the circle. 
# Add the two results together and print tit out
r=5
pi=3.142
def circle():
    area=2*(pi*r*r)
    print(area)
    return area

def circumference():
    circumference=1/3*2*pi*r
    print(circumference)
    return circumference

def total(area,circumference):
    total=area+circumference
    print(total)
total(circle(),circumference())    
    
    