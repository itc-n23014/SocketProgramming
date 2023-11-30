def reverse_s(s):
    s_l = [i for i in s[::-1]]
    return ''.join(s_l)


s = input()
print(reverse_s(s))

