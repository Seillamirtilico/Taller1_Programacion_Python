print("Bienvenido a tu programa para calcular el (IMC) Índice de Masa Corporal")
print("A continuación, ingresa tu estatura en metros")
estatura = float(input())
print("A continuación, ingresa tu peso en kilos")
peso = float(input())
print("A continuación, ingresa tu edad en años")
annos = int(input())

imc = peso / (estatura ** 2)
print("Tu índice de masa corporal es", imc)

if annos < 45:
    if imc < 22.0:
        print("Tienes bajo riesgo de contraer enfermedades coronarias")
    else:
        print("Tienes riesgo medio de contraer enfermedades coronarias")
else:
    if imc < 22.0:
        print("Tienes riesgo medio de contraer enfermedades coronarias")
    else:
        print("Tienes alto riesgo de contraer enfermedades coronarias")
