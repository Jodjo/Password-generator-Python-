import secrets
import string

letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

pool = letters_lowercase + letters_uppercase + numbers + symbols

def check_number_of_lowercase_characters(string) :
    counter = 0
    for x in range(len(string)) :
        if string[x].islower() :
            counter = counter + 1
    return counter

def check_number_of_uppercase_characters(string) :
    counter = 0
    for x in range(len(string)) :
        if string[x].isupper() :
            counter = counter + 1
    return counter

def check_number_of_digits_characters(string) :
    counter = 0
    for x in range(len(string)) :
        if string[x].isnumeric() :
            counter = counter + 1
    return counter

def check_number_of_symbols_characters(string) :
    counter = 0
    for x in range(len(string)) :
        if string[x] in symbols :
            counter = counter + 1
    return counter

def check_number(number) :
    if number < 3 :
        print ("\nPlease chose a length superior to 2 \n")
        return 0
    elif number >= 3 :
        return 1

def random_string(characters, length) :
    result = ''
    for x in range(length) :
        result += ''.join(secrets.choice(characters))
    return result

def shuffled_string(string) :
    char_list = list(string)
    result = ''
    secrets.SystemRandom().shuffle(char_list)
    result = ''.join(char_list)
    return result

def automatic_password_generator() :
    length = 12
    result = ''

    for x in range(length) :
        result += ''.join(secrets.choice(pool))

    print(result)

# automatic_password_generator()

def user_defined_length_password_generator() :
    length = 0
    while length < 12 :
        length = int(input("Length of the password : "))
        if length < 12 :
            print ("Please chose a length superior to 11")

    result = ''

    for x in range(length) :
        result += ''.join(secrets.choice(pool))

    print(f"Here is the {length} characters generated password : {result}")

# user_defined_length_password_generator()

def user_defined_password_generator() :
    number_of_letters_lowercase = 0
    number_of_letters_uppercase = 0
    number_of_numbers = 0
    number_of_symbols = 0
    result = ''

    while check_number(number_of_letters_lowercase) != 1 :
        number_of_letters_lowercase = int(input("1. How many lowercase letters do you want your password to contain ? "))
        
    while check_number(number_of_letters_uppercase) != 1 :
        number_of_letters_uppercase = int(input("2. How many uppercase letters do you want your password to contain ? "))
        
    while check_number(number_of_numbers) != 1 :  
    	number_of_numbers = int(input("3. How many numbers do you want your password to contain ? "))

    while check_number(number_of_symbols) != 1 : 
        number_of_symbols = int(input("4. How many symbols do you want your password to contain ? "))

    length = number_of_letters_lowercase + number_of_letters_uppercase + number_of_numbers + number_of_symbols

    lowercase_random_string = random_string(letters_lowercase, number_of_letters_lowercase)
    uppercase_random_string = random_string(letters_uppercase, number_of_letters_uppercase)
    numbers_random_string = random_string(numbers, number_of_numbers)
    symbols_random_string = random_string(symbols, number_of_symbols)

    full_random_characters = lowercase_random_string + uppercase_random_string + numbers_random_string + symbols_random_string

    result = shuffled_string(full_random_characters)

    print("f", full_random_characters)
    print('l', lowercase_random_string)
    print('U', uppercase_random_string)
    print('n', numbers_random_string)
    print('s', symbols_random_string)
    print(len(result))
    print('R', result)

user_defined_password_generator()