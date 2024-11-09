def distance_point(ball_write, ball):
    return ((ball_write[0] - ball[0])**2 + (ball_write[1] - ball[1])**2)**0.5

number_tests = int(input())
for _ in range(number_tests):
    number_ball = int(input())

    ball_write = list(map(int, input().split()))
    balls = [list(map(int, input().split())) for _ in range(number_ball)]
    
    smaller_distance = float('inf')
    closest_index = 0
    
    for i, ball in enumerate(balls):
        distance = distance_point(ball_write, ball)
        if distance < smaller_distance:
            smaller_distance = distance
            closest_index = i
    print(closest_index + 1)
