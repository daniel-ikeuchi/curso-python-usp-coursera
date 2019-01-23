# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:53:50 2019

@author: Daniel

Jogo COH-PIAH - projeto programa completo, semana 09 do curso Introdução à 
Ciência da Computação com Python Parte 1 (Coursera/USP)
"""
#------------------------------------------------------------------------------
import re

def le_assinatura():
    '''
    A funcao le os valores dos tracos linguisticos do modelo e devolve uma 
    assinatura a ser comparada com os textos fornecidos
    '''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

#------------------------------------------------------------------------------
    
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + 
                      " (aperte enter para sair): ")

    return textos

#------------------------------------------------------------------------------

def tamanho_medio_palavras(texto):
    '''
    Essa funcao recebe um texto e devolve o tamanho médio das palavras
    '''
    total_caracteres = 0
    lista_palavras = re.split(r'[.,!?\s]+', texto)
    lista_palavras.remove('')
    
    for p in lista_palavras:
        total_caracteres += len(p)
        
    return total_caracteres / len(lista_palavras)
     
#------------------------------------------------------------------------------

def type_token(texto):
    '''
    Essa função recebe um texto e devolve a relação type-token das palavras
    '''
    lista_palavras = re.split(r'[.,!?\s]+', texto)
    
    if lista_palavras[-1] == '':
        del lista_palavras[-1]    
        
    nro_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    
    return nro_palavras_diferentes / len(lista_palavras)

#------------------------------------------------------------------------------
    
def hapax_legomana(texto):
    '''
    Essa função recebe um texto e devolve a razão hapax legomana do texto
    '''
    lista_palavras = re.split(r'[.,!?\s]+', texto)
    
    if lista_palavras[-1] == '':
        del lista_palavras[-1]    
    
    nro_palavras_unicas = n_palavras_unicas(lista_palavras)
    
    return nro_palavras_unicas / len(lista_palavras)

#------------------------------------------------------------------------------

def tamanho_medio_sentencas(texto):
    '''
    Essa função recebe um texto e devolve o tamanho médio das sentenças do
    mesmo
    '''
    sentencas = separa_sentencas(texto)
    total_caracteres = 0
    
    for sentenca in sentencas:
        total_caracteres += len(sentenca)
        
    return total_caracteres / len(sentencas)

#------------------------------------------------------------------------------    
    
def complexidade_media_sentencas(texto):
    '''
    Esta função recebe um texto e devolve a complexidade média das suas 
    sentenças
    '''
    sentencas = separa_sentencas(texto)
    total_frases = 0
    
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        total_frases += len(frases)
        
    return total_frases / len(sentencas)

#------------------------------------------------------------------------------
    
def tamanho_medio_frases(texto):
    '''
    Esta função recebe um texto e devolve o tamanho médio das frases do
    mesmo
    '''
    sentencas = separa_sentencas(texto)
    total_caracteres = 0
    nro_frases = 0
    
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        nro_frases += len(frases)
        for frase in frases:
            total_caracteres += len(frase)
            
    return total_caracteres / nro_frases

#------------------------------------------------------------------------------
    
def separa_sentencas(texto):
    '''
    A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    '''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
        
    return sentencas

#------------------------------------------------------------------------------
    
def separa_frases(sentenca):
    '''
    A funcao recebe uma sentenca e devolve uma lista das frases dentro da 
    sentenca
    '''
    return re.split(r'[,:;]+', sentenca)

#------------------------------------------------------------------------------
    
def separa_palavras(frase):
    '''
    A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    '''
    return frase.split()

#------------------------------------------------------------------------------
    
def n_palavras_unicas(lista_palavras):
    '''
    Essa funcao recebe uma lista de palavras e devolve o numero de palavras que
    aparecem uma unica vez
    '''
    freq = dict()
    unicas = 0

    for palavra in lista_palavras:
        p = palavra.lower()

        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

#------------------------------------------------------------------------------
    
def n_palavras_diferentes(lista_palavras):
    '''
    Essa funcao recebe uma lista de palavras e devolve o numero de palavras 
    diferentes utilizadas
    '''
    freq = dict()

    for palavra in lista_palavras:
        p = palavra.lower()
        
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
            

    return len(freq)

#------------------------------------------------------------------------------
    
def compara_assinatura(as_a, as_b):
    '''
    Essa funcao recebe duas assinaturas de texto e deve devolver o
    grau de similaridade nas assinaturas.
    '''
    somatoria = 0
    
    for i in range(len(as_a)):
        somatoria += abs(as_a[i] - as_b[i])
        
    return somatoria / 6

#------------------------------------------------------------------------------
    
def calcula_assinatura(texto):
    '''
    Essa funcao recebe um texto e deve devolver a assinatura do 
    texto.
    '''
    wal = tamanho_medio_palavras(texto)
    ttr = type_token(texto)
    hlr = hapax_legomana(texto)
    sal = tamanho_medio_sentencas(texto)
    sac = complexidade_media_sentencas(texto)
    pal = tamanho_medio_frases(texto)
    
    return [wal, ttr, hlr, sal, sac, pal]

#------------------------------------------------------------------------------
    
def avalia_textos(textos, ass_cp):
    '''
    Essa funcao recebe uma lista de textos e deve devolver o 
    numero (1 a n) do texto com maior probabilidade de ter sido infectado por 
    COH-PIAH.
    '''
    infectado = 0
    similaridade = 1000
    
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        
        if compara_assinatura(ass_cp, assinatura) < similaridade:
            infectado += 1
            similaridade = compara_assinatura(ass_cp, assinatura)
            
    return infectado
    

#------------------------------------------------------------------------------
    
def main():
    assinatura = le_assinatura()
    textos = le_textos()
    nro_texto_infectado = avalia_textos(textos, assinatura)
    
    print('\nO autor do texto', nro_texto_infectado, 'está infectado com COH-PIAH')        
    
#------------------------------------------------------------------------------
    
main()