import pandas as pd
import csv
import glob
import os

# merging the files
files_joined = os.path.join('C:\\Users\\BMX\\Desktop\\vaccination-covid\\data\\raw', "donnees-*.csv")

# Return a list of all joined files
list_files = glob.glob(files_joined)


# Merge files by joining all files
fu = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
fu.to_csv("fusion.csv", index=False)
print(fu)



