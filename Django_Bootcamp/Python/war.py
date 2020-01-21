#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'Hearts Diamonds Spades Clubs'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

my_cards = [(s,r) for s in SUITE for r in RANKS]

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(r,s) for s in SUITE for r in RANKS];

    def shuffle(self):
        print("The deck will now be shuffled!")
        shuffle(self.allcards)

    def split(self):
        return (self.allcards[26:], self.allcards[:26])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards;

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_cards(self,added_cards):
        self.cards.extend(added_cards);

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name;
        self.hand = hand;

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has played: {} ".format(self.name,drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for i in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards;

    def has_cards(self):
        return len(self.hand.cards ) != 0;

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
new_Deck = Deck();              # Create new deck
new_Deck.shuffle();             # Shuffle new deck
p1,p2 = new_Deck.split();       # Split deck into 2 halves

# Defining both players
cpu = Player("CPU",Hand(p1))
player = Player(input("What is your name?: "),Hand(p2))

# Start the Game
active = True;
total_rounds = 0;
war_rounds = 0;
print("Let the games begin!")
print("\n")

while cpu.has_cards() and player.has_cards() == True:
    total_rounds += 1;
    print("\n")
    print("Time for Round {}".format(total_rounds))
    print("Here are the current standings:")
    print(player.name+" has {} cards ".format(len(player.hand.cards))+cpu.name+" has {} cards".format(len(cpu.hand.cards)))
    print("-------------------------------------------------------------------")

    # draw cards
    cpu_card = cpu.play_card()
    player_card = player.play_card()
    table_cards = [];
    table_cards.append(cpu_card)
    table_cards.append(player_card)

    # WAR
    if cpu_card[0] == player_card[0]:
        # Check if players have cards
        if cpu.has_cards() == False:
            break
        elif player.has_cards() == False:
            break
        else:
            war_rounds += 1;
            print("War!")



        cpu_war = cpu.remove_war_cards()
            player_war = player.remove_war_cards()
            print("CPU has played: "+str(cpu_war))
            print(player.name+" has played: "+str(player_war))
            table_cards.extend(cpu_war)
            table_cards.extend(player_war)
            if RANKS.index(cpu_card[0]) < RANKS.index(player_card[0]):
                player.hand.add_cards(table_cards)
            else:
                cpu.hand.add_cards(table_cards)

    # compare values
    elif RANKS.index(cpu_card[0]) > RANKS.index(player_card[0]):
        cpu.hand.add_cards(table_cards)
    else:
        player.hand.add_cards(table_cards)
# Results
print("\n")
print("The Game has Ended!")
# Determine loser
if cpu.has_cards() == False:
    print("CPU has lost")
if player.has_cards() == False:
    print(player.name+" has lost")
print("{} rounds occured with {} war rounds!".format(total_rounds,war_rounds))
