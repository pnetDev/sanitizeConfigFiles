#!/bin/bash

sourceDir=/pnetBackup/tftpboot/CMTSs/today
destDir=/pnetBackup/tftpboot/CMTSs/forDeletion
 
while read configFile
        do
        #echo $configFile
        moveName=$(echo $configFile | awk -F '/' ' { print $6 } ')
        echo mv -p $configFile, $destDir/$moveName
        mv $configFile $destDir/$moveName
done < flagDelete.txt

