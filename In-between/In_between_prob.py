""" This is a simulation for the poker game called In Between in python. This simulation calculates the probability 
of winning and the probability of losing double each round and take into account cards that were previously discarded
so that probabilities will stay true and accurate."""

# Initialize deck
cards_numeric = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
cards_actual = {"A":4, "2":4, "3":4, "4":4, "5":4, "6":4, "7":4, "8":4, "9":4, "10":4, "J":4, "Q":4, "K":4}

# Simulate 2 cards being dealt for a round
def deal_hand():
    card_1 = 0
    card_2 = 0
    # Get input of 2 cards
    while card_1 not in cards_actual:
        card_1 = input("What is the first card? ")
        card_1 = card_1.upper()
    print()    
    while card_2 not in cards_actual: 
        card_2 = input("What is the second card? ")
        card_2 = card_2.upper()
    print()    
    card_list = [card_1, card_2] 
    # Converting non numerical cards into numerical values
    for i in range(len(card_list)):
        if card_list[i] == "A":
            card_list[i] = 1
        elif card_list[i] == "J":
            card_list[i] = 11
        elif card_list[i] == "Q":
            card_list[i] = 12
        elif card_list[i] == "K":
            card_list[i] = 13
        else:
            card_list[i] = int(card_list[i])  
    card_list = sorted(card_list)           
    return card_list             

# Update the deck after each card dealt
def update_deck(card_list):
    for card in card_list:
        cards_numeric[card] -= 1
        
# Calculate the probabilities of losing double and winning
def probability(card_list):
    total_cards = 0
    within = 0
    double = 0
    for key in cards_numeric:
        total_cards += cards_numeric[key] 
        if key > card_list[0] and key < card_list[1]:
            within += cards_numeric[key]
        elif key == card_list[0] or key == card_list[1]:
            double += cards_numeric[key]
    probability_win = round((within/total_cards) * 100, 2)
    probability_double = round((double/total_cards) * 100, 2)

    return [probability_win, probability_double]   

# Get the input of the actual 3rd card dealt and update deck
def actual_card():
    actual = 0
    while actual not in cards_actual:
        actual = input("What card came out? ")
        actual = actual.upper()
    print()    
    print("Noted")  
    print()  
    if actual == "A":
        actual = 1
    elif actual == "J":
        actual = 11
    elif actual == "Q":
        actual = 12
    elif actual == "K":
        actual = 13
    else:
        actual = int(actual)
    cards_numeric[actual] -= 1       



# Create gameplay 
def gameplay():
    # Total 17 rounds only for each deck since one round will reduce deck by 3 cards
    for i in range(17):
        card_list = deal_hand()
        update_deck(card_list)
        probability_list = probability(card_list)
        print(f"Your odds of winning are {probability_list[0]} %. Your odds of paying double are {probability_list[1]} %")
        print()
        actual_card()

gameplay()
