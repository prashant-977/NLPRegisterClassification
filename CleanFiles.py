import os
import re
import glob
from fileinput import FileInput

files = glob.glob('*\*\*.txt')


for file in files:

    folder=os.path.dirname(file).split('\\')[-2]

    with open(file,'r+',errors='ignore') as file: #there are special characters in the file which are not being decoded.
        text=file.read()
        p = re.compile(r'<.*?>')
        clean_file =p.sub('', text)
#         var=re.sub('<.*?>', '', f.read())
#         va='__label__'+folder +'\n' +var.lstrip()
        
        file.seek(0)
        file.write('__label__'+folder +'\n' +clean_file.lstrip())
        file.truncate()