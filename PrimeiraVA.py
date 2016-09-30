#prova de iP

#1ª questão - Determinar se ano é bissexto

ano=int(input("Digite um ano: "))
if (ano%400==0) or ((ano%4==0 and ano%100!=0)):
	print("%d é bissexto."%ano)
else:
	print("%d não é bissexto."%ano)
	
#2- Questão - Vencedor da eleição do DA-DEINFO

A, B, C, total,primeiro,segundo,terceiro=0,0,0,0,0,0,0
votosprimeiro,votossegundo,votosterceiro=0,0,0

def vots(candidato,total):
	return (candidato/total)*100

print("Opções:\n1 - Candidato A\n2 - Candidato B\n3 - Candidato C\n4- Encerrar a votação")
while True:
	voto= int(input("Opção: "))
	if voto==4:
		break
	elif voto==1:
		total+=1
		A+=1
	elif voto==2:
		total+=1
		B+=1
	elif voto==3:
		total+=1
		C+=1
if A>1 or B>1 or C>1:								#não deve haver divisão por zero na função vots
	if A>=B and A>=C:
		primeiro,votosprimeiro='A',vots(A,total)
		if B>=C:
			segundo,votossegundo='B',vots(B,total)
			terceiro,votosterceiro='C',vots(C,total)
		else:
			segundo,votossegundo='C',vots(C,total)
			terceiro,votosterceiro='B',vots(B,total)
	elif B>A and B>=C:
		primeiro,votosprimeiro='B',vots(B,total)
		if A>=C:
			segundo,votossegundo='A',vots(A,total)
			terceiro,votosterceiro='C',vots(C,total)
		else:
			segundo,votossegundo='C',vots(C,total)
			terceiro,votosterceiro='A',vots(A,total)
	elif C>A and C>=B:
		primeiro,votosprimeiro='C',vots(C,total)
		if A>B:
			segundo,votossegundo='A',vots(A,total)
			terceiro,votosterceiro='B',vots(B,total)
		else:
			segundo,votossegundo='B',vots(B,total)
			terceiro,votosterceiro='A',vots(A,total)
	else:
		primeiro,votosprimeiro='A',vots(A,total)
		segundo,votossegundo='B',vots(B,total)
		terceiro,votosterceiro='C',vots(C,total)
		
	print("Candidato %s: %f%% dos votos." % (primeiro,votosprimeiro))
	print("Candidato %s: %f%% dos votos." % (segundo,votossegundo))
	print("Candidato %s: %f%% dos votos." % (terceiro,votosterceiro))
	
	#3ª questão - Lista de Passageiros
	
	#Dados:
	passageirosVoo=["João Guilherme", "Allan Vieira", "José Marcos","Pedro Cavalcanti"]
	embarcados=["João Guilherme", "Allan Vieira","Pedro Cavalcanti","Allan Vieira"]
	maisdeuma=[]
	for nome in passageirosVoo:
		if nome not in embarcados:
			print(nome,"não embarcou")
	for nome in embarcados:
		if nome not in maisdeuma and embarcados.count(nome)>1:
			maisdeuma.append(nome)
			print(nome,"está repetido")
			
	#4ª questão -  Buscas:
	
	def buscaSqn(valor,lista):
		for n in range(len(lista)):
			if lista[n]==valor:
				return n
		return -1
	
	def buscaBnr(valor,lista):
		inicio=0
		fim = len(lista)
		while inicio<=fim:
			meio=(inicio + fim)//2
			if lista[meio]<valor:
				inicio=meio+1
			elif lista[meio]>valor:
				fim=meio-1
			else:
				return meio
			
lista=[2,3,12,15,25,32,45,56,67,74,83,90]
print(buscaSqn(25,lista))
print(buscaBnr(25,lista))
