# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

num_range = range(100)
counter = 7
secret_number = 100

# helper function to start and restart the game

def new_game():
    global num_range
    global secret_number
    global counter
    counter = 7
    if num_range == range(100):       
       secret_number = random.randrange(0, 100)
       print "New game. Range is from 0 to 100."
       print "Number of remaining guesses is", counter
       print ""      
    elif num_range == range(1000):
       secret_number = random.randrange(0, 1000)
       counter = 10
       print "New game. Range is from 0 to 1000."
       print "Number of remaining guesses is", counter
       print "" 
    else:
        pass
    # initializes global variables used in code
 
    
# event handlers for control panel

def range100():
    global num_range
    num_range = range(100)
    new_game()
    # button that changes the range to [0,100) and starts a new game 


def range1000():
    global num_range
    num_range = range(1000)
    new_game()
    # button that changes the range to [0,1000) and starts a new game     
    
    
def input_guess(guess):
    global counter
    counter -= 1
    global secret_number
    if secret_number == int(guess):
        print "Guess was", guess
        print "Number of remaining guesses is", counter
        print "Correct!"
        print ""
        return new_game()
    elif counter == 0:
        print "Guess was", guess
        print "Number of remaining guesses is", counter
        print "You ran out of guesses. The number was", secret_number
        print ""
        return new_game()
    elif secret_number < int(guess):
        print "Guess was", guess
        print "Number of remaining guesses is", counter
        print "Lower!"
        print ""
    elif secret_number > int(guess):
        print "Guess was", guess
        print "Number of remaining guesses is", counter
        print "Higher!"
        print ""
    else:
        pass

    
# creates frame
frame = simplegui.create_frame ("Guess the number", 300, 300)

# registers event handlers for control elements and starts frame
frame.add_button ("Range is [0, 100)", range100, 200)
frame.add_button ("Range is [0, 1000)", range1000, 200)
frame.add_input ("Enter a guess", input_guess, 200)
frame.start()

# calls new_game 
new_game()


