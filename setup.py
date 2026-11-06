#!/usr/bin/env python3
"""Mera Editor: ek baar chalao (python3 setup.py).
Flat files ke naam mein '__' folder ki jagah hai (app__src__server__index.ts -> app/src/server/index.ts).
Yeh script unhein sahi folders mein rakh deti hai. Dobara chalane se koi nuqsan nahi."""
import os, shutil
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
moved = 0
for name in sorted(os.listdir(here)):
    if name == os.path.basename(__file__) or "__" not in name or not os.path.isfile(name):
        continue
    dest = os.path.join(*name.split("__"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.move(name, dest)
    moved += 1
print(f"Done: {moved} files sahi folders mein rakh di gayi.")
print("Ab README.md ya SETUP_PROMPT.md ke mutabiq aage barhein.")
