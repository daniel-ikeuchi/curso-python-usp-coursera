# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:50:00 2019

@author: Daniel

Jogo Nim - projeto programa completo, aula 06 do curso Introdução à Ciência
da Computação com Python Parte 1 (Coursera/USP)
"""

def computador_escolhe_jogada(n, m):
    return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
                
    while not jogada_valida:
        jogada = int(input('Quantas peças você vai tirar? '))
        if jogada > m:
            print('\nOops! Jogada inválida! Tente de novo.')
        else:
            jogada_valida = True
    
    return jogada
    
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    terminou = False
    primeira_rodada = True
    vencedor = ''
    
    while not terminou:
        if primeira_rodada:
            primeira_rodada = False
            if n % (m + 1) == 0:
                print('\nVocê começa!')
                pecas_retiradas = usuario_escolhe_jogada(n, m)
                n -= pecas_retiradas
            
                if n != 0:
                    if pecas_retiradas == 1:
                        print('\nVocê tirou uma peça.')
                    else:
                        print('\nVocê tirou', pecas_retiradas, 'peças.')
                    if n == 1:
                        print('Agora resta apenas uma peça no tabuleiro.')
                    elif n > 1:
                        print('Agora restam', n, 'peças no tabuleiro.')
                    computador_escolhe_jogada(n, m)
                else:
                    terminou = True
                    vencedor = 'Você'
            else:
                print('\nComputador começa!')
                pecas_retiradas = computador_escolhe_jogada(n, m)
                n -= pecas_retiradas
            
                if n != 0:
                    if pecas_retiradas == 1:
                        print('\nO computador tirou uma peça.')
                    else:
                        print('\nO computador tirou', pecas_retiradas, 'peças.')
                    if n == 1:
                        print('Agora resta apenas uma peça no tabuleiro.')
                    elif n > 1:
                        print('Agora restam', n, 'peças no tabuleiro.')
                    usuario_escolhe_jogada(n, m)
                else:
                    terminou = True
                    vencedor = 'O computador'
        else:
            
                
    print('Fim de jogo!', vencedor, 'ganhou!')
    
def campeonato():
    return True
    
def main():
    escolha = int(input('Bem-vindo ao jogo do NIM! Escolha:\
                        \n\n1 - para jogar uma partida isolada\
                        \n2 - para jogar um campeonato '))
    
    if escolha == 1:
        print('\nVoce escolheu uma partida!')
        partida()
    else:
        print('\nVoce escolheu um campeonato!')
        
#------------------------------------------------------------------------------

main()
    