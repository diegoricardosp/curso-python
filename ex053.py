"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
Exemplos de palíndromos: 
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("Você digitou a frase:\n {}".format(frase))
if inverso == junto:
    print("Temos um palíndromo!")
    print("A frase inversa da digitada é {}!".format(inverso))
else:
    print("Não temos um palíndromo. ):")
