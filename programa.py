from funcoes import imprime_cartela
from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada
from funcoes import faz_jogada

cartela = {'regra_simples': {1: -1,2: -1,3: -1,4: -1,5: -1,6: -1},'regra_avancada' : {'sem_combinacao': -1,'quadra': -1,'full_house': -1,'sequencia_baixa': -1,'sequencia_alta': -1,'cinco_iguais': -1}}
imprime_cartela(cartela)

todascat = ['1', '2', '3', '4', '5', '6', 'sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']
categorias = []
i=0
while i<12:
    n = 5
    rolados = rolar_dados(n)
    guardados=[]
    print('Dados rolados:', rolados)
    print('Dados guardados:', guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    resposta = input(">" )
    a = 0
    while resposta!= '0':
        if resposta=='1':
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            while indice >= len(rolados):
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input(">"))
            guardar = guardar_dado(rolados, guardados,indice)
            print('Dados rolados:', rolados)
            print('Dados guardados:', guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input(">" )

        elif resposta=='2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice_remover=int(input(">"))
            while indice_remover >= len(guardados):
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice_remover=int(input(">"))
            remover = remover_dado(rolados, guardados, indice_remover)
            print('Dados rolados:', rolados)
            print('Dados guardados:', guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input(">" )

        elif resposta=='3':
            if a == 2:
                print("Você já usou todas as rerrolagens.")
                print('Dados rolados:', rolados)
                print('Dados guardados:', guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                resposta = input(">" )
            else:
                a += 1
                n = len(rolados)
                rolados = rolar_dados(n)
                print('Dados rolados:', rolados)
                print('Dados guardados:', guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                resposta = input(">" )

        elif resposta=='4':
            imprime_cartela(cartela)
            print('Dados rolados:', rolados)
            print('Dados guardados:', guardados)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resposta = input(">" )
        else:
            print("Opção inválida. Tente novamente.")
            resposta = input(">")

    print ("Digite a combinação desejada:")
    categoria = input(">")

    while categoria in categorias or categoria not in todascat:
        if categoria in categorias:
            print("Essa combinação já foi utilizada.")
            categoria = input(">")
        elif categoria not in todascat:
            print("Combinação inválida. Tente novamente.")
            categoria = input(">")
    categorias.append(categoria)

    tudo = []
    for ponctos in rolados:
        tudo.append(ponctos)
    for puntos in guardados:
        tudo.append(puntos)

    cartela = faz_jogada(tudo, categoria, cartela)

    i+=1
    
imprime_cartela(cartela)
soma = 0
for oi, tipo in cartela.items():
    for num in tipo.values():
        soma+=int(num)

if cartela['regra_simples'][1]+cartela['regra_simples'][2]+cartela['regra_simples'][3]+cartela['regra_simples'][4]+cartela['regra_simples'][5]+cartela['regra_simples'][6]>=63:
    soma+=35

print("Pontuação total:",str(soma))