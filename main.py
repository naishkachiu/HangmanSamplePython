import random
import hangmanimages

def getWord(num):
  with open("words", 'r') as fp:
      # To store lines
      lines = ""
      for i, line in enumerate(fp):
          # read line 4 and 7
          if i == num:
              lines += line.strip()
              break
  return lines

hangmanset = [
  '\n\n\n\n\n_______',
  '\n|\n|\n|\n|\n|_____',
  '______\n| /\n|/\n|\n|\n|_____',
  '______\n| /  |\n|/\n|\n|\n|_____',
  '______\n| /  |\n|/   O\n|\n|\n|_____',
  '______\n| /  |\n|/   O\n|    |\n|\n|_____',
  '______\n| /  |\n|/   O\n|   -|\n|\n|_____',
  '______\n| /  |\n|/   O\n|   -|-\n|\n|_____',
  '______\n| /  |\n|/   O\n|   -|-\n|   /\n|_____',
  '______\n| /  |\n|/   O\n|   -|-\n|   / \\ \n|_____'
]

#hangmanimages.test()
#Some variables used in the game
hangman = hangmanset[::-1] #Get a list of the drawings.
tries = 0 #total number of guesses
lives = len(hangman) -1  #number of lives defined by the hangman images
letters = [] #list of letters the user has used
solved = False #used to track whether the puzzle is solved or not

#which words to use from the dictionary file
start_word_num = 1 #starting word line number
end_word_num = 4 #ending word line number

#Get a random word from the dictionary file
answer = list(getWord(random.randint(start_word_num - 1,end_word_num - 1)))
#Make a list to hold the user's guess. This is what will be displayed to the user.
guess = []
#Make the guess "_" for each letter
for i in range(0,len(answer)):
  guess.append("_")

#Welcome the player
print("Let's play hangman!")
#Display the current guess (blanks)
print("\n",*guess)

#Main game loop. Keeps running while not solved and player still has lives
while not solved and (lives > 0):
  tries = tries + 1 #add 1 to our rounds

  #Loop input until user enters an unused letter
  while True:
    #Print the round and lives
    print("Round: ", tries,"  Lives: ",lives)
    #Ask for a letter.
    this_guess = input("What letter would you like to guess?").upper()[0] 
    #If the letter has already been used, print an error message.
    if this_guess in letters:
      print("You've already used that letter!")
    #if letter has not been used, add it to the used letters list and break out of input loop
    else:
      letters.append(this_guess)
      break

  #variable to check if letter is in the word.
  found = False
  #loop through each letter in the answer and check it for this guess
  for ltr in range(0,len(answer)):
    #if the letter is found, make it show up in the guess list
    if answer[ltr] == this_guess:
      guess[ltr] = this_guess
      found = True #flag that letter has been found
  
  #if the letter was not found (bad guess)
  if not found:
    #minus a life
    lives = lives - 1 
    #Print that you lost a life
    print("sorry, no letter ", this_guess)

  #Check to see if the puzzle has been solved 
  solved = answer == guess

  #Draw the hangmanimages
  print(hangman[lives])

  #print the current guess (board)
  print("\n",*guess)


#Game has ended. Check if it was solved
if solved:
  #if solved, print well done.
  print("Well done!")
#If not solved, print the correct answer
else:
  print("Game over. The word was ", *answer)

