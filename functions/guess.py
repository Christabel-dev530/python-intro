
passcode ='good'
password=""
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

#print('Yes, the password is ' + password + '. You may enter.')