#!/usr/bin/python
 
 
## usage listFiles.py <path>
 
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time, re

dirContents = []
cmtsList = []
 
# path to the directory (relative or absolute)
dirpath = sys.argv[1]  
cmts = sys.argv[2]
 
# get all entries in the directory w/ stats
entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
entries = ((os.stat(path), path) for path in entries)
 
# leave only regular files, insert creation date
entries = ((stat[ST_CTIME], path)
           for stat, path in entries if S_ISREG(stat[ST_MODE]))
#NOTE: on Windows `ST_CTIME` is a creation date
#  but on Unix it could be something else
#NOTE: use `ST_MTIME` to sort by a modification date
 
for cdate, path in sorted(entries):
    #print time.ctime(cdate), os.path.basename(path)
    entry = time.ctime(cdate), os.path.basename(path)
    entry = str(entry)
    dirContents.append(entry)                   ## Add the entry to dirContents
 
#print ("\n".join(dirContents))
 
## Search dirContents for cmts and print results:
regex=re.compile(".*({}).*".format(cmts))
result = [m.group(0) for l in dirContents for m in [regex.search(l)] if m]

## Iterate through the results and add to list cmtsList
for cmts in result:
	print cmts.split(" ")
