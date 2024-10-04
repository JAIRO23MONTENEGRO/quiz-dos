Nombre = input("Escribe tu nombre: ")
Dias = int(input("Escriba los dias laborados: "))
Salario =int(input("Escriba el salario: "))

prima = ((Salario*Dias)/360)
Cesantias = (Salario*Dias)/360
Intereses_cesantias = (Cesantias*0.12)/Dias
Vacaciones = (Salario * Dias) /720

Liquidacion =prima+Cesantias+Intereses_cesantias+Vacaciones
print(f"Señor {Nombre} para los {Dias} laborados y salario ${Salario}, su liquidacion se compone asi: ")

print(f"\n Prima: ${prima:.2f}\n Cesantias: ${Cesantias:.2f}\n Intereses cesantias: ${Intereses_cesantias:.2f}\n Vacaciones: ${Vacaciones:.2f}\n Liquidacion: ${Liquidacion:.2f}")
