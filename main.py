# Author: Andrew Pham and Matthew Richardson
# Description: Player wonders around a map and tries to get to the exit without dying from monsters.
# Date: 10/30/24
import hero
import enemy
import map
import check_input
import random

def main():
    user_name = input("What is your name, traveler? ")
    h = hero.Hero(user_name)
    m = map.Map()
    m.reveal(h.loc)
    i = True
    while i: #loop of the game
        print(h)
        print(m.show_map(h.loc))
        user_input = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter Choice: ", 1, 5)
        if user_input == 1:
            move = h.go_north()
            if move == 'o': #check if its 'o'
                print("You cannot go that way...")
                print()
            
            elif m[move[0]][move[1]] == 'n': #checks if 'n
                m.reveal(move)
                print("There is nothing here...\n")
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 's': #checks if 's'
                print("You somehow made it back to the start...\n")
            
            elif m[move[0]][move[1]] == 'i': #checks if 'i'
                m.reveal(move)
                print("You found a Health Potion! You drank it to restore your health.\n")
                h.heal()
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 'm': #checks if 'm'
                monster = enemy.Enemy()
                print(f"You have encounter a {monster}")
                j = True
                while j: #loop for user to attack the monster or run away(exits when monster is killed or user runs away)
                    user_action = check_input.get_int_range(f"1. Attack {monster.name}\n2. Run Away\nEnter choice: ", 1, 2)
                    if user_action == 1: #user attacks
                        result = h.attack(monster)
                        print(result)
                        if monster.hp != 0: #checks if monster is not already dead
                            result = monster.attack(h)
                            print(result)
                            if h.hp == 0: #after monster attacks hero, checks if hero died from that monster and ends the game if hero died
                                print("You have been slain.\nGAME OVER!")
                                j = False
                                i = False
                        elif monster.hp == 0 :
                            print(f"You have slain a {monster.name}\n")
                            j = False
                    else: #user runs away
                        m.reveal(move)
                        rand_move = [h.go_north(), h.go_south(), h.go_east(), h.go_west()]
                        move = random.choice(rand_move)
                        j = False

            elif m[move[0]][move[1]] == 'f':
                print("Congratulations! You found the exit.\nGAME OVER!")
                i = False
        
        elif user_input == 2:
            move = h.go_south()
            if move == 'o': #check if its 'o'
                print("You cannot go that way...")
                print()
            
            elif m[move[0]][move[1]] == 'n': #checks if 'n
                m.reveal(move)
                print("There is nothing here...\n")
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 's': #checks if 's'
                print("You somehow made it back to the start...\n")
            
            elif m[move[0]][move[1]] == 'i': #checks if 'i'
                m.reveal(move)
                print("You found a Health Potion! You drank it to restore your health.\n")
                h.heal()
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 'm': #checks if 'm'
                monster = enemy.Enemy()
                print(f"You have encounter a {monster}")
                j = True
                while j: #loop for user to attack the monster or run away(exits when monster is killed or user runs away)
                    user_action = check_input.get_int_range(f"1. Attack {monster.name}\n2. Run Away\nEnter choice: ", 1, 2)
                    if user_action == 1: #user attacks
                        result = h.attack(monster)
                        print(result)
                        if monster.hp != 0: #checks if monster is not already dead
                            result = monster.attack(h)
                            print(result)
                        elif monster.hp == 0 :
                            print(f"You have slain a {monster.name}\n")
                            j = False
                    else: #user runs away
                        m.reveal(move)
                        rand_move = [h.go_north(), h.go_south(), h.go_east(), h.go_west()]
                        move = random.choice(rand_move)
                        j = False

            elif m[move[0]][move[1]] == 'f':
                print("Congratulations! You found the exit.\nGAME OVER!")
                i = False
        
        elif user_input == 3:
            move = h.go_east()
            if move == 'o': #check if its 'o'
                print("You cannot go that way...")
                print()
            
            elif m[move[0]][move[1]] == 'n': #checks if 'n
                m.reveal(move)
                print("There is nothing here...\n")
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 's': #checks if 's'
                print("You somehow made it back to the start...\n")
            
            elif m[move[0]][move[1]] == 'i': #checks if 'i'
                m.reveal(move)
                print("You found a Health Potion! You drank it to restore your health.\n")
                h.heal()
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 'm': #checks if 'm'
                monster = enemy.Enemy()
                print(f"You have encounter a {monster}")
                j = True
                while j: #loop for user to attack the monster or run away(exits when monster is killed or user runs away)
                    user_action = check_input.get_int_range(f"1. Attack {monster.name}\n2. Run Away\nEnter choice: ", 1, 2)
                    if user_action == 1: #user attacks
                        result = h.attack(monster)
                        print(result)
                        if monster.hp != 0: #checks if monster is not already dead
                            result = monster.attack(h)
                            print(result)
                        elif monster.hp == 0 :
                            print(f"You have slain a {monster.name}\n")
                            j = False
                    else: #user runs away
                        m.reveal(move)
                        rand_move = [h.go_north(), h.go_south(), h.go_east(), h.go_west()]
                        move = random.choice(rand_move)
                        j = False

            elif m[move[0]][move[1]] == 'f':
                print("Congratulations! You found the exit.\nGAME OVER!")
                i = False

        elif user_input == 4:
            move = h.go_west()
            if move == 'o': #check if its 'o'
                print("You cannot go that way...")
                print()
            
            elif m[move[0]][move[1]] == 'n': #checks if 'n'
                m.reveal(move)
                print("There is nothing here...\n")
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 's': #checks if 's'
                print("You somehow made it back to the start...\n")
            
            elif m[move[0]][move[1]] == 'i': #checks if 'i'
                m.reveal(move)
                print("You found a Health Potion! You drank it to restore your health.\n")
                h.heal()
                m.remove_at_loc(move)
            
            elif m[move[0]][move[1]] == 'm': #checks if 'm'
                monster = enemy.Enemy()
                print(f"You have encounter a {monster}")
                j = True
                while j: #loop for user to attack the monster or run away(exits when monster is killed or user runs away)
                    user_action = check_input.get_int_range(f"1. Attack {monster.name}\n2. Run Away\nEnter choice: ", 1, 2)
                    if user_action == 1: #user attacks
                        result = h.attack(monster)
                        print(result)
                        if monster.hp != 0: #checks if monster is not already dead
                            result = monster.attack(h)
                            print(result)
                        elif monster.hp == 0 :
                            print(f"You have slain a {monster.name}\n")
                            j = False
                    else: #user runs away
                        m.reveal(move)
                        rand_move = [h.go_north(), h.go_south(), h.go_east(), h.go_west()]
                        move = random.choice(rand_move)
                        print("You ran away!")
                        j = False

            elif m[move[0]][move[1]] == 'f':
                print("Congratulations! You found the exit.\nGAME OVER!")
                i = False

        else:
            i = False

main()