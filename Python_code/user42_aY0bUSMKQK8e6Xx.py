# template for "Stopwatch: The Game"
'''The goal of the game is to click "Stop" button at the exact same time 
the stopwatch counts one second (e.g. "0:01:0", "0:03:0", "0:15:0" etc.)'''

import simplegui

# define global variables
value = 0
display_text = "0:00.0"
tries = 0
wins = 0
start_game = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global display_text
    minute = int(t/600)
    sec = int(t/10)%60
    tsec = t%10
    display_text = str(minute) + ":" + '%02d'%sec + "." + str(tsec)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    global start_game
    start_game = True

def Stop():
    timer.stop()
    global start_game
    global tries
    global wins
    if start_game == True:
        if value%10 == 0:
            wins += 1
        start_game = False
        tries += 1
       
def Reset():
    global value
    global tries
    global wins
    timer.stop()
    tries = 0
    wins = 0
    value = 0
    return format(value)    
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
       global value
       value += 1
       return format(value)
 

# define draw handler
def draw(canvas):
    canvas.draw_text(display_text, (125,162), 44, 'White')
    canvas.draw_text("Hit Stop exactly when a second is counted", (5, 30), 20, 'White')
    canvas.draw_text(str(wins) + "/" + str(tries), (267, 285), 30, 'Orange')
    canvas.draw_text("Wins/Number of Tries: ", (25, 285), 25, 'Orange')
    
# create frame
frame = simplegui.create_frame('Stopwatch game', 350, 300)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 110)
frame.add_button("Stop", Stop, 110)
frame.add_button("Reset", Reset, 110)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
