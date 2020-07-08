# Hangman Game
import time, os

print('Hello and Welcome, to hangman!')
print('Ready to play?')

# Actually we need to be the one to randomly generate a word
# - we can use a txt file with a whole list of words and a random number 
#   generator to randomly select a word
#  test

word = input('Please enter a word: ') 

word_length = len(word)

# I just realized thats not how this works, I can either limit it to six letter
# words exclusively or im gonna have to write a function that checks guesses

print('Ok you get 6 tries') 

# display_string = '' 
# I still think im in c++ -->  "_" * word_length


# Guess function maybe a class?
# Add the functionality of it saving which letters have been guessed

class guess_check():
    name = ''
    guess = ''

    #state = ['0' * word_length] 

    def __init__(self, name):
        self.name = name
    
    def display_string():
        return display_string

    def gcheck(self, guess):
        self.guess = guess
        display_string = '' 
        x = 0
        repeat = ''

        state = {
            self.name[0]: 0,
            
        }
        ## repeat_val = ""
        # rep = False

        # Lets make a dictionary with the keys being the letters and the value being their state
        #
        

        for letter in self.name:
            rep = False
            for let in repeat:
                if guess == let:
                    rep = True
                  ## repeat_val = let  
                

      
            if guess == letter:
                display_string = display_string + letter # + '_' * (word_length - x)

                if rep == False:
                    repeat += letter
            # elif rep == True:

            else:

                display_string += '_'
        print(display_string)

    

# Find a way to iterate through this, we can go through it but is ther any 
# way to keep track on which iteration it is on
index = 0 
cinst = guess_check(word)
display_str = cinst.display_string

while display_str != word:
    index = index + 1
    g = input('Guess ' + str(index) + ': ')
    cinst.gcheck(g)







# first = guess_check(word)
# g = input('Guess #1: ')
# first.gcheck(g)

