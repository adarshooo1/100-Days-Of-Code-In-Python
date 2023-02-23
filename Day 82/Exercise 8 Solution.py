# to install PyPDF Module cmd:- pip install PyPDF2
from PyPDF2 import PdfWriter
# Pdfwriter helps and reading and writing pdf files in Python

# os module provode the facility to establish interaction between the user and the operating system.
import os

merge = PdfWriter()

# It will iterater over the file inside the folder and os.listdir(#Path) we have to mention the path then it will iterate only those file endswith(.pdg) then count and store those pdf in the reference variable in the form of list.
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    # It will take those pdf files and append eachother
    merge.apppend(pdf)

# This will cearte the new pdf and the name when pdf file will be merged.
merge.write("Merged-Pdf.pdf")
# for closure of this program
merge.close()  