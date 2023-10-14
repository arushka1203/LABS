# 1
a = int(input())
i = 1
while i <= a:
    print(i, end = ' ')
i += 2


# 2
a = int(input())
if a < 0:
     print("negative numbers")
else:
     factorial = 1
     i = 1
     while i <= a:
         factorial *= i
         i += 1
     print(factorial)

# 3
while True:
     number = int(input())
     if number == 42:
         print("You entered the number 42. Exiting the program.")


#4
user_input = input()
count_of_a = user_input.count('a')
print(count_of_a)

#5
a = input()
sum_of_digits = 0
num_digits = len(a)
index = 0
while index < num_digits:
     digit_char = a[index]

     if digit_char.isdigit():
         digit = int(digit_char)
         sum_of_digits += digit
     index += 1
print(sum_of_digits)

# 6
n = int(input())
first, last, nxt = 1, 1, 2
if n == 1 or n == 2:
     print(first)
else:

     i = 2
     while i != n:
         nxt = first + last
         last, first = nxt, last
         i += 1
     print(nxt)


# 7
s = input()
print(s[::-1])


# 8
sum = 0
for i in range(5):
     x = int(input())
     if x % 2 == 0:
         continue
     sum += x
     print(sum)

# 9
import random
ai_number = random.randint(1, 100)
while True:
     mid = int(input())
     if mid > ai_number:
         print("Too large")
     elif mid < ai_number:
         print("Too small")
     else:
         print("Correct")
         break

#10
s = input()
if s == s[::-1]:
     print("Palindrome")
else:
     print("Not palindrome")


# 11
x = int(input())
y = int(input())
ans = 1
while y > 0:
     ans *= x
     y -= 1
print(ans)


# 12

n = int(input("Enter a positive integer (N): "))
num = 2
while num <= n:
     is_prime = True
     for i in range(2, int(num**0.5) + 1):
         if num % i == 0:
             is_prime = False
             break
     if is_prime:
         print(num, end=' ')
     num += 1




#13
n = int(input())
s = str(n)
print(s[::-1])

# # 14
def isPrime(x):
     if x == 1:
         return False
     if x == 2:
         return True
     for i in range(2, x):
         if x % i == 0:
             return False
     return True
while True:
     x = int(input())
     if isPrime(x):
         print("Prime number")
         break
     else:
         while isPrime(x) == False:
             x += 1
             print(x)

# 15
s = input()
n = int(input())
n %= 26
for i in s:
    print(chr(ord(i) + n), end="")