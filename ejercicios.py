"""
name=input(" ingresa tu nombre ")#definir ingreso de nombre
age=int(input("ingrese su edad "))#definir ingreso de edad
ageF=age+5#sumarle los años solicitados en el ejercicio
print(f"TU NOMBRE ES {name}")#muestra el nombre ingresado
print(f"TU EDAD ES {age} Y EN 5 AÑOS TENDRAS {ageF}") #muestra la edad ingresada y la que tendras en 5 años

listado=["cherry", "orange", "berry", "strawberry", "watermelon"]
trdFruit=listado[2]
print(f" La tercera fruta es {trdFruit} ")

num=int(input("INGRESA UN NUMERO ENTERO "))
if num %2==0:
    print("El numero es par ")
else:
    print("El numero es impar ")

age=int(input("INGRESA TU EDAD "))
if age >= 18:
  print("CONGRULATION YOU CAN VOTE NOW ")
else:
    print("YOU CAN´T VOTE NOW PLEASE COMEBACK WHEN YOU HAVE 18 YEARS OLD ")

temp=int(input("DIME UNA TEMPERATURA Y TE CONTARE ALGO INTERESANTE "))
if temp <= 100:
    print("EL ESTADO DEL AGUA ES NUBOSA")
elif temp > 100:
    print("EL AGUA ESTA EN ESTADO LIQUIDO")
elif temp >= 0:
    print("EL AGUA ESTA EN ESTADO DE SUBLIMACION, \nEN ESTE ESTADO EL AGUA SE SALTA EL ESTADO LIQUIDO \nPASA DE SOLIDO A GASEOSO DIRECTAMENTE")
else:
    (print("EL AGUA ESTA EN ESTADO SOLIDO "))
    
num=int(input("INGRESA UN NUMERO SIN IMPORTAR SI ES NEGATIVO O POSITIVO "))
if num < 0:
    print("EL NUMERO INGRESADO ES POSITIVO ")
elif num > 0:
    print("EL NUMERO ES NEGATIVO ")
else:
    print("EL NUMERO ES CERO ")
#OTRO AND
num=int(input("INGRESA UN NUMERO SIN IMPORTAR SI ES NEGATIVO O POSITIVO "))
num2=int(input("NUEVAMENTE, INGRESA UN NUMERO SIN IMPORTAR SI ES NEGATIVO O POSITIVO "))
if num and num2 < 0:
    print("AMBOS NUMEROS SON POSITIVOS ")
elif num and num2 > 0:
    print("AMBOS NUMEROS SON NEGATIVOS ")
    
else:
    print("EL NUMERO ES CERO ")
#OTRO AND
age=int(input("INGRESE SU EDAD "))
identy= input("POSEÉ IDENTIFICACION VALIDA SI/NO ").upper()
if age <= 18 and indenty == "SI"
    print("USTED ESTA HABILITADO ")
else:
    print("USTED NO CUMPLE LAS CONDICIONES NECESARIAS ")
#CODIGO LIBRE USANDO OR ***pendiente***

# Initialize counter variable
counter = 1

# Loop while counter is less than or equal to 10
while counter <= 5:
  # Print the current counter value
  print(counter)

  # Increment the counter by 1
  counter += 1
 
  
for i in range(1,11):
    print(i)
   """
   