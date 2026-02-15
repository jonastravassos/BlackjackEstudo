# BlackjackEstudo
Método de Monte Carlo Aplicado ao Blackjack

Projeto de Cálculo Numérico

Descrição geral

Este projeto implementa uma simulação do jogo Blackjack utilizando o Método de Monte Carlo.
O objetivo é analisar estatisticamente o comportamento probabilístico do jogo, testar diferentes estratégias do jogador e avaliar o valor esperado das apostas ao longo de muitas rodadas.
O trabalho foi desenvolvido como projeto da disciplina de Cálculo Numérico, utilizando inicialmente programação orientada a objetos e métodos de aproximação estocástica.

Motivação
O jogo Blackjack é um excelente caso de estudo por combinar probabilidade, tomada de decisão e processos estocásticos.
A Simulação Monte Carlo permite avaliar estratégias de forma prática, aproximando resultados reais através de múltiplas execuções.
O projeto também reforça conceitos de:

1 - Probabilidade e Estatística

2 - Lógica de Programação

3 - Otimização de Algoritmos

4 - Estruturas de Dados

5 - Cálculo Numérico (aproximações por amostragem)

O grande motivo por trás desse projeto é saber se esse jogo (blackjack) pode ser lucrativo ao jogador ou é um jogo feito para perder dinheiro, usando métodos matemáticos e computacionais para fundamentar a resposta.

Regras do Blackjack
No jogo, o jogador joga contra o “dealer”, nome de quem distribui as cartas, normalmente funcionário do cassino também conhecido como “crupiê”, e o objetivo do jogo é chegar o mais próximo de 21 sem ultrapassar. Antes de começar, o jogador faz a sua aposta. 

Em cada rodada, tanto o jogador quanto o dealer têm duas cartas, porém o jogador só pode ver apenas uma carta do dealer enquanto o valor da outra permanece oculto. O jogador tem várias ações no jogo, tais como:

1 - Hit / Pedir - compra uma carta do baralho. Ao fazer isso, o jogador admite que sua mão, conjunto de cartas, pode melhorar e adquire uma carta para esse objetivo;


2 - Stop / Parar - o jogador para de receber cartas matendo a maão atual e em seguida o dealer joga o jogo, pedindo cartas até atingir 17 pontos;

3 - Double Down / Dobro ou Nada - dobra a aposta, recebe uma carta e para imediatamente, podendo ganhar o dobro se ganhar ou perder o dobro se perder;

4 - Split / Dividir - divide a mão atual caso o jogador tenha duas cartas de mesmo valor (por exemplo, dois oitos), tendo duas mãos independentes com o mesmo valor da aposta inicial, no entanto, se o jogador dividir dois ases, geralmente só é distribuída uma carta a cada mão e não é considerado um blackjack caso essa carta forme um 21, ou seja, se tiver 21, ele paga 1:1, não 3:2, embora muitos cassinos proíbem dobrar após dividir ases por ser muito vantajoso ao jogador mesmo que ele receba apenas uma carta em cada mão. O número máximo de divisões de cartas é 4.

5 - Insurance / Aposta do seguro - caso o dealer tenha um ás à mostra, ele oferece uma aposta paralela à aposta inicial. Ela vale até metade da aposta inicial e paga o dobro (pagamento 2:1) e consiste em apostar que o dealer tem um blackjack (um ás + qualquer carta que vale 10). Se o jogador fizer a aposta e vencer, ele perde a rodada porque o dealer tem um blackjack (a menos que o jogador tenha um blackjack também, o que configura empate), mas ganha a aposta do seguro, resultando em um lucro de R$ 0,00 (se o jogador apostou R$ 100,00 inicialmente e apostou R$ 50,00 no seguro, ele perde os R$ 100,00 por causa do blackjack, porém ganha 2 × R$ 50,00 = R$ 100,00). Entretanto, se o jogador fizer a aposta do seguro e perder (ou seja, o dealer não tem um blackjack), além de perder metade da aposta inicial, há uma alta probabilidade de o jogador também perder os R$ 100,00 porque o ás é a melhor carta desse jogo, podendo dar um prejuízo de R$ 150,00 nesse cenário hipotético.

Pontuação

Cada carta tem seu valor, cartas numéricas têm seu valor naquele número, ou seja, se a carta tem 5 como valor, é esse 5 que vai contar na soma das cartas, e cartas não numéricas valem 10, exceto o ás, que tem o valor inicial igual a 11 se o valor da mão for menor ou igual 21 e igual a 1 caso seja maior que 21, sendo considerado a melhor carta por ter seu valor adaptado. O naipe da carta não interfere na contagem. 

