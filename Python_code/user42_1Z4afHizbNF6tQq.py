# implementation of card game - Memory

import simplegui
import random

#images
image1 = simplegui.load_image("http://www.picturesflowers.net/free_flowers_pictures/stock_photo_of_an_orange_flower_0001-0211-0617-3706_SMU.jpg")
image2 = simplegui.load_image("http://www.flower-angels.com/images/flowers/flower_cornflower.jpg")
image3 = simplegui.load_image("https://i.pinimg.com/736x/2c/e4/38/2ce4388ef4fa2b831b971086dafc8424--orange-flower-names-orange-flowers.jpg")
image4 = simplegui.load_image("http://thumbs.dreamstime.com/x/pink-lotus-flower-10683674.jpg")
image5 = simplegui.load_image("http://www.golden-gate-park.com/wp-content/uploads/2011/03/conservatory_of_flowers3.jpg")
image6 = simplegui.load_image("http://img11.hostingpics.net/pics/43857617.hibiscus_rouge.jpg")
image7 = simplegui.load_image("http://www.graphix1.co.uk/wp-content/uploads/2011/08/08Flowers.jpg")
image8 = simplegui.load_image("http://www.cvijet.info/images/galleries/230-265/eae607f8-Pakujac%20%E2%80%93cvijet.jpg")

#global variables
WIDTH = 50
HEIGHT = 100
image_list = []
exposed = []
state = 0
turns = 0
choices = [-1, -1]

# helper function to initialize globals
def new_game():
    global image_list, exposed 
    global state, turns, choices
    image_list = [image1, image2, image3, image4, image5, image6, image7, image8]
    image_list.extend(image_list)
    random.shuffle(image_list)
    random.shuffle(image_list)
    exposed = [0]*16
    state = 0
    turns = 0   
    choices = [-1, -1]
    label.set_text("Turns = " + str(turns))  
     
# define event handlers
def mouseclick(pos):
    global state, turns, choices
    x = int(pos[0]/WIDTH)
    if state == 0:
        if exposed[x] == 0:
            if image_list[choices[0]] != image_list[choices[1]]:
                exposed[choices[0]] = 0
                exposed[choices[1]] = 0
            exposed[x] = 1
            state = 1
            choices[0] = x
    elif state == 1:
        if exposed[x] == 0:          
            exposed[x] = 1
            state = 0
            choices[1] = x
            turns += 1    
            label.set_text("Turns = " + str(turns))
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for x in range(0, len(image_list)):
        if exposed[x] == 0:        
            canvas.draw_polygon([(WIDTH*x, 0), (WIDTH*(x+1), 0), (WIDTH*(x+1), HEIGHT), (WIDTH*x, HEIGHT)], 3, 'White', 'Green')
        else:
            for value in image_list:
                canvas.draw_image(image_list[x], [image_list[x].get_width()/2, 
                                  image_list[x].get_height()/2], [image_list[x].get_width(), 
                                  image_list[x].get_height()], [WIDTH * (0.5 + x), HEIGHT/2], [WIDTH, HEIGHT])
                
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


