#registeration
import random
import os
import pickle
import math
import sys
import datetime
import security_2
def check_pass(password):
    c_no=0
    c_small=0
    c_big=0
    c_spe=0
    for i in password:
        if i.islower()==True:
            c_small+=1
        elif i.isdigit()==True:
            c_no+=1
        elif i.isupper()==True:
            c_big+=1
       
    print "Number of small letters: ",c_small
    print "Number of Capital letters: ",c_big
    
    print "Number of digits: ",c_no

    if c_small>=3 and c_big>=2 and c_no>=3:
        
        return True
    else:
        return not True
            
                       
            
        

def pas():
    print "You must have at least 3 numbers, 3 small and 2 capital characters  in your password (No specifications on Length)\n\n "
    password=raw_input("Your password?  ")
    x=check_pass(password)
    if x==True:
        pass2=raw_input("Enter it again ")

        while pass2!=password:
            print "We couldn't match the passwords, please enter it again"
            pass2=raw_input("Enter it again ")

        return pass2 

    else:
        print "ENTER IT AGAIN"
        pas()

    
def sign_up():
    date='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    
    name=raw_input("Please enter your first name (ONLY):   ")
    while True:
        try:
            inter=int(raw_input("Please enter your age:   "))
            break
        except ValueError:
            print "Does your Age contains letters?? SERIOUSLY BRUH?? -.-"

    age=str(inter)    
    gender=raw_input("Please enter your gender (male/female/other):    ").lower()

    pass2=pas()
    
        
    random.seed()
    x=str(random.randint(1,100000))
        
    f=open("log.txt",'a')
    f.write(name+" has been assigned a user id of "+x)
    f.write("\n")
    f.close()
        

        
    g=open("users.txt",'a')
    g.write(str(x)+" "+str(pass2)+" "+name+" "+age+" "+gender)
    g.write("\n")
    g.close()
    
    updation=[str(x),str(pass2),str(name),str(age),str(gender)]
    security_2.update(updation)
    f=open("log.txt",'a')
    f.write(name+" has just joined StorySnatch!"+"\n"+str(date) )
    f.write("\n")
    f.close()
        
    z=open("wall.txt",'a')
        
    z.write(name+" has just joined StorySnatch! ")
    z.write(str(date)+"\n")
    z.close()

    

    mes=open("messages "+str(name)+".txt",'w+')
    mes.write("-------------------"+name+"'s chats "+"-------------------\n")
    mes.close()

    print "And the world knows that you are here now!!\n"
        
    print "Congrats!! You have been signed up!!\n"
    print "You will need to remember this for signing up next time:\n"
    print "Name: ",name
    print "Password: ",pass2
    print "your unique id: ",x
        
    
        
    
    
