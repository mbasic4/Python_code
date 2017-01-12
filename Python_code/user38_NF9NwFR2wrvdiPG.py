# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
dealer_score = 0
your_score = 0
deck = []
you = []
dealer = []
message = ""
message_1 = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.player_hand = []  # create Hand object
    
    def __str__(self):
        stri = " "
        for i in self.player_hand:
           stri = stri + str(i) + " "
        return stri	  # return a string representation of a hand

    def add_card(self, card):
        self.player_hand.append(card)

    def get_value(self):
        self.value = 0 
        for card in self.player_hand:
             rank = Card.get_rank(card)
             self.value = self.value + VALUES[rank]
        for card in self.player_hand: 
             rank = Card.get_rank(card)
             if rank == 'A' and self.value <= 11:
                self.value += 10                        
        return self.value 
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.player_hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [95,218], CARD_BACK_SIZE)
        # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle the deck 

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        strin = " "
        for c in self.deck:
           strin = strin + str(c) + " "
        return strin  	# return a string representing the deck



#define event handlers for buttons
def deal():
    global in_play, deck, you, dealer, dealer_score, message, message_1, outcome    
    if in_play == False:
        deck = Deck()
        you = Hand()
        dealer = Hand()
        you.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        you.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        message = "New hand. Do you want to hit or stand?" 
        message_1 = ""
    elif in_play == True:
        message = "You lost. New hand. Do you want to hit or stand?"
        message_1 = ""
        deck = Deck()
        you = Hand()
        dealer = Hand()
        you.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        you.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer_score += 1
    outcome = ""    
    in_play = True

def hit():
    global in_play, outcome, dealer_score, message, message_1
    if in_play == True:
        you.add_card(deck.deal_card())
        message = "Do you want to hit or stand?"
        message_1 = ""
        if you.get_value() > 21:
            in_play = False
            message_1 = "You busted! You lose! Want to play again?"
            message = ""
            dealer_score += 1
            outcome = "Dealer: " + str(dealer.get_value()) + "     You: " + str(you.get_value()) 
    # if the hand is in play, hit the player   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
     global in_play, outcome, dealer_score, your_score, message, message_1
     if in_play == False:
         message = "The hand is over. Want a new deal?"
         message_1 = ""
     else:
         while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
         if dealer.get_value() > 21:
            message_1 = "Dealer busted! You win! Want to play again?"
            message = ""
            your_score += 1
            in_play = False           
         elif dealer.get_value() >= you.get_value():
            message_1 = "Dealer wins! Want to play again?"
            message = ""
            dealer_score += 1
            in_play = False      
         else:
            message_1 = "You win! Want to play again?"
            message = ""
            your_score += 1
            in_play = False           
         outcome = "Dealer: " + str(dealer.get_value()) + "     You: " + str(you.get_value())   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    canvas.draw_text("Black", [227,40], 42, 'Red')
    canvas.draw_text("jack", [326,40], 42, 'Black')
    canvas.draw_text(message, [60,105], 28, 'White')
    canvas.draw_text(message_1, [20,560], 33, 'Red')
    canvas.draw_text("Dealer :", [60,160], 26, 'Black')
    canvas.draw_text("You :", [60,330], 26, 'Black')
    canvas.draw_text("Dealer score: " + str(dealer_score), [420,165], 26, 'Black')
    canvas.draw_text("Your score: " + str(your_score), [420,335], 26, 'Black')
    canvas.draw_text(outcome, [60,500], 26, 'White')    
    dealer.draw(canvas, [60,170])
    you.draw(canvas, [60,345])
  
# initialization frame
frame = simplegui.create_frame("Blackjack", 650, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

