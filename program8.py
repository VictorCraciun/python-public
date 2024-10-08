# To change the value of global variable inside function, refer to the variable by using the global keyword:
x = "Craciun"
def myfunc():
    global x
    x = "Victor"
    print("My name is " + x)

myfunc()

print("My name is " + x)