def calcularLiquidacion(nombre, dias, salario):

  prima = float(salario * dias / 360)
  cesantias = float(salario * dias / 360)
  interesesCesantias = float(cesantias * 0.12 / dias)
  vacaciones = float(salario * dias / 720)

  liquidacionTotal = int(prima + cesantias + interesesCesantias + vacaciones)

  resultado = f"Señor {nombre} para los {dias} días laborados y salario ${salario}, su liquidación se compone así:\n"
  resultado += f"Prima: ${prima:.2f}\n"
  resultado += f"Cesantía: ${cesantias:.2f}\n"
  resultado += f"Intereses cesantías: ${interesesCesantias:.2f}\n"
  resultado += f"Vacaciones: ${vacaciones:.2f}\n"
  resultado += f"Liquidación: ${liquidacionTotal:.2f}"

  return resultado

nombre = input("Ingresa tu nombre: ")
dias = float(input("Ingresa los día laborados: "))
salario = float(input("Ingresa tu salario: "))

resultado = calcularLiquidacion(nombre, dias, salario)
print(resultado)