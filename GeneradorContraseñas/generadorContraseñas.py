
#importamos el modulo secrets, es un modulo para generar secuencias aleatorias seguras
import secrets
#importamos el modulo string para tener acceso a trabajar con strings, no es necesario pero da mejores herramientas para ello
import string

#definimos las letras, digitos y caracteres especiales que seran la base para las contraseñas que se vayan a generar
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#concatenamos las anteriores variables para crear el alfabeto
alphabet = letters + digits + special_chars

#determinaremos la longitud de nuestra contraseña
pwd_length = int(input("Introduce la longitud de la contraseña por favor (Recuerda que debe de ser un numero) => "))

#generamos una variable para nuestra contraseña (output) y la inicializamos como vacia
pwd = ''

#en el rango entre el 1 y la longitud de la contraseña que ha intoducido el usuario generaremos un caracter aleatoriamente
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

#imprimimos la contraseña que se ha generado
print("")
print("Tu contraseña es => " + pwd)





