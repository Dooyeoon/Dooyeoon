x = 1
y = 1
n = int(input())
moves = input().split()

move_type = ["L", "R", "U", "D"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            tx = x + dx[i]
            ty = y + dy[i]

    if tx < 1 or ty < 1 or tx > n or ty > n:
        continue
    x, y = tx, ty
print(y, x)


