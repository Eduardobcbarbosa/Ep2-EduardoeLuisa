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
    marcou_pontuacao_na_rodada = False

    while not marcou_pontuacao_na_rodada:
        opcao = input("Digite 1 para guardar, 2 para remover, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        if opcao == '1':
            indice = int(input("Índice do dado a guardar (0 a 4):"))
            if 0 <= indice < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

        elif opcao == '2' and dados_guardados:
            indice = int(input("Índice do dado a remover (0 a 4):"))
            if 0 <= indice < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)

        elif opcao == '3' and rerrolagens < 2:
            dados_a_rolar = numero_de_dados - len(dados_guardados)
            novos_dados = rolar_dados(dados_a_rolar)
            dados_rolados = novos_dados + dados_guardados
            dados_guardados = []
            rerrolagens += 1

        elif opcao == '4':
            imprime_cartela({'regra_simples': cartela, 'regra_avancada': cartela_avancada})

        elif opcao == '0':
            combinacao = input("Qual combinação marcar?")
            if combinacao in regras_simples or combinacao in cartela_avancada:
                if combinacao not in jogadas_feitas:
                    dados_pontuar = dados_rolados[:]
                    cartela_de_pontos = {'regra_simples': cartela, 'regra_avancada': cartela_avancada}

                    if combinacao in regras_simples:
                        categoria_int = int(combinacao)
                        pontuacao_simples = 0
                        pontos_contagem = calcula_pontos_regra_simples(dados_pontuar)
                        if categoria_int in pontos_contagem:
                            pontuacao_simples = pontos_contagem[categoria_int] * categoria_int
                        cartela_de_pontos['regra_simples'][categoria_int] = pontuacao_simples
                    elif combinacao in cartela_avancada:
                        cartela_de_pontos = faz_jogada(dados_pontuar, combinacao, cartela_de_pontos)

                    cartela = cartela_de_pontos['regra_simples']
                    cartela_avancada = cartela_de_pontos['regra_avancada']
                    jogadas_feitas.append(combinacao)
                    marcou_pontuacao_na_rodada = True
                else:
                    print("Essa combinação já foi utilizada.")
                    marcou_pontuacao_na_rodada = True
            else:
                print("Combinação inválida. Tente novamente.")

    rodada += 1

print(f"Tipo de cartela antes da impressão final: {type(cartela)}")
print(f"Conteúdo de cartela antes da impressão final: {cartela}")
imprime_cartela({'regra_simples': cartela, 'regra_avancada': cartela_avancada})

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

print("Pontuação total:", pontuacao_total)