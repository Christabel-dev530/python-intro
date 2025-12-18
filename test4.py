#calculate the area of a circle
#calculate the volume of a cylinder
#calculate the surface area of a cylinder. return them
#collect the addition of the the three and give the
#final result.
pi=3.142
print("enter the radius")
r=float(input())
print("enter the height")
h=float(input())
def areacircle():
    area=pi*r*r
    print(area)
    return area

def volumecylinder():
    volume=pi*r*r*h
    print(volume)
    return volume

def surfacearea():
    surfacearea=(2*pi*r*h)+(2*pi*r*r)
    print(surfacearea)
    return surfacearea

def total(area,volume,surfacearea):
    total=float(area+volume+surfacearea)
    print(total)
total(areacircle(),volumecylinder(),surfacearea())


#write a python function that will print your name
#surname. return them and collect the two.
#then print with a greeting.


def firstname():
    print("enter firstname")
    firstname=input()
    return firstname

def surname():
    print("enter surname")
    surname=input()
    return surname

def greeting(firstname,surname):
    #greeting=firstname,surname
    print("Hello " + firstname + " " + surname + " you are welcome")
greeting(firstname(),surname())    

        
    