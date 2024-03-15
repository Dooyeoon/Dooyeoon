import time

n, m ,k = map(int, input().split())
sum = 0

num_list = list(map(int, input().split()))
start = time.time()
num_list.sort(reverse=True)
count_m = 0
count_k = 0

for i in range(m):
    if k > count_k:
        sum += num_list[0]
        count_k += 1
    else:
        sum += num_list[1]
        count_k = 0

print(sum)

end = time.time()
play_time = end - start
print(play_time)