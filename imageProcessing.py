#!/usr/bin/env python3

import os
from PIL import Image

src_dir = "images/"
new_dir = "/opt/icons/"
imgfiles = [x for x in os.listdir(src_dir) if x.startswith("ic_")]
size = (128, 128)
angle = 270

for file in imgfiles:
    with Image.open(src_dir + file).convert("RGB") as img:
        img.thumbnail(size)
        img.rotate(angle).save(new_dir + file, "JPEG")

