import random
import datetime
def check(ide,name,password):
    
    date='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    f=open("users.txt","r")
    for line in f:
        inter=line.rstrip().split()
        if len(inter)>=5:
            id_check=inter[0]
            pass_check=inter[1]
            name_check=inter[2]

            if str(id_check)==str(ide) and str(name_check)==str(name) and str(pass_check)==str(password):
                print "confirmed"
                f=open("wall.txt",'a')
                f.write(name+" is now online!!")
                f.write(str(date))
                f.write("\n")
                f.close()
                return True
    
    
        
            
            
        
        
        

    
