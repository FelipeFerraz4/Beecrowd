count = 0
while True:
    try:
        year = int(input())

        if count != 0:
            print()
        count += 1

        leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        huluculu = (year % 15 == 0)
        bulukulu = (year % 55 == 0 and leap)

        if leap:
            print("This is leap year.")
        if huluculu:
            print("This is huluculu festival year.")
        if bulukulu:
            print("This is bulukulu festival year.")
        if not (leap or huluculu or bulukulu):
            print("This is an ordinary year.")
            
    except EOFError:
        break