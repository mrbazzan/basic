
def merge(seqs):
    res = []
    while True:
        nonempty = [seq for seq in seqs if seq]
        if not nonempty: return res

        for seq in nonempty:
            cand = seq[0]
            nothead = [seq for seq in nonempty if cand in seq[1:]]

            if nothead: cand = None
            else: break

        if not cand: raise "Error"
        res.append(cand)

        # remove good head
        for seq in nonempty:
            if seq[0] == cand: del seq[0]

def cls_mro(cls: tuple|None):
    bases = []
    if cls["parent"] is not None:
        for klass in cls["parent"]:
            bases.append(klass)

    # c3 algorithm
    return merge([[cls]] + list(map(cls_mro, bases)) + [bases])

def make(cls, *args):
    return cls["_new"](*args)

def find(cls, method_name):
    mro = cls["_mro"](cls)
    for klass in mro:
        if method_name in klass:
            return klass[method_name]
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

#TODO: Prime to be converted to static method
def piece_content(thing, content=""):
    if content in ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]:
        return "pawn"
    return "not sure"

def piece_new(thing):
    pass

Shape = {
    "density": shape_density,
    "_mro": cls_mro,
    "_new": shape_new,
    "parent": None,
    "_classname": "Shape",
}

Piece = {
    "content": piece_content,
    "_mro": cls_mro,
    "_new": piece_new,
    "parent": (Shape,),
    "_classname": "Piece",
}

Rectangle = {
    "area": rect_area,
    "perimeter": rect_perimeter,
    "_mro": cls_mro,
    "_new": rect_new,
    "parent": (Shape,),
    "_classname": "Rectangle",
}

Square = {
    "_new": square_new,
    "_mro": cls_mro,
    "parent": (Rectangle, Piece),
    "_classname": "Square",
}
