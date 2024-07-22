import random
print("NOSTRADAMUS🧙‍♂️ \nI SEE THE FUTURE🔮 ╰(*°▽°*)╯ ")
num= random.randint(1,10)#simula pensar un numero
isGuessRigth=False
while isGuessRigth !=True:
    guess=int(input("INGRESA EL NUMERO QUE ESTOY PENSANDO \nTE DARE UNA PISTA ES DE 1 A 10: "))
    if guess == num:
        isGuessRigth=True
        print("FELICIDADES ERES CASI TAN BUENO COMO YO 👁️")
    else:
        print("MALA SUERTE INTENTA DENUEVO ❌")
print(num)