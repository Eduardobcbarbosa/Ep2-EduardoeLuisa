import random 

def rolar_dados (numero):
    i = 0 
    listavalores= []
    while i< numero:
        n = random.randint(1, 6)
        listavalores.append(n)
        i +=1
    return listavalores

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    nova_dados_rolados = []
    for i in range (len(dados_rolados)):
        if i != dado_para_guardar:
            nova_dados_rolados.append(dados_rolados[i])
    dados_no_estoque.append(dado)
    return [nova_dados_rolados, dados_no_estoque]