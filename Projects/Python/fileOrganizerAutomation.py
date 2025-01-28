# WIP 

# File Organizer Automation 
# Python program 

# Program that automates the organization of messy files in a selected folder
# The program uses a list of extensions as reference to complete the organization and the list can be updated to include more
# extensions. 

# Program creates new folders if the target folder to move the file to doesn't exist 
# If the folder does exist then it just moves the file to the target folder to move to 

# The program only moves files within the same folder / only works within the same directory 
# Future scope - make it move files to other directories 


# Library that will allow the program to use operating system functions (access files and directories in our case)
import os 

# Library that will allow the program to use file movement 
import shutil 

# We're creating a variable called directory and assigning it a path
# In this case the path that's being assigned is the folder we want to organize 
# expanduser helps us not have to type in the full path, it does it for you as long as you give it the target folder 
directory = os.path.join(os.path.expanduser("~"), "Downloads")

# Defining the extensions we want the program to target and what folders they should be moved to 
# "targetExtensionInSelectedFolder": "targetFolderToMoveFileTo"
extensions = { 
    # Testing 
    ".txt": os.path.join(os.path.expanduser("~"), "Documents"),

    # ".jpg": "Images", 
    # ".png": "Images", 
    # ".gif": "Images", 
    # ".mp4": "Videos", 
    # ".avi": "Videos", 
    # ".doc": "Documents", 
    # ".pdf": "Documents",
    # ".pptx": "Documents", 
    # ".xlxs": "Documents",
    # ".txt": "Documents", 
    # ".zip": "Documents",
    # ".mp3": "Music", 
    # ".wav": "Music", 
}

# Looping through the file names in the directory that we selected 
for filename in os.listdir(directory): 

    # Define the file path
    # Which is going to be the directory and then the file name 
    file_path = os.path.join(directory, filename)

    # Making sure what's being selected is a file and not a directory 
    if os.path.isfile(file_path): 

        # We split the filename out into the variable extension 
        # .lower() to make everything lowercase (to make sure we don't miss anything because of naming conventions)
        extension = os.path.splitext(filename) [1].lower()

        # If this extension is in our list of extensions 
        if extension in extensions: 

            # 
            folder_name = extensions[extension]

            # Folder path that will join the directory and the folder name 
            folder_path = os.path.join(directory, folder_name)

            # Making a new directory with the folder_path and if it exists make it true 
            os.makedirs(folder_path, exist_ok=True)

            # 
            destination_path = os.path.join(folder_path, filename)

            # Moving the current file_path to the destination_path 
            shutil.move(file_path, destination_path)

            # Notifying the user that a file has been moved and notifying them of the location it was moved to
            print(f"Moved {filename} to {folder_name} folder.")

        # 
        else: 

            # Notifying the user that a file was skipped because the extension was not in the list available 
            # for the program to handle 
            print(f"Skipped {filename}. File extension hasn't been added to list for organizing.")

    # 
    else:

        # Notifying user that a folder/directory was skipped 
        print(f"Skipped {filename}. It's a folder/directory.") 

# Notifying user that the organization is complete 
print("File organization completed!")