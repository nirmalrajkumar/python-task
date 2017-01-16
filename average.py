L = [15, 18, 2, 36, 12, 78, 55,100,154]

total = 0

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

print average(L)
