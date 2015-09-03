#!/bin/bash
if [ -f "$HOME/Virtual\ VMs/windows-7"]
	then
	echo VBoxManage showvminfo "windows-7"
	# VBoxManage unregistervm "windows-7"
fi
