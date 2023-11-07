def sport(s):
    sports_dict = {
        'baseball': 9,
        'soccer': 11,
        'rugby': 15,
        'basketball': 5
    }

    return sports_dict.get(s, 6)

s = input()
print(sport(s))

