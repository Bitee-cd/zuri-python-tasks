import random

while True:
    choices = ["r", "p", "s"]
    values = {"r": "Rock",
              "p": "Papper",
              "s": "Scissors"
              }

    cpu = random.choice(choices)

    player = input("R, P, or S?: ").lower()

    while player in choices:
        if player == cpu:
            print("CPU: ", values[cpu])
            print("player: ", values[player])
            print("Tie!")

        elif player == "r":
            if cpu == "p":
                print("CPU: ", values[cpu])
                print("player: ", values[player])
                print("You lose!")
            if cpu == "s":
                print("CPU: ", values[cpu])
                print("player: ", values[player])
                print("You win!")

        elif player == "s":
            if cpu == "r":
                print("CPU: ", values[cpu])
                print("player: ", values[player])
                print("You lose!")
            if cpu == "p":
                print("CPU: ", values[cpu])
                print("player: ", values[player])
                print("You win!")

        elif player == "p":
            if cpu == "s":
                print("CPU: ", values[cpu])
                print("player: ", values[player])
                print("You lose!")
            if cpu == "r":
                print("CPU: ", values[cpu])
                print("player: ", values[player])
                print("You win!")

        play_again = input("Play again? (yes/no): ").lower()

        if play_again != "yes":
            break

    if not player in choices:
        print("Error Please reselect ")
print("Bye!")
