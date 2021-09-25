# decorators: 
import functools

# function decorators
# example of sytax
# @mydecorator
# def dosomething():
#     pass

### example 1 - using a decorator with no arguments
def start_end_decorator(func):
    def wrapper():
        print("print start")
        func()
        print("print end")
    return wrapper

@start_end_decorator
def print_name():
    print("alex")


# print_name = start_end_decorator(print_name) # not needed when making a decorator. extending function
print_name()

### example 2 - using a decorator with an argument
def deco_func(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("start")
        result = func(*args,**kwargs)
        print("end")
        return result
    return wrapper

@deco_func
def add_five(num):
    return num + 5

result = add_five(10)
print(result)

# print(help(add_five))
print(add_five.__name__)


### example 3 -  using decorator where the decorator has an argument
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"hello {name}")

greet("jack")

### example 4 - using multiple decorators on a function
def start_end_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("start")
        result = func(*args,*kwargs)
        print("ends")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        result = func(*args,**kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator2
def say_hello(name):
    greeting = f"hello {name}"
    print(greeting)
    return greeting

say_hello("jack")



######################################
# class decorators
## example 1
class CountCalls:
    def __init__(self,func) -> None:
        self.func = func
        self._num_calls = 0 # custom state
    def __call__(self, *args, **kwargs):
        self._num_calls += 1
        print(f"this is executed {self._num_calls} times")
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()

@CountCalls
def say_hi():
    print("hello")

say_hi()
say_hi()
