# Operadores lógicos aula sobre o (or)
# and (e) or (ou) not (não)
# or - Qualquer condição como verdadeira avalia toda a expressão como True.
# Se qualquer valor for considerado verdadeiro, a expressão inteira sera avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0.0.0 '' false
# Tambem existe o tipo None que é usado para representar um não valor

entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Digite a Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou')
else:
    print('Sair')