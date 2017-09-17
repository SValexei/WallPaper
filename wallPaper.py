#!/usr/bin/python

import json, random, subprocess

jsonList = []
randomId = random.randint(0, 1000)

with open('/home/alexei/Scripts/WallPaper/list') as json_data:
    jsonList = json.load(json_data)

imageUrl = jsonList[randomId].get('post_url')

subprocess.run("wget -O /home/alexei/Scripts/WallPaper/randomImage.jpg " + imageUrl +"/download?force=true", shell=True)
subprocess.run("feh --bg-scale /home/alexei/Scripts/WallPaper/randomImage.jpg", shell=True)
