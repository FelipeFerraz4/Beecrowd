while True:
    try:
        operation = input()
        
        par_quantity = 0
        status = True
        for item in operation:
            if item == '(':
                par_quantity += 1
            
            if item == ')':
                if par_quantity <= 0:
                    status = False
                    break 
                par_quantity -= 1
                
        
        if par_quantity == 0 and status:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break