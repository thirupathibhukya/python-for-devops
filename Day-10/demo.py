import os
folders = input("provides list of folders with spoaces:").split()
for folder in folders:
    files = os.listdir(folder)
