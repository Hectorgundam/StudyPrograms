
# File Organizer
# Python Program 

# Program that automates the organization of messy files in the Downloads folder
# The program has a list of extensions that it works on and more can be added as desired 

# The program uses a folder called SortedFiles inside the Downloads folder as the folder where it moves the sorted files 
# If the folder doesn't exist, a new one will be created

# SortedFiles folder structure is as follows 
# SortedDocuments - For files with extensions: txt, doc, docx, pdf, pptx, xlsx 
# SortedAudio - For files with extensions: mp3, wav, flac
# SortedVideo - For files with extensions: mp4, avi, flac
# SortedFiles - For files with extensions: zip, rar, tar, exe, dmg
# SortedOther - For any other files that don't match the previous ones 

# Additional file types can be added to the dictionary as needed 


# Library - allows the use of operating system functions (access files and directories in our case)
import os
# Library - allows files movement 
import shutil
# Library - allows the use of current date and time functions
import datetime

# Define base directory (Downloads)
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Define the main sorting directory inside Downloads
sorted_base_dir = os.path.join(downloads_dir, "SortedFiles")

# Define subfolders for different file types
sorted_folders = {
    "Documents": os.path.join(sorted_base_dir, "SortedDocuments"),
    "Images": os.path.join(sorted_base_dir, "SortedDocuments"),
    "Audio": os.path.join(sorted_base_dir, "SortedAudio"),
    "Video": os.path.join(sorted_base_dir, "SortedVideo"),
    "Files": os.path.join(sorted_base_dir, "SortedFiles"),  # For archives, executables, etc.
    "Other": os.path.join(sorted_base_dir, "SortedOther"),  # For unknown file types
    "Folders": os.path.join(sorted_base_dir, "SortedFolders") # For folders
}

# Ensure all sorting folders exist
for folder in sorted_folders.values():
    os.makedirs(folder, exist_ok=True)

# Define file type categories and their destination folders
extensions = {

    # Document file extensions
    ".txt": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents",

    # Image file extensions
    ".jpeg": "Images",
    ".png": "Images",
    ".svg": "Images",
    ".webp": "Images",

    # Audio file extensions
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",

    # Video file extensions
    ".mp4": "Video",
    ".avi": "Video",
    ".mov": "Video",

    # Files (Archives, executables) file extensions
    ".zip": "Files",
    ".rar": "Files",
    ".tar": "Files",
    ".exe": "Files",
    ".dmg": "Files",
}

# Function to handle duplicate files
def get_unique_filename(destination_path):
    """Ensures the file/folder name is unique before moving by appending a number."""
    if not os.path.exists(destination_path):
        return destination_path

    base, extension = os.path.splitext(destination_path)
    counter = 1

    while os.path.exists(destination_path):
        destination_path = f"{base}({counter}){extension}"
        counter += 1

    return destination_path

# Log file path
log_file_path = os.path.join(sorted_base_dir, "file_organizer_log.txt")

# Open log file for writing
with open(log_file_path, "w") as log_file:
    log_file.write(f"File Organizer Log - {datetime.datetime.now()}\n")
    log_file.write("=" * 50 + "\n")

    # Loop through items in the Downloads folder
    for filename in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, filename)

        # Skip the main SortedFiles directory to prevent moving itself
        if filename == "SortedFiles":
            continue

        # Determine target folder (based on extension for files, or "Folders" for directories)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            target_folder = sorted_folders.get(extensions.get(extension, "Other"))
        else:  # If it's a folder, move it to SortedFolders
            target_folder = sorted_folders["Folders"]

        # Define the destination path
        destination_path = os.path.join(target_folder, filename)

        # Ensure the file/folder name is unique before moving
        unique_destination_path = get_unique_filename(destination_path)

        # Move the file/folder
        shutil.move(file_path, unique_destination_path)

        # Log the action
        log_file.write(f"Moved: {filename} -> {unique_destination_path}\n")

    log_file.write("=" * 50 + "\n")
    log_file.write("File organization completed!\n")

# Notify the user
print(f"File organization completed! Log saved to {log_file_path}")

# Open the log file
if os.name == "nt":  # Windows
    os.startfile(log_file_path)
elif os.name == "posix":  # macOS or Linux
    os.system(f"open '{log_file_path}'")
else:
    print(f"Please open the log file manually: {log_file_path}")