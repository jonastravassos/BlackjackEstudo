# BlackjackEstudo
Método de Monte Carlo Aplicado ao Blackjack
Projeto de Cálculo Numérico

Descrição geral
Este projeto implementa uma simulação do jogo Blackjack utilizando o Método de Monte Carlo.
O objetivo é analisar estatisticamente o comportamento probabilístico do jogo, testar diferentes estratégias do jogador e avaliar o valor esperado das apostas ao longo de muitas rodadas.
O trabalho foi desenvolvido como projeto da disciplina de Cálculo Numérico, utilizando programação orientada a objetos e métodos de aproximação estocástica.

Motivação
O jogo Blackjack é um excelente caso de estudo por combinar probabilidade, tomada de decisão e processos estocásticos.
A simulação Monte Carlo permite avaliar estratégias de forma prática, aproximando resultados reais através de múltiplas execuções.
O projeto também reforça conceitos de:

1 - Probabilidade e Estatística
2 - Lógica de Programação
3 - Otimização de Algoritmos
4 - Estruturas de Dados
5 - Cálculo Numérico (aproximações por amostragem)

O grande motivo por trás desse projeto é saber se esse jogo (blackjack) pode ser lucrativo ao jogador ou é um jogo feito para perder dinheiro, usando métodos matemáticos e computacionais para fundamentar a resposta.

Regras do Blackjack
No jogo, o jogador joga contra o “dealer”, nome de quem distribui as cartas, normalmente funcionário do cassino também conhecido como “crupiê”, e o objetivo do jogo é chegar o mais próximo de 21 sem ultrapassar. Antes de começar, o jogador faz a sua aposta. 

Em cada rodada, tanto o jogador quanto o dealer têm duas cartas, porém o jogador só pode ver a segunda carta do dealer enquanto o valor da outra permanece oculto. O jogador tem várias ações no jogo, como pedir, pede mais uma carta do baralho, parar, o jogador para de receber carta e em seguida o dealer joga o jogo, dobrar, dobra a aposta, recebe uma carta e para imediatamente, e dividir, divide a mão atual (conjunto de cartas em posse) caso o jogador tenha duas cartas de mesmo valor, tendo duas mãos independentes com o mesmo valor da aposta inicial, no entanto, se o jogador dividir dois ases, geralmente só é distribuída uma carta a cada mão e não é considerado um blackjack caso essa carta forme um 21, ou seja, se tiver 21, ele paga 1:1, não 3:2, embora muitos cassinos proíbem dobrar após dividir ases por ser muito vantajoso ao jogador mesmo que ele receba apenas uma carta em cada mão. 

Cada carta tem seu valor, cartas numéricas têm seu valor naquele número, ou seja, se a carta tem 5 como valor, é esse 5 que vai contar na soma das cartas, e cartas não numéricas valem 10, exceto o ás, que tem o valor inicial igual a 11 se o valor das cartas for menor ou igual 21 e igual a 1 caso contrário, sendo considerado a melhor carta por ter seu valor adaptado. O naipe da carta não interfere na contagem. 

Quando o jogador para, o dealer revela a carta que estava virada e pede cartas enquanto o valor total de suas cartas for menor que 17, e a contabilização da vitória só ocorre depois que o dealer atinge esse objetivo. O primeiro que ultrapassar 21 perde (estouro), o primeiro que chegar a 21 ganha e se nenhum dos cenários anteriores forem verdadeiros, ganha quem tiver mais próximo de 21. Se, no final da rodada, os dois tiverem a mesma pontuação, é considerado empate e a aposta é devolvida ao jogador. 

Se um deles, jogador ou dealer, tiverem um ás e uma carta que vale 10 logo nas duas primeiras cartas, o portador das cartas ganha automaticamente com um “blackjack”, mas, para o jogador, o blackjack paga 3:2. Então, se ele apostou R$ 100,00, em vez de receber R$ 100,00 como é normalmente, ele recebe R$ 50,00. 

