import json

def coleta(arquivo):
    # Lê o arquivo com os códigos
    codes = open(arquivo, "rb")
<<<<<<< ours
<<<<<<< HEAD
    objeto = json.loads(codes.read())
=======
    objeto = json.loads(codes.readline())
>>>>>>> 9f38a656ab9cbe4aa4e4eb1b46b6a1956d8bf0bc
=======
    objeto = json.loads(codes.readline())
>>>>>>> theirs
    codes.close()
    
    return objeto
