#!/bin/bash
$oldVMNAME = "windows-7"
$newVMNAME
if [ -d "${HOME}/VirtualBox VMs/${oldVMNAME}-7" ]
    then
    VBoxManage showvminfo $oldVMNAME
    # VBoxManage unregistervm "windows-7"
    # rm -rf "${HOME}/VirtualBox VMs/windows-7"
    # Begin Building Your VM

else
    # Check to make sure your vm is built
    echo 'Checking for Current VM'
    if [ ! -d "${HOME}/VirtualBox VMs/${newVMNAME}" ]
        then
        # Begin Building Your VM
    fi
fi
