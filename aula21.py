entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Digite senha: ')

senha_permitida = '12345'

if entrada == 'E' and senha_digitada ==senha_permitida:
    print('Senha validada com sucesso')
else:
    print('Senha incorreta')



