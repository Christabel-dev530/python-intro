#calculate the surface area of a circle whose height =15meter 
# and the radius is 5m. if pie=3.142, calculate the surface area of the
# circle using pathin function. hint surarea=nr2h
def surfacearea():
    print("Enter your height")
    h=float(input())
    print("Enter your radius")
    r=float(input())
    p=3.142
    surfacearea=p*r*r*h
    print(surfacearea)
surfacearea()