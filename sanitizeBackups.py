#!/usr/bin/python

import filecmp

## Create empty lists

flagDelete = []
flagPreserve = []

## CM This is raw code and needs to be better presented for final version.
print ""
print ""

with open('cmtsConfigList.txt.development') as f:                                   ## Read backup file names
        backupList = f.read().splitlines()
        print backupList

listLength = len(backupList)                                            ## How many files in the list
print "listLength: ", listLength
mainFile = backupList[0]                                                ## This is our starting point, the first item in the list

print ""
print "Main file: ", mainFile

## We need to start an iteration of the list starting at 2nd item, because the first item is our starting point

for backupFile in backupList[1:]:                                       ## We start the for at the second item in the list. Python starts counting at zero
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

