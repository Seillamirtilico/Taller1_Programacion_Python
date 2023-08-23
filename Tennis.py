print("""
               /xxxx\\
              |xxxxxx|
              |xxxxxx|      _
              \\xxxxxx/     (~)
               \\xxxx/
                \\--/
                 ||
                 ||
                 ||
                 ||
                 ||
                 []
Bienvenido a tu programa de sets de tennis
--------------------------------------------""")

print("Ingresa los juegos ganados por el equipo A")
GanadosA = int(input())
print("Ingresa los juegos ganados por el equipo B")
GanadosB = int(input())
Paraganarb = GanadosA + 2
Paraganara = GanadosB + 2

if GanadosA == 5 and GanadosB == 5:
    print("Empate 5 a 5")
elif GanadosA > 6 and GanadosA - GanadosB > 2:
    print("Invalido!!")
elif GanadosB > 6 and GanadosB - GanadosA > 2:
    print("Invalido!!")
elif GanadosA == 6 and GanadosB == 6:
    print("Empate 6 a 6")
elif GanadosB >= 6 and GanadosB >= Paraganarb and Paraganarb >= 2:
    print("Gano el equipo b")
elif GanadosA >= 6 and GanadosA >= Paraganara and Paraganara >= 2:
    print("Gano el Equipo A")
elif 0 <= GanadosA <= 6 and 0 <= GanadosB <= 6:
    print("El juego aun no termina")
else:
    print("Opción inválida")
