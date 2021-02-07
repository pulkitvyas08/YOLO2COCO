import sys
import os

directory = sys.argv[1]

files = []
import pathlib
for filepath in pathlib.Path(directory).glob('**/*'):
    ext = os.path.splitext(filepath)[1]
    if ext == '.jpg' or ext == '.jpeg':
        files.append(filepath.absolute())

resFile = os.path.basename(os.path.normpath(directory))
resFile += ".txt"

with open(resFile, 'w') as f:
    for item in files:
        f.write("%s\n" % item)
