import random
import os

places = ['Airplane', 'Bank', 'Beach', 'Cathedral', 'Circus tent', 'Corporate Party', 'Crusader Army', 'Casino',
          'Day Spa', 'Embassy', 'Hospital', 'Hotel', 'Military Base', 'Movie Studio', 'Ocean Liner', 'Passenger Train',
          'Space Station', 'Restaurant', 'School', 'Service Station', 'Space Station', 'Submarine', 'Supermarket',
          'Theatre', 'University', 'World War II Squad']


def new_place(number_of_players, places):
    new_int = random.randint(0, len(places))
    player_places = [places[new_int]] * (number_of_players - 1)
    player_places.append("You are the Spy")
    return player_places


def game(number_of_players, places):
    places = new_place(number_of_players)
    print("initial")
    print("places:" + str(len(places)))
    for i in range(len(places)):

        print("enumerate: " + str(len(places)) + " people left to play")
        input("please hit enter to play..")
        integer = random.randint(0, len(places) - 1)
        place = places.pop(integer)
        print("\n\n#################    " + place + "    #################\n\n -- This is your place. read it. Dont tell anyone. If you are the spy. Tell no one.")
        print("enter number of places left: " + str(len(places)) + "... These places are " + str(places))
        input("if you have read it. Hit enter.")
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        os.system('CLS')


number_of_players = None

play = True
while play:
    number_of_players = input("Please enter the number of players: ")
    try:
        number_of_players = int(number_of_players)
    except ValueError:
        print("\nYou haven't entered an integer, please try again\n")
    
    if isinstance(number_of_players, int):
            play = False

game(number_of_players, places)
