import random
import os


def clear_screen():
    os.system('CLS')
    os.system('clear')


def new_place(number_of_players, places):
    new_int = random.randint(0, len(places))
    player_places = [places[new_int]] * (number_of_players - 1)
    player_places.append("You are the Spy")
    return player_places


def print_result(place):
    if place =='You are the Spy':
        print("\n\n#################    " + place + "    #################\n\n -- You are the spy. Tell no one.")

    else:
        print("\n\n#################    " + place + "    #################\n\n -- This is your location. Read it and"
                                                    " don't tell anyone.")
    input("if you have read it. Hit enter.")
    clear_screen()


def game(number_of_players, place_list):

    places = new_place(number_of_players, place_list)
    for i in range(len(places)):
        input("please hit enter to play..")
        integer = random.randint(0, len(places) - 1)
        place = places.pop(integer)
        print_result(place)


number_of_players = None

play = True
while play:
    clear_screen()
    number_of_players = input("Please enter the number of players: ")
    try:
        number_of_players = int(number_of_players)
    except ValueError:
        print("\nYou haven't entered an integer, please try again\n")
    
    if isinstance(number_of_players, int):
            play = False

print('Let the game begin.')

places = ['Airplane', 'Bank', 'Beach', 'Cathedral', 'Circus tent', 'Corporate Party', 'Crusader Army', 'Casino',
          'Day Spa', 'Embassy', 'Hospital', 'Hotel', 'Military Base', 'Movie Studio', 'Ocean Liner', 'Passenger Train',
          'Space Station', 'Restaurant', 'School', 'Service Station', 'Space Station', 'Submarine', 'Supermarket',
          'Theatre', 'University', 'World War II Squad']

game(number_of_players, places)
