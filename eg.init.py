#initiate seccurity
 
import pickle
x=open("database.dat","ab")
sample=["12345","23141","Uddeshya","afO223o34"]
pickle.dump(sample,x)
x.close()
