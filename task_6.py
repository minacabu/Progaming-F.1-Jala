def cripto(mensagem):
    textoFinal= ""
    for i in mensagem:
        textoFinal += str(ord(i)) + "."
    print (textoFinal)    
    return textoFinal [:-1]
cripto(input('diga o seu text o  '))