Se o dealer tem um ás à mostra, o jogador pode fazer uma “aposta do seguro”, em que o jogador aposta se o dealer tem um blackjack ou não. Se tiver, ele ganha essa aposta paralela, de até metade da aposta inicial, que paga 2:1. Assim, supondo que o jogador aposte R$ 100,00 inicialmente, se o dealer tiver um blackjack e o jogador fizer a aposta do seguro, ele ganha R$ 100,00 pelo seguro, mas perde R$ 100,00 pelo blackjack, ficando com um lucro de R$ 0,00. 

Metodologia
De forma resumida, eu fiz um programa que joga blackjack 1 milhão de vezes e registra todas as informações relevantes, como número de vítorias, de derrotas, de empates, de blackjacks, de busts (estouro) e do saldo do jogador após as 1 milhão de rodadas começando em R$ 0,00.

Além disso, a pontuação do jogador e a carta visível do dealer foram registradas numa matriz. Isso serve para conclusões do tipo: "Se o jogador adotar essa estratégia, tiver essa pontuação e a carta visível for essa, a probabilidade de vencer é x%". Esse tipo de registro é essencial, pois o tipo de probabilidade envolvido aqui é a probabilidade condicional, já que o número de combinações e cenários diferentes que podem acontecer é bastante alto para analisar analiticamente.

As estratégias usadas foram as seguintes:
Parar em duas cartas - O jogador para em duas cartas, o programa registra a pontuação e a carta do dealer numa matriz e depois faz a contabilidade de vitórias, de derrotas e de empates. Por exemplo, se o jogador tiver 20H e a carta visível for 2, a probabilidade de o jogador ganhar é cerca de 75%. No entanto, se tiver 20H e a carta for um ás, a probabilidade de ganhar é cerca de 50%, o que mostra que o ás é a melhor carta desse jogo.

Pedir até L - O jogador pede cartas até atingir um limite. Por exemplo, se esse limite for 17, o jogador pede cartas até atingir pelo menos 17 pontos. A pontuação registrada é pontuação antes da última carta. Por exemplo, digamos que o jogador tenha 11H pontos, pede mais uma carta e fica com 18H, a pontuação registrada no código será 11H, pois foi a última pontuação antes de atingir pelo menos 17 pontos. Se ele tinha 11H, pediu uma, ficou 13H, pediu outra, ficou com 20H, a pontuação registrada será 13H. Se a pontuação do jogador já for maior ou igual a 17 pontos logo nas duas cartas, será essa a pontuação registrada.   

Nas últimas atualizações do código, com o intuito de minimizar a perda do jogador, foi feito uma seguinte otimização nas estratégias: dobrar a aposta em determinadas condições. Foi notado que a estratégia que otimiza o lucro do jogador é a de pedir até 17 e que dobrar a aposta quando a pontuação for 11 e a carta do dealer não for um ás, por exemplo, a chance de ganhar é maior que 50%. Conclui-se, então, que se o jogador tiver 11 pontos, é aconselhável que ele dobre a aposta a menos que a carta visiível seja um ás, porque nesse caso a probabilidade de ganhar é menor que 50%.

Resultados
1 - A melhor estratégia de todas dá um prejuízo de aproximadamente R$ 100.000,00 ao jogador ao longo de 1 milhão de rodadas.
2 - Dobrar em condições específicas reduz a perda em cerca de R$ 20.000,00 ou mais ao jogador.
3 - Dependendo da carta do dealer, ter 8 a 10 pontos pedindo até 17 aumentam drasticamente as chances de ganhar.
4 - Por enquanto, não há uma otimização que faça o jogador ter lucro postivo no longo prazo, mas isso é um outro objeto de estudo.

Conclusão
O Método de Monte Carlo se mostrou extremamente eficiente para estimar o valor esperado do Blackjack e demonstrar matematicamente que o jogo é desfavorável ao jogador comum.
Apesar disso, estratégias inteligentes conseguem reduzir parcialmente o prejuízo, o que abre espaço para futuras explorações, como contagem de cartas e otimização de políticas. Esta é uma prova científica que apostar nesse jogo não compensa.

Possíveis expansões
1 - Contagem de cartas (Hi-Lo)
2 - Estratégia básica completa
3 - MDP / Reinforcement Learning
4 - Análise da vantagem da casa
5 - Análises gráficas mais elaboradas
6 - Cálculo rápido usando NumPy ou Cython
7 - Investigar a aposta do seguro
8 - Investigar a divisão de cartas.