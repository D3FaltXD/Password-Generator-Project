def encrypt(password,PIN):
    r=""
    for i in password:
        r+=" "+ str(ord(i)+PIN)
    return r
def decrypt(password,PIN):
    r=""
    password=password.split()
    for i in password:
        r+=chr(int(i)-PIN)
    return r
