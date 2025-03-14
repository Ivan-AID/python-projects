import random

def roll_dice():
    input("Press Enter to roll the dice...")
    dice_number = random.randint(1, 6)
    print(f"The dice rolled: {dice_number}")

roll_dice()
