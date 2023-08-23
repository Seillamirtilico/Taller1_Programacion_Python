print("Bienvenido a tu programa para saber si el año es bisiesto o no")
print("Ingresa El Año")
anno = int(input())

if anno % 400 == 0:
    print("el año", anno, "es bisiesto")
elif anno % 4 == 0 and anno % 100 != 0:
    print("el año", anno, "es bisiesto")
else:
    print("el año", anno, "NO es bisiesto")
