#def outer_function():
#    print("I'm Outer")

#    def nested_function():
#        print("I'm Inner") 

#    return nested_function

#inner_function = outer_function()
#inner_function()


## Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function() #run twice for eg, say_hello() below twice
    return wrapper_function

#what if i want to delay
@delay_decorator
def say_hello():
    #tim.sleep(2)
    print("Hello")

#what if i want to delay
@delay_decorator
def say_bye():
    #time.sleep(2)
    print("Bye")

def say_greeting():
    print("Yo how are you")

say_bye()
say_greeting()

# a decorator func is simply a function which wraps another function and give some functionality 
#@ = syntatic sugar
#instead of @ we can use

decorated_function = delay_decorator(say_greeting)
decorated_function()
