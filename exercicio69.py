# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


L=[15,7,27,39]
p=int(input("Digite o primeiro valor a procurar: "))
v=int(input("Digite o segundo valor a procurar: "))

achouPrimeiro=0
x=0
while x<len(L):
    if L[x]==p and achouPrimeiro==0:
        achouPrimeiro=p
        break
    elif L[x]==v and achouPrimeiro==0:
        achouPrimeiro=v
    x+=1
if achouPrimeiro==0:
    print("%d e %d nao encontrados" % (p,v))
else:
    print("%d foi o primeiro a ser encontrado" %achouPrimeiro)
        
