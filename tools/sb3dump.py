import sys
import json
import zipfile
from rich import print


project_file = zipfile.ZipFile(sys.argv[1])
project_json = json.loads(project_file.read("project.json"))


blocks = project_json["targets"][1]["blocks"]

for block_id, block in blocks.items():
    print(
        f"{block_id!r}:" + "\n"
        f"      OPCODE: {block['opcode']!r}" + "\n"
        f"      INPUTS: {block['inputs']!r}" + "\n"
        f"      FIELDS: {block['fields']!r}" + "\n-----------"
    )
