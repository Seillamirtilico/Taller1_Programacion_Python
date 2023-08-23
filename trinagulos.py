print("Bienvenido a tu programa para determinar qué tipo de triángulo tienes")
print("A continuación, ingresa el lado A de tu triángulo")
ladoa = float(input())
print("A continuación, ingresa el lado B de tu triángulo")
ladob = float(input())
print("A continuación, ingresa el lado C de tu triángulo")
ladoc = float(input())

if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
    if ladoa == ladob == ladoc:
        print("Tu triángulo es válido y es un triángulo equilátero, es decir, tiene 3 lados iguales")
    elif ladoa == ladob or ladob == ladoc or ladoa == ladoc:
        print("Tu triángulo es válido y es un triángulo isósceles, es decir, tiene 2 lados iguales")
    elif ladoa != ladob and ladob != ladoc and ladoc != ladoa:
        print("Tu triángulo es válido y es un triángulo escaleno, es decir, tiene 3 lados diferentes")
else:
    print("Tu triángulo es inválido ya que no cumple con la desigualdad triangular")
