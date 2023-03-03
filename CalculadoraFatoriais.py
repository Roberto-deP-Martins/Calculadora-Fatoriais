from Functions import *

operacoesSuportadas = range(0, 6)
# Respostas possíveis para a pergunta quanto ao desejo do usuário de ver a solução ou não. Contém variações de escrita
# para facilitar o uso e reduzir erros.
while True:
    operacao = input("Digite o número da operação desejada:\n[1] - Permutação    [2] - Arranjo    [3] - Permutação Com Repetição     [4] - Arranjo Com Repetição     [5] - Combinação\nOu pressione 'Enter' para encerrar: ")
    operacao = 0 if operacao == '' else int(operacao)
    # Se valor operação não for válido, dá-se um aviso e se pede mais uma vez a operação
    if operacao not in operacoesSuportadas:
        print('Operação não suportada, por favor digite uma operação suportada')
    # Daqui pra frente será feito o cálculo da operação digitada, que é conferida ao verificar o valor inteiro
    elif operacao == 1:
        while True:
            numPermutado = input('Digite o valor a ser permutado:').strip()
            if len(numPermutado) == 0:  # Caso o usuário não digite um valor
                print("Parece que você não digitou um valor. Por favor, tente novamente.")
            elif len(numPermutado.split()) > 1:  # Se houver mais de um número digitado
                print("Parece que você digitou mais de um valor ou cometeu outro erro de escrita. "
                      "Por favor, tente novamente.")
            else:
                break
        resultado = permutacao(numPermutado)
        print(resultado)
        verSolucao = mostrarSolucao()
        while verSolucao is None:
            verSolucao = mostrarSolucao()
        if verSolucao:
            print('\nA fórmula da Permutação é: n!')
            print('Sua operação é', numPermutado)
            print(f'Calcula se o fatorial:')
            fatNumerador = listaFatorialSimples(numPermutado)
            fatNumerador = explicaFatorial(fatNumerador)

    elif operacao == 2:
        print('A fórmula do Arranjo é: n!/(n - k)!')
        while True:  # Permite repetição em caso de erro de sintaxe
            numeradorTemp = input('Digite o numerador (número acima da barra de divisão):').strip()
            if len(numeradorTemp) == 0:  # Caso o usuário não digite um valor
                print("Opa! Parece que você não digitou um valor. Por favor, tente novamente.")
            elif len(numeradorTemp.split()) > 1:  # Se houver mais de um número digitado
                print("Parece que você digitou mais de um valor ou cometeu outro erro de escrita. "
                      "Por favor, tente novamente.")
            else:
                break
        while True:  # Permite repetição em caso de erro de sintaxe
            divisorTemp = input('Digite o divisor (A subtração, entre parênteses e seguida do ponto de exclamação, '
                                'que fica abaixo da barra de divisão)\nExemplo: (n - k)!:').strip()
            if len(divisorTemp) == 0:  # Caso o usuário não digite um valor
                print('Você não digitou um valor para o divisor. Por favor tente novamente.')
            else:
                break
        resultado, numerador, divisor, subtracao = arranjo(numeradorTemp, divisorTemp)
        print(resultado)
        verSolucao = mostrarSolucao()
        while verSolucao is None:
            verSolucao = mostrarSolucao()
        if verSolucao:
            print('\nA fórmula do Arranjo é : n! / (n - k)!')
            print(f'\nSua operação é: {numeradorTemp} / {divisorTemp}')  # Valores que o usuário digitou, sem mods
            fatNumerador = listaFatorialSimples(numeradorTemp)
            print('\nCalcula-se os fatoriais:\nNumerador:')
            explicaFatorial(fatNumerador)
            print('\nCalcula-se o divisor:')
            subtracaoParaFat(subtracao)
            print(f'Faz se a divisão {numerador} / {divisor} = {resultado}')

    elif operacao == 3:
        numeradorTemp = input('Digite o numerador (número acima da barra de divisão):').strip()
        divisorTemp = input('Digite o divisor (número abaixo da barra de divisão):').strip()
        resultado, resultadoNumerador, resultadoDivisor = permutacaoComRepeticao(numeradorTemp, divisorTemp)
        print(resultado)
        verSolucao = mostrarSolucao()
        while verSolucao is None:
            verSolucao = mostrarSolucao()
        if verSolucao:
            print('\nA fórmula da Permutação Com Repetição é: n! / k! ')
            print(f'\nSua operação é: {numeradorTemp} / {divisorTemp}')
            fatNumerador = listaFatorialSimples(numeradorTemp)
            fatDivisor = listaFatorialSimples(divisorTemp)
            print('\nCalcula-se os fatoriais:\nNumerador:')
            explicaFatorial(fatNumerador)
            print('\nCalcula-se os fatoriais:\nDivisor:')
            explicaFatorial(fatDivisor)
            print(f'\nFaz se a divisão {resultadoNumerador} / {resultadoDivisor} = {resultado}')

    elif operacao == 4:
        conta = input('Digite a base (quantidade de elementos do conjunto) elevado pela potência '
                      '(quantidade de elementos que serão escolhidos)\nEx.: n^k:')
        lista = []  # Lista onde será adicionado o necessário para a explicação da potenciação
        base, potencia, resultado = arranjoComRepeticao(conta)
        print(resultado)
        verSolucao = mostrarSolucao()
        while verSolucao is None:
            verSolucao = mostrarSolucao()
        if verSolucao:
            print('\nA fórmula de Arranjo com Repetição é: n^k')
            print('Sua conta é:,', conta)
            # Explica a potenciação
            if potencia > 10:
                print(f'Multiplica-se {base} {potencia} vezes\nEx: {base} x {base} x {base} x {base}...')
                break
            else:
                for i in range(potencia - 1):
                    lista.append(base)
                    lista.append('X')
                lista.append(base)
                print(*lista, '=', resultado)
                
    elif operacao == 5:
        print('A fórmula da Combinação: n!/k! x (n - k)!')
        numeradorTemp = input('Digite o numerador (número acima da barra de divisão):').strip()
        divisorTemp = input('Digite o divisor (A subtração, entre parênteses, e em seguida, o fatorial):').strip()
        numerador, divisor, resultado, subtracao, numFatorial = combinacao(numeradorTemp, divisorTemp)
        print(resultado)
        verSolucao = mostrarSolucao()
        while verSolucao is None:
            verSolucao = mostrarSolucao()
        if verSolucao:
            print('\nA fórmula da Combinação é : n! / (n - k)! X k!')
            print(f'\nSua operação é: {numeradorTemp} / {divisorTemp}')
            fatNumerador = listaFatorialSimples(numeradorTemp)
            print('\nCalcula-se os fatoriais:\nNumerador:')
            explicaFatorial(fatNumerador)
            print('\nCalcula-se o divisor:')
            subtracaoParaFat(subtracao)
            print('Calcula-se o segundo fatorial:')
            numFatorial = listaFatorialSimples(numFatorial)
            explicaFatorial(numFatorial)
            print(f'Faz-se a divisão: {numerador} / {divisor} = {resultado}')
    else:
        exit()
