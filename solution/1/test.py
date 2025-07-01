
from obj import (
    make, call,
    Square, Rectangle
)

examples = [make(Square, "sq", 3), make(Rectangle, "rect", 3, 4)]
for ex in examples:
    n = ex["name"]
    d = call(ex, "density", 5)
    print(f"{n}: {d:.2f}")

