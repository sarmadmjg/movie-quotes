import json
import random


fileName = 'data.json'
questionsPerGame = 4
blankSequence = '___'



# Loads the quiz data and answers
def loadData():
  fileStream = open('data.json')
  return json.load(fileStream)



# Prompt the user for the level of hardness
def getLevel(levels):
  print('Select a hardness level:')

  # Print a list of all levels
  for i in range(len(levels)):
    print(str(i) + ': ' + levels[i])
  print()

  # Get user selection
  while (True):
    userInput = input('Enter the level number: ')

    try:
      selectedIndex = int(userInput)

      if selectedIndex >= 0 and selectedIndex <= (len(levels) - 1):
        return levels[selectedIndex]
      else:
        print('Invalid level number, try again')
        continue

    except (ValueError):
      print('Invalid level, try again')
      print()



# Prompt the user for the number of tries
def getTries():
  while (True):
    try:
      tries = int(input('How many tries do you get? '))
      if tries <= 0:
        print('Enter a number that is more than zero')
        continue
      return tries

    except (ValueError):
      print('Invalid number, try again')



# Get a question randomly from a list of questions
def getRandomQuestion(questions, count):
  return random.sample(questions, count)



# Play the game
def play(allQuestions, tries, questionsPerGame):
  print('\n\nLet\'s Start playing!!')
  print('---------------------')

  questions = getRandomQuestion(allQuestions, questionsPerGame)
  print('\nFill the blanks in the following movie quotes:\n')
  
  i = 0

  while(tries >= 1 and i < len(questions)):
    quote = questions[i]['quote']
    answer = questions[i]['answer']

    print()
    print(quote)
    userAnswer = input('what goes in the blank? ')

    # strip whitespace and convert to lowercase to make the answers case insensitive
    if userAnswer.lower().strip() == answer.lower().strip():
      print('Correct!')
      print(quote.replace(blankSequence, answer))
      print()
      i += 1                   # Go to the next blank, if any
      continue
    else:
      print('Wrong answer!\n')
      tries -= 1

  # Game has ended, check if it's a win
  if tries <= 0:
    print('\nYou lost :(\n')
  else:
    print('\nYou won! :D\n')



print('\n\nWelcome to movie quotes game\n')
print('Hit ctrl + c anytime to exit the game\n')

try:
  data = loadData()
  level = getLevel(data['levels'])
  tries = getTries()
  play(data['questions'][level], tries, questionsPerGame)

  print('Bye!')

except (KeyboardInterrupt):
  print('\nYou closed the game, bye')
