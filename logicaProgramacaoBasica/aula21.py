# Operadores lógicos aula sobre o (and)
# and (e) or (ou) not (não)
# and - Todas as condições precisan ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira sera avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0.0.0 '' false
# Tambem existe o tipo None que é usado para representar um não valor

entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Digite a Senha: ')

senha_permitida = '123'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou')
else:
    print('Sair')