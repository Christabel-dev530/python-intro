# if the area of a triangle is 102 square meter
# and the base is 24m 
# find the height using python fucntion
# using the height as the parameter, 

# find the surface area of a cylinder
#whose height is the same as that of the 
# triangle using python functions
#formula: A=2πrh+2πr2

def height():
    a=102
    b=24
    h=2*a/b
    print(h)
    return h

def surfacearea(h):
    pi=3.142
    print("Enter the radius")
    radius=float(input())
    surfacearea=(2*pi*radius*radius)+(2*pi*radius*h)
    print("The surface area is", surfacearea)
surfacearea(height())    
    