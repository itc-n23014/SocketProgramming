def breaktime(h):
    return '45 min' if 6 < h <= 8 else ('60 min' if h > 8 else 'no break')

h = int(input())
print(breaktime(h))
