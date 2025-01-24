spam = 42 #global variable

def eggs():
    spam = 53 #local variable

#variable can't be both local and global
#local var is created when a function is called an when the function returns,
    #it is destroyed and stops existing
#code in a global scope cannot use local variables
#code in local scope can use global vairbales
#code in one function's local scope cannot use vars in another local scope
#code in one function's local scope cannot use vars in any other local scope




def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0

spam()
######################

def spam():
    eggs = 99
    
    print(bacon())
    
def bacon():
    ham = 101
    eggs = 0
    return eggs

spam()

####################


def spam2():
    print(eggs)

eggs = 42

spam2()

###################

def spam3():
    eggs='Hello'
    print(eggs)

eggs =42
spam3()
print(eggs)


######### Assign new value to a global var from inside a function

def spam4():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
print(eggs)
spam4()
print(eggs)

