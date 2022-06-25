from clearsoda import *

from main import Self as main_sprite

stage = Sprite("Stage", costumes=["assets/blank.svg"])

Project(sprites=[stage, main_sprite]).export("demonstration.sb3", debug=True)
