
from translate import Translator
from pip._internal.utils import encoding
t_s=Translator(to_lang='ja')
try:
    my_file=open('C:\\Users\\Acer\\Desktop\\biru.txt')
    text_in_file= my_file.read()
    print(text_in_file)
    translated=t_s.translate(text_in_file)
    print(translated)
    
    my_fileX=open('C:\\Users\\Acer\\Desktop\\biruX.txt',mode='w', encoding='utf-8')
    my_fileX.write(translated)
except FileNotFoundError as FNFE:
    print(f"check the file location if it file exist\n\n {FNFE}")
except UnicodeEncodeError as UEE:
    print(f"This kind of language need additional setting \n\n {UEE}")

#open('C:\\Users\\Acer\\Desktop\\biruX.txt',mode='w', encoding='utf-8')