print("Bienvenido a tu programa para saber si tu división es exacta o no")
print("Ingresa el dividendo")
dividendo = int(input())
print("Ingresa el divisor")
divisor = int(input())
cociente = dividendo / divisor
modulo = dividendo % divisor

if modulo == 0:
    print(f"La división es exacta\nSu cociente es {cociente}")
    print(f"Y su residuo es {modulo}")
else:
    print(f"La división NO es exacta\nSu cociente es {cociente}")
    print(f"Y su residuo es {modulo}")
