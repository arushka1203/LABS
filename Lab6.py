from datetime import datetime

def get_keys_with_value_true(dictionary):
    return [key for key, value in dictionary.items() if value]
print("\nTask 1.1")
dictionary = {
    "a": True,
    "b": False,
    "c": True
}
print(get_keys_with_value_true(dictionary))


def get_unique_elements(input_list):
    return [item for item in input_list if input_list.count(item) == 1]
print("\nTask 1.2")
input_list = [1, 2, 3, 1, 2, 4]
print(get_unique_elements(input_list))

def get_date_in_format(date):
    date_parts = date.split('.')
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
print("\nTask 1.3")
date = "2023.10.23"
print(get_date_in_format(date))

def get_elements_with_no_more_than_two_occurrences(input_list):
    result = []
    for item in input_list:
        if input_list.count(item) <= 2 and item not in result:
            result.append(item)
    return result
print("\nTask 1.4")
input_list = [1, 2, 3, 1, 2, 4, 1, 2]
print(get_elements_with_no_more_than_two_occurrences(input_list))

def get_words_from_string(input_string):
    words = input_string.split()
    return words
print("\nTask 1.5")
string = "This is a string with several words."
print(get_words_from_string(string))


def get_unique_elements_with_count(input_list):
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
print("\nTask 2.6")
input_list = [1, 2, 3, 1, 2, 4, 1, 2]
print(get_unique_elements_with_count(input_list))

def get_prime_numbers(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for divisor in primes:
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print("\nTask 2.7")
n = 100
print(get_prime_numbers(n))

def get_prime_numbers_in_list(input_list):
    max_num = max(input_list)
    prime_numbers = get_prime_numbers(max_num)
    return [item for item in input_list if item in prime_numbers]
print("\nTask 2.8")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
print(get_prime_numbers_in_list(input_list))

def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    date1_obj = datetime.strptime(date1, date_format)
    date2_obj = datetime.strptime(date2, date_format)
    return (date2_obj - date1_obj).days
print("\nTask 2.9")
date1 = "2023.10.23"
date2 = "2023.10.24"
print(get_difference_between_dates(date1, date2))

def get_decimal_number_from_binary_string(binary_string):
    return int(binary_string, 2)
print("\nTask 2.10")
binary_string = "10110011"
print(get_decimal_number_from_binary_string(binary_string))

def get_perfect_squares(input_list):
    perfect_squares = [item for item in input_list if int(item ** 0.5) ** 2 == item]
    return perfect_squares
print("\nTask 2.11")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_perfect_squares(input_list))

def sort_by_price(shopping_list):
    return sorted(shopping_list, key=lambda x: x['price'])
print("\nTask 2.12")
shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
            ]
print(sort_by_price(shopping_list))

def get_words_starting_with_vowel(words):
    vowels = "aeiou"
    return [word for word in words if word[0].lower() in vowels]
print("\nTask 2.13")
words = ["apple", "banana", "orange", "bear", "cat"]
print(get_words_starting_with_vowel(words))