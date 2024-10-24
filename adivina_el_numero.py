import random



def adivina_el_numero(x):
    print("========================")
    print("Bienvenido(a) al juego!")
    print("========================")
    print("Tu objetivo es adivinar el número generado por la consola")

    numero_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x inclusive

    adivinacion = 0 #Variable

    while adivinacion != numero_aleatorio:
        #El usuario ingresa un número
        adivinacion = int(input(f"Adivina un número  entre 1 y {x}: "))

        if adivinacion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif adivinacion > numero_aleatorio:
            print("Intenta otra vez. Este número es muy grande. ")

    print(f"Felicitaciones! Adiviniaste el número {numero_aleatorio} correctamente.")

adivina_el_numero(10)
