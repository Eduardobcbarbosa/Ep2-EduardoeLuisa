from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela

import random

cartela = {'regra_simples': {1: -1,2: -1,3: -1,4: -1,5: -1,6: -1},
           'regra_avancada' : {'sem_combinacao': -1,'quadra': -1,'full_house': -1,'sequencia_baixa': -1,'sequencia_alta': -1,'cinco_iguais': -1}}
imprime_cartela(cartela)

todas_categorias = ['1', '2', '3', '4', '5', '6', 'sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']
categorias = []
i=0
while i < 12:
    n = 5
    rol = rolar_dados(n)
    guard = []
    print('Dados rolados:', rol)
    print('Dados guardados:', guard)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    resp = input(">" )
    c = 0
    while resp!= '0':
        if resp=='1':
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            while indice >= len(rol):
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input(">"))
            armazen = guardar_dado(rol, guard, indice)
            print('Dados rolados:', rol)
            print('Dados guardados:', guard)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resp = input(">" )

        elif resp=='2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice_remover=int(input(">"))
            while indice_remover >= len(guard):
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice_remover=int(input(">"))
                remover = remover_dado(rol, guard, indice_remover)
                print('Dados rolados:', rol)
                print('Dados guardados:', guard)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                resp = input(">" )

        elif resp=='3':
            if c == 2:
                print("Você já usou todas as rerrolagens.")
                print('Dados rolados:', rol)
                print('Dados guardados:', guard)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                resp = input(">" )
            else:
                c += 1
                n = len(rol)
                rol = rolar_dados(n)
                print('Dados rolados:', rol)
                print('Dados guardados:', guard)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                resp = input(">" )

        elif resp=='4':
            imprime_cartela(cartela)
            print('Dados rolados:', rol)
            print('Dados guardados:', guard)
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            resp = input(">" )
        else:
            print("Opção inválida. Tente novamente.")
            resp = input(">")

    print ("Digite a combinação desejada:")
    categoria = input(">")

    while categoria in categorias or categoria not in todas_categorias:
        if categoria in categorias:
            print("Essa combinação já foi utilizada.")
            categoria = input(">")
        elif categoria not in todas_categorias:
            print("Combinação inválida. Tente novamente.")
            categoria = input(">")
            categorias.append(categoria)
    tudo = []
    for pontos in rol:
        tudo.append(pontos)
    for pontos2 in guard:
        tudo.append(pontos2)
    cartela = faz_jogada(tudo, categoria, cartela)

    i+=1

imprime_cartela(cartela)
soma = 0
for a, tipo in cartela.items():
    for num in tipo.values():
        soma+=int(num)

if cartela['regra_simples'][1]+cartela['regra_simples'][2]+cartela['regra_simples'][3]+cartela['regra_simples'][4]+cartela['regra_simples'][5]+cartela['regra_simples'][6]>=63:
    soma += 35

print("Pontuação total:",str(soma))