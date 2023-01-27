opção = int(input('seleciona a sua opção:\n (1) converter binario para decimal\n (2) converter decimal para binario\n'))
if opção == 1:
    num=(int(input('Digite seu número Decimal para ser convertido ')))
    print(bin(num))
else:
    num=(input('Digite seu número Binario para ser convertido '))
    var1=int(num,2)
    print(var1)





