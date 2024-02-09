""" Programa que valide si una contraseña especificada por el usuario es segura.

    Considerando para una contraseña segura, lo siguiente: 

    -> La contraseña debe tener más de 8 caracteres.
    -> Debe contener al menos una letra mayúscula.
    -> Debe contener al menos un número.    """


def comprobarPassword(password):
    largo = False
    Mayuscula = False
    Numero = False

    if len(password) > 8:
        largo = True

    for i in range(len(password)):
        if password[i].isupper():
            Mayuscula = True
        
        if password[i].isnumeric():
            Numero = True

    if largo and Mayuscula and Numero:
        return True
    else:
        return False
    
print("La contraseña debe incluir mínimo 8 caracteteres.")
print("La contraseña debe incluir como mínimo una letra mayúscula.") 
print("La contrasela debe incluir mínimo un número.")   

contrase = input("Ingresa una contraseña: ")
verificacion = comprobarPassword(contrase)
if verificacion:
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura. No contiene los caracteres requeridos.")
    print("La contraseña debe incluir mínimo 8 caracteteres.")
    print("La contraseña debe incluir como mínimo una letra mayúscula.") 
    print("La contrasela debe incluir mínimo un número.")   


