def Times():
    code = True
    varNumber = 2
    varSum = 0
    while code:
        varSum += varNumber 
        varNumber +=2
        if varNumber >100:
            code = False
    print(f'The result is: {varSum}')
Times()