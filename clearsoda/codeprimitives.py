from typing import Union


def serialize_block_inputs(inputs):
    ret = {}
    for input_name, input_value in inputs.items():
        if isinstance(input_value, ReporterBlock):
            ret[input_name] = [3, str(id(input_value))]
        elif isinstance(input_value, StatementStack):
            ret[input_name] = [2, str(id(input_value.stack[0]))]
        elif isinstance(input_value, Var):
            ret[input_name] = [3, [12, input_value.name, input_value.name]]
        elif isinstance(input_value, (str, int, float, bool)):
            ret[input_name] = [1, [10, str(input_value)]]
    return ret


class Block:
    def define(self, opcode, inputs={}, fields={}):
        self.opcode = opcode
        self.inputs = inputs
        self.fields = fields


class StatementStack:
    def __init__(self, stack):
        self.stack = stack

    def serialize(self, parent_id):
        ret = []

        for i, code in enumerate(self.stack):
            if i == 0:
                ret.append(
                    self.stack[0].serialize(
                        str(id(self.stack[1])) if len(self.stack) > 1 else None,
                        parent_id,
                    )
                )
                continue
            if i == len(self.stack) - 1:
                ret.append(self.stack[-1].serialize(None, str(id(self.stack[-2]))))
                continue
            ret.append(
                code.serialize(str(id(self.stack[i + 1])), str(id(self.stack[i - 1])))
            )

        return ret


class StatementBlock(Block):
    def serialize(self, next_id, parent_id):
        return [
            {
                "id": str(id(self)),
                "opcode": self.opcode,
                "next": next_id,
                "parent": parent_id,
                "inputs": serialize_block_inputs(self.inputs),
                "fields": self.fields,
                "shadow": False,
                "topLevel": False,
            },
            [
                i.serialize(str(id(self)))
                for i in self.inputs.values()
                if isinstance(i, (ReporterBlock, StatementStack))
            ],
        ]


class ReporterBlock(Block):
    def serialize(self, parent_id):
        return [
            {
                "id": str(id(self)),
                "opcode": self.opcode,
                "next": None,
                "parent": parent_id,
                "inputs": serialize_block_inputs(self.inputs),
                "fields": self.fields,
                "shadow": False,
                "topLevel": False,
            },
            [
                i.serialize(str(id(self)))
                for i in self.inputs.values()
                if isinstance(i, ReporterBlock)
            ],
        ]


InputType = Union[ReporterBlock, "Var", str, int, float, bool]


class SetVariable(StatementBlock):
    def __init__(self, variable: str, value: InputType):
        self.define(
            "data_setvariableto",
            inputs={"VALUE": value},
            fields={"VARIABLE": [variable, variable]},
        )


class ChangeVariable(StatementBlock):
    def __init__(self, variable: str, change: InputType):
        self.define(
            "data_changevariableby",
            inputs={"VALUE": change},
            fields={"VARIABLE": [variable, variable]},
        )


class ShowVariable(StatementBlock):
    def __init__(self, variable: str):
        self.define(
            "data_showvariable",
            fields={"VARIABLE": [variable, variable]},
        )


class HideVariable(StatementBlock):
    def __init__(self, variable: str):
        self.define(
            "data_hidevariable",
            fields={"VARIABLE": [variable, variable]},
        )


class Var:
    def __init__(self, name: str):
        self.name: str = name

    def change(self, change: InputType):
        return ChangeVariable(self.name, change)

    def set(self, value: InputType):
        return SetVariable(self.name, value)

    def show(self):
        return ShowVariable(self.name)

    def hide(self):
        return HideVariable(self.name)

    def serialize(self, parent_id):
        return []
