while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    tickets = list(map(int, input().split()))
    counter = 0
    tickets_control = {}
    for ticket in tickets:
        if ticket in tickets_control:
            tickets_control[ticket] += 1
        else:
            tickets_control[ticket] = 1
    for value in tickets_control.values():
        if value >= 2:
            counter += 1
    print(counter)
    