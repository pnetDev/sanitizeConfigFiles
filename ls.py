#!/usr/bin/python

from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time, re, filecmp

#Relative or absolute path to the directory
dir_path = '/pnetBackup/sanitiseProject/'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
        for stat, path in data if S_ISREG(stat[ST_MODE]))
for cdate, path in sorted(data):
        #print(time.ctime(cdate), os.path.basename(path))
        fileName = os.path.basename(path)
        print fileName

