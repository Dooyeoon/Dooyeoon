n, m = map(int, input().split())
count = 0

while n != 1:
    if int(n%m) != 0:
        n -= 1
        count += 1
    else:
        n //= m
        count += 1
print(count)