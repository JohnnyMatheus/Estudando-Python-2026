#operadores in e not in
#strings são iteráveis

# nome = 'Johnny'
# print('ny' in nome)
# print(10* '-')
#
# print('0' not in nome)

nome = input('Digite seu nome: ')
encontrar =  input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em nome {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

