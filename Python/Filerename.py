import os
import sys
path= os.chdir("C:\\Users\\poshik\\Downloads\\JPEG")

i=0
for file in os.listdir(path):
    
    new_file_name = "pic{}.jpg".format(i)
    os.rename(file,new_file_name)
    i=i+1

