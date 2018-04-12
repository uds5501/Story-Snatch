def success():
    print "DONE"

while True:
    try:
        x=int(raw_input("Enter a number "))
        success()
        
    except ValueError:
        print "Nopes"
        
