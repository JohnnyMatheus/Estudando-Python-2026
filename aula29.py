"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""
numero_str = input('Dobrar o valor lido: ')

try:
    print('STR: ',numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float )
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float *2}')
except:
    print('Isso não é um número')




# numero_str = input('Dobrar o valor lido: ')
#
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float *2}')
#
# else:
#     print('Isso não é um número')