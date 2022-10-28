from pass_engine import *
from pass_encrypt import *
import os


print(""" 
░█▀▀█ █▀▀█ █▀▀ █▀▀ █───█ █▀▀█ █▀▀█ █▀▀▄ 　 ░█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
░█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █──█ █▄▄▀ █──█ 　 ░█─▄▄ █▀▀ █──█ █▀▀ █▄▄▀ █▄▄█ ──█── █──█ █▄▄▀ 
░█─── ▀──▀ ▀▀▀ ▀▀▀ ─▀─▀─ ▀▀▀▀ ▀─▀▀ ▀▀▀─ 　 ░█▄▄█ ▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀ ▀──▀ ──▀── ▀▀▀▀ ▀─▀▀ """)
while(True):
    response=int(input("""\n\nWelcome To Password Generator ! 
    \n\rPress 0 to generate Password
    \n\rPress 1 to view saved Passwords 
    \n\rPress 2 to Exit Application \n"""))
    if(response==0):
        leng=int(input(f"Enter the Length of the Password: "))
        password=gen(leng)
        print("\nGenerated Password is : %s"%(password))
        save=input(("\n\nDo you want to Save the password (y/n): "))
        if(save=='y'):
            FN=input("Enter File Name: ")
            f = open("Passwords\\"+FN+".txt", "w")
            PIN=int(input("Enter a numeric PIN for file(1-10): "))
            f.write("%s"%(encrypt("Password is: "+password,PIN)))
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
        with open("Passwords\\"+files[f],'r') as o:
            line = o.readlines()
            os.system('cls')
            print(decrypt(line[0],PIN))
            break
        
    elif(response==2):
            break        
    


