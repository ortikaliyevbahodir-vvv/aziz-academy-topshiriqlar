h = 15
while True:
    try:
        g = int(input())
    except:
        break
    if g == h:
        print("Correct")
    elif abs(g - h) > 5:
        print("Far")
    else:
        print("Close")