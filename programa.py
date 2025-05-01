from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela

import random


numero_de_dados = 5
cartela = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}
cartela_avancada = {'sem_combinacao': -1, 'quadra': -1, 'full_house': -1, 'sequencia_baixa': -1, 'sequencia_alta': -1, 'cinco_iguais': -1}
jogadas_feitas = []
rodada = 1
regras_simples = ['1', '2', '3', '4', '5', '6']

while rodada <= 12 and len(jogadas_feitas) < 12:
    dados_rolados = rolar_dados(numero_de_dados)
    dados_guardados = []
    rerrolagens = 0
    marcou_pontuacao_na_rodada = 0

    print(f"Rodada {rodada}:")
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    while not marcou_pontuacao_na_rodada:
        opcao = input("Digite 1 para guardar, 2 para remover, 3 para rerrolar ou 0 para marcar:")

        if opcao == '1':
            indice = int(input("Índice do dado a guardar (0 a 4):"))
            if 0 <= indice < len(dados_rolados):
                resultado = guardar_dado(dados_rolados, dados_guardados, indice)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]
        elif opcao == '2':
            if dados_guardados:
                indice = int(input("Índice do dado a remover (0 a 4):"))
                if 0 <= indice < len(dados_guardados):
                    resultado = remover_dado(dados_rolados, dados_guardados, indice)
                    dados_rolados = resultado[0]
                    dados_guardados = resultado[1]
            else:
                print("Sem dados para remover.")
        elif opcao == '3':
            if rerrolagens < 2:
                dados_a_rolar = numero_de_dados - len(dados_guardados)
                novos_dados = rolar_dados(dados_a_rolar)
                dados_rolados = novos_dados + dados_guardados
                dados_guardados = []
                rerrolagens += 1
            else:
                print("Sem rerrolagens.")
        elif opcao == '0':
            combinacao = input("Qual combinação marcar?")
            if combinacao in regras_simples or combinacao in cartela_avancada:
                if combinacao not in jogadas_feitas:
                    dados_pontuar = dados_rolados[:]
                    if combinacao in regras_simples:
                        num = int(combinacao)
                        cartela[num] = calcula_pontos_regra_simples(dados_pontuar)[num]
                    elif combinacao in cartela_avancada:
                        pontuacoes = calcula_pontos_regra_avancada(dados_pontuar)
                        cartela_avancada[combinacao] = pontuacoes[combinacao]
                    jogadas_feitas.append(combinacao)
                    marcou_pontuacao_na_rodada = 1
                else:
                    print("Já marcado.")
            else:
                print("Inválido.")

    rodada += 1

pontuacao_total = 0
for valor in cartela.values():
    if valor != -1:
        pontuacao_total += valor
for valor in cartela_avancada.values():
    if valor != -1:
        pontuacao_total += valor

bonus = 0
soma_simples = 0
for valor in cartela.values():
    if valor != -1:
        soma_simples += valor
if soma_simples >= 63:
    bonus = 35
    pontuacao_total += bonus

print("Pontuação Final:", pontuacao_total)