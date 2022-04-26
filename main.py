from random import randint


class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def choose_difficulty(self):
        print("Choose difficulty")
        print("[1] LEVEL 1 : Guess the number between 1 and 5")
        print("[2] LEVEL 2 : Guess the number between 1 and 10")
        print("[3] LEVEL 3 : Guess the number between 1 and 20")
        self.difficulty = int(input())
        return f'You chose level {self.difficulty}'



    def play(self):
        if self.difficulty == 1:
            cycles = 0
            lives = 2
            while cycles != 3:
                random_number = randint(1, 5)
                number = int(input())
                if number > 5 or number < 1:
                    print("Number has to be between 1 and 5")
                    break
                elif number != random_number:
                    print(f"Number was: {random_number}. Try again.")
                    print(f"There is {lives} lives left.")
                elif number == random_number:
                    print(f"Congrats!! Number was: {random_number}.")
                    break
                cycles += 1
                lives -= 1
            print("End of program")

        if self.difficulty == 2:
            cycles = 0
            lives = 2
            while cycles != 3:
                random_number = randint(1, 10)
                number = int(input())
                if number > 10 or number < 1:
                    print("Number has to be between 1 and 10")
                    break
                elif number != random_number:
                    print(f"Number was: {random_number}. Try again.")
                    print(f"There is {lives} lives left.")
                elif number == random_number:
                    print(f"Congrats!! Number was: {random_number}.")
                    break
                cycles += 1
                lives -= 1
            print("End of program")

        if self.difficulty == 3:
            cycles = 0
            lives = 2
            while cycles != 3:
                random_number = randint(1, 20)
                number = int(input())
                if number > 20 or number < 1:
                    print("Number has to be between 1 and 20")
                    break
                elif number != random_number:
                    print(f"Number was: {random_number}. Try again.")
                    print(f"There is {lives} lives left.")
                elif number == random_number:
                    print(f"Congrats!! Number was: {random_number}.")
                    break
                cycles += 1
                lives -= 1
            print("End of program")


start = Game(1)
print(start.choose_difficulty())
start.play()

