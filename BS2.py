import sys
import random


def boat_placement(boat_type, place_board, boat_lenght, boat_letter):
    o = "o"
    p1_placement_board = [[o for x in range(10)] for y in range(10)]
    p2_placement_board = [[o for x in range(10)] for y in range(10)]
    boat_x_coord = 0
    boat_y_coord = 0
    check_boat = 0
    while True:
        try:
            do_you_want_random = input("\nDo you want random placement of your %s? (y/n) " % boat_type)
            if do_you_want_random == "y":
                vert_or_horiz = random.choice('vh')
                if vert_or_horiz == 'v':
                    boat_x_coord = random.randint(0, 9)
                    boat_y_coord = random.randint(0, 5)
                elif vert_or_horiz == 'h':
                    boat_x_coord = random.randint(0, 5)
                    boat_y_coord = random.randint(0, 9)
            else:
                user_input = input("\nEnter the coordinates & direction of your %s in (Y X v/h) format: " % boat_type)
                boat_y_coord = int(user_input[0]) - 1
                boat_x_coord = int(user_input[2]) - 1
                vert_or_horiz = user_input[4]
            if vert_or_horiz == "v":
                for v in range(boat_lenght):
                    if place_board[boat_y_coord + v][boat_x_coord] == o:
                        check_boat += 1
                if check_boat == boat_lenght:
                    check_boat = 0
                    for v in range(boat_lenght):
                        place_board[boat_y_coord + v][boat_x_coord] = boat_letter
                else:
                    print("\nThere is another ship!\n")
                    check_boat = 0
                    continue
                print("\n")
                for s in place_board:
                    print(*s)
                return place_board
            elif vert_or_horiz == "h":
                for h in range(boat_lenght):
                    if place_board[boat_y_coord][boat_x_coord + h] == o:
                        check_boat += 1
                if check_boat == boat_lenght:
                    check_boat = 0
                    for h in range(boat_lenght):
                        place_board[boat_y_coord][boat_x_coord + h] = boat_letter
                else:
                    print("\nThere is another ship!\n")
                    check_boat = 0
                    continue
                print("\n")
                for s in place_board:
                    print(*s)
                return place_board
            else:
                print("Please enter Y X coordinates and v or h separated with SPACE!")
        except IndexError:
            print("Please enter Y X coordinates and v or h separated with SPACE!")
            continue
        except ValueError:
            print("Please enter Y X coordinates and v or h separated with SPACE!")
            continue
        except KeyboardInterrupt:
            keyboard_quit = input("\nAre you sure you want to quit? (y/n) ")
            if keyboard_quit == "y":
                sys.exit()
            elif keyboard_quit == "n":
                continue
            else:
                continue


def list_present_quick(tree, element):
    for e in tree:
        if e == element:
            return True
        elif type(e) == list:
            if e.count(element) >= 1:
                return True
    return False


def player_shoot(player, place_board, battle_board, sunk_boats):
    while True:
        print(" ")
        for s in battle_board:
            print(*s)
        print("\n \n \n \n \n")
        try:
            input_coord = input("              %s   Where do you want to shoot? : " % player)
            shoot_coord = list(map(int, input_coord.split()))
            if shoot_coord[0] <= 0:
                print("Out of bounds. Please only use coordinates from 1 up to 10!")
                continue
            elif shoot_coord[1] <= 0:
                print("Out of bounds. Please only use coordinates from 1 up to 10!")
                continue
            elif place_board[shoot_coord[0] - 1][shoot_coord[1] - 1] == "o":
                print("\n \n \n \n You Missed!\n")
                battle_board[shoot_coord[0] - 1][shoot_coord[1] - 1] = "-"
            else:
                print("\n \n \n \n You've hit a boat!\n")
                battle_board[shoot_coord[0] - 1][shoot_coord[1] - 1] = "X"
                place_board[shoot_coord[0] - 1][shoot_coord[1] - 1] = "X"

                for ship in ['A', 'B', 'D', 'S', 'P']:
                    if not list_present_quick(place_board, ship):
                        sunk_boats[ship] += 1

                if 1 in sunk_boats.values():
                    print("\n You sank a boat! \n")

                continue

            return place_board, battle_board, sunk_boats

        except IndexError:
            print("Out of bounds. Please only use coordinates from 1 to 10!")
            continue
        except ValueError:
            print("Please enter only integers as 'y' and 'x' coordinates!")
            continue
        except KeyboardInterrupt:
            keyboard_quit = input("\nAre you sure you want to quit? (y/n) ")
            if keyboard_quit == "y":
                sys.exit()
            elif keyboard_quit == "n":
                continue
            else:
                continue


def game_over(player, sunk_boats):
    if min(sunk_boats.values()) > 0:
        print("\n %s WINS! \n" % player)
        return True


def main():
    print("IIIIIIII        II     IIIIIIIIII IIIIIIIIII  II         IIIIIIIII   IIIIIII  II     II   II   IIIIIIII")
    print("II     II      IIII        II         II      II         II         II        II     II   II   II     II")
    print("II     II     II  II       II         II      II         II         II        II     II   II   II     II")
    print("IIIIIIII     II    II      II         II      II         IIIIIII     IIIIII   IIIIIIIII   II   IIIIIIII")
    print("II     II   IIIIIIIIII     II         II      II         II               II  II     II   II   II")
    print("II     II  II        II    II         II      II         II               II  II     II   II   II")
    print("IIIIIIII   II        II    II         II      IIIIIIIII  IIIIIIIII  IIIIIII   II     II   II   II")
    player_1 = "Player 1"
    player_2 = "Player 2"
    p1_sunk_boats = {
        "A": 0,
        "B": 0,
        "D": 0,
        "S": 0,
        "P": 0,
    }
    p2_sunk_boats = {
        "A": 0,
        "B": 0,
        "D": 0,
        "S": 0,
        "P": 0,
    }
    o = "o"
    p1_placement_board = [[o for x in range(10)] for y in range(10)]
    p2_placement_board = [[o for x in range(10)] for y in range(10)]
    p1_battle_board = [[o for x in range(10)] for y in range(10)]
    p2_battle_board = [[o for x in range(10)] for y in range(10)]
    print("\n\n\n\n\n\n\n\n\n\n\n\nPlayer 1's turn\n\n")
    boat_placement('Aircraft Carrier', p1_placement_board, 5, "A")
    boat_placement('Battleship', p1_placement_board, 4, "B")
    boat_placement('Destroyer', p1_placement_board, 3, "D")
    boat_placement('Submarine', p1_placement_board, 3, "S")
    boat_placement('Patrol Boat', p1_placement_board, 2, "P")
    print("\n" * 25)
    print("\n\nPlayer 2's turn\n\n")
    boat_placement('Aircraft Carrier', p2_placement_board, 5, "A")
    boat_placement('Battleship', p2_placement_board, 4, "B")
    boat_placement('Destroyer', p2_placement_board, 3, "D")
    boat_placement('Submarine', p2_placement_board, 3, "S")
    boat_placement('Patrol Boat', p2_placement_board, 2, "P")
    print("\n" * 25)
    print("LET'S START THE BATTLE!\n\nEnter the coordinates in (Y X) format!\n")
    while True:
        if not game_over(player_2, p1_sunk_boats):
            player_shoot(player_1, p2_placement_board, p1_battle_board, p2_sunk_boats)
        else:
            break
        if not game_over(player_1, p2_sunk_boats):
            player_shoot(player_2, p1_placement_board, p2_battle_board, p1_sunk_boats)
        else:
            break
    print("GAME OVER")


main()
