"""
Tool to encrypt passwords quickly using python hashlib
Pass to Hash by Lukas Martínez
"""

import hashlib

def logo():
    baner = """
    ██████╗  █████╗ ███████╗███████╗    ████████╗ ██████╗     ██╗  ██╗ █████╗ ███████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗    ██║  ██║██╔══██╗██╔════╝██║  ██║
██████╔╝███████║███████╗███████╗       ██║   ██║   ██║    ███████║███████║███████╗███████║
██╔═══╝ ██╔══██║╚════██║╚════██║       ██║   ██║   ██║    ██╔══██║██╔══██║╚════██║██╔══██║
██║     ██║  ██║███████║███████║       ██║   ╚██████╔╝    ██║  ██║██║  ██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                          <Lukas Martínez>
    Available Hashes:
        [*] MD5
        [*] SHA256                                                                                               
"""
    print(baner)


def encrypt():

    logo()

    # Here we encrypt the password in md5
    hash_password_md5 = hashlib.md5()
    user_password_md5 = input("Enter the password to encrypt: ")
    hash_password_md5.update(user_password_md5.encode('utf-8'))

    # Here we encrypt the password in sha256
    hash_password_sha256 = hashlib.sha256()
    user_password_sha256 = input("Enter the password to encrypt: ")
    hash_password_sha256.update(user_password_sha256.encode('utf-8'))

    print()

    # Here we show the hashes
    print("The password hash MD5 => ",hash_password_md5.hexdigest())
    print("The password hash SHA256 =>", hash_password_sha256.hexdigest())

encrypt()
