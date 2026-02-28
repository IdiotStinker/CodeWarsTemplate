def convertbase(string, bStart, bFinal):
    alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
    n = int(string, bStart)
    if n == 0: return "0"
    result = ""
    while n:
        result = alpha[n % bFinal] + result
        n //= bFinal
    return result

if __name__ == "__main__":
    print(convertbase("14", 10, 2))
