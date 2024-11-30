import sys

for line in sys.stdin:
    try:
        number_test = int(line.strip())
        stack = []
        queue = []
        priority_queue = []
        option = [1, 1, 1]

        for _ in range(number_test):
            order, value = map(int, input().split())

            if order == 1:
                stack.append(value)
                queue.append(value)
                priority_queue.append(value)
            elif order == 2:
                if stack:
                    if stack.pop() != value:
                        option[0] = 0
                else:
                    option[0] = 0

                if queue:
                    if queue.pop(0) != value:
                        option[1] = 0
                else:
                    option[1] = 0

                if priority_queue:
                    if priority_queue.pop(priority_queue.index(max(priority_queue))) != value:
                        option[2] = 0
                else:
                    option[2] = 0

        if sum(option) == 0:
            print('impossible')
        elif sum(option) > 1:
            print('not sure')
        elif option[0] == 1:
            print('stack')
        elif option[1] == 1:
            print('queue')
        else:
            print('priority queue')

    except EOFError:
        break
