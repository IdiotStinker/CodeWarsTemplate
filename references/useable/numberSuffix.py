def numberSuffix(number):
    if number % 10 == 1: return str(number) + "st"
    if number % 10 == 2: return str(number) + "nd"
    if number % 10 == 3: return str(number) + "rd"
    return str(number) + "th"

if __name__ == "__main__":
    print(f"It is the {numberSuffix(33)} day of this year!")