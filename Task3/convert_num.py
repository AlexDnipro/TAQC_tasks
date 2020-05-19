from num2words import num2words

def convert(number) -> str:
    """
    :return The function will return the word representation of input number
    """
    return num2words(number)

def main():
    number = int(input("Hi! Please provide the number to convert into letters:"))
    print(convert(number))
