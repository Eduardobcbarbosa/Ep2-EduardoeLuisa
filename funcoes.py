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

def calcula_pontos_soma(listainteiros):
    total = 0
    for numero in listainteiros:
        total += numero
    return total

def calcula_pontos_sequencia_baixa(listainteiros):
    if 1 in listainteiros and 2 in listainteiros and 3 in listainteiros and 4 in listainteiros:
        return 15
    elif 2 in listainteiros and 3 in listainteiros and 4 in listainteiros and 5 in listainteiros:
        return 15
    elif 3 in listainteiros and 4 in listainteiros and 5 in listainteiros and 6 in listainteiros:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(listainteiros):
    if 1 in listainteiros and 2 in listainteiros and 3 in listainteiros and 4 in listainteiros and 5 in listainteiros:
        return 30
    elif 2 in listainteiros and 3 in listainteiros and 4 in listainteiros and 5 in listainteiros and 6 in listainteiros:
        return 30
    else:
        return 0

def calcula_pontos_full_house (listainteiros):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for numero in listainteiros:
        dic[numero] += 1  
    if 3 in dic.values() and 2 in dic.values():
        soma = 0
        for numero in listainteiros:
            soma += numero
        return soma
    else:
        return 0

def calcula_pontos_quadra(listainteiros):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for numero in listainteiros:
        dic[numero] +=1

    for quantidade in dic.values() :
        if quantidade>= 4:
            soma = 0 
            for numero in listainteiros:
                soma+=numero
            return soma
    else:
        return 0
    

def calcula_pontos_quina(listainteiros):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for numero in listainteiros:
        dic[numero] +=1
    for quantidade in dic.values() :
        if quantidade>= 5:
            return 50
    else:
        return 0    
    
def calcula_pontos_regra_avancada(listainteiros):
    pontuacoes = {
        'cinco_iguais': 0,
        'full_house': 0,
        'quadra': 0,
        'sem_combinacao': 0,
        'sequencia_alta': 0,
        'sequencia_baixa': 0
    }
    pontuacoes['cinco_iguais'] = calcula_pontos_quina(listainteiros)
    pontuacoes['full_house'] = calcula_pontos_full_house(listainteiros)
    pontuacoes['quadra'] = calcula_pontos_quadra(listainteiros)
    if calcula_pontos_quina(listainteiros) == 0 and calcula_pontos_full_house(listainteiros)== 0 and calcula_pontos_quadra(listainteiros) == 0 and calcula_pontos_sequencia_alta(listainteiros) == 0 and calcula_pontos_sequencia_baixa(listainteiros) == 0:
        pontuacoes['sem_combinacao'] = calcula_pontos_soma(listainteiros) 
    else:
        pontuacoes['sem_combinacao'] = 0
    pontuacoes['sequencia_alta'] = calcula_pontos_sequencia_alta(listainteiros)
    pontuacoes['sequencia_baixa'] = calcula_pontos_sequencia_baixa(listainteiros)

    return pontuacoes