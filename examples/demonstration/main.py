from clearsoda import *

a = Var("a")
b = Var("b")

sprite = Sprite(
    name=__name__, costumes=["assets/scratchcat.svg"], variables=[a, b]
).WhenFlagClicked(
    a <= 0,
    Repeat(10) (
        SayFor(a, 0.24),
        a >= 1,
    )
)
