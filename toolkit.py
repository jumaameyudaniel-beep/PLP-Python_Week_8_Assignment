
# PLP Python Week 8 Final Project
# My Menu-Driven Python Toolkit

# This list stores tasks added by the user.
tasks = []


# Tool 1: Simple Calculator
# Performs basic mathematical operations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = first_number + second_number
            print(f"The answer is: {result}")

        elif operation == "2":
            result = first_number - second_number
            print(f"The answer is: {result}")

        elif operation == "3":
            result = first_number * second_number
            print(f"The answer is: {result}")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, division by zero is not allowed.")
            else:
                result = first_number / second_number
                print(f"The answer is: {result}")

        else:
            print("Invalid operation. Please choose from 1 to 4.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# Allows users to add, view, and remove tasks.
def todo_list():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")


# Tool 3: Number Checker
# Checks whether a number is positive, negative, or zero.
def number_checker():
    print("\n--- NUMBER CHECKER ---")

    try:
        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is a positive number.")
        elif number < 0:
            print(f"{number} is a negative number.")
        else:
            print("The number is zero.")

    except ValueError:
        print("Please enter a valid number.")


# Tool 4: Countdown
# Counts backwards from the number entered by the user.
def countdown():
    print("\n--- COUNTDOWN ---")

    try:
        number = int(input("Enter a number to start counting down: "))

        if number < 0:
            print("Please enter zero or a positive number.")
        else:
            while number >= 0:
                print(number)
                number -= 1

            print("Countdown complete!")

    except ValueError:
        print("Please enter a whole number.")


# Main menu: keeps the toolkit running until the user quits.
def main():
    print("Welcome to My Python Toolkit!")
    print("Explore the tools and enjoy learning Python.")

    while True:
        print("\n====================================")
        print("       WELCOME TO MY PYTHON TOOLKIT")
        print("====================================")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Checker")
        print("4. Countdown")
        print("5. Quit")
        print("====================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            number_checker()

        elif choice == "4":
            countdown()

        elif choice == "5":
            print("Thank you for using My Python Toolkit. Goodbye!")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please select 1 to 5.")


# Start the program.
if __name__ == "__main__":
    main()
