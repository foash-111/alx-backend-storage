#!/usr/bin/env python3

# def f1():
#     print("call f1 and execute what inside it")

# print(f1)

# def f2(f):
#     f()

# f2(f1)

##################################################

def f3(f):
    def wrapper():
        print('started')
        f()
        print('ended')
    return wrapper

# # it's like if we want to do the same thing every time but there is something different inside it, this thing which we will call.


# def f():
#     print('hello')

# f3(f) # without anthor () like if we returns wrapper as object and we want to add anthor () like we call what's returns and call it as a function again not as a objet so:
# f3(f)()

# x = f3(f)
# x() # like if we call what's f3 retuens, like if wee call wrapper()


##################################33


# decorator

# @f3
# def fsmall():
#     print('hello world')


# # every time we call fsmall() as we pass fsmall as a parameter to f1 
# fsmall()


######################################3

import datetime

def calc(func):
    # to make it more dynamic and recive any number of parameters
    def wrapper(*args, **kwargs): 
        print("hello today is ", datetime.datetime.now())
        val = func(*args, **kwargs)
        print("have a nice day")
        return val
    return wrapper




@calc
def law(salary = 0):
    print('i am a lawyer')
    return salary + (salary * .15)

@calc
def counting(salary):
    print('i am a counter')
    return salary + (salary * .25)


net_salary = law(1000)
print('salary: ', net_salary)

print()

net_salary = counting(1000)
print('salary: ', net_salary)


#####################

class Oraganization:
        
    @calc
    def lawyer_salary(self, salary=0):
        print('i am a lawyer')
        return salary + (salary * .15)

    @calc
    def accounter_salary(self, salary):
        print('i am a counter')
        return salary + (salary * .25)

lawyer = Oraganization()

print(lawyer.lawyer_salary(1000))
