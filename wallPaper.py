#!/usr/bin/python

import json, random, subprocess
from pathlib import Path

jsonList = []
randomId = random.randint(0, 1000)
home = str(Path.home())

with open(home +'/Scripts/WallPaper/list') as json_data:
    jsonList = json.load(json_data)

imageUrl = jsonList[randomId].get('post_url')

subprocess.run("wget -O " + home + "/Scripts/WallPaper/randomImage.jpg " + imageUrl +"/download?force=true", shell=True)
subprocess.run("feh --bg-scale " + home + "/Scripts/WallPaper/randomImage.jpg", shell=True)
