
from obj import (
    make, call,
    Square, Rectangle
)

sq = make(Square, "sq", 3)
rect = make(Rectangle, "rect", 3, 4)
for ex in sq, rect:
    n = ex["name"]
    p = call(ex, "perimeter")
    d = call(ex, "density", 5)
    print(f"{n}: {d:.2f} {p}")

print("Piece on B2", call(sq, "content", content="b2"))
