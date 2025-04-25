import random 

i = 0 
listavalores= []

def rolar_dados (numero):
    while i< numero:
        n = random.randint(1, 6)
        listavalores.append(n)
        i +=1
    return listavalores
    
