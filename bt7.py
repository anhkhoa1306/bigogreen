def my_function():   
    a, b = map(int, input().split())
    c = b - a
    d = 0.1
    if (c >= 0 and c <= 50):
        print(int(c * 1484 + (c * 1484 * d)))
        return
    c = c - 50
    result = 50 * 1484
    c = c - 50
    if (c < 0):
        result += (c + 50) * 1533
        result += result * d
        print(int(result))
        return
    result += 50 * 1533
    c = c - 100
    if (c < 0):
        result += (c + 100) * 1786
        result += result * d
        print(int(result))
        return
    result += 100 * 1786
    c = c - 100
    if (c < 0):
        result += (c + 100) * 2242
        result += result * d
        print(int(result))
        return
    result += 100 * 2242
    c = c - 100
    if (c < 0):
        result += (c + 100) * 2503
        result += result * d
        print(int(result))
        return
    result += 100 * 2503
    c = c - 100
    if (c < 0):
        result += (c + 100) * 2587
        result += result * d
        print(int(result))
        return
    result += 100 * 2587
    result += c * 2587
    print(int(result + result * d))

my_function()