# calculater.py

def add(x, y): #add function
    z=x+y
    symbol = "+"
    return z, symbol #substract function
    
def sub(x, y):
    z=x-y
    symbol = "-"
    return z, symbol
    
def mul(x, y): #multiply function
    z=x*y
    symbol = "*"
    return z, symbol
    
def div(x, y): #divide function
        z=x/y
        symbol = "/"
        return z, symbol
    
def inp (): #input number
    a = input ()
    num = float(a)
    return num
    
def dis(w, x, y, z): #output answer
    print("{}{}{}={}".format(w, x, y, z))
    return
    



#main
print("<number1 symbol number2>") #enter first number
print("Please enter your number1:")
a=inp()
print("Please enter your number2:") #enter second number
b=inp()
print("Please choose your option by number:" ) #choose option
print("1. add   2. substract    3. multiply   4. divide")
o=inp()
if o == 1: #calculate
    ans,sym = add(a, b)
    dis(a, sym, b, ans)
elif o == 2:
    ans,sym = sub(a, b)
    dis(a, sym, b, ans)
elif o == 3:
    ans, sym = mul(a, b)
    dis(a, sym, b, ans)
elif o == 4:
    if b==0:
        print("divisor can't be 0")
    else:
        ans,sym = div(a, b)
        dis(a, sym, b, ans)
else:
    print ("you entered a wrong number")
print("Done")