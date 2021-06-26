#Hangman Game
#Author: Thiago González

import random
import os
import words 
import ASCII

#Creating a words list
words_list = []
#Ask user: english or portuguese words
language = input('What language do you choose? Type "br" for portuguese or "en" for english.\n')
if language == "br":
  words_list = words.br_words_list
else:
  words_list = words.en_words_list
os.system('clear') or None

#Game loop. User will still playing while his answer is yes
want_play = "yes"
while want_play == "yes":

  #Randomly choose a word from the words_list and assign it to a variable called chosen_word
  chosen_word = random.choice(words_list)

  #Creates a null list
  blank_word_list = []

  #Creates a null string
  word = ""

  #Fills the word_letters_blank_list, with same chosen_word's lenght, with blank spaces ("_")
  for _ in range(0, len(chosen_word)):
    blank_word_list.append("_ ")

  #Creates the number of lifes the hanged man has
  lifes = 6

  #Transforms blank_word_list into a string named word
  for letter in blank_word_list:
    word += letter


  #Prints
  print(ASCII.hangman)
  print(ASCII.hangedman_body_parts[0])
  print(word)

  #Creates a condition to end loop
  end_of_the_game = False

  #Creates a letter list
  letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', '-', 'á', 'ã', 'â', 'é', 'ê', 'í', 'ó','õ', 'ô', 'ú']


  #Loops until the game is not ended
  while not end_of_the_game:

    #Allows the user to know all the letters he can still try to guess
    #Transforms letters list into a string
    letters_print = ' '.join(letters_list)
    #Prints letters user can still use
    print('Letters you still can use: ')
    print(letters_print)

    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lower case
    guess = input("\nGuess a letter: ").lower()

    #Checks if user has already guessed an especific letter
    while guess not in letters_list:
      print("You've already chosen this letter, please choose another. ")
      guess = input("\nGuess a letter: ").lower()

    #Letters already guessed
    for letter in letters_list:
      if guess == letter:
        letters_list.remove(letter)
      
  
    #Checks if the guessed letter (guess) is one of the letters in the chosen_word
    for letter in range(0, len(blank_word_list)):
      #If the guessed letter is one of the letters in the chosen_word, replaces the corresponding space of the letter
      if guess == chosen_word[letter]:
        blank_word_list[letter] = guess
  
    #Checks if the guessed letter (guess) is one of the letters in the chosen_word
    #If it is not, lose a life
    if guess not in chosen_word:
      lifes -= 1

    #Creates a null string and adds the letters of blank_word_list to it
    word = ""
    for letters in blank_word_list:
      word += letters

    #Checks conditions to end loop
    if lifes == 0 or word == chosen_word:
      end_of_the_game = True

    #Clear the console
    os.system('clear') or None

    #Prints game logo, hanged man's body and the word to be completed
    print(ASCII.hangman)
    if lifes == 6:
      print(ASCII.hangedman_body_parts[0])
    elif lifes == 5:
      print(ASCII.hangedman_body_parts[1])
    elif lifes == 4:
      print(ASCII.hangedman_body_parts[2])
    elif lifes == 3:
      print(ASCII.hangedman_body_parts[3])
    elif lifes == 2:
      print(ASCII.hangedman_body_parts[4])
    elif lifes == 1:
      print(ASCII.hangedman_body_parts[5])
    else:
      print(ASCII.hangedman_body_parts[6])
    print(word)
  
  
  #Checks if all letters has been already guessed or if lost all lifes
  if lifes == 0:
    print(f"The word was: {chosen_word}")
    print("You lost!")
  elif word == chosen_word:
    print("You won!")

  #Ask user if still wants to play
  want_play = input('Do you still want to play? Type "yes" or "no".\n')
  os.system('clear') or None