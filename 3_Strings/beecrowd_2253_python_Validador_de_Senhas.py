import re

while True:
    try:
        password = input()
        valid = True
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{1,}$'
        
        if 6 > len(password) or len(password) > 32:
            valid = False
        
        if re.fullmatch(regex, password) and valid:
            print('Senha valida.')
        else:
            print('Senha invalida.')
            
    except EOFError:
        break