from clearsoda import *

sprite = Sprite(name=__name__, costumes=["assets/scratchcat.svg"]).WhenFlagClicked(
    *flatten(
        [
            [
                SayFor(f"{i} bottles of beer on the wall, {i} bottles of beer.", 0.5),
                SayFor(
                    f"Take one down and pass it around, {i-1} bottles of beer on the wall.",
                    0.5,
                ),
            ]
            for i in range(99, 1, -1)
        ]
    ),
    SayFor("1 bottle of beer on the wall, 1 bottle of beer.", 0.5),
    SayFor("Take one down and pass it around, No bottles of beer on the wall.", 0.5),
)
