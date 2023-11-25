def task1():
    print(f"Task 1")
    data = open("text1.txt")
    for i, line in enumerate(data):
        print(line, end='')
    data.close()


task1()

import random


def task2():
    print(f"\n\nTask 2")
    data = open("text1.txt")
    lines = data.readlines()
    print(lines[random.randint(0, len(lines))])


task2()


def task3():
    print(f"\n\nTask 3")
    data = open("text1.txt").read()
    uppercaseCount = 0
    for i in range(0, len(data)):
        if data[i].isupper():
            uppercaseCount += 1
    print(uppercaseCount)


task3()


def task4():
    print(f"\n\nTask 4")
    data = open("text1.txt")
    lines = data.readlines()
    cnt = 0
    for line in range(0, len(lines)):
        if lines[line][0].upper() != 'D':
            cnt += 1
    print(cnt)


task4()


def task5():
    print(f"\n\nTask 5")
    data = open("text1.txt")
    lines = data.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if line[len(line) - 1] == '\n':
            if line[len(line) - 2].upper() == 'F':
                cnt += 1
        else:
            if line[len(line) - 1].upper() == 'F':
                cnt += 1
    print(cnt)


task5()


def task6():
    print(f"\n\nTask 6")
    data = open("text1.txt")
    lines = data.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        line = " " + lines[i].lower() + " "
        cnt += line.count(" all ") + line.count(" none ") + line.count(" all\n") + line.count(" none\n")
    print(cnt)


task6()


def task7():
    print(f"\n\nTask 7")
    data = open("text1.txt")
    punctuation = ".?!,;:-_'\" "
    lines = data.readlines()
    words = [i.lower().split() for i in lines]
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j][len(words[i][j]) - 1] in punctuation:
                words[i][j] = words[i][j][:-1]
    wordsDic = {}
    for i in words:
        for j in i:
            if j in wordsDic:
                wordsDic[j] += 1
            else:
                wordsDic[j] = 1
    print(wordsDic)


task7()


def task8():
    print(f"\n\nTask 8")
    data = open("text1.txt")
    lines = data.readlines()
    words = [i.lower().split() for i in lines]
    punctuation = ".?!,;:-_'\" "
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j][len(words[i][j]) - 1] in punctuation:
                words[i][j] = words[i][j][:-1]
    longestWord = words[0][0]
    for i in words:
        for j in i:
            if len(j) > len(longestWord):
                longestWord = j
    print(longestWord)


task8()


def task9():
    print(f"\n\nTask 9")
    data = open("text1.txt").read()
    data = data.replace('B', 'J')
    data = data.replace('b', 'j')
    print(data)


task9()


def task10():
    print(f"\n\nTask 10")
    data = open("text1.txt")
    lines = data.readlines()
    cntA = 0
    cntB = 0
    for i in range(0, len(lines)):
        line = " " + lines[i].lower() + " "
        cntA += line.count('a')
        cntB += line.count('b')
    print(f"a={cntA}, b={cntB}")


task10()

   
             
       