As pontuações são feitas da seguinte forma: soma dos valores da mão + mão com ás alto versus mão sem ás alto. Por exemplo, a pontuação 13H ('H' significa "Hard", enquanto 'S' significa indica "Soft") que a soma dos valores das cartas vale 13 pontos e nehnuma delas é um ás que vale 11, enquanto que 13S indica que a soma dos valores das cartas vale 13 pontos e uma delas é um ás que vale 11 pontos.

Quando o jogador para, o dealer revela a carta que estava virada e pede cartas enquanto o valor total de suas cartas for menor que 17, e a contabilização da vitória só ocorre depois que o dealer atinge esse objetivo. O primeiro que ultrapassar 21 perde (bust / estouro), o primeiro que chegar a 21 ganha e se nenhum dos cenários anteriores forem verdadeiros, ganha quem estiver mais próximo de 21. Se, no final da rodada, os dois tiverem a mesma pontuação, é considerado empate e a aposta é devolvida ao jogador. 

Se um deles, jogador ou dealer, tiverem um ás e uma carta que vale 10 logo nas duas primeiras cartas, o portador das cartas ganha automaticamente com um “blackjack”, mas, para o jogador, o blackjack paga 3:2. Então, se ele apostou R$ 100,00, em vez de receber R$ 100,00 como é normalmente, ele recebe R$ 50,00. 

Metodologia

De forma resumida, eu fiz um programa que joga blackjack 1 milhão de vezes e registra todas as informações relevantes, como número de vítorias, de derrotas, de empates, de blackjacks, de busts (estouro) e do saldo do jogador após as 1 milhão de rodadas começando em R$ 0,00. No entanto, essa metodologia se mostrou muito ineficaz por dois simples motivos: Python é considerada uma linguagem lenta, então com apenas 1 milhão de rodadas, o código levava cerca 6 segundos para executado. Isso é muito lento considerando que são apenas 1 milhão de rodadas sendo divididas para 27 pontuações e 13 cartas do dealer no total, resultando numa matriz de 351 células (1 milhão dividido para mais 300 células). 

Outro problema era a chance de ocorrência de uma pontuação. A probabilidade de sair um 4H (2 + 2) é muito menor que a probabilidade de sair um 12H (2 + 10, 3 + 9, 4 + 8, 5 + 7, 6 + 6, 7 + 5, 8 + 4, 9 + 3, 10 + 2) e a probabilidade sair um 12S é muito menor que sair um 12H. Isso resulta numa ocorrência maior de certas pontuações, o que acaba enviesando a pesquisa. A solução para ambos os problemas era a seguinte: usar NumPy, uma bibliotecas de array para alto desempenho, e Cython, uma extensão do Python que permite rodar códigos com a velocidade de C, além de fixar as pontuações. Durante muito tempo, eu estudei essas duas ferramentas, testei na prática, realizei testes, me deparei com vários problemas, mas finalmente consegui um resultado bastante satisfatório.

Além disso, a pontuação do jogador e a carta visível do dealer foram registradas numa matriz. Isso serve para conclusões do tipo: "Se o jogador adotar essa estratégia, tiver essa pontuação e a carta visível for essa, a probabilidade de vencer é x%". Esse tipo de registro é essencial, pois o tipo de probabilidade envolvido aqui é a probabilidade condicional, já que o número de combinações e cenários diferentes que podem acontecer é bastante alto para analisar analiticamente.

Cython

Poucas pessoas conhecem essa ferramenta, ela não é exatamente uma biblioteca como se espera do Python, ela é uma extensão dele que deve ser instalada externamente. O ganho de performance é absurdo, os programas foram cerca de 100 vezes mais rápido em comparação ao Python puro durante meus testes. Isso possibilita fazer 270 milhões de rodadas, 1 milhão para cada pontuação, em apenas 16 a 17 segundos, um feito impossível no Python puro. O problema dela dela é que, para os programas terem um alto ganho de performance, todo o código deve ser escrito como se fosse C, com tipagens estáticas, com absolutamente nada exclusivo do Python como funções e classes, com programação estruturada em vez de orientada a objetos. Todavia, nada disso era um problema de fato exceto por uma pequena coisa essencial.

