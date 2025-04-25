import random 

def rolar_dados (numero):
    i = 0 
    listavalores= []
    while i< numero:
        n = random.randint(1, 6)
        listavalores.append(n)
        i +=1
    return listavalores
    
