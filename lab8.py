import random

def task2():
    print(f"\n\nTask 2")
    data = open("text1.txt")
    lines = data.readlines()
    print(lines[random.randint(0, len(lines))])


task2()