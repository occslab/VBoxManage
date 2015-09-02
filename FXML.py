# This will be used to transfer an admin's xml to all EXISTING home folders. 
# The Assumption is made that an adminstrator has gone through and connected
# the master to one 'perfect' VirtualBox.xml file.

# $ python3.4 /AdminHome/.VirtualBox/VirtualBox.xml /RootUserFolderPath/ groupid [check]
# User1@CSLab:~$ pwd
# /RootUserFolderPath/user1
# -> ls /RootUserFolderPath
# user1 user2 user3 <-
 
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys # .argv
import os # {Unix Only} .chmod(filename, 0o000),  .chown(file, ownerid, groupid), isfile(), 
from shutil import copy2

# Returns all users absolute paths to their VirtualBox.xml
def all_users(users_folders_loc):
    """(str) -> dict

    Takes root directories where all user folders are generated to pull
    pull down the exact path of their VirtualBox.xml

    If there is no .VirtualBox folder inside the users folders
    an error will be printed and the folder will be skipped for file drop

    This functions makes the assumption that you have all users collected 
    in one 'home' folder on a computer. If you do not, another function
    may appear in the future for your situation, until then stay strong."""

    all_folders = os.listdir(users_folders_loc)
    real_folders = {}
    for folder in all_folders:
        if not folder[0] == '.':
            current_user = '{}/{}'.format(users_folders_loc, folder)
            folder_contents = os.listdir(current_user)
            if '.VirtualBox' in folder_contents:
                abs_path = '{}/.VirtualBox'.format(current_user)
                if os.path.isdir(abs_path):
                    real_folders[folder] = abs_path
                else:
                    print('VirtualBox is not a folder?')
                    print('Skipping: {}'.format(folder))
            else:
                print('No VirtualBox folder found!')
                print('Skipping: {}'.format(folder))
    if len(real_folders) < 1:
        print('No Folders Were Detected . . . \n Exiting . . .')
        exit()
    return real_folders


# Does the .bak and the copy procedures
def fxml(admin_xml, users, groupid, check=False):
    """(str, list of strs, bool) -> Bool

    Takes the direct path to the admins VirtualBox.xml, a dictionary of users
    and their paths to the /user/.VirtualBox folder. the groupid all these users
    SHOULD AND WILL BE universally a part of. Then finally a 'check' boolean
    explained more in Problems.

    Problems:
    If for any reason there is no VirtualBox.xml to replace an error statement
    will be printed. If check is True, then the program will not place ANY
    XML files into the folder and instead will just exit out. For some, no
    VirtualBox.xml may indicate a problem with VirtualBox settings and will
    warrant different troubleshooting such as a different default machine folder
    problems. Therefore placing a new .xml at the location will create problems,
    or use unneeded cpu power and time."""
    if check:
        # User : .VBoxFolder
        for user in users:
            problem_folders = []
            user_path = users[user]
            if not os.path.isfile('{}/VirtualBox.xml'.format(user_path)):
                print('File DNE In: {}'.format(user_path))
                problem_folders.append(user_path)
        if len(problem_folders) > 0:
            exit()
    else:
        for user in users:
            xml_path = '{}/VirtualBox.xml'.format(users[user])
            if os.path.isfile(xml_path):
                os.rename(xml_path, '{}.bak'.format(xml_path))
            # Copy The 'Perfect' admin xml to the users folder
            copy2(admin_xml, xml_path)
            # Convert owner to something that dropbox loves
            os.chown(xml_path, user, groupid)



# For Troubleshooting and feeding data
def main(arguments):
    """(list of strings) -> None"""
    if len(arguments) == 4 and arguments[2].lower() == 'check':
        vbox_folders = all_users(arguments[1])
        print('Operation Complete: {}'.format(fxml(arguments[0],
                                    vbox_folders, arguments[2], check=True)))
    elif len(arguments) == 3:
        vbox_folders = all_users(arguments[1])
        print('Operation Complete: {}'.format(fxml(arguments[0],
                                            vbox_folders, arguments[2])))
    else:
        print('Not Enough Arguments')
        print('-> Please read the README for help with this script!')
        print(arguments)
        exit()

if __name__ == '__main__':
    main(sys.argv[1:])
