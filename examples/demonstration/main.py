from clearsoda import *

sprite = Sprite(name=__name__, costumes=["assets/scratchcat.svg"]).Code(
    WhenFlagClicked(
        Say("Hello, World!"),
    )
)
