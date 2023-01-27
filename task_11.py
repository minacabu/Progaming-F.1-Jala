varTexto = input('insira sua palavra ')
varReverso = varTexto [::-1]
if varTexto == varReverso:
    print(f'sua palavra é um palindromo\n {varTexto}\n {varReverso}')
else:   
    print(f'sua palavra não é um palindromo\n {varTexto}\n {varReverso}')