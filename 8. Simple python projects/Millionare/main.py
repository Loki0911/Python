import time
import sys
import random

questions = [
    ["What is the capital city of France?", "Paris", "London", "Berlin", "Madrid", 1],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["In which continent is Brazil located?", "Africa", "Asia", "South America", "Australia", 3],
    ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which river is the longest in the world?", "Nile", "Amazon", "Yangtze", "Mississippi", 1],
    ["What is the chemical symbol for gold?", "Ag", "Au", "Fe", "Cu", 2],
    ["Which country hosted the 2016 Summer Olympics?", "China", "Brazil", "Japan", "Russia", 2],
    ["What is the smallest country by land area?", "Monaco", "Vatican City", "San Marino", "Liechtenstein", 2],
    ["Which element has the atomic number 1?", "Hydrogen", "Helium", "Lithium", "Beryllium", 1],
    ["In which year did the Titanic sink?", "1908", "1912", "1916", "1920", 2]
]

prices = [1000, 2000, 3000, 5000, 10000, 20000, 32000, 74000, 100000, 1000000]

random.shuffle(questions)
for i, question in enumerate(questions):
    print(f"\nQuestion {i+1}: {question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    try:
        a = int(input("Enter your answer (1-4): "))
        if a not in [1, 2, 3, 4]:
            print("Invalid input! Please enter a number between 1 and 4.")
            sys.exit(0)
    except ValueError:
        print("Invalid input! Please enter a number.")
        sys.exit(0)

    if question[5] == a:
        print(f"Correct Answer! You won ${prices[i]}")
        time.sleep(1)  # Pause before the next question
    else:
        print(f"Incorrect. The correct answer is {question[question[5]]} (Option {question[5]})")
        if i == 0:
            print("You won $0. Better luck next time!")
        else:
            print(f"You won ${prices[i-1]}. Better luck next time!")
        sys.exit(0)

print("\nCongratulations! You answered all questions correctly and won $1,000,000!")