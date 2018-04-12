#security check
import os
import pickle
def check():
    a=[]
    b=[]
    try:
        ref=open("refer.txt","r")
        for line in ref:
            a.append(line)
        ref.close()

        

        main=open("users.txt","r")

        for line in main:
            b.append(line)
        main.close()
        

        if a==b:
            return True
        else:
            return False
            
        
    except IOError or EOFError:
        print "File not found"
    

