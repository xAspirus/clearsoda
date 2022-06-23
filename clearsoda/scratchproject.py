import zipfile
import json
from .helpers import *


class Project:
    def __init__(self, output_path: str):
        self.output_path: str = output_path
        self.assets: list[str]

    def serialize(self):
        return project(
            {
                i["id"]: {a: b for a, b in i.items() if a != "id"}
                for i in flatten(self.code.serialize())
            }
        )

    def build(self):
        sb3 = zipfile.ZipFile(self.output_path, "w")
        sb3.writestr("project.json", json.dumps(self.serialize()))
