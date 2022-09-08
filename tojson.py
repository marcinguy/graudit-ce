#!/usr/bin/python
import sys
import re
import json
import pprint

def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)

my_file = open(sys.argv[1], 'r')
data = my_file.readlines()
outjson = []
val ={}
for line in data:
    out=line.split(":")
    if(len(out)==3):
      val["line"]=out[1]
      val["data"]=out[2]
      outjson.append(val)

print(json.dumps(outjson))

