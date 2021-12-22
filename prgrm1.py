import string
import random
l=int(input("length of password\n"))
x=string.ascii_uppercase
y=string.ascii_lowercase
z=string.digits
all=x+y+z
#a1=int(input("enter the number of uppercase alphabets\n"))
#a2=int(input("enter the number of lowercase digits in password\n"))
#a3=int(input("enter the nnumber of digits in password\n"))
password=[]
for i in range(l):
    password.append(random.choice(all))
#for i in range(l):
    #password.append(random.choice(y)) 
#for i in range(l):
    #password.append(random.choice(z))
random.shuffle(password)
print("".join(password))    
           