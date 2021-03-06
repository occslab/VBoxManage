import os
import sys
from shututil import copyfile

def replace(file_path, file_name, uni_home, cfolder=None):
    """(str, str, str, str) -> None

    Takes the file path of a plain text file, like a Icon.desktop file,
    and unified home folder link. This would be for users who don't use
    the standard /home/username/stuff architechture. The uni_home MUST
    be the ABSOLUTE path. No relative pathing will be and the program
    will exit out if the uni_home does not detect :/ or / as the first,
    appropriate, characters. 

    cfolder, is the folder of choice. If you wanted to replace old
    desktop icons you would drop in the unified user folder and then
    'Desktop' as the cfolder. The program would drop new file in every
    detected user's desktop.

    >>> replace('/home/user/', 'thing.txt', '/other/')
    >>> replace('C:/windows/users/user/', 'thing.txt', 'C:/windows/user/', 'dir')"""
    if cfolder == None:
        cfolder = ''
    if file_path[0] != '/' and file_path[1:3] != ':/':
        print('File Path: Incorrect')
        exit()
    uni_dirs = os.listdir(uni_home)
    for user in uni_dirs:
        if '.' != user[0]:
            item = user
            user += '/' + cfolder[1:]
            copyfile(file_path, '{}{}'.format(uni_home, user))
            if sound:
                print('Completed: {}'.format(item))

def gather():
    """() -> listdir

    Gathers command-line input and returns it. The format is appropriate
    for the replace function"""
    arguments = sys.argv[1:]
    if len(arguments) < 3:
        print('Error! Not Enough Arguments')
        exit()
    elif len(arguments) == 4:
        cfolder = arguments[3]
    else:
        cfolder = None
    file_path = arguments[0]
    file_name = arguments[1]
    uni_home = arguments[2]
    return [file_path, file_path, uni_home, cfolder]
if __name__ == '__main__'
    args = gather()
    replace(args[0], args[1], args[2], args[3])
