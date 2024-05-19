import os as iron
import auth as pw

iron.system ("cls")
menu = True
while menu:
    print ("Welcome to Ironclad V1")
    print ("Menu \n1.Login \n2.Daftar\n3.Exit")

    homeinp = input(str(" >> "))

    if homeinp == '1' :
        iron.system ("cls")
        pw.login()
        
        print ("1")
    elif homeinp == '2':
        iron.system ("cls")
        pw.daftar()

    elif homeinp == '3':
        break

    else :
        iron.system ("cls")
        print ("Err")
