def convertbase(string, bStart, bFinal):
    alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
    decimal = int(string, bStart)
    if decimal == 0: return "0"
    result = ""
    while decimal:
        result = alpha[decimal % bFinal] + result
        decimal //= bFinal
    return result

if __name__ == "__main__":
    print(convertbase("code", 36, 35))
    print(convertbase("357", 8, 10))
