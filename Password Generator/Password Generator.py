import random
import string

#main program
s1=string.ascii_lowercase

s2=string.ascii_uppercase

s3=string.digits

s4=string.punctuation

print("===================================================")
plength=int(input("\tEnter password length:"))
print("=====================================================")
s=[]
s.extend(s1) #adding the string data to empty list
s.extend(s2)
s.extend(s3)
s.extend(s4)

random.shuffle(s)

print("===========================================================")
print("\tyour password is:{}".format("".join(s[0:plength])))
print("=============================================================")