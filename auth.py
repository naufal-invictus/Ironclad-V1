import hashlib
import menu as m

def login():
    print ("Login ....")
    id = input("ID :")
    pwd = input("Password : ")

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open('credentials.txt', 'r') as f:
         stored_id, stored_pwd = f.read().split("\n")
    f.close()

    if id == stored_id and auth_hash == stored_pwd:
        print("Logged in Successfully")
        m.mainmenu()
        
    else:
        print("Login failed! \n")


def daftar():
    id = input("ID : ")
    pwd = input("Password : ")
    enc = pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    with open('credentials.txt', 'w') as f:
         f.write(id + '\n')
         f.write(hash1)
    f.close()
    print("You have registered successfully!")