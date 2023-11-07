def elevator(f1,f2):
    return 'up' if f1[0] < f2[0] else 'down'



f1,f2 = input().split()
print(elevator(f1,f2))

