user_input = input()
user_x = user_input[0]
user_y = int(user_input[1:])

x_num = {'a':1, 'b': 2, 'c': 3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
user_x = x_num.get(user_x)

dx_one = [-1, 1]
dy_one = [-1, 1]
dx_two = [-2, 2]
dy_two = [-2, 2]

count = 0

for x1 in dx_one:
    for y2 in dy_two:
        tx = user_x + int(x1)
        ty = user_y + int(y2)
        if tx < 1 or ty < 1 or tx > 8 or ty > 8:
            continue
        else:
             count += 1
for x2 in dx_two:
    for y1 in dy_one:
        tx = user_x + int(x2)
        ty = user_y + int(y1)
        if tx < 1 or ty < 1 or tx > 8 or ty > 8:
            continue
        else:
             count += 1
print(count)



