def generatePassword():
    import random
    import string

    while True:
        print("Programa para generar contraseñas")
        for x in range(1):
            longitud=random.randint(4, 16)
        caract=string.ascii_letters+string.digits+string.punctuation
        while True:
            contraseña=("").join(random.choice(caract)for i in range(longitud))
            if(sum(c.islower() for c in contraseña)>=1
                and sum(c.isupper() for c in contraseña)>=1
                and sum(c.isdigit() for c in contraseña)>=1):
                break
        print("")
        print("La contraseña es:",contraseña)
        print("")
        break

generatePassword()