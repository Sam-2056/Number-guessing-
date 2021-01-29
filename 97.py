import random
guesses = 0

number = random.randint(1,50)
print("pick a number between (1,50)")

while guesses < 50:
    print("Take a guess: ")
    guess = input ()
    guess = int(guess)

    guesses = guesses + 1
    if guess < number: 
        print("number is too low")
    if guess > number: 
         print("number is too high")
    if guess == number:
        break
if guess == number:
    guesses = str(guesses)
    print("you guessed the number in : ", +guesses)

    if guess != number:
        number = str(number)
        print("Wrong, the number was: " +number)
   
