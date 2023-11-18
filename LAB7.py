def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line)

import random

def read_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        print(random_line)


def count_uppercase_characters(filename):
    uppercase_count = 0
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
    return uppercase_count


def count_lines_not_starting_with_d(filename):
    lines_without_d = 0
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('D'):
                lines_without_d += 1
    return lines_without_d


def count_words_ending_with_f(filename):
    words_ending_with_f = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower().endswith('f'):
                    words_ending_with_f += 1
    return words_ending_with_f


def count_words_all_none(filename):
    all_count = 0
    none_count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() == 'all':
                    all_count += 1
                elif word.lower() == 'none':
                    none_count += 1
    return all_count, none_count


def count_word_frequencies(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1
    return word_counts


def find_longest_word(filename):
    longest_word = ''
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def replace_b_with_j(filename):
    corrected_content = ''
    with open(filename, 'r') as file:
        for line in file:
            corrected_line = line.replace('B', 'J')
            corrected_content += corrected_line
    return corrected_content

def count_characters_a_b(filename):
    a_count = 0
    b_count = 0
    with open(filename, 'r') as file:
        for line in file:
            for char in line.lower():
                if char == 'a':
                    a_count += 1
                elif char == 'b':
                    b_count += 1
    return a_count, b_count
