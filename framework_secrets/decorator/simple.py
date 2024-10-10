
#####################
# SIMPLE DECORATORS #
#####################

def decorator(func):
    print("name: ", func.__name__)
    print("# arguments: ", func.__code__.co_argcount)
    print("_"*50)
    return func


@decorator
def func1(a,b,c):
    print(a, b, c)


@decorator
def func2(w, x, y, z):
    print(w, x, y, z)

# func1 = decorator(func1)
# func2 = decorator(func2)


#############################
# DECORATORS THAT TRANSFORM #
#############################

import time

def transform_decorator(func):
    def inner(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print(f"It took {end-start} seconds")
        return res
    return inner

@transform_decorator
def sum_of_range(start, stop, step):
    return sum([i for i in range(start, stop, step)])

# sum_of_range = transform_decorator(sum_of_range)
print(sum_of_range(345, 999999, 3))


#####################
# DECORATOR METHODS #
#####################

class Template:
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        def inner(*args):
            return self.message % func(*args)
        return inner


@Template("%s your %s belong to %s")
def qog(quantity, obj, group):
    return quantity, obj, group

# qog = Template("%s your %s belong to %s")(qog)
print(qog("All", "base", "us"))


#####################################
# DECORATORS THAT RETURN DECORATORS #
#####################################

def template(message):
    def decorator(func):
        def inner(*args):
            return message % func(*args)
        return inner
    return decorator

@template("%s your %s belong to %s")
def qog2(quantity, obj, group):
    return quantity, obj, group

# qog2 = template("%s your %s belong to %s")(qog2)
print(qog2("All", "base", "us"))


################################
# APPLYING MULTIPLE DECORATORS #
#     (STACKING DECORATORS)    #
################################

def decorator1(func):
    print("Inside 1")
    return func


def decorator2(func):
    print("Inside 2")
    return func

@decorator1
@decorator2
def multiple(a, b, c):
    return a, b, c

# multiple = decorator1(decorator2(multiple))
print(multiple("All", "base", "us"))

