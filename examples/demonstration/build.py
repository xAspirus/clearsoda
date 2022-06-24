import sys

sys.path.append("../..")

from clearsoda import *

from main import sprite as main_sprite

stage = Sprite("Stage", costumes=["assets/scratchcat.svg"])

Project(sprites=[stage, main_sprite]).export("demonstration.sb3")
