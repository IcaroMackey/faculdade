saida = [z.lower() for z in ['']]

def adicao(num1,num2):
    soma = num1+num2
    return soma

def subtracao(num1,num2):
    sub = num1-num2
    return sub

def multiplicacao(num1,num2):
    mult = num1*num2
    return mult

def divisao(num1,num2):
    if num1 and num2 > 0:
        div = num1/num2
    else:
        print('Não foi possível realizar a divisão por 0')
    return div

def calculadora(num1,num2,operacao):
    if operacao == '+':
        exec = adicao(num1,num2)
    elif operacao == 'soma':
        exec = adicao(num1,num2)
    elif operacao == '-':
        exec = subtracao(num1,num2)
    elif operacao == 'subtracao':
        exec = subtracao(num1,num2)
    elif operacao == '*':
        exec = multiplicacao(num1,num2)
    elif operacao == 'multiplicacao':
        exec = multiplicacao(num1,num2)
    elif operacao == '/':
        exec = divisao(num1,num2)
    elif operacao == 'divisao':
        exec = divisao(num1,num2)

    return exec

while saida != 'n':
    x = int(input('Primeiro numero: '))
    #if x != int():
    #    print('Valor invalido')
    #    x = int(input('Primeiro numero: ')) Ñ deu certo
    oper = str(input('Qual operação: '))
    y = int(input('Segundo numero: '))
    resultado = calculadora(x,y,oper)
    print(f'resultado da operação: {resultado}')
    saida = str(input('Deseja continuar?:S/N  ')).lower()
    if saida != 'n' or 's':
        print('comando errado')
        saida = str(input('Deseja continuar?:S/N  ')).lower()

