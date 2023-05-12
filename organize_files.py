'''

This script organizes the files in a directory by file extension.

Usage:
   organize_files.py [--copy] [--directory directory_path]

The default is to move the files from the current directory into the new directories based on file type.

'''


import os, shutil
import sys


dir_names_dict = {".txt":"TEXT_FILES",".jpg":"JPEG_FILES",".py":"PYTHON_FILES"}

def file_walk(cur_dir):
    for folderName, subfolders, filenames in os.walk(cur_dir):
        for file in filenames:
            get_extension(file)

def get_extension(file):
    filename, file_ext = os.path.splitext(file)
    create_dir(file, file_ext)
    move_file(file, file_ext)

def create_dir(file, file_ext):
    if file != os.path.basename(__file__):
        if file_ext in dir_names_dict:
            check_folder = os.path.isdir(dir_names_dict[file_ext])

            if not check_folder:
                os.makedirs(dir_names_dict[file_ext])
def misc_file():
    '''Creates an OTHER_FILES directory for any file types not specified in the dir_names_dict dictionary'''
    check_misc_folder = os.path.isdir("OTHER_FILES")
    if not check_misc_folder:
        os.makedirs("OTHER_FILES")

def move_file(file, file_ext):
    if file != os.path.basename(__file__):
        if org_method == "copy":
            try:
                shutil.copy(file,dir_names_dict[file_ext])
            except:
                misc_file()
                shutil.copy(file,"OTHER_FILES")
        else:
            try:
                shutil.move(file,dir_names_dict[file_ext])
            except:
                misc_file()
                shutil.move(file,dir_names_dict[file_ext])
                
    


if __name__ == '__main__':
    the_directory = os.getcwd()
    org_method = "move"

    
    if "--copy" in sys.argv:
        org_method = "copy"

    if "--directory" in sys.argv:
        directory_index = sys.argv.index("--directory") + 1
        if directory_index < len(sys.argv):
            new_directory = sys.argv[directory_index]
            the_directory = f"{the_directory}\{new_directory}"

    try:
        os.chdir(the_directory)
    except:
        sys.stderr.write("Invalid directory path.\n")
        sys.exit(1)
        
    file_walk(the_directory)
    

    print("Finished")
