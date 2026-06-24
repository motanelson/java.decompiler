import os
import copy
compilers="javac --release 8 "
decompilers="javap -c -private "
print("\033c\033[47;31m\ngive me file to decompile: ? \n")
a=input().strip()
#a="Hello.java"
b=a.replace(".java","")
os.system(compilers + a)
os.system(decompilers + b+".class > "+b +".s")
f1=open(b+".s","r")
v=f1.read()
f1.close()
fff=""
bodys=v.split("\n")
for f in bodys:
    ff=f.split("//")
    if len(ff)>1:
        fff=fff+"\n"+"//"+ff[1]
    fff=fff+"\n"+ff[0]


f1=open(b+".s","w")
f1.write(fff)
f1.close()

