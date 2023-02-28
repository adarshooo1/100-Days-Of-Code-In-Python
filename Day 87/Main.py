import shutil

import os

# Example 1
# shutil.copy("file_Name", "New-File_Name") with this we can copy one file and make a new file with the new name and the same content in both the file.
shutil.copy("Main.py" , "Main2.py")
shutil.copy("Main.py" , "Main3.py")


#Example 2
# shutil.copytree("Folder Name" , "New Folder Name") to copy a folder with all its content in the new folder which will be same.
shutil.copytree("Tutorial" , "New_tutorial")

# Example 3
# shutil.move("path + /file Name" , "Destination_Name to move or place." )
shutil.move("New_tutorial/shutil.move.txt" , "shutil.move.txt")
# This will move the item inside a folder


# Example 4
# os.remove(file name or location will remove the item inside the directory)
os.remove("Tutorial/abc.txt")
