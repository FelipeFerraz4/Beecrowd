number_to_words = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN",
    8: "EIGHT", 9: "NINE", 10: "TEN", 11: "ELEVEN", 12: "TWELVE",
    13: "THIRTEEN", 14: "FOURTEEN", 15: "FIFTEEN", 16: "SIXTEEN", 17: "SEVENTEEN",
    18: "EIGHTEEN", 19: "NINETEEN", 20: "TWENTY", 30: "THIRTY", 40: "FORTY",
    50: "FIFTY", 60: "SIXTY", 70: "SEVENTY", 80: "EIGHTY", 90: "NINETY",
    100: "ONE HUNDRED"
}

def number_length(number):
    if number in number_to_words:
        return len(number_to_words[number])
    else:
        tens, ones = divmod(number, 10)
        return len(number_to_words[tens * 10]) + (1 + len(number_to_words[ones]) if ones else 0)

number = int(input())

for _ in range(1000):
    result = number_length(number)
    if number not in number_to_words:
        number_to_words[number] = result
    number = result
print(number)
    