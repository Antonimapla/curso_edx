
try:

    horas = int(input("introduzca las horas: "))
    tarifa = int(input("Introduzca el precio tarifa: "))
    if horas >= 40:
        print(f"El salario bruto de 40 horas es de, {40 * int(tarifa)} €")
        
        extra = int(horas) - 40
        print(f"El salario bruto de {extra} horas extra es de, {int(extra) * int(tarifa * 1.5)} €")

    else:
        print(f"El salario bruto de {horas} horas es de, {int(horas) * int(tarifa)} €")
except:
    print("***ERROR***, ingresar valores numaricos.")
