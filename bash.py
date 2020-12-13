from os import system, remove
import sys, time
system('apt-get install nodejs -y')
system('npm install -g bash-obfuscate')
system('git pull')
logo = """
\033[1;34m                       dP   dP
\033[1;34m                       88   88
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b.
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP
\033[1;34m   88            .88
\033[1;34m   dP        d8888P\n
\033[1;34m   dP    8888b
\033[1;37m   88 o  88
\033[1;33m   88 dP 88aaa  .d8888b.
\033[1;33m   88 88 88     88ooood8
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad\t\033[1;36m
\033[1;34m   dP dP dP     `88888P\n"""
def list():
    print('\033[1;3+m++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\033[1;31m[1] \033[1;32mEncrypt \033[1;31mBash Shell')
    print('\033[1;31m[2] \033[1;32mEncryptDecode \033[1;31mBash Shell')
    print('\033[1;31m[3] \033[1;32mYouTube')
    print('\033[1;31m[4] \033[1;32mInstagram')
    print('\033[1;31m[0] Exit\n')
    
def clear():
    system('clear')
def cod():
    clear()
    print(logo)
    ask1 = input('\033[1;32mFile >\033[1;31m')
    enc = 'bash-obfuscate ' + ask1 + ' -o enc.sh'
    system(enc)
def dec():
    clear()
    print(logo)
    file = input('\033[1;32mEncryptFile >\033[1;31m')
    openfile = open(file, 'r')
    readfile = openfile.read()
    openfile.close()
    newcode = readfile.replace('eval', 'echo')
    outfile = input('\033[1;32mOutput > \033[1;31m')
    newfile = open(outfile, 'w')
    newfile.write(newcode)
    newfile.close()
    system('touch tools.sh')
    system('bash ' + outfile + '> tools.sh')
    remove(outfile)
    system('mv -f tools.sh ' + outfile)
    print('success decrypt | file save as ' + outfile)
clear()
print(logo)
list()
choose = input('\033[1;31m[?] \033[1;3mChoose :\033[1;31m')
if choose == 1:
    cod()
elif choose == 2:
    dec()
elif choose == 3:
    system('xdg-open https://www.youtube.com/c/pythonlife')
elif choose ==4:
    system('xdg-open http://www.instagram.com/python.life')
else:
    print('\033[1;31mplease choose 1 or 2 or 3 or 4 or 0 for exit '.upper())

















