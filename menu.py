import os as sys


def mainmenu():
        menu = True
        while menu:
            sys.system("cls")
        
            print ("Welcome")
            print ("Menu \n1.Internet Check \n2.Calculator\n3.Exit")

            inp = input(" >> ")

            if inp == '1':
                sys.system("ping 8.8.8.8")
         

