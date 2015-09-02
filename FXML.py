# This will be used to transfer an admin's xml to all EXISTING home folders. 
# The Assumption is made that an adminstrator has gone through and connected
# the master to one 'perfect' VirtualBox.xml file.

# $ python3.4 /AdminHome/.VirtualBox /RootUserFolderPath/
# User1@CSLab:~$ pwd
# /RootUserFolderPath/user1
# -> ls /RootUserFolderPath
# user1 user2 user3 <-
 
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys # .argv
import os # {Unix Only} .chmod(filename, 0o000),  .chown(file, ownerid, groupid)
from shutil import copy2

# Returns all users absolute paths to their VirtualBox.xml
def all_users(users_folders):
    """(str) -> list of strs

    Takes root directories where all user folders are generated to pull
    pull down the exact path of their VirtualBox.xml

    If for any reason there is no VirtualBox.xml to replace an error statement
    will be printed. If there is no .VirtualBox folder inside the users folders
    an error will be raised and the program will close down."""

    all_folders = os.listdir(users_folders)
    real_folders = []
    for folder in all_folders:
        if not folder[0] == '.':
            


# Does the .bak and the copy procedures
def fxml(admin_xml, users, check=False):
    """(str, list of strs) -> Bool"""
    pass


# For Troubleshooting and feeding data
def main(arguments):
    """(list of strings) -> None"""
    if len(arguments) == 3 and arguments[2].lower() == 'check':
        vbox_folders = all_users(arguments[1])
        print('Operation Complete: {}'.format(fxml(arguments[0],
                                            vbox_folders, True))
    elif len(arguments) == 2:
        vbox_folders = all_users(arguments[1])
        print('Operation Complete: {}'.format(fxml(arguments[0],
                                            vbox_folders))
    else:
        print('Not Enough Arguments')
        print('-> Please read the README for help with this script!')
        return

if __name__ == '__main__':
    main(sys.argv)