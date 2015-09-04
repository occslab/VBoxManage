#!/bin/bash
oldVMNAME="windows-7"
newVMNAME="fall2015"
initpath="./virtualbox-init"
if [ -d "${HOME}/VirtualBox VMs/${oldVMNAME}" ]
    then
    VBoxManage showvminfo $oldVMNAME
    VBoxManage unregistervm "${oldVMName}" --delete
    # rm -rf "${HOME}/VirtualBox VMs/windows-7"
    # Begin Building Your VM
    $initpath
else
    # Check to make sure your vm is built
    echo 'Checking for Current VM'
    if [ ! -d "${HOME}/VirtualBox VMs/${newVMNAME}" ]
        then
        # Begin Building Your VM
        $initpath
    fi
fi
