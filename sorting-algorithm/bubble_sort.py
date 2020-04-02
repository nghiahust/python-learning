import time
start_time = time.time()
l = [5, 8, 1, 3, 2]
swapping = True
while swapping:
    swapping = False
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            swapping = True
print(l)
end_time = time.time()

total_time = end_time - start_time
print(total_time)
