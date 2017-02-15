#!/usr/bin/python
import os, sys, csv
from tkinter.filedialog import askdirectory

folder = askdirectory()
outfile = "out.csv"
f = open(outfile, "w")

for dirpath, dirnames, filenames in os.walk(folder):
    for file in filenames:
        f.write(dirpath + ',' + file + '\n')

print("All done! Results are in " + outfile + ".")
