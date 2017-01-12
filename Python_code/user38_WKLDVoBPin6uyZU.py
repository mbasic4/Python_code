# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400  
ball_pos = [WIDTH/2, HEIGHT/2]
x = random.randrange(120, 240)/60.0
y = random.randrange(60, 180)/60.0
ball_vel = [x, -y]
ball_radius = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
pad1_pos = HEIGHT/2.0
pad2_pos = HEIGHT/2.0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT (True), the ball's velocity is upper right, else upper left
def spawn_ball(direction):    
    global ball_pos, ball_vel # these are vectors stored as lists
    global x, y
    x = random.randrange(120, 240)/60.0
    y = random.randrange(60, 180)/60.0
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[1] = -y
    if direction == True:
        ball_vel[0] = x
    else:
        ball_vel[0] = -x
    global pad1_pos, pad2_pos
    pad1_pos = HEIGHT/2.0
    pad2_pos = HEIGHT/2.0 
        
# define event handlers
def new_game():
    global pad1_pos, pad2_pos, pad1_vel, pad2_vel  # these are numbers
    global score1, score2  # these are ints 
    score1 = 0
    score2 = 0
    pad1_pos = HEIGHT/2.0
    pad2_pos = HEIGHT/2.0
    pad1_vel = 0.0
    pad2_vel = 0.0   
    return spawn_ball(1 == random.randrange(0,2))
     
    
def draw(canvas):
    global score1, score2 
    global pad1_pos, pad2_pos, ball_pos
    global pad1_vel, pad2_vel, ball_vel
               
    # draw mid line and gutters
    canvas.draw_line([WIDTH/2, 0],[WIDTH/2, HEIGHT], 1, 'White')
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, 'White')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, 'White')
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]    
    if ball_pos[0] <= (PAD_WIDTH + ball_radius):
        if ball_pos[1] < (pad1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (pad1_pos + HALF_PAD_HEIGHT):         
            score2 += 1
            spawn_ball(True) 
        else:
            ball_vel[0] = - ball_vel[0] * 1.1          
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - ball_radius):
        if ball_pos[1] < (pad2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (pad2_pos + HALF_PAD_HEIGHT):
            score1 += 1
            spawn_ball(False) 
        else:
            ball_vel[0] = - ball_vel[0] * 1.1
    if ball_pos[1] <= ball_radius or ball_pos[1] >= (HEIGHT - ball_radius):
        ball_vel[1] = - ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 1, 'Yellow', 'Yellow')
    
    # update paddle's vertical position, keep paddle on the screen
    pad1_pos += pad1_vel 
    if pad1_pos < HALF_PAD_HEIGHT:
        pad1_pos = HALF_PAD_HEIGHT
    elif pad1_pos > (HEIGHT - HALF_PAD_HEIGHT):
        pad1_pos = (HEIGHT - HALF_PAD_HEIGHT)
    
    pad2_pos += pad2_vel
    if pad2_pos < HALF_PAD_HEIGHT:
        pad2_pos = HALF_PAD_HEIGHT
    elif pad2_pos > (HEIGHT - HALF_PAD_HEIGHT):
        pad2_pos = (HEIGHT - HALF_PAD_HEIGHT)
    
    # draw paddles
    canvas.draw_polygon([(HALF_PAD_WIDTH, pad1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, pad1_pos + HALF_PAD_HEIGHT )], PAD_WIDTH, 'White')
    canvas.draw_polygon([(WIDTH - HALF_PAD_WIDTH, pad2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, pad2_pos + HALF_PAD_HEIGHT )], PAD_WIDTH, 'White')
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2 - 70, 50), 32, 'White')
    canvas.draw_text(str(score2), (WIDTH/2 + 50, 50), 32, 'White')                
 
    
def keydown(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['w']:
        pad1_vel = -4.0
    elif key == simplegui.KEY_MAP['s']:
        pad1_vel = 4.0
    elif key == simplegui.KEY_MAP['up']:
        pad2_vel = -4.0
    elif key == simplegui.KEY_MAP['down']:
        pad2_vel = 4.0 
   
def keyup(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['w']:
        pad1_vel = 0.0
    elif key == simplegui.KEY_MAP['s']:
        pad1_vel = 0.0
    elif key == simplegui.KEY_MAP['up']:
        pad2_vel = 0.0
    elif key == simplegui.KEY_MAP['down']:
        pad2_vel = 0.0  

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Green')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button ("RESTART", new_game, 110)

# start frame
frame.start()
new_game()


