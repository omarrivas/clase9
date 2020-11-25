import random

datos =[[1,1,1],
        [1,0,0],
        [0,1,0],
        [0,0,0]]

pesos = [random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)]

iteracion = 0
tasaAprende = 0.3

aprendiendo = True
while(aprendiendo== True):
    iteracion= iteracion + 1
    aprendiendo= False
    for cont in range(0,4):
        salidaReal =  (datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + pesos[2])
        print("salida: ", datos[cont][0], " * ", pesos[0], " + ", datos[cont][1], " * ", pesos[1], " + ", pesos[2])
        print("salida: ", salidaReal)

        if salidaReal > 0:
            salidaEntera = 1
        else:
            salidaEntera = 0
        print("salida entera: " + str(salidaEntera))

        error =  int(datos[cont][2] - salidaEntera)
        print("error: " + str(error))
        if (error != 0):
            pesos[0] += tasaAprende * error * datos[cont][0]
            pesos[1] += tasaAprende * error * datos[cont][1]
            pesos[2] += tasaAprende * error * 1
            aprendiendo = True

    if aprendiendo == False:
        break

print("********RESULTADOS FINALES********")
print("iteraciones: " , iteracion)
print("peso 1: ", pesos[0])
print("peso 2: ", pesos[1])
print("peso 3: ", pesos[2])

print("********TESTEA********")
#entradas:  1  y  1  =  1 perceptron:  1
#entradas:  1  y  0  =  0 perceptron:  0
#entradas:  0  y  1  =  0 perceptron:  0
#entradas:  0  y  0  =  0 perceptron:  0
valor1= 1
valor2= 1
salida = valor1 * pesos[0] + valor2 * pesos[1] + pesos[2]
print("formula: (", valor1 , " * ", pesos[0], " + ", valor2, " * ", pesos[1], " + ", pesos[2], " )")
print(salida)
if salida > 0 :
    salidaEntera = 1
else:
    salidaEntera = 0
print("entradas: ", valor1 , " y " , valor2, " = " , "perceptron: " , salidaEntera)
