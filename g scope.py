#This function uses global variables
# name same as s
def f():
    s="Me too"
    print(s)
    
#Global scope
s= "I love programming in python"
f()
print(s)