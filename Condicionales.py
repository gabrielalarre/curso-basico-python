#Declaración de una variable
calificación = input("Introduce tu calificación de la AZ-900: ")

calificación = int(calificación) #transforma en número

# Preguntamos si la calificación es menor a 700
if calificación < 700 : 
    print("Veeees, por no estudiar")
elif calificación == 700 :
    print("¡panzazo!")
elif calificación > 1000 :
    print("¡Mientes! No puedes sacar más de mil!")
else : #Si no se cumple la condición anterior, pasa a esta línea
    print("¡Felicidades, pasa por tu certificado!") #se ejecuta si no se cumple la condición anterior

#Verificador de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("¡Bienvenido al mamitas!")
elif edad > 100 :
    print ("Si vienes acompañado de tus abuelitos, sí te podemos fiar")
elif edad < 0 :
    print ("Ni que fueras viejero en el tiempo")
else:
    print ("No puedes llevarte esos cigarros")