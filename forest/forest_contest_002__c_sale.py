def calculate_total(n):
    total_sum = 0
    pants = False

    for i in range(n):
        c, p = input().split()
        total_sum += int(p)
        if c == "pants":
            pants = True

    if pants and total_sum >= 2000:
        total_sum -= 500

    return total_sum

n = int(input())
result = calculate_total(n)
print(result)
