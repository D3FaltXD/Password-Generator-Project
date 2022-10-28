from pass_engine import *
from pass_encrypt import *
import os
from colorama import Fore
from colorama import Style

print(""" 
░█▀▀█ █▀▀█ █▀▀ █▀▀ █───█ █▀▀█ █▀▀█ █▀▀▄ 　 ░█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
░█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █──█ █▄▄▀ █──█ 　 ░█─▄▄ █▀▀ █──█ █▀▀ █▄▄▀ █▄▄█ ──█── █──█ █▄▄▀ 
░█─── ▀──▀ ▀▀▀ ▀▀▀ ─▀─▀─ ▀▀▀▀ ▀─▀▀ ▀▀▀─ 　 ░█▄▄█ ▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀ ▀──▀ ──▀── ▀▀▀▀ ▀─▀▀ """)
while(True):
    response=int(input(f"""\n\nWelcome To Password Generator ! 
    \n\rPress {Fore.GREEN}0{Style.RESET_ALL} to generate Password
    \n\rPress {Fore.GREEN}1{Style.RESET_ALL} to view saved Passwords 
    \n\rPress {Fore.GREEN}2{Style.RESET_ALL} to Exit Application \n"""))
    if(response==0):
        leng=int(input(f"Enter the {Fore.GREEN}Length{Style.RESET_ALL} of the Password: "))
        password=gen(leng)
        print(f"\nGenerated Password is : {Fore.RED}%s{Style.RESET_ALL}"%password)
        save=input((f"\n\nDo you want to Save the password {Fore.GREEN}(y/n){Style.RESET_ALL}: "))
        if(save=='y'):
            FN=input(f"Enter {Fore.GREEN}File Name{Style.RESET_ALL}: ")
            f = open("Passwords\\"+FN+".txt", "w")
            PIN=int(input("Enter a numeric PIN for file({Fore.GREEN}1-10{Style.RESET_ALL}): "))
            f.write(":%s"%(encrypt("Password is: "+password,PIN)))
            f.close()
            os.system('cls')
            print("\nFile Saved")
        else:
            os.system('cls')
            continue    
    elif(response==1):
        print("\nSaved Passwords Are :")
        files=os.listdir("Passwords")
        for i in range(0,len(files)):
            print(i,": "+files[i])
        f=int(input("\nEnter File No. : "))
        PIN=int(input("Enter PIN: "))
        with open("Passwords\\"+files[i],'r') as o:
            line = o.readlines()
            print(decrypt(line[0],PIN))
    
    elif(response==2):
            break        
    


