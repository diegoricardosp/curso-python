listaPalavras = ('VAMO', 'GALO', 'DISGRAÇA')
for p in listaPalavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')