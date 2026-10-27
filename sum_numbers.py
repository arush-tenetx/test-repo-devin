def add(a, b):
    return a + b


def to_number(text):
    try:
        return int(text)
    except ValueError:
        return float(text)


if __name__ == "__main__":
    first = to_number(input("Enter first number: "))
    second = to_number(input("Enter second number: "))
    print("Sum:", add(first, second))
