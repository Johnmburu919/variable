#This function modifies global variable "s"
def f():
    global s
    print(s)
    s="Look for Geeksforgeeks Python Section"
    print(s)
    
#Global scope
s= "Python is great!"
f()
print(s)