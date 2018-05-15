#!/usr/bin/python
'''
## CM 10/05/18 Development notes.

This is how the Python code works:

The user runs the script and supplies the path and cmts name eg:
    ./sanitizeBackupsSysArgs.py /pnetBackup/tftpboot/CMTSs/today/ knock6-

The script generates a list ordered by date of all file names in the path.  dirList[ ]
The script iterates the dirList and searches for the CMTS name. 
Another list is generated fileNameList[ ] from the search results. This will be a list of config file names which match the supplied CMTS name. 
fileNameList[ ] iterated starting with the second item. backupFile
The first item mainFile becomes the file other files are compared to EG: 
1 compared with 2 - no difference, 2 added to flagDelete.
1 compared with 3 - no difference, 3 added to flagDelete.
1 compared  with 4 - 4 is different, 4 added to flagPreserve.
4 now becomes the file the rest of the files are compared with
4 is compared with 5 - no difference, 5  added to flagDelete
4 is compared with 6 - no difference, 6  added to flagDeleted
4 is compared with 7 - 7 is different, 7  added to flagPreserve.
This repeats until the CMTS name has been fully iterated.
List of flagDelete printed.
List of flagPreserve printed.


Log changes here:
CM 10/05/18 paths for compare files are now correct

'''

from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time, re, filecmp

# Define the lists
dirList = []
fileNameList = []
flagDelete = []
flagPreserve = []

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
cmts     = sys.argv[2] 

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    #print(time.ctime(cdate), os.path.basename(path))
    fileName = os.path.basename(path)
    #print fileName
    #fileName = str(fileName)
    dirList.append(fileName)

#print ("\n".join(dirList))

## Now we have the file names saved in the list dirList
## Next we search for cmts in the list using iteration

for fileName in dirList:
	if fileName.startswith(cmts):
		fileNameList.append(fileName)
		
#print ("\n".join(fileNameList))

###===================================================================##

# Sanitize the files:

## We need to start an iteration of the list starting at 2nd item, because the first item is our starting point
listLength = len(fileNameList)                                            ## How many files in the list
print "listLength: ", listLength
mainFile = fileNameList[0]                                                ## This is our starting point, the first item in the list

print ""
print "Main file: ", mainFile


for backupFile in fileNameList[1:]:                                       ## We start the for at the second item in the list. Python starts counting at zero
        #print backupFile
        #print "Now comparing ", mainFile, "with", backupFile
        compare = filecmp.cmp(mainFile, backupFile)                     ## This is the Python module for comparing files.
        print "Compare result", mainFile, "with", backupFile, compare
        if compare == True:
                print "\t", backupFile, "flagged for deletion"
                flagDelete.append(backupFile)
                print ""
        if compare == False:
                print "\t", backupFile, "is different to ", mainFile
                print "\t", backupFile, "will be preserved and has become the new file to compare to for remaining files"
                flagPreserve.append(backupFile)
                mainFile = backupFile
                print ""

print "-----------------------------------------------"
print "                 REPORT                        "
print "-----------------------------------------------"
print ""
print "For deletion"
print ("\n".join(flagDelete)) ## Prints each list item on seperate line
print ""
print "For preservation"
print ("\n".join(flagPreserve)) ## Print easch list item on seperate line
print ""



