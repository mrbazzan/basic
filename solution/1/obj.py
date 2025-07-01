
def make(cls, *args):
    return cls["_new"](*args)

def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["parent"]
    raise NotImplementedError(f"{method_name} does not exist")

def call(thing, method_name, *args, **kwargs):
    method = find(thing["_class"], method_name)
    return method(thing, *args, **kwargs)

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

def square_new(name, side):
    # Inheritance trick
    return make(Shape, name) | {
        "side": side,
        "_class": Square,
    }

def shape_density(thing, weight):
    return weight / call(thing, "area")

def shape_new(name):
    return {
        "name": name,
        "_class": Shape,
    }

Shape = {
    "density": shape_density,
    "_new": shape_new,
    "parent": None,
    "_classname": "Shape",
}
Circle = Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_new": square_new,
    "parent": Shape,
    "_classname": "Square",
}
