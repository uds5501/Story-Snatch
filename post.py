import datetime
import pickle
date=' {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

def moderator(word):
    banned=["fuck","fucked","fucker","shit","bullshit","nigga","faggot","slut","felch","cunt","skullfuck","cum","bitch","bastard","rascal","ass","asshole","motherfucker","dick","pussy","tits","chutia","saala","saale","kutta","kutte","kamina","bc"]
    if word.lower() not in banned:
        return word
    
    else:
        return "***"
        
    
class post:
        def __init__(self,content,title,user):
            self.content=content
            self.user=user
            self.title=title

        def display(self):
            print str(self.user)+": |||| \t "+ str(self.title) + "\t ||||"
            print str(self.user)+str(date)+": |||| \t "+ str(self.content) + "\t ||||"

        def update_n(self):
            f=open("log.txt",'a')
            f.write(str(self.user)+" at "+str(date)+"quoted: \n"+str(self.content))
            f.write("\n")
            f.close()

            f=open("wall.txt",'a')
            f.write(str(self.user)+" at "+str(date)+"quoted: \n"+str(self.content))
            f.write("\n")
            f.close()

       

    
def posting(user):
    print "Okay , so the posting procedures are as follows:\n1.Be imaginative and make original quotes.\n2.You cannot use abusive language and derogatory words, they will be automatically censored.\n3.You can keep writing and hit enter for new line. To stop writing, just type -END- and we will know that's it."
    print "MAXIMUM CHARACTER LIMIT IS 15000, and spacebar also counts"
    print "                                        ||||||||| PEN IS MIGHTIER THAN THE SWORD ||||||||||\n\n"
    remainder=15000 
    cont=""
    inter=""
    l=[]
    print "Start Typing now"
    while inter!="-END-" and remainder>0:
        length=len(cont)
        remainder=remainder-length
        print "You have ",remainder," Characters left"
        
        inter=raw_input("--> ")
        l=inter.split()
        for i in l:
            x=moderator(i)
            cont=cont+" "+x
        cont=cont+"\n"
        

    title=raw_input("So, what's gonna be the Title of your Quote? ")

    
    new_post=post(cont,title,user)
    new_post.update_n()
    


        
        
        
        
        
        
        
