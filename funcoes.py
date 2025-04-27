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

def remover_dado(dados_rolados1, dados_no_estoque1, dado_para_remover):
    dado1 = dados_no_estoque1[dado_para_remover]
    nova_dados_no_estoque=[]
    for i in range (len(dados_no_estoque1)):
        if i != dado_para_remover:
            nova_dados_no_estoque.append(dados_no_estoque1[i])
    dados_rolados1.append(dado1)
    return [dados_rolados1, nova_dados_no_estoque]

def calcula_pontos_regra_simples(listainteiros):
    dicsoma = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for numero in listainteiros:
        if 1 <= numero <= 6:
            dicsoma[numero] += numero  
    return dicsoma
