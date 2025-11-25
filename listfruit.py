listfruit=["orange","orange","orange","apple","apple","apple","apple","apple","apple","banana","pineapple","mango","pawpaw","groundnut"]
listme=["orange","yam","chiz","chiz","pineapple","pineapple","mango","pawpaw","groundnut"]
for i in listfruit:
    if i=="orange":
        #print(i)
        listfruit.remove(i)
    else:
        continue
print(listfruit)

for i in listme:
    if i=="orange":
        #print(i)
        listme.remove(i)
    else:
        continue
print(listme)
    
    
     
