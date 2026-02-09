"""
This is a word scramble game. The player will choose a category and then be given a scrambled word
from that category.They will then have to guess the unscrambled version of the word. This will go
on for 3 rounds. Each round will tell the player whether they got the answer right or not.
The player can also add their own words to a category.
"""

# Random module is used to select and scramble words
import random

# These are the lists of different categories each start with 10 predefined words
animals = ["Capybara", "Axolotl", "Pangolin", "Narwhal", "Quokka", "Fennec Fox", "Red Panda", "Manatee", "Wombat",
           "Platypus"]

physical_objects = ["Laptop", "Coffee Mug", "Desk Chair", "Smartphone", "Notebook", "Water Bottle", "Backpack",
                    "Table Lamp", "Keyboard", "Headphones"]

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White",
          "Gray"]

# Dictionary linking categories to lists
categories = {
    "animals": animals,
    "physical objects": physical_objects,
    "colors": colors
}

# Allow user to modify lists
def add_words():
        category_to_edit = input("Which category do you want to add words to? animals, physical objects, or colors? ").strip().lower()

        if category_to_edit in categories:

            print("Type words to add. Type 'stop' to finish.")

            while True:

                new_word = input("Enter a word: ").strip()

                # Exit loop if user types stop
                if new_word.lower() == "stop":
                    break

                # Add new word to selected list
                categories[category_to_edit].append(new_word)

                print(f"'{new_word}' added to {category_to_edit}")

def output_shuffled_words(chosen_list):
    # Choose random word from selected list
    index = random.randrange(0, len(chosen_list))

    chosen_word = chosen_list[index]

    # Scramble word
    shuffled_word = "".join(random.sample(chosen_word, len(chosen_word)))

    print("\nScrambled word:", shuffled_word)
    return chosen_word

def main():
    # Ask user if they want to add their own words
    adding_words = input("Do you want to add your own words to a category? (yes/no): ").strip().lower()

    if adding_words == "yes":
        add_words()
    else:
        print("That category does not exist. Skipping word addition.")

    # Ask user for category
    category_input = input("\nWhich category do you want? animals, physical objects, or colors? ").strip().lower()

    # Initial score
    score = 0

    # Check if category exists
    if category_input in categories:

        chosen_list = categories[category_input]

        # Play 3 rounds
        for i in range(0, 3):
            chosen_word = output_shuffled_words(chosen_list)

            # Get user answer
            answer = input("Enter the unscrambled word: ")

            # Check answer
            if answer.strip().lower() == chosen_word.lower():
                print("Correct!!")
                score += 1

            else:
                print("WRONG!! The answer was:", chosen_word)

        # Display final score
        print(f"\nYou got {score} correct answers out of 3")


    else:
        print("Sorry, that category does not exist!")

main()
