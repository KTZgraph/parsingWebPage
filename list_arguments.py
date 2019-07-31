

def dekorator(func):
    def wrapper(args):
        for argument in [args,]:
            print(argument)
            func(argument)
    return wrapper


def multicall0(arglist):
    def decorator(func):
        def wrapped_function(*args):
            for arg in arglist:
                func(arg)
        return wrapped_function
    return decorator

@multicall0([[2,3,4435,5]])
def double(x):
    print(x*2)
    return x*2

# double([2,3,4435,5])

# @dekorator
# def double2(x):
#     print(x*2)
#     return x*2

# double2([2,3,4435,5])