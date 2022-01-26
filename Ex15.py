from tracemalloc import stop

i = int

i = -1

while i != 11:
    i = i + 1
    stop
    print(i)
