'''
Introdução a programação com Python
Cap. 7 - Exercicio 7.3
'''

primeiraString=input()
segundaString=input()
terceirastring=""

for letra in primeiraString:
	if letra not in segundaString:
		terceirastring+=letra

for letra in segundaString:
	if letra not in primeiraString:
		terceirastring+=letra

print(terceirastring)
