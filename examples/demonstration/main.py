from clearsoda import *

Self = Sprite(
    name=__name__,
    costumes=["assets/blank.svg"],
)

variable = Self.Var("variable")

Self.WhenFlagClicked(
    If (variable) (
        Say("True"),
    )
    .Else (
        Say("False"),
    )
)
