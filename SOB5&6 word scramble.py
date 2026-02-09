""" This is a word scramble game.The player will choose a category and then be given a scrambled word from that category.They will then have to guess the unscrambled version of the word.This will go on for 3 rounds.Each round will tell the player whether they got the answer right ot not """

#random module is used when selecting which words are unscrambled each round.It will pick a random value which corresponds to an index value and whatever the value is will be the chosen word to scramble
import random

#These are the lists of different categories each with 10 words which can be scrambled
animals = ["Capybara", "Axolotl", "Pangolin", "Narwhal", "Quokka", "Fennec Fox", "Red Panda", "Manatee", "Wombat",
           "Platypus"]

physical_objects = ["Laptop", "Coffee Mug", "Desk Chair", "Smartphone", "Notebook", "Water Bottle", "Backpack",
                    "Table Lamp", "Keyboard", "Headphones"]

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White",
          "Gray"]

#This is the dictionary "categories" which will help with matching what the user inputs to the respective category
categories = {
    "animals": animals,
    "physical objects": physical_objects,
    "colors": colors}

#This is where the user inputs which category they want to use
category_input = str(input("Which category do you want? animals, physical objects, or colors? ")).strip().lower()

#The initial score is defined as zero
score = 0

#In this IF statement the category will be chosen and then the rounds start
if category_input in categories:
    chosen_list = categories[category_input]

    #The game will go on for 3 rounds,each round a random index will be chosen and will then be shuffled and outputted to the user
    for i in range(0,3):

        index = random.randrange(0,9)

        chosen_word = chosen_list[index]

        shuffled_word = "".join(random.sample(chosen_word, len(chosen_word)))

        print(shuffled_word)

        answer = str(input("Enter the unscrambled word: "))

        #the answer given will be in lower case and white spaces will be removed so that it will more likely match the unscrambled words
        #If the answer is correct then the score will increment by 1 otherwise it will output that it is wrong
        if answer.strip().lower() == chosen_word.lower():
            print("Correct!!")
            score += 1

        else:
            print("WRONG!!")

    
    print (f"You got {score} correct answers")


else:
    print("Sorry, that category does not exist!")

