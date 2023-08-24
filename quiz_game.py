print("Welcome to my quiz app!")

play = input("Do you want to play?(y/n) ")

if play != "y":
    quit()

score = 0
answer = input("What is the capital city of Kenya? ").lower()
if answer == "nairobi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the owner of Tesla? ").lower()
if answer == "elon musk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does cpu stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")