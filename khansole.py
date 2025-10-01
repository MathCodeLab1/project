import random

def math_level():
    
    #prompt the user to choose a math level.
    
    print("Choose your math level:")
    print("1 = Junior (1-digit numbers)")
    print("2 = Intermediate (2-digit numbers)")
    print("3 = Advance (3-digit numbers)")
    
    while True:
        option = input("Enter 1, 2, or 3: ")
        if option not in ["1", "2", "3"]:
            print("Invalid input, Please try again.")
        else:
            break

    if option == "1":
        return option, 1, 9
    elif option == "2":
        return option, 10, 99
    else:
        return option, 100, 999


def math_operation():
    
    #prompt the user to choose an operation type.
    
    
    print("\nChoose operation type:")
    print("1 = Addition (+)")
    print("2 = Subtraction (-)")
    print("3 = Multiplication (*)")
    
    while True:
        option = input("Enter 1, 2, or 3: ")
        if option not in ["1", "2", "3"]:
            print("Invalid input, Please try again.")
        else:
            break
    return option


def math_game(rand_num1, rand_num2, operation):
    
    #prompt the user to make a math calculation based on the operation.
    
    if operation == "1":  # Addition
        prompt = f"{rand_num1} + {rand_num2}"
        right_answer = rand_num1 + rand_num2
    elif operation == "2":  # Subtraction
        # Make sure the result is non-negative
        if rand_num1 < rand_num2:
            rand_num1, rand_num2 = rand_num2, rand_num1
        prompt = f"{rand_num1} - {rand_num2}"
        right_answer = rand_num1 - rand_num2
    else:  # Multiplication
        prompt = f"{rand_num1} * {rand_num2}"
        right_answer = rand_num1 * rand_num2

    while True:
        try:
            user_input = int(input(f"What is {prompt}? : "))
            break
        except ValueError:
            print("Please enter a valid number!")

    if user_input == right_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The actual answer is {right_answer}.")
        return False


def main():
    
    print("Welcome to Khansole Academy!")
    level, low, high = math_level()
    option = math_operation()
    user_score = 0
    attempts = 0
    

    levels = {"1" : "junior", "2" : "intermediate", "3" : "advanced"}
    operations = {"1" : "addition", "2" : "subtraction", "3" : "multiplication"}

    print("\nGreat! Solve 3 problems in a row correctly to win.\n")

    while user_score < 3:
        rand_num1 = random.randint(low, high)
        rand_num2 = random.randint(low, high)
        

        print("-" * 30)
        correct = math_game(rand_num1, rand_num2, option)
        attempts += 1


        if correct:
            user_score += 1
            print(f"You've gotten {user_score} correct in a row.\n")
        else:
            user_score = 0
            print("")
            

    

    print(f"Congratulations! You've solved {attempts} problems and mastered {operations[option]} at {levels[level]} math level.")


if __name__ == "__main__":
    
    while True:
        main()
        repeat = input("Do you want to play again? (y/n): ").lower()
        if repeat != "y":
            print("Thanks for playing! Goodbye.")
            break



