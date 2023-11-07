def rectangular(e1,e2):
    area = e1*e2
    return area if area != 0 else 'invalid'


e1,e2 = map(int,(input().split()))
print(rectangular(e1,e2))
