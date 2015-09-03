#!/bin/bash
if [ -d "${HOME}/VirtualBox\ VMs/windows-7" ]
	then
	echo VBoxManage showvminfo "windows-7"
	# VBoxManage unregistervm "windows-7"
else
	echo '-> Folder DNE'
	echo $HOME
fi
