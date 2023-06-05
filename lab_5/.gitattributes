import num2words

def greet_user():
    print("   Вітаю!")

def get_user_input():
    number = input("Ведіть Число: ")
    return number

def convert_number_to_words(number):
    try:
        words = num2words.num2words(number, lang='uk')
        return words
    except ValueError:
        return

def main():
    greet_user()
    number = get_user_input()
    words = convert_number_to_words(number)
    print("представлення числа:", words)

if __name__ == "__main__":
    main()

