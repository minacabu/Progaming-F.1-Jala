senha = str(input('create your password' ))
def Saque():
    saldo = float(input('Qual o seu saldo?'))
    saque = float(input('Qual o valor do seu saque?'))
    testeSenha = input('Qual a sua senha?')
    if testeSenha == senha:
        saldo-=saque
        if saldo <0:
            print('saque impossibilitado')
        else: print(f'Saque de R${saque:.2f} reais realizado com sucesso, e agora seu novo saldo é R${saldo:.2f} reais')
    else: print('senha incorreta '), Saque()
Saque()