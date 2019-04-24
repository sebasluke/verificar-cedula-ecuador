# -*- coding: utf-8 -*-
#permite ingresar un número de cédula
from sys import argv
script, numeroCedula = argv

#Crea un int para que bote error si es número y un str para partirle y validar
cedulaInt = int(numeroCedula)
cedulaStr = str(numeroCedula)

#validar que tiene 10 dígitos
if len(cedulaStr) == 10:
    print(f"La cédula {cedulaInt} es un número y tiene 10 dígitos, ahora debemos saber si representa a una provincia...")
    tamanoCedula = True

else:
    print(f"El número {cedula} no tiene 10 dígitos, no es una cédula.")
    tamanoCedula = False

#si se valida que tiene 10 dígitos, validar que los 2 primeros son menores que 26

#elegir 2 primeros digitos y validar que son menores que 26
digitosProvincia = int(cedulaStr[0:2])

if tamanoCedula:
#si es menor que 24 continúa, y asigna True a provincia
    if digitosProvincia <= 24:
        print(f"Los dígitos {digitosProvincia} son menores o iguales a 24, ahora, a validar si el tercer dígito es menor a 6...")
        provincia = True
#else asigna False a provincia
    else:
        print(f"Los dígitos {digitosProvincia} son mayores o iguales que 24, la cédula no es válida")
        provincia = False

# si la cédula tiene 10 dígitos y la provincia está bien, validar que el tercer dígito sea menor que 6
tercerDigito = int(cedulaStr[2])

if tamanoCedula and provincia:
    if tercerDigito < 6:
        print(f"El tercer dígito {tercerDigito} es menor que 6, podemos continuar a multiplicar y sumar")
        tercerDigitoValido = True
#si es mayor que 6, asignar falso
    else:
        print(f"El tercer dígito {tercerDigito} es mayor que 6, la cédula no es válida")
        tercerDigitoValido = False


if tamanoCedula and provincia and tercerDigitoValido:
    #Crear una lista con la cédula

    listaCedula = []

    for digit in cedulaStr[0:9]:
        eachNumber = int(digit)
        listaCedula.append(eachNumber)

    print(f"Paso 1, convertir la cédula en lista, así {listaCedula}")

    #Crear la lista de impares:
    pares = [y for x,y in enumerate(listaCedula) if x%2 != 0]
    impares = [y for x,y in enumerate(listaCedula) if x%2 == 0]

    print(f"Paso 2, crear la lista de pares {pares}")
    print(f"paso 3, crear la lista de impares {impares}")

    #Ahora sí, crear una función que multiplique

    #la función recoge el número, el coeficiente y la lista a la que debe agregar
    def multiplicadorCoeficientes(numero, coeficiente, lista):
        numeroMultiplicado = int(numero) * int(coeficiente)
        if numeroMultiplicado > 10:
            numeroMultiplicado -= 9
        lista.append(numeroMultiplicado)

        #Multiplica los dígitos de posiciones pares
    coeficientePares = 1
    paresMultiplicados = []
    for par in pares:
        multiplicadorCoeficientes(par, coeficientePares, paresMultiplicados)
    print(f"Estos son los resultados de los pares {paresMultiplicados}")

    #Multiplica los dígitos de posiciones impares
    coeficienteImpares = 2
    imparesMultiplicados = []
    for impar in impares:
        multiplicadorCoeficientes(impar, coeficienteImpares, imparesMultiplicados)
    print(f"Estos son los resultados de los impares {imparesMultiplicados}")

    #Suma todos los elementos de la lista de impares:
    imparesTotal = 0
    for impares in imparesMultiplicados:
        imparesTotal += impares
    print(f"El total de los impares es {imparesTotal} ")

    #suma todos los elementos de la lista pares:
    paresTotal = 0
    for pares in paresMultiplicados:
        paresTotal += pares
    print(f"El total de los pares es {paresTotal}")

    #suma de los 2 elementos:
    totalFinal = paresTotal + imparesTotal
    print(f"Este es el número al que hay que restarle la decena superior {totalFinal}")

    #define la decena superior

    totalFinalStr = str(totalFinal)
    numeroFinal = totalFinalStr[0]

    #verificar que no sea decena y crear decena superior
    if int(totalFinalStr[-1]) != 0:
        decenaSuperior = (int(numeroFinal) + 1) * 10
    #si es decena, no le suma 1
    if int(totalFinalStr[-1]) == 0:
        decenaSuperior = int(numeroFinal) * 10

    print(f"Esta es la decena superior a la que hay que restar {decenaSuperior}")

    #resta la decena superior del número y compáralo con el último número de la cédula
    digitoFinal = decenaSuperior - totalFinal
    digitoVerificador = int(cedulaStr[-1])

    print(f"El dígito verificador es {digitoVerificador}")

    #Si son iguales los 2 números la cédula está verificada
    if digitoVerificador == digitoFinal:
        cedulaVerificada = True

    if digitoVerificador != digitoFinal:
        cedulaVerificada = False

    print(f"Después de analizar si el {digitoVerificador} es igual al {digitoFinal} podemos decir que es {cedulaVerificada} que la cédula es real")
