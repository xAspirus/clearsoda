from clearsoda import *

Self = Sprite(
    name=__name__,
    costumes=["assets/blank.svg"],
)

my_function = Self.Def(
    Func(Arg.arg1, Arg.arg2, Arg.arg3)(
        Say(Arg.arg1),
        Say(Arg.arg2),
        Say(Arg.arg3),
    )
)

Self.WhenFlagClicked(
    Say("Hello, World!"),
    my_function(1, 2, 3),
)
