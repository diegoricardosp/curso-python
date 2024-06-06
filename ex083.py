"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

lista1 = []
lista2 = []

valor = str(input('Digite uma expressão matemática: '))
priP = valor.count('(')
lista1.append(priP)
ultP = valor.count(')')
lista2.append(ultP)

if lista1 != lista2:
    print('Sua expressão está incorreta!')
else:
    print('Sua expressão está correta!')
