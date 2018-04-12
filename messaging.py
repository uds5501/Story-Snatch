import datetime
import pickle
date=' {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
def message(user,to,text):
    
    try:
        f=open("messages "+str(to)+".txt","a")
        f.write(str(date)+"\n")
        f.write("Message by "+str(user)+":\n")
        f.write(text)
        f.close()
    except IOError:
        print "Sorry but your message couldn't be delivered"

def read(user):
    
    
    try:
        f=open("messages "+str(user)+".txt","r")
        for line in f:
            print line
    except EOError:
        print "Messaging file not detected, we are sorry for inconvinience"
        
    

    
    
