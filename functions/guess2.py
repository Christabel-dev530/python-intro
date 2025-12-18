def supplypasscode():
   passcode="good"
   return passcode

def supplypassword():
   print("Enter your password")
   password=input()
   return password

def login(passcode,password):
    counter=0
    while passcode != password:
        print('What is the password?')
        password = input()
        if password != passcode:
           print("the password is incorrect")
           counter=counter+1
           print("you have made invalid attempt " ,counter)
           if counter>3:
              break
           else:
              continue
        else:
            print("Hurray, the password is correct")
login(supplypasscode(),supplypassword())                
