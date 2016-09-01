# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


L=[15,7,27,39]
p=int(input("Digite o primeiro valor a procurar: "))
v=int(input("Digite o segundo valor a procurar: "))

achouPrimeiro=0
primeiroEncontrado=False
segundoEncontrado=False
x=0
while x<len(L):
    if L[x]==p:
        print("%d achado na posicao %d" % (p,x))
        primeiroEncontrado=True
        if achouPrimeiro==0:
            achouPrimeiro=p
    elif L[x]==v:
        print("%d achado na posicao %d" % (v,x))
        segundoEncontrado=True
        if achouPrimeiro==0:
            achouPrimeiro=v
    x+=1
else:
    if achouPrimeiro==0:
        print("%d e %d nao encontrados" % (p,v))
    else:
        print("%d foi o primeiro a ser encontrado" %achouPrimeiro)
    if primeiroEncontrado and not segundoEncontrado:
        print("%d nao encontrado" % v)
    elif not primeiroEncontrado and segundoEncontrado:
        print("%d nao encontrado" % p)
    
        