PRNG (Gerador de Números Pseudo-Aleatórios)

Essa parte é a mais importante da simulação. É absolutamente necessário que as cartas escolhidas sejam aleatórias, com uma distribuição perfeita, se não a pesquisa apresenta um viés. O uso da função randint() do Python no Cython está fora de questão e a função rand() de C tem uma distribuição imperfeita e é levemente enviesada. Para uma simulação de precisão quase que absoluta, o uso dessas funções é estritamente proibido, então, como resolver esse grande obstáculo?

A solução é fazer meu próprio PRNG, meu próprio algoritmo de geração de números pseudo-aleatórios. O algoritmo que escolhi foi o xorshift64, ele funciona da seguinte forma: quando a semente (seed) é fornecida, um inteiro positivo de 64 bits, faça operações bitwase (operações simples de bits) de modo que o modelo pareça caótico. Assim, uma pequena diferença na seed pode resultar num número totalmente diferente, parecendo de fato caótico.

Para a função randint() funcionar sem viés, basta pegar o número gerado por xorshift64() e extrair o resto da divisão do intervalo dos números. Se, por exemplo, eu queira gerar um inteiro aleatório de 0(min) a 9 (max), o interavalo é 9 - 0 + 1 = 10, depois faço xorshift64() % 10 + min.
Ainda implemento o loop da rejeição para garantir que todos os inteiros gerados tenha a mesma chance de ocorrer, mas isso não será detalhado aqui.

As estratégias usadas foram as seguintes:
Parar em duas cartas - O jogador para em duas cartas, o programa registra a pontuação e a carta do dealer numa matriz e depois faz a contabilidade de vitórias, de derrotas e de empates. Por exemplo, se o jogador tiver 20H e a carta visível for 2, a probabilidade de o jogador ganhar é cerca de 75%. No entanto, se tiver 20H e a carta for um ás, a probabilidade de ganhar é cerca de 50%, o que mostra que o ás é a melhor carta desse jogo.

Pedir até 17 - O jogador pede cartas até atingir um limite. Por exemplo, se esse limite for 17, o jogador pede cartas até atingir pelo menos 17 pontos. A pontuação registrada é a soma dos valores das duas cartas iniciais.

Resultados

Com todos os problemas resolvidos e com todas as regras implementadas corretamente, os resultados podem ser visualizados nas tabelas / matrizes gerados(as) no Excel. Cada linha da matriz é uma pontuação do jogador e cada coluna é a carta virada do dealer. Note que são 10 colunas em vez de 13 porque, apesar de haver 13 cartas diferentes, no blackjack 4 cartas valem 10, permitindo uma redução no número de colunas.
Duas simulações diferentes são executadas: uma em que a pontuação do jogador é fixada (270 milhões de rodadas) e outra que não é (100 milhões de rodadas).

1 - Parar sempre é a pior estratégia, dando um prejuízo médio de R$ 0,205226345 por rodada;
2 - Pedir até 17 é consideravelmente melhor que parar, dando um prejuízo médio de R$ 0,102059635 por rodada;
3 - Pedir até 17, mas parando em certas cartas do dealer é melhor ainda, o prejuízo médio é R$ 0,08042182 por rodada;
4 - Pedir até 17, parando ou dobrando em situações específicas consegue superar com o prejuízo médio de R$ 0,05853610 por rodada;

Note que o jogador sempre está no prejuízo, independentemente da estratégia utilizada, e que a matriz que diz qual é a melhor ação para cada pontuação e carta do dealer pode ser encontrada nos arquivos .xlsx, embora a divisão de cartas não foi implementada até esse momento (quando for, esta mesnagem será apaga).

Conclusão

O Método de Monte Carlo se mostrou extremamente eficiente para estimar o valor esperado do Blackjack e demonstrar matematicamente que o jogo é desfavorável ao jogador comum.
Apesar disso, estratégias inteligentes conseguem reduzir parcialmente o prejuízo, o que abre espaço para futuras explorações, como contagem de cartas e otimização de políticas. Esta é uma prova científica que apostar nesse jogo não compensa.

Possíveis expansões

1 - Contagem de cartas (Hi-Lo)

2 - Estratégia básica completa

3 - MDP / Reinforcement Learning

4 - Análise da vantagem da casa

5 - Análises gráficas mais elaboradas

6 - Tempo de execução menor com Numpy e Cython [Feito].

7 - Investigar a aposta do seguro

8 - Investigar a divisão de cartas.
