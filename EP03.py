"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Tobias dos Santos Neto
  NUSP : 11848688
  Turma: 2020221
  Prof.: Renata Wassermann

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

import math

DELTA_T = 0.1
GRAVIDADE = 2

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP3.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

def leArquivo(nomeArquivo = 'entrada.txt'):
    '''
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    Entrada: arquivo cujo nome está armazenado em nomeArquivo.
             Por default, é 'entrada.txt'
    Saída: uma lista de listas, onde o primeiro elemento é uma
           lista de inteiros [m, n] (dimensões da matriz) e os
           elementos subsequentes são listas que representam as
           característica lidas dos Pokémons na forma:
                [nome, raio, x, y]
    '''

    fin = open(nomeArquivo)
    pokemons = fin.read()
    pokemons = pokemons.split('\n')
    for i in range(len(pokemons)):
        pokemons[i]=pokemons[i].split()
    return pokemons


def criaMatriz(m, n):
    '''
    Esta função cria e retorna uma lista de listas.
    Entrada: dois inteiros que representam o número de linhas e
             o número de colunas da matriz.
    Saída: uma lista de m listas, cada uma com n elementos, todos
           inicializados com zeros.
    '''
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)
    
    return matriz


def populaMatriz(matriz, pokemons):
    '''
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    Entrada: matriz representada por uma lista de listas
    Saída: A matriz fornecida é modificada.
    '''
    for id in range(1,len(pokemons),1):
        raio=int(pokemons[id][1])
        xp=int(pokemons[id][2])
        yp=int(pokemons[id][3])
        preenchePokemon(matriz, id, xp, yp, raio)
    return 


def preenchePokemon(matriz, id, x, y, raio):
    '''
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)
    Entrada: matriz representada por uma lista de listas
             id é o número a preencher a matriz; para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente.
             x,y são as coordenadas do ponto central
             raio é a distância a ser guardada a partir do
             ponto central.
    Saída: A matriz fornecida é modificada.
    '''
    m=len(matriz)
    n=len(matriz[0])
    for i in range(y-raio,y+raio+1,1):
        for j in range(x-raio,x+raio+1,1):
            if 0<i<m and 0<j<n:
                matriz[i][j] = id
    return matriz


def removePokemon(matriz, id, pokemons):
    '''
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    Entrada: matriz representada por uma lista de listas;
             id é o número a preencher a matriz, para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente;
             pokemons lista contendo as listas que representam pokémons.
    Saída: A matriz fornecida é modificada.
    '''
    m=len(matriz)
    n=len(matriz[0])
    for i in range(m):
        for j in range(n):
            if matriz[i][j]==id:
                matriz[i][j] = 0
    pokemons.pop(id)
    return
    


def imprimeMatriz(matriz):
    '''
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical, 
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    '''
    m=len(matriz)
    n=len(matriz[0])
    i=m-1
    while i >= 0:
        for j in range(n):
            if matriz[i][j] == 0:
                print('.', end=' ')
            else:
                print(matriz[i][j], end= ' ')
        print()
        i=i-1
    return 


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    x = x + (vx*dt)
    y = y + (vy*dt)-(GRAVIDADE)*(dt*dt)/2
    return x,y
    


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    vx = vx
    vy = vy - (GRAVIDADE*dt)
    return vx, vy
    


def grau2Radiano(theta):
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''
    radiano = (theta*math.pi)/180
    return radiano
    
def copiaMatriz(matriz):
	m=len(matriz)
	n=len(matriz[0])
	copia = []
	for i in range(m):
		copia.append([])
		for j in range(n):
			copia[i].append(matriz[i][j])
	return copia



def main():
    nomeArquivo = input("Digite o nome do arquivo: ")
    pokemons = leArquivo(nomeArquivo)
    m = int(pokemons[0][0])
    n = int(pokemons[0][1])
    matriz = criaMatriz(m, n)
    populaMatriz(matriz, pokemons)
    N = int(input("Digite o numero N de pokebolas: "))
    capturado = False
    x = 0
    while N > 0 and len(pokemons) > 1:
        if capturado:
            x = round(x)
        else:
            xt = int(input("Digite a coordenada x do treinador: "))
            x = xt
        print("pokebolas disponivels = %d"%(N))
        print("Estado atual do jogo: ")
        matriz[0][x] = 'T'
        imprimeMatriz(matriz)
        velocidade = int(input("Digite a velocidade de lancamento m/s: "))
        theta = int(input("Digite o angulo de lancamento em graus: "))
        vx = (velocidade*math.cos(grau2Radiano(theta)))
        vy = (velocidade*math.sin(grau2Radiano(theta)))
        dt = DELTA_T
        y = 0
        velocidades = 0
        posicoes = 0
        capturado = False
        chao = False
        matriz[0][xt] = 0
        copia = copiaMatriz(matriz)
        while x < len(matriz[0]) and not capturado and not chao:
            velocidades = atualizaVelocidade(vx, vy, dt)
            posicoes = atualizaPosicao(x, y, vx, vy, dt)
            vx = velocidades[0]
            vy = velocidades[1]
            x = posicoes[0]
            y = posicoes[1]
            if 0 < round(x) < len(matriz[0]) and 0 <= round(y) < len(matriz):
                if matriz[round(y)][round(x)] != 0 and matriz[round(y)][round(x)] != 'o':
                    id = matriz[round(y)][round(x)]
                    copia[round(y)][round(x)] = 'o'
                    capturado = True
                else:
                    copia[round(y)][round(x)] = 'o'
            if y < 0:
                chao = True
        print("Representacao grafica do lancamento: ")
        copia[0][xt] = 'T'
        imprimeMatriz(copia)
        
        if capturado:
            print("Um %s foi capturado!"%(pokemons[id][0]))
            removePokemon(matriz, id, pokemons)
        else:
            print("O lancamento nao capturou pokemon algum")
        N-=1
    if len(pokemons) > 1:
        print("Jogo Encerrado")
    else:
        print("Parabens! Todos pokemons foram capturados")

main ()
