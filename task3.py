import random
L = ["banana","apple","strawberry","mostafa"]  # [m,o,s,t,a,f,a]

randomWord = random.choice(L)
m = list(randomWord)
random.shuffle(m)
shuffleWord = ''.join(m)

print("Welcome to the Word Scramble Game! ")
print(f"Try to guess the original word from the scrambled word: {shuffleWord}")
print("You have 5 attempts.")

x = 5

while x > 0 : 
    inn = input("Enter your guess: ")

    if inn == randomWord:
        print("Congratulations! You guessed the correct word!")
        break

    else:
        x-=1
        if x > 0:
            print(f"Incorrect! Try again. You have {x} attempts left.")
        else:
            print(f"You're out of attempts! The correct word was: {randomWord}")