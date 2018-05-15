#!/bin/bash
source /root/.bashrc
srcPath=/pnetBackup/tftpboot/CMTSs/today/
sanitize=/pnetBackup/sanitiseProject/sanitizeBackupsSysArgs.py
while read cmtsName
	do
	echo Processing $cmtsName
	fileName=$(echo $cmtsName-)
	$sanitize $srcPath $fileName
done < CMTSName.txt	
