# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:50:00 2019

@author: Daniel

Jogo Nim - projeto programa completo, aula 06 do curso Introdução à Ciência
da Computação com Python Parte 1 (Coursera/USP)
"""
#------------------------------------------------------------------------------

def computador_escolhe_jogada(n, m):
    if n <= m:
        jogada = n
    else:
        jogada = n % (m + 1)
        
    return jogada

#------------------------------------------------------------------------------
    
def usuario_escolhe_jogada(n, m):
    jogada_valida = False
                
    while not jogada_valida:
        jogada = int(input('Quantas peças você vai tirar? '))
        if jogada > m or jogada <= 0:
            print('\nOops! Jogada inválida! Tente de novo.')
        else:
            jogada_valida = True
    
    return jogada

#------------------------------------------------------------------------------
    
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    jogador = ''
    
    # Primeira rodada - definir jogador
    if n % (m + 1) == 0:
        jogador = 'Você'
        print('\nVocê começa!')
    else:
        jogador = 'O computador'
        print('\nComputador começa!')
        
    # Varíavel de controle
    terminou = False
    
    while not terminou:
        if jogador == 'Você':
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            n -= pecas_retiradas
            exibe_jogada(jogador, pecas_retiradas, n)
            
            if n != 0:
                jogador = 'O computador' # Alterna para o computador
            else:
                terminou = True
        else:
            pecas_retiradas = computador_escolhe_jogada(n, m)
            n -= pecas_retiradas
            exibe_jogada(jogador, pecas_retiradas, n)
            
            if n != 0:
                jogador = 'Você' # Alterna para o usuário
            else:
                terminou = True
                
    print('Fim de jogo!', jogador, 'ganhou!')
    
    '''
    Jogo finalizado. Dessa forma, o jogador corrente é o vencedor.
    Retorno para contar os vencedores em um campeonato.
    '''
    return jogador 

#------------------------------------------------------------------------------
    
def campeonato():
    vitorias_computador = 0
    vitorias_usuario = 0
    rodada = 1
    
    while rodada <=3:    
        print('')
        print('**** Rodada', rodada, '****')
        vencedor = partida()
        
        if vencedor == 'Você':
            vitorias_usuario += 1
        else:
            vitorias_computador += 1
            
        rodada += 1
        
    print('')
    print('**** Final do campeonato! ****')
    print('')
    print('Placar: Você', vitorias_usuario, 'X', vitorias_computador, 'Computador')
    

#------------------------------------------------------------------------------
    
def exibe_jogada(jogador, pecas_retiradas, pecas_restantes):
    # Exibe o número de peças retiradas
    if pecas_retiradas == 1:
        print('')
        print(jogador, 'tirou uma peça.')
    else:
        print('')
        print(jogador, 'tirou', pecas_retiradas, 'peças.')
        
    # Exibe o número de peças restantes
    if pecas_restantes == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    elif pecas_restantes > 1:
        print('Agora restam', pecas_restantes, 'peças no tabuleiro.')


#------------------------------------------------------------------------------
    
def main():
    escolha = int(input('Bem-vindo ao jogo do NIM! Escolha:\
                        \n\n1 - para jogar uma partida isolada\
                        \n2 - para jogar um campeonato '))
    
    if escolha == 1:
        print('\nVoce escolheu uma partida!')
        partida()
    else:
        print('\nVoce escolheu um campeonato!')
        campeonato()
        
#------------------------------------------------------------------------------

main()

    
