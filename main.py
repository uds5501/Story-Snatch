#Author : Uddeshya Singh
#Encryption Verion: python 2.7.11



import about_us
import sign_in
import register
import post
import messaging
import datetime
import time
import pickle

date='{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

def after_in(user,name):
    userid=user
    name=name
    print"**********************************************************************************************************************************************************************"
    print "                                                          WELCOME ",name.upper(),"!"
    print"**********************************************************************************************************************************************************************"
    print "                                             So.. now that you are here, show the world what you are upto. My upcoming Shakespeare!!"
    print "\n                                                           1.Check out the Wall and see what are other writers upto"
    print "\n                                                           2.Check out your messages for compliments, complaints and other stuff maybe?"
    print "\n                                                           3.Post a new story!!"
    print "\n                                                           4.Logout of your account"

    while True:
        try:
            choice=int(raw_input("---> "))
            if choice==1:
                f=open("wall.txt","r")
                try:
                    print "                                                           THE WALL ADORED BY THY QUOTES"
                    for line in f:
                        print "-->",line
                    f.close()
                    print"**********************************************************************************************************************************************************************"
                    print "                                                           SO, this was all for the wall xD"
                    for i in range(3):
                        print "                                                       .      .   . ...REDIRECTING... .  .      ."
                        time.sleep(1)
                    after_in(userid,name)
                    break
                except EOFError :
                    print "Sorry, nothing to show on the wall"
                    
                
            elif choice==2:
                messaging.read(name)
                print"**********************************************************************************************************************************************************************"

                print "\n\nWanna Send a message to someone? Yes or no?"
                new=raw_input("---> ")
                if new.lower()=="yes":
                    to=raw_input("Please enter the name of Recepient: ")
                    print "TYPE ANYTHING YOU WANT, BUT BE POLITE. OKAY? and ENTER END when you want to stop"
                    text=""
                    inter=""
                    while inter!="END":
                        inter=raw_input("--> ")
                        text=text+" "+inter+"\n"
                    messaging.message(name,to,text)

                    for i in range(3):
                        print "                                                       .      .   . ...REDIRECTING... .  .      ."
                        time.sleep(1)
                    after_in(userid,name)
                elif new.lower()=="no":
                    for i in range(3):
                        print "                                                       .      .   . ...REDIRECTING... .  .      ."
                        time.sleep(1)
                    after_in(userid,name)
                    break

            elif choice==3:
                post.posting(name)
                for i in range(3):
                        print "                                                       .      .   . ...REDIRECTING... .  .      ."
                        time.sleep(1)
                after_in(userid,name)
                break
            elif choice==4:
                f=open("wall.txt","a+")
                f.write(name+" is now offline!!")
                f.write(str(date))
                f.write("\n")

                f=open("log.txt","a+")
                f.write(name+" is now offline!!")
                f.write(str(date))
                f.write("\n")
                for i in range(3):
                        print "                                                       .      .   . ...REDIRECTING TO HOME... .  .      ."
                        time.sleep(1)
                
                home()       
                              
                            
                        
                        
                        
                        
                    
        except ValueError:
            print "Please give value in 1,2,3 or 4"
              
                        
                                    


def home():
    print"**********************************************************************************************************************************************************************"
    print "PLEASE ACTIVATE FULL SCREEN MODE"
    print"**********************************************************************************************************************************************************************"
    print "                                                                                       -----------  "
    print "                                                                                     /"
    print "                                                                                    /"
    print "                                                                                   |TORY"
    print "                                                                                   -----------"
    print "                                                                                        SNATCH|"
    print "                                                                                             /"
    print "                                                                                            /"
    print "                                                                                -----------"

    print "                                                                              StorySnatch \xa9 2016"
    print "                                                                           Where words weave the magic"
                
    print"\n\n NOTE: StorySnatch",u"\u2122"," is a registered trademark, any plagiarism attempt is offense with a penalty of upto 3 weeks of jail ,1000 bucks and maybe a treat to the owner :P"

    print "\n\n                      1.LOGIN                                         2.SIGN UP                                         3.ABOUT US"
    while True:
        try:
            x=int(raw_input("--->  "))
            if x==1:
                while True:
                    try:
                        userid=int(raw_input("Please Enter your Unique ID : "))
                        break
                    except ValueError:
                        print "Hello dude, the Id is in numbers. You lost it or what!?"
                    
                name=raw_input("Please Enter your name :")
                password=raw_input("Please enter your password: ")
                

                really=sign_in.check(userid,name,password)
                
                if really==True:
                    after_in(userid,name)
                    
                            
                                       
                    




                    
                elif really is not True:
                    now=raw_input("Looks like some error has occured, 'coz something You entered doesn't match with our database, We are taking you back at the home page, try again later")
                    for i in range(3):
                        print "                                                            Please wait.... .  .   .    .          ."
                        time.sleep(1)
                    home()
                    break                   
                        
                    

            elif x==2:
                register.sign_up()
                print "\nWe are redirecting you to our homepage now!"
                for i in range(3):
                    print "                                                            Please wait.... .  .   .    .          ."
                    time.sleep(1)
                home()
                break
            elif x==3:
                about_us.about()
                    
                    
                    
        except ValueError:
            print "Please Enter an intger, 1 for LOGIN,2 for SIGNUP and 3 for ABOUT US"


home()        
