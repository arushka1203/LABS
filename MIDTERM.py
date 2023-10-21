#1
name = input("Enter your name please: ")
salary_input = input("Enter your desired salary level: ")
if salary_input.isdigit():
    salary = int(salary_input)
    tax_level = salary * 0.2
    print(f"{name}, the tax level you will pay with the salary {salary} is {tax_level}")
else:
    print(f"{name}, please enter your desired salary as a digit.")

#2
    operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y,
    4: lambda x, y: x ** y
}

print("Please chose the task you want to perform:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

choice = int(input())
if choice in operations:
    numbers = input("Please enter two numbers, comma separated: ")
    x, y = map(float, numbers.split(','))
    result = operations[choice](x, y)
    print(result)

#3
length = int(input("Please enter the length of Fibonacci sequence: "))
fib_sequence = [1, 1]

while len(fib_sequence) < length:
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

print(f"The Fibonacci sequence for {length} is")
print(', '.join(map(str, fib_sequence)))

#4
unique_items = set()
non_unique_items = []
task = input("Please enter items separated by comma: ")
items = task.split(', ')

for item in items:
    if items.count(item) > 1:
        non_unique_items.append((item, items.count(item)))
    else:
        unique_items.add(item)

print("Items are saved")
print(f"Unique items: {unique_items}")
print(f"Not unique items: {tuple(non_unique_items)}")

#5
tasks = []
completed_tasks = []

while True:
    print("Please chose the task you want to perform:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")

    choice = int(input())

    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print(f'The task "{task}" was added to the todo list')

    elif choice == 2:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    elif choice == 3:
        task_name = input("Enter the name of the task: ")
        if task_name in tasks:
            tasks.remove(task_name)
            completed_tasks.append(task_name)
            print(f'The task "{task_name}" is marked as completed')
        else:
            print(f'The task "{task_name}" was not found in the todo list')

    elif choice == 4:
        print("Completed Tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")

    elif choice == 5:
        break
