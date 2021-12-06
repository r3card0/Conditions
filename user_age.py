# Preguntarle al usuario cual es su edad y en base a su respuesta
#responderle si es mayor o no.
# 1. Crear un mensaje de entrada. Preguntarle su edad. Esto a través de una variable
# 2. convertir la variable en un entero
# 3. Si la edad del usuario es mayor a 17 años, 
# entonces le diremos que es mayor de edad
# si su edad es menor a 17 años,
# entonces le diremos que es menor de edad
# if significa: si
# else significa: sino
# edad = input("Hola Superusuario! Mi propósito es decir si eres mayor de edad o no, en base a tu respuesta. ¿Te gustaría ayudarme? Por favor dime cuál es tu edad: ")
edad = input("Hola! ¿Cuál es tu edad?: ")
edad = int(edad)
if edad > 17:
    print("Usted es mayor de edad")
else: 
    print("Usted es menor de edad")