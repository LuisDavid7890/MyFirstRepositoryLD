#Conversion de numeros decimales a binario

numero = int (input ("Ingresa el valor de un numero: "))

binario = []

while numero != 0:
	cociente = numero //2;
	binario.append(numero % 2)
	numero = cociente


print (f"El numero convertido a binario es: ")
for i in binario:
		print(f"{i}", end = " ")