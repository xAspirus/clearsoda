import json
import zipfile

from .helpers import *


class Sprite:
    def __init__(
        self,
        name: str,
        variables: list[str] = [],
        lists: list[str] = [],
        costumes: list[str] = [],
        sounds: list[str] = [],
    ):
        self.name: str = name
        self.variables: list[str] = variables
        self.lists: list[str] = lists
        self.costumes: list[str] = costumes
        self.sounds: list[str] = sounds
        self.code: list = []

    def Code(self, *code):
        self.code: list = code
        return self

    def serialize_costumes(self):
        return [
            {
                "assetId": md5ext(costume),
                "name": filename_from_path(costume),
                "md5ext": md5ext(costume) + "." + extension_from_path(costume),
                "dataFormat": extension_from_path(costume),
            }
            for costume in self.costumes
        ]

    def serialize_blocks(self):
        return {
            i["id"]: {a: b for a, b in i.items() if a != "id"}
            for i in flatten([x.serialize() for x in self.code])
        }

    def serialize_variables(self):
        return {var: [var, 0] for var in self.variables}

    def serialize_lists(self):
        return {var: [var, []] for var in self.lists}

    def serialize_sounds(self):
        return []  # TODO
        return [
            {
                "assetId": md5ext(sound),
                "name": filename_from_path(sound),
                "dataFormat": extension_from_path(sound),
                "rate": 48000,
                "sampleCount": 61300,
                "md5ext": md5ext(sound) + "." + extension_from_path(sound),
            }
            for sound in self.sounds
        ]

    def serialize(self):
        return {
            "isStage": self.name == "Stage",
            "name": self.name,
            "variables": self.serialize_variables(),
            "lists": self.serialize_lists(),
            "blocks": self.serialize_blocks(),
            "costumes": self.serialize_costumes(),
            "sounds": self.serialize_sounds(),
        }


class Project:
    def __init__(self, sprites: list[Sprite]):
        if len(sprites) < 1 or sprites[0].name != "Stage":
            raise Exception("First sprite must be Stage.")
        self.sprites: list[Sprite] = sprites

    def serialize(self):
        return {
            "targets": [sprite.serialize() for sprite in self.sprites],
            "extensions": [],
            "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": ""},
        }

    def export(self, output_path: str):
        sb3 = zipfile.ZipFile(output_path, "w")
        costumes = flatten([sprite.costumes for sprite in self.sprites])
        for costume in costumes:
            sb3.write(
                costume, arcname=md5ext(costume) + "." + extension_from_path(costume)
            )
        sb3.writestr("project.json", json.dumps(self.serialize()))
        return self
