def reduction_length(text):
    if len(text) >= 10:
        return text[:10]
    return text

string1 = input()
string2 = input()
string3 = input()

print(string1 + string2 + string3)
print(string2 + string3 + string1)
print(string3 + string1 + string2)

print(reduction_length(string1) + reduction_length(string2) + reduction_length(string3))