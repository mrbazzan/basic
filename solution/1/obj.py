
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

def square_new(name, side):
    # Inheritance trick
    return make(Rectangle, name, side, side) | {
        "_class": Square,
    }

def shape_density(thing, weight):
    return weight / call(thing, "area")

def shape_new(name):
    return {
        "name": name,
        "_class": Shape,
    }

def rect_perimeter(thing):
    return 2 * (thing['side_a'] + thing['side_b'])

def rect_area(thing):
    return thing['side_a'] * thing['side_b']

def rect_new(name, side_a, side_b):
    return make(Shape, name) | {
        "side_a": side_a,
        "side_b": side_b,
        "_class": Rectangle,
    }

Shape = {
    "density": shape_density,
    "_new": shape_new,
    "parent": None,
    "_classname": "Shape",
}

Rectangle = {
    "area": rect_area,
    "perimeter": rect_perimeter,
    "_new": rect_new,
    "parent": Shape,
    "_classname": "Rectangle",
}

Square = {
    "_new": square_new,
    "parent": Rectangle,
    "_classname": "Square",
}
