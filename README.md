# MAC0115-USP
Introdução à Computação para Ciências Exatas e Tecnologia. Segundo Semestre (2020.2)

A última avaliação da disciplina e seu enunciado podem ser vistos aqui! A avaliação consistiu na criação de um mini-game de Pokemon.

O jogo começa pedindo o nome de um arquivo de entrada. Tal arquivo possui dados como: quantidade de linhas e colunas de uma matriz, o nome dos pokemons que estarão nessa matriz e seus respectivos dados (raio do pokemon e coordenadas do mesmo na matriz). Em seguida, é necessário informar a quantidade de pokebolas que serão utilizadas, a coordenada inicial do treinador, a velocidade de lançamento (em m/s) e o ângulo de lançamento (em °).

Depois de informar os parâmetros iniciais, é realizado a simulação do lançamento e seu resultado: atingiu algum pokemon (se a pokebola tocar em qualquer ponto que seja ocupado por um pokemon e seu raio) ou nenhum pokemon foi atingido (se a pokebola atravessar a matriz sem ter contato com algum ponto que possua um pokemon).

* *Caso o pokemon não seja atingido*:

Se ainda houver pokebolas restantes, será necessário informar novos valores dos parâmetros necessários (coordenada, velocidade e ângulo de laçamento).

* *Caso o pokemon seja atingido*:

Se ainda houver pokebolas restantes e pokemons na matriz, a nova coordenada do treinador será o ponto em que a pokebola capturou o último pokemon. Assim, será necessário inserir os novos parâmetros de lançamento.

#

O jogo é encerrado quando todos os pokemons são capturados ou caso não sobre pokebolas.
