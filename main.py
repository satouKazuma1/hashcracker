import hashlib

hash_file="c1f3c7a30cd6890ec0ac64345b18a70a6615091d763604ca3bac81e4f894250d"
dic_file=input("Ingrese la direccion del archivo del diccionario: ")
with open(dic_file,'r') as file:
    diccionario=[line.strip() for line in file]

    for password in diccionario:
        hash_calculado=hashlib.sha256(password.encode()).hexdigest()
        if hash_calculado==hash_file:
            print("Encontrado: "+ password)
        else:
            print("No coincide: "+ password)