def uniform(n):
    a = 'white,black,red,blue,yellow,green,orange,pink,purple'.split(',')
    return a[n-1]

n = int(input())
print(uniform(n))
