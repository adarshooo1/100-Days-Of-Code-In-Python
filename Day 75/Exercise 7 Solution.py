# This for seperately re-naming the file name.
import os

os.rename("ClutterFolder/Clutter.txt", "ClutterFolder/clutterFolder.txt")

# This will rename all the file which will ends with .png

files = os.listdir("ClutterFolder")
i = 1
for file in files:
  if file.endswith(".jpg"):
    print(file)
    os.rename(f"ClutterFolder/{file}", f"ClutterFolder/{i}.png")
    i += 1