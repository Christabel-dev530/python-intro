def add(a,b):
    c=a+b
    #return c
    print(c)
add(4,9)

def calculate(a,b,c):
    result=a*b/c
    print(result)
calculate(85,65,3)

def supplyh():
    print("Enter the height")
    h=float(input())
    return h
#calculating the volume of a cylinder
def main(height):
    r=7
    p=3.142
    vol=p*r*r*height
    print(vol)
main(supplyh())


#calculate the surface area of a cylinder
def supplyradius():
    print("enter the radius")
    r=float(input())
    return r
def supplyheight():
    print("enter the height")
    h=float(input())
    return h
def surfacearea(r,h):
    p=3.142
    surfacearea=float((2*p*r*r)+(2*p*r*h))
    print(surfacearea)
surfacearea(supplyradius(),supplyheight())    
    


            
