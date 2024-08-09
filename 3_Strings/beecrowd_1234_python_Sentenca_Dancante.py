while True:
    try:
        sequence_test = input()
        
        upper_case = True
        for i in range(len(sequence_test)):
            if sequence_test[i] != ' ':
                if upper_case:
                    print(sequence_test[i].upper(), end='')
                    upper_case = False
                else:
                    print(sequence_test[i].lower(), end='')
                    upper_case = True
            else:
                print(sequence_test[i], end='')
        print()
    except EOFError:
        break