data={"person1":"abc","person2":"xyz","person3":"jkl"}
condition=False
while not condition:
    username=input("enter the username\n")
    password=input("enter the password\n")
    if(username==data and password==password):
        continue
    elif(password==data[username]):
        print("welcome",username)
        finish=True
