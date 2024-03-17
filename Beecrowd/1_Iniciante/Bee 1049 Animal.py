first_id = input()
second_id = input()
third_id = input()

if 'vertebrado' == first_id:
    if 'ave' == second_id:
        if 'carnivoro' == third_id:
            print("aguia")
        else:
            print("pomba")
    else:
        if 'onivoro' == third_id:
            print("homem")
        else:
            print("vaca")

else:
    if 'inseto' == second_id:
        if 'hematofago' == third_id:
            print("pulga")
        else:
            print("lagarta")
    else:
        if 'onivoro' == third_id:
            print("minhoca")
        else:
            print("sanguessuga")
