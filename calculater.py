# calculater.py

def add(x, y):
    z=x+y
    print("{}+{}={}".format(x, y, z))
    return z
    
def sub(x, y):
    z=x-y
    print("{}-{}={}".format(x, y, z))
    return z
    
def mul(x, y):
    z=x*y
    print("{}*{}={}".format(x, y, z))
    return z

x = input ("Enter a letter:")
print ("You entered {}".format (x))
if x == "a":
    d = add(55, 60)
    if d>100:
        print("this number is too high.")
elif x == "s":
    c = sub(55, 60)
    if c<0:
        print("this number is too low")
elif x == "m":
    c=mul(2, 3)
    if c==6:
        print("this number is amazing")
else:
    print("The {} command is not recognized.".format(x))
print("done")