L=[15,7,27,39]
p=int(input("Digite o valor a procurar: "))
#achou=False
x=0
while x<len(L):
    if L[x]==p:
        print("%d achado na posicao %d" % (p,x))
        break
    x+=1
else:
    print("%d nao encontrado" % p)
        
