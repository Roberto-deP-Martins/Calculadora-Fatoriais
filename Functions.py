from math import factorial as fatorial, prod

operadores = ('x', 'X', '/', '+', '-')
# Operações que a calculadora é capaz de realizar. A lista tem variações de escrita de
# cada variação para facilitar o uso

def mostrarSolucao():
    resposta = input('Deseja ver a solução? [Sim/Não]').lower().strip()
    if resposta == 'sim':  # Sim
        return True
    elif resposta == 'não':  # Não
        return False


def explicaFatorial(num):
    for t in num:  # Para cada fatorial...
        print(*t, '=', fatorial(int(t[0])))  # Mostra os valores na lista do fatorial = o resultado do fatorial


def listaFatorialSimples(e):  # Gera uma matriz com listas com os valores n, n-1, n-2,...,1 dos valores digitados
    matriz = []
    e = e.split()  # Separa os fatoriais e operandos
    for t in e:
        if t not in operadores:  # Só adiciona à matriz listas com o elemento do qual se fará o fatorial
            t = t.split(sep='!')  # Remove a exclamação
            matriz.append([int(t[0])])  # Dá o int do número do qual se quer o fatorial
    for y in matriz:
        subtraendo = 1
        if y[0] >= 10:  # Se for um fatorial maior ou igual a 10
            for u in range(3):  # Dá n, n - 1, n - 2 , n - 3 e põe o sinal de multiplicação entre esses valores
                y.append('X')
                y.append(y[0] - subtraendo)
                subtraendo += 1
            y.append('...')  # Põe reticências para indicar que há valores entre os gerados e o último
            y.append(str(y[0] - (y[0] - 1)))  # Põe o último valor do fatorial (1) na lista
        else:
            for u in range(y[0] - 1):  # 9 ou menores
                y.append('X')  # Põe o sinal de multiplicação
                y.append(y[0] - subtraendo)
                subtraendo += 1
            y[-1] = str(y[-1])
    return matriz


def permutacao(x):
    while True:  # Repete para casos de erro de sintaxe
        x = x.strip('!')  # Remove o ponto de exclamação para que se possa fazer o fatorial
        try:
            resultadoPermutacao = fatorial(int(x))
            return resultadoPermutacao
        except ValueError:
            print('Algo deu errado e, possivelmente, não foi digitado um número. Por favor, tente novamente.')
            x = input('Digite o valor a ser permutado:').strip()


def arranjo(n, d):
    numeradorArranjo = n.strip('!')  # Remove o ponto de exclamação para que se possa fazer o fatorial
    numeradorArranjo = fatorial(int(numeradorArranjo))
    # Remove os parênteses e exclamações
    while True:  # Repete para casos de erro de sintaxe
        d = d.strip('(')
        d = d.strip(')!')
        # Faz uma lista com 3 itens, o minuendo (primeiro número da subtração), o '-', e o subtraendo
        numsSub = d.split()
        try:
            numsSub.remove('-')
            break
        except ValueError:  # Em caso de erro de sintaxe
            print('Opa! Algo deu errado. Possivelmente você esqueceu da subtração no divisor. '
                  'Por favor, tente novamente')
            d = input('Digite o divisor (A subtração, entre parênteses e seguida do ponto de exclamação, '
                      'que fica abaixo da barra de divisão)\nExemplo: (n - k)!:').strip()
    divisorArranjo = int(numsSub[0]) - int(numsSub[1])  # Faz a subtração, cujo fatorial é o divisor do arranjo
    divisorArranjo = fatorial(divisorArranjo)  # Faz o fatorial da subtração
    resultadoArranjo = numeradorArranjo // divisorArranjo
    return resultadoArranjo, numeradorArranjo, divisorArranjo, numsSub


def permutacaoComRepeticao(n, d):
    numeradorPermRepeticao = n.strip('!')  # Remove a exclamação, deixando apenas o valor inteiro cujo se quer fatorial
    numeradorPermRepeticao = int(numeradorPermRepeticao)
    resultadoNumeradorPermRepeticao = fatorial(numeradorPermRepeticao)
    divisorPermRepeticao = d.split()  # Separa a string do divisor em uma lista
    encontraFatorial(divisorPermRepeticao)
    trataLista(divisorPermRepeticao)
    # noinspection PyTypeChecker
    resultadoDivisorPermRepeticao = prod(divisorPermRepeticao)  # Faz a multiplicação dos fatoriais
    resultadoPermRepeticao = resultadoNumeradorPermRepeticao // resultadoDivisorPermRepeticao
    return resultadoPermRepeticao, resultadoNumeradorPermRepeticao, resultadoDivisorPermRepeticao


