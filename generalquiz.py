print("===== GENERAL KNOWLEDGE QUIZ =====")

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer = input("\n3. How many continents are there on Earth? ").strip()

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final Score
print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/ 3")

if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good Job!")
elif score == 1:
    print("Keep Practicing!")
else:
    print("Better luck next time!")