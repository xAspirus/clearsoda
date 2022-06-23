from .codeprimitives import *
from .motion import *
from .looks import *
from .sound import *


class WhenFlagClicked:
    def __init__(self, *stack):
        self.stack = StatementStack(stack)

    def serialize(self):
        return [
            {
                "id": str(id(self)),
                "opcode": "event_whenflagclicked",
                "next": str(id(self.stack.stack[0]))
                if len(self.stack.stack) > 0
                else None,
                "parent": None,
                "inputs": {},
                "fields": {},
                "shadow": False,
                "topLevel": True,
                "x": 0,
                "y": 0,
            },
            self.stack.serialize(str(id(self))),
        ]


class Broadcast(StatementBlock):
    def __init__(self, event: InputType):
        self.define("event_broadcast", inputs={"BROADCAST_INPUT": event})


class BroadcastAndWait(StatementBlock):
    def __init__(self, event: InputType):
        self.define("event_broadcastandwait", inputs={"BROADCAST_INPUT": event})


class Wait(StatementBlock):
    def __init__(self, time: InputType):
        self.define("control_wait", inputs={"DURATION": time})


class WaitUntil(StatementBlock):
    def __init__(self, condition: InputType):
        self.define("control_wait_until", inputs={"CONDITION": condition})


class CreateClone(StatementBlock):
    def __init__(self, sprite: InputType):
        self.define("control_create_clone_of", inputs={"CLONE_OPTION": sprite})


def CreateCloneOfSelf():
    return CreateClone("_myself_")


class DeleteThisClone(StatementBlock):
    def __init__(self):
        self.define("control_delete_this_clone")


class Stop(StatementBlock):
    def __init__(self, operation: str):
        self.define("control_stop", fields={"STOP_OPERATION": [operation, None]})


def StopAll():
    return Stop("all")


def StopThisScript():
    return Stop("this script")


def StopOtherScriptsInSprite():
    return Stop("other scripts in sprite")