def arranjoComRepeticao(c):
    enunciadoPotenciacao = c.split(sep='^')  # Separa os elementos em uma lista que contém a base([0]) e a potência([1)
    basePotenciacao, potenciaPotenciacao = int(enunciadoPotenciacao[0]), int(enunciadoPotenciacao[1])
    resultadoPotenciacao = basePotenciacao ** potenciaPotenciacao  # Faz a potenciação
    return basePotenciacao, potenciaPotenciacao, resultadoPotenciacao


def combinacao(n, d):
    numeradorCombinacao = n.strip('!')
    numeradorCombinacao = fatorial(int(numeradorCombinacao))
    grafiaDeX = ''
    # Verifica se o sinal de multiplicação é maiúsculo ou minúsculo para que haja suporte para ambas as grafias.
    while True:  # Permite repetição em caso de erro de sintaxe
        if 'X' in d:
            grafiaDeX = 'maiusculo'
            indice = d.find('X')
        else:
            indice = d.find('x')
        subtracaoFat = d[indice:]  # Faz lista com o conteúdo do divisor até o espaço anterior ao sinal de multiplicação
        fat = d[0:indice:]  # Faz lista com  o conteúdo do divisor do sinal de multiplicação ao fim
        if grafiaDeX == 'maiusculo':
            subtracaoFat = subtracaoFat.strip('X')
        else:
            subtracaoFat = subtracaoFat.strip('x')
        subtracaoFat = subtracaoFat.lstrip()
        subtracaoFat = subtracaoFat.strip('(')
        subtracaoFat = subtracaoFat.strip()
        subtracaoFat = subtracaoFat.strip(')!')
        subtracaoFat = subtracaoFat.split()
        try:
            subtracaoFat.remove('-')  # Após a remoção de '-', resta apenas os dois números da subtração
            break  # Sai do loop se o usuário não tiver cometido erros
        except ValueError:  # Caso o usuário digite a fórmula de forma errada
            print("Opa! Parece que você esqueceu de escrever a subtração no divisor. Tente digitá-lo novamente")
            d = input('Digite o divisor (A subtração, entre parênteses, e em seguida, o fatorial):').strip()
    subtracaoCombinacao = int(subtracaoFat[0]) - int(subtracaoFat[1])
    subtracaoCombinacao = fatorial(subtracaoCombinacao)
    fat = fat.strip()
    fat = fat.split('!')  # Após a remoção de '!', resta apenas o valor cujo se quer o fatorial
    resultadoFatorial = fatorial(int(fat[0]))
    numFat = fat[0]  # Numero cujo se deseja obter o fatorial
    divisorCombinacao = subtracaoCombinacao * resultadoFatorial  # Faz a multiplicação dos fatoriais no divisor
    resultadoCombinacao = numeradorCombinacao // divisorCombinacao
    return numeradorCombinacao, divisorCombinacao, resultadoCombinacao, subtracaoFat, numFat


def subtracaoParaFat(sub):  # Faz a explicação do fatorial de subtraçãoes
    resultadoSubtracao = int(sub[0]) - int(sub[1])
    print(f'\nPrimeiro resolve-se a subtração ({sub[0]} - {sub[1]})'
          f'\n{resultadoSubtracao}!')
    fatSubtracao = listaFatorialSimples(str(resultadoSubtracao) + '!')
    print('\nCalcula-se os fatoriais:')
    explicaFatorial(fatSubtracao)


def encontraFatorial(e):
    for t in e:
        if t not in operadores:  # Qualquer elemento diferente dos presentes em operadores
            indice = e.index(t)  # Pega o indice dele na lista
            t = t.split(sep='!')  # Remove a exclamação, deixando só a string do número cujo fatorial é desejado
            e[indice] = fatorial(int(t[0]))  # Põe o fatorial do número na lista, na posição que ele ocupava antes


def trataLista(e):  # A lista agora contém os fatoriais e os sinais de multiplicação, que precisam ser removidos
    for t in e:
        if t in operadores:
            e.remove(t)  # Remove os operadores da lista, deixando apenas os fatoriais

