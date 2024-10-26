
import inspect, traceback, pdb


def get_debugger_func(func):
    def new_func(*args):
        try:
            return func(*args)
        except:
            traceback.print_exc()
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


if __name__ == "__main__":
    e = Example()
    print(e.divide(0))

    print("-"*80)
    print(e.interpolate('Chi', 'very', 'cool'))

