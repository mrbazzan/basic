
import inspect, traceback, sys, pdb


def get_debugger_func(func):
    def new_func(*args):
       try:
           return func(*args)
       except Exception as e:
           traceback.print_exc()
           print("-"*80)
           pdb.post_mortem(sys.exc_info()[2])
    return new_func


class __debugger__(type):
    def __new__(meta, classname, bases, class_dict):
        for attr_name, attr in class_dict.items():
            if inspect.isfunction(attr):
                class_dict[attr_name] = get_debugger_func(attr)
        return super().__new__(meta, classname, bases, class_dict)


class Example(metaclass=__debugger__):
    def divide(self, v):
        result = 100/v
        return result

    def interpolate(self, *args):
        result = "%s is %s" % args
        return result


e = Example()
print(e.divide(10))
print(e.divide(0))  # enters debugger

