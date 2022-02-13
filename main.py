import random

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

#Some variables
lives = 6 #number of guesses the user got wrong
letters = [] #list of letters the user has used
solved = False #used to track whether the puzzle is solved or not

#Get a random word from the dictionary file
answer = list(getWord(random.randint(0,3)))
guess = []
for i in range(0,len(answer)):
  guess.append("_")

print("Let's play hangman!")
print(*guess)

while not solved and (lives > 0):
  this_guess = input("What letter would you like to guess?").upper()[0]
  found = False
  for ltr in range(0,len(answer)):
    if answer[ltr] == this_guess:
      guess[ltr] = this_guess
      found = True
  if not found:
    lives = lives - 1
    print("sorry, no letter ", this_guess)
  solved = answer == guess
  print(*guess)

if solved:
  print("Well done!")
else:
  print("Game over. The word was ", *answer)

