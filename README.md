# Virtual Box Manage Utilities
## Things To Understand
 - VirtualBox by Oracle has an extremely powerful command line utility called VBoxManage. the only unfortunate part is that their documentation, while it does include everything you'd need for full control of the virtual machines, does not, however, have any sort of "setup" like instruction. Start -> Finish.
 -The things inside this git repository will be for fixing VMs, Building VMs, and Some small network tools with manage several VMs through Ansible. More documentation to come!

## Ansible Commands TODOs (Completed Commands will be marked)
 - VBoxManage list vms
 - vboxmanage showvminfo *
 - vboxmanage storagattach --storagectrl * --port * --device * --type * --*
  - This will be broken into several commands
    - Adding Media
    - Removing Media
    - Adjusting Properties like setting drives as empty
    - Misc
 - vboxmanage closemedium *
 - vboxmanage modifyvm * --* 
  - It is woth noting that this is a VERY large list and will not be fully implemented unless I have the free time. A LOT of free time. I will for sure, try to hit a lot o the main ones like ram, vram, cpu#, and some other standards that you can easily access through the gui.
 - vboxmanage registervm/unregistervm *

## Other Files
 - FXML.py will be used for changing a user's xml file if for whatever reason you would need to do that without using the command line. The exact implementation of what it will do / can do is up in the air but a rough list:
  - Will be able to take a line of 'Correct XML' and replace the 'Incorrect XML' inside of a VirtualBox.xml file (NOT THE .VBOX YOU MONSTER)
  - If you're operating with a 'master' admin xml and want to juse overwrite other users' xmls to be in line with the 'master' this should be the file you're looking to use
 - VirtualBoxCheck.sh will be used for people who use /etc/skel/ or /etc/.profile.d to build their virutalbox with some init. If for some reason you have virtualbox-init file generate your .vbox files this shell script can be changed (where commented) to delete the old .vbox folder, NOT THE VDI, and either:
  1. Run a shell .vbox creation script
  2. Run a series of vboxmanage commands for creating a .vbox

