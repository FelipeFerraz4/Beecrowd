test1 = input().split()
test2 = input().split()

verify = True
for i in range(5):
    if test1[i] == test2[i]:
        verify = False

if verify:
    print('Y')
else:
    print('N')