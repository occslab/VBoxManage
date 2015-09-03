#!/bin/bash
if [ -d "${HOME}/VirtualBox VMs/windows-7" ]
    then
    VBoxManage showvminfo "windows-7"
    # VBoxManage unregistervm "windows-7"
    # rm -rf "${HOME}/VirtualBox VMs/windows-7"
    # Begin Building Your VM

else
    # Check to make sure your vm is built
    echo 'Checking for Current VM'
    if [ ! -d "${HOME}/VirtualBox VMs/VMNAMEHERE" ]
        then
        # Begin Build Your VM
    fi
fi
