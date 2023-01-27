
def times():
    code = True
    varNumber = 1
    varSum = 0
    while code:
        varSum= varNumber + varSum
        varNumber +=1
        if varNumber >100:
            code = False
    print(f'The result is: {varSum}')    
times()            
    
