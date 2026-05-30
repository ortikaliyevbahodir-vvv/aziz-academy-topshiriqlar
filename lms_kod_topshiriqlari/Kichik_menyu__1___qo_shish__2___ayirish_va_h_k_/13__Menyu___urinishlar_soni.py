count = 0
while True:
    line = input().strip()
    if line == "0":
        break
    a, b = map(int, line())
    if a == 0 or b == 0:
        break
    count += 1
print(count)