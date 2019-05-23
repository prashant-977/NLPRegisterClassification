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

        
        file.seek(0)
        file.write('__label__'+folder +' ' +clean_file.replace('\n', ' ').lstrip())
        file.truncate()
