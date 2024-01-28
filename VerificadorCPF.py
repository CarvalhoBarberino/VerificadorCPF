print('Digite os 9 primeiros digitos do CPF')
primeiros9 = int(input())
aux = primeiros9
vec = []
grad1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
dig1 = 0
grad2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dig2 = 0
for i in range(9):
	d = aux%10
	vec.append(d)
	aux = (aux - d) / 10
somaTexto = ''
for i in range(len(grad1)):
	dig1 = dig1 + grad1[i] * vec[i]
	somaTexto = somaTexto + ' + ' + str(grad1[i]) + '*' + str(vec[i])
somaTexto = somaTexto + ' = ' + str(dig1)
print()
print('PARTE 1 - CALCULO DA DEZENA')
print(somaTexto)
print('O resto da divizao por 11 eh: ' + str(dig1%11))
if (dig1%11 < 2):
	dig1 = 0
	print('resto da divisao eh menor que 2, entao a dezena eh: ' + str(dig1))
else:
	dig1 = 11 - dig1%11
	print('resto da divisao eh maior que 1, entao a dezena eh 11 - ' + str(11-dig1) + ' = ' + str(dig1))
vec.insert(0, dig1)
somaTexto = ''
for i in range(len(grad2)):
	dig2 = dig2 + grad2[i] * vec[i]
	somaTexto = somaTexto + ' + ' + str(grad2[i]) + '*' + str(vec[i])
somaTexto = somaTexto + ' = ' + str(dig2)
print()
print('PARTE 2 - CALCULO DA UNIDADE')
print(somaTexto)
print('O resto da divizao por 11 eh: ' + str(dig2%11))
if (dig2%11 < 2):
	dig2 = 0
	print('resto da divisao eh menor que 2, entao a unidade eh: ' + str(dig2))
else:
	dig2 = 11 - dig2%11
	print('resto da divisao eh maior que 1, entao a unidade eh 11 - ' + str(11-dig2) + ' = ' + str(dig2))
vec.insert(0, dig2)
print()
print( 'Então, os dois digitos verificadores são: ' + str(int(dig1)) + str(int(dig2)))
