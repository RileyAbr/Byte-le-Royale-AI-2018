import random

from game.client.user_client import UserClient
from game.common.enums import *


class CustomClient(UserClient):
    global knight_counter
    knight_counter = 0
    global wizard_counter
    wizard_counter = 0
    global pikeman_counter
    pikeman_counter = 0

    global first_turn
    first_turn = True
    global second_turn
    second_turn = False

    global current_floor
    current_floor = 0

    global turns_remaining
    turns_remaining = 29

    global ol_flip_flop
    ol_flip_flop = True

    global shopping_list
    shopping_list = [1, 0, 1, 1, 1, 1]
    global next_on_list
    next_on_list = 0
    global last_alive
    last_alive = False

    def __init__(self):
        """ Use the constructor to initialize any variables you would like to track between turns. """

    def team_name(self):
        print("Sending Team Name")

        return "Byte Lé-Royale"

    def unit_choice(self):
        print("Sending Unit Choices")

        return [
            {
                "name": "zach",
                "class": UnitClass.knight
            },
            {
                "name": "wyly 2.1",
                "class": UnitClass.wizard
            },
            {
                "name": "riley",
                "class": UnitClass.pikeman
            },
            {
                "name": "quinn",
                "class": UnitClass.rogue
            }
        ]

    def town(self, units, gold, store):
        print()
        print("*" * 50)
        print("Town")
        print("*" * 50)
        print("Gold: {}".format(gold))
        global next_on_list
        global shopping_list

        if store.get_town_number() is 0:
            global current_floor
            current_floor = 1
            unit1 = self.get_unit("zach", units)
            unit2 = self.get_unit("wyly 2.1", units)
            unit3 = self.get_unit("riley", units)
            unit4 = self.get_unit("quinn", units)
            store.purchase(unit1, ItemType.armor, 1)
            store.purchase(unit2, ItemType.armor, 1)
            store.purchase(unit3, ItemType.armor, 1)
            store.purchase(unit4, ItemType.armor, 1)
            if unit2 is not None: #Wizard spells
                store.purchase(unit2, ItemType.wand, 1)
                # store.purchase(unit2, ItemType.fire_ball, 1, item_slot=1)
                # store.purchase(unit2, ItemType.sonic_blast, 1, item_slot=2)
                # store.purchase(unit2, ItemType.ice_spike, 1, item_slot=3)

            #if unit4 is not None: #Rogue or Alchemist. Bombs are free
                #store.purchase(unit4, ItemType.guided_bomb, 1, item_slot=2)
                #store.purchase(unit4, ItemType.frost_bomb, 1, item_slot=3)
        elif store.get_town_number() % 2 == 1:  #Print lines are broken
            current_floor = store.get_town_number() - 1
            unit1 = self.get_unit("zach", units)
            unit2 = self.get_unit("wyly 2.1", units)
            unit3 = self.get_unit("riley", units)
            unit4 = self.get_unit("quinn", units)
            current_town = store.get_town_number()
            current_gold = gold
            print("Town time")
            continue_shopping = True
            while continue_shopping:
                continue_shopping = False
                # store.purchase(unit3, ItemType.spear, unit3.primary_weapon.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: spear lvl ")
                # store.purchase(unit1, ItemType.armor, unit1.armor.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: armor lvl ")
                # store.purchase(unit4, ItemType.dagger, unit4.primary_weapon.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: dagger lvl ")
                # store.purchase(unit1, ItemType.sword, unit1.primary_weapon.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("..")
                # store.purchase(unit2, ItemType.wand, unit2.primary_weapon.level + 2)
                # if current_gold > gold:
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: dagger lvl ")
                # store.purchase(unit2, ItemType.armor, unit2.armor.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: armor lvl " + shopping_list[1])
                # store.purchase(unit4, ItemType.armor, unit4.armor.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: armor lvl ")
                # store.purchase(unit3, ItemType.armor, unit3.armor.level + 2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: armor lvl ")
                store.purchase(unit3, ItemType.spear, current_town + 1)
                if current_gold > gold:  #purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: spear lvl ")
                store.purchase(unit1, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl ")
                store.purchase(unit4, ItemType.dagger, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: dagger lvl " )
                store.purchase(unit1, ItemType.sword, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: sword lvl " + unit1.primary_weapon.level + 1)
                store.purchase(unit2, ItemType.wand, current_town + 1)
                if current_gold > gold:
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: dagger lvl ")
                # store.purchase(unit2, ItemType.ice_spike, unit2.spell_3.level + 1, item_slot=3)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: ice_spike lvl ")
                # store.purchase(unit2, ItemType.sonic_blast, unit2.spell_2.level + 1, item_slot=2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: sonic_blast lvl " + unit2.spell_1.level)
                # store.purchase(unit2, ItemType.fire_ball, unit2.spell_1.level + 1, item_slot=1)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: fire_ball lvl " + unit2.spell_1.level + 1)
                store.purchase(unit2, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl " + shopping_list[1])
                store.purchase(unit4, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl ")
                store.purchase(unit3, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl ")
        elif store.get_town_number() % 2 == 0:
            current_floor = store.get_town_number() - 1
            unit1 = self.get_unit("zach", units)
            unit2 = self.get_unit("wyly 2.1", units)
            unit3 = self.get_unit("riley", units)
            unit4 = self.get_unit("quinn", units)
            current_town = store.get_town_number()
            current_gold = gold
            print("Town time")
            continue_shopping = True
            while continue_shopping:
                continue_shopping = False
                store.purchase(unit3, ItemType.spear, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: spear lvl ")
                store.purchase(unit3, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl ")
                store.purchase(unit4, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl ")
                store.purchase(unit2, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl " + shopping_list[1])
                store.purchase(unit2, ItemType.wand, current_town + 1)
                if current_gold > gold:
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: dagger lvl ") #...
                store.purchase(unit1, ItemType.sword, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: sword lvl " + unit1.primary_weapon.level + 1)
                store.purchase(unit4, ItemType.dagger, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: dagger lvl ")
                store.purchase(unit1, ItemType.armor, current_town + 1)
                if current_gold > gold:  # purchase went through
                    continue_shopping = True
                    current_gold = gold
                    print("Purchased: armor lvl ")



                # store.purchase(unit2, ItemType.ice_spike, unit2.spell_3.level + 1, item_slot=3)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: ice_spike lvl ")
                # store.purchase(unit2, ItemType.sonic_blast, unit2.spell_2.level + 1, item_slot=2)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: sonic_blast lvl " + unit2.spell_1.level)
                # store.purchase(unit2, ItemType.fire_ball, unit2.spell_1.level + 1, item_slot=1)
                # if current_gold > gold:  # purchase went through
                #     continue_shopping = True
                #     current_gold = gold
                #     print("Purchased: fire_ball lvl " + unit2.spell_1.level + 1)



                #wizard, rogue, pikeman
        # elif store.get_town_number() is 1:
        #     unit1 = self.get_unit("zach", units)
        #     unit2 = self.get_unit("wyly 2.1", units)
        #     unit3 = self.get_unit("riley", units)
        #     unit4 = self.get_unit("quinn", units)
        #     if unit1 is not None:
        #         store.purchase(unit1, ItemType.armor, 2)
        #     if unit3 is not None:
        #         store.purchase(unit3, ItemType.spear, 2)
        #     if unit4 is not None:
        #         store.purchase(unit4, ItemType.dagger, 2)
        #     if unit2 is not None:
        #         store.purchase
        #         #store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
        #         #store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)
        #
        #
        # elif store.get_town_number() is 2:
        #     unit1 = self.get_unit("zach", units)
        #     unit2 = self.get_unit("wyly 2.1", units)
        #     unit3 = self.get_unit("riley", units)
        #     unit4 = self.get_unit("quinn", units)
        #     if unit1 is not None:
        #         store.purchase(unit1, ItemType.sword, 2)
        #     if unit2 is not None:
        #         store.purchase(unit2, ItemType.mace, 2)
        #     if unit3 is not None:
        #         store.purchase(unit3, ItemType.spear, 2)
        #     if unit4 is not None:
        #         store.purchase(unit4, ItemType.dagger, 2)
        #         #store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
        #         #store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)
        #
        # elif store.get_town_number() is 3:
        #     unit1 = self.get_unit("zach", units)
        #     unit2 = self.get_unit("wyly 2.1", units)
        #     unit3 = self.get_unit("riley", units)
        #     unit4 = self.get_unit("quinn", units)
        #     if unit1 is not None:
        #         store.purchase(unit1, ItemType.sword, 2)
        #     if unit2 is not None:
        #         store.purchase(unit2, ItemType.mace, 2)
        #     if unit3 is not None:
        #         store.purchase(unit3, ItemType.spear, 2)
        #     if unit4 is not None:
        #         store.purchase(unit4, ItemType.dagger, 2)
        #         #store.purchase(unit4, ItemType.fire_bomb, 1, item_slot=2)
        #         #store.purchase(unit4, ItemType.shock_bomb, 1, item_slot=3)

    def room_choice(self, units, options):
        # global knight_counter
        # knight_counter = 0
        # global wizard_counter
        # wizard_counter = 0
        # global pikeman_counter
        # pikeman_counter = 0
        global last_alive
        last_alive = False
        global first_turn
        first_turn = True
        global turns_remaining
        turns_remaining = 29
        global ol_flip_flop
        ol_flip_flop = True
        global second_turn
        second_turn = False

        if len(options) == 1: #don't change this, only one option available
            return Direction.forward


        elif len(options) == 2:  #return Direction.left or Direction.right
            doorLeft = options[Direction.left]
            doorRight = options[Direction.right]
            print(doorLeft)
            print(doorRight)

            print(doorLeft.node_type)
            print(doorRight.node_type)

            doorLeftValue = 10
            doorRightValue = 10
            unit1 = self.get_unit("zach", units)
            unit2 = self.get_unit("wyly 2.1", units)
            unit3 = self.get_unit("riley", units)
            unit4 = self.get_unit("quinn", units)


            if doorLeft.node_type == NodeType.monster and doorRight.node_type == NodeType.trap:
                team_health = unit1.health + unit2.health + unit3.health + unit4.health
                team_current_health = unit1.current_health + unit2.current_health + unit3.current_health + unit4.current_health
                if team_current_health <= team_health * .25:
                    return Direction.right
                else:
                    return Direction.left
            elif doorLeft.node_type == NodeType.trap and doorRight.node_type == NodeType.monster:
                team_health = unit1.health + unit2.health + unit3.health + unit4.health
                team_current_health = unit1.current_health + unit2.current_health + unit3.current_health + unit4.current_health
                if team_current_health <= team_health * .25:
                    return Direction.left
                else:
                    return Direction.right
            elif doorLeft.node_type == NodeType.monster and doorRight.node_type == NodeType.monster:
                global current_floor

                if doorLeft.node_type == MonsterType.beholder:
                    doorLeftValue = 1
                elif doorLeft.node_type == MonsterType.vampire:
                    doorLeftValue = 2
                if current_floor <= 4:
                    if doorLeft.node_type == MonsterType.dragon:
                        doorLeftValue = 3
                    if doorLeft.node_type == MonsterType.slime:
                        doorLeftValue = 4
                    if doorLeft.node_type == MonsterType.wraith:
                        doorLeftValue = 5
                    if doorLeft.node_type == MonsterType.wisp:
                        doorLeftValue = 6
                    if doorLeft.node_type == MonsterType.minotaur:
                        doorLeftValue = 7
                else:
                    if doorLeft.node_type == MonsterType.slime:
                        doorLeftValue = 3
                    if doorLeft.node_type == MonsterType.minotaur:
                        doorLeftValue = 4
                    if doorLeft.node_type == MonsterType.wisp:
                        doorLeftValue = 5
                    if doorLeft.node_type == MonsterType.wraith:
                        doorLeftValue = 6
                    if doorLeft.node_type == MonsterType.dragon:
                        doorLeftValue = 7
                if doorRight.node_type == MonsterType.beholder:
                    doorRightValue = 1
                elif doorRight.node_type == MonsterType.vampire:
                    doorRightValue = 2
                if current_floor <= 4:
                    if doorRight.node_type == MonsterType.dragon:
                        doorRightValue = 3
                    if doorRight.node_type == MonsterType.slime:
                        doorRightValue = 4
                    if doorRight.node_type == MonsterType.wraith:
                        doorRightValue = 5
                    if doorRight.node_type == MonsterType.wisp:
                        doorRightValue = 6
                    if doorRight.node_type == MonsterType.minotaur:
                        doorRightValue = 7
                else:
                    if doorRight.node_type == MonsterType.slime:
                        doorRightValue = 3
                    if doorRight.node_type == MonsterType.minotaur:
                        doorRightValue = 4
                    if doorRight.node_type == MonsterType.wisp:
                        doorRightValue = 5
                    if doorRight.node_type == MonsterType.wraith:
                        doorRightValue = 6
                    if doorRight.node_type == MonsterType.dragon:
                        doorRightValue = 7

                # Decide which monster is best
                if doorLeftValue < doorRightValue:
                    return Direction.left
                elif doorLeftValue > doorRightValue:
                    return Direction.right
                else:
                    return Direction.left



            elif doorLeft.node_type == NodeType.trap and doorRight.node_type == NodeType.trap:
                if doorLeft.node_type == TrapType.falling_ceiling:
                    if unit1.current_health == 0 or unit2.current_health == 0 or unit3.current_health == 0 or unit4.current_health == 0:
                        doorLeftValue = 7
                    else:
                        doorLeftValue = 1
                if doorLeft.node_type == TrapType.pendulum_bridge:
                    doorLeftValue = 2
                if doorLeft.node_type == TrapType.riddles_of_the_sphinx:
                    doorLeftValue = 3



                if unit1.current_health < unit1.health * .3 or unit2.current_health < unit2.health * .3 or unit3.current_health < unit3.health * .3 or unit4.current_health < unit4.health * .3:
                    if doorLeft.node_type == TrapType.eldritch_barrier:
                        doorLeftValue = 4
                    elif doorLeft.node_type == TrapType.spike_trap:
                        doorLeftValue = 5
                    elif doorLeft.node_type == TrapType.puzzle_box:
                        doorLeftValue = 6
                else:
                    if doorLeft.node_type == TrapType.puzzle_box:
                        doorLeftValue = 4
                    if doorLeft.node_type == TrapType.eldritch_barrier:
                        doorLeftValue = 5
                    elif doorLeft.node_type == TrapType.spike_trap:
                        doorLeftValue = 6

                if doorLeft.node_type == TrapType.falling_ceiling:
                    if unit1.current_health == 0 or unit2.current_health == 0 or unit3.current_health == 0 or unit4.current_health == 0:
                        doorLeftValue = 7
                    else:
                        doorLeftValue = 1
                if doorRight.node_type == TrapType.pendulum_bridge:
                    doorRightValue = 2
                if doorRight.node_type == TrapType.riddles_of_the_sphinx:
                    doorRightValue = 3

                if unit1.current_health < unit1.health * .3 or unit2.current_health < unit2.health * .3 or unit3.current_health < unit3.health * .3 or unit4.current_health < unit4.health * .3:
                    if doorRight.node_type == TrapType.eldritch_barrier:
                        doorRightValue = 4
                    elif doorRight.node_type == TrapType.spike_trap:
                        doorRightValue = 5
                    elif doorRight.node_type == TrapType.puzzle_box:
                        doorRightValue = 6
                else:
                    if doorRight.node_type == TrapType.puzzle_box:
                        doorRightValue = 4
                    if doorRight.node_type == TrapType.eldritch_barrier:
                        doorRightValue = 5
                    elif doorRight.node_type == TrapType.spike_trap:
                        doorRightValue = 6

                #Decide which trap is best
                if doorLeftValue < doorRightValue:
                    return Direction.left
                elif doorLeftValue > doorRightValue:
                    return Direction.right
                else:
                    return Direction.left
            else:
                print("random door")
                return Direction.left
        else:
            return MessageType.null

    def combat_round(self, monster, units):
        global pikeman_counter
        global wizard_counter
        global knight_counter
        global first_round

        print()
        print("*" * 50)
        print("Combat")
        print("*" * 50)
        print(monster.summary())

        for u in units:
            print(u.summary())

        for u in units:

            if u.unit_class == UnitClass.rogue:
                if u.bomb_1_quantity > 0:
                    u.use_bomb_1()
                elif u.bomb_2_quantity > 0:
                    u.use_bomb_2()
                elif u.bomb_3_quantity > 0:
                    u.use_bomb_3()
                else:
                    u.attack()

            elif u.unit_class == UnitClass.pikeman:
                unit1 = self.get_unit("zach", units)
                unit2 = self.get_unit("wyly 2.1", units)
                unit4 = self.get_unit("quinn", units)

                if pikeman_counter == 0:
                    print("pikeman: turn 1!")
                    if unit1.current_health == 0 and unit4.current_health == 0 and not unit2.current_health == 0:
                        pikeman_counter += 1
                        u.attack()
                    else:
                        pikeman_counter += 1
                        u.target_weakness()
                        #print("Wizard buff!")
                elif pikeman_counter == 1:
                    print("pikeman: turn 2!")
                    pikeman_counter += 1
                    u.target_weakness()
                elif pikeman_counter == 2:
                    pikeman_counter = 0
                    print("pikeman: turn 3!")
                    u.target_weakness()

            elif u.unit_class == UnitClass.knight:
                unit1 = self.get_unit("zach", units)
                unit2 = self.get_unit("wyly 2.1", units)
                unit3 = self.get_unit("riley", units)
                unit4 = self.get_unit("quinn", units)

                targeted_enemy = unit2
                targeting_melee = False
                targeting_group = False
                if monster.monster_type == MonsterType.dragon:
                    targeted_enemy = unit1
                elif monster.monster_type == MonsterType.wraith:
                    targeted_enemy = unit2
                elif monster.monster_type == MonsterType.minotaur:
                    # if first_round:
                    #     original_health1 = unit1.current_health
                    #     original_health2 = unit2.current_health
                    #     original_health3 = unit3.current_health
                    #     original_health4 = unit4.current_health
                    #     first_round = False
                    #     second_round = True
                    # elif second_round:
                    #     if unit1.current_health != 0 and unit1.current_health < original_health1:
                    #         targeted_enemy
                    if unit3.current_health == 0 and unit4.current_health == 0:
                        targeted_enemy = unit1
                    else:
                        targeting_melee = True
                elif monster.monster_type == MonsterType.beholder:
                    targeting_group = True
                elif monster.monster_type == MonsterType.wisp:
                    #????
                    targeted_enemy = unit2
                elif monster.monster_type == MonsterType.vampire:
                    if unit3.current_health == 0 and unit4.current_health == 0:
                        targeted_enemy = unit1
                    else:
                        targeting_melee = True
                else:
                    targeting_group = True

                if targeted_enemy == unit1 or u.current_health < u.health * .4:
                    u.attack()
                elif targeting_group:
                    if (unit2.current_health < unit2.health * .15 and unit2.current_health != 0) or (unit3.current_health < unit3.health * .15 and unit3.current_health != 0) or (unit4.current_health < unit4.health * .15 and unit4.current_health != 0):
                        u.taunt()
                    elif (unit2.current_health < unit2.health * .3 and unit2.current_health != 0) or (unit3.current_health < unit3.health * .3 and unit3.current_health != 0) or (unit4.current_health < unit4.health * .3 and unit4.current_health != 0):
                        if knight_counter == 0:
                            print("knight: turn 1!")
                            knight_counter += 1
                            u.taunt()
                        elif knight_counter == 1:
                            print("knight: turn 2!")
                            knight_counter = 0
                            u.attack()
                    else:
                        u.attack()
                elif targeting_melee:
                    if (unit3.current_health < unit3.health * .1 and unit3.current_health != 0) or (unit4.current_health < unit4.health * .1 and unit4.current_health != 0):
                        u.taunt()
                    elif (unit3.current_health < unit3.health * .2 and unit3.current_health != 0) or (unit4.current_health < unit4.health * .2 and unit4.current_health != 0):
                        if knight_counter == 0:
                            print("knight: turn 1!")
                            knight_counter += 1
                            u.taunt()
                        elif knight_counter == 1:
                            print("knight: turn 2!")
                            knight_counter = 0
                            u.attack()
                    else:
                        u.attack()
                elif targeted_enemy == unit2:
                    if unit2.current_health < unit2.health * .3 and unit2.current_health != 0:
                        u.taunt()
                    if unit2.current_health < unit2.health * .5 and unit2.current_health != 0:
                        if knight_counter == 0:
                            print("knight: turn 1!")
                            knight_counter += 1
                            u.taunt()
                        elif knight_counter == 1:
                            print("knight: turn 2!")
                            knight_counter = 0
                            u.attack()
                    if unit2.current_health < unit2.health * .7 and unit2.current_health != 0:
                        if knight_counter == 0:
                            print("knight: turn 1!")
                            knight_counter += 1
                            u.taunt()
                        elif knight_counter == 1:
                            print("knight: turn 2!")
                            knight_counter += 1
                            u.attack()
                        elif knight_counter == 2:
                            print("knight: turn 3!")
                            knight_counter = 0
                            u.attack()
                    else:
                        u.attack()
                    # elif knight_counter == 2:
                    #     print("knight: turn 3!")
                    #     knight_counter = 0
                    #     u.attack()

            elif u.unit_class == UnitClass.brawler:
                if monster.current_health > 5000 and u.current_health > 6000:
                    u.fit_of_rage()
                    print("Getting real angry!")
                else:
                    u.attack()
            elif u.unit_class == UnitClass.wizard:
                if wizard_counter == 0:  #buff
                    unit1 = self.get_unit("zach", units)
                    unit3 = self.get_unit("riley", units)
                    unit4 = self.get_unit("quinn", units)
                    print("wizard: turn 1!")
                    wizard_counter += 1
                    if unit4.current_health != 0:
                        u.invigorate(unit4)
                    elif unit1.current_health != 0:
                        u.invigorate(unit1)
                    elif unit3.current_health != 0:
                        u.invigorate(unit3)
                    else:
                        u.attack()

                    print("invigorating!")

                elif wizard_counter == 1: #attack
                    print("wizard: turn 2!")
                    wizard_counter += 1
                    u.attack()
                    # if monster.monster_type == MonsterType.beholder or monster.monster_type == MonsterType.wisp or monster.monster_type == MonsterType.minotaur:
                    #     u.use_spell_3()
                    # elif monster.monster_type == MonsterType.dragon or monster.monster_type == MonsterType.slime:
                    #     u.use_spell_2()
                    # else:
                    #     u.use_spell_1()

                elif wizard_counter == 2: #attack and reset
                    print("wizard: turn 3!")
                    wizard_counter = 0
                    u.attack()
                    # if monster.monster_type == MonsterType.beholder or monster.monster_type == MonsterType.wisp or monster.monster_type == MonsterType.minotaur:
                    #     u.use_spell_3()
                    # elif monster.monster_type == MonsterType.dragon or monster.monster_type == MonsterType.slime:
                    #     u.use_spell_2()
                    # else:
                    #     u.use_spell_1()
            else: #Any other class
                u.attack()

    def trap_round(self, trap, units):
        print()
        print("*" * 50)
        print("Trap!")
        print("*" * 50)
        print(trap.summary())
        current_unit = 4
        global first_turn
        global turns_remaining
        global ol_flip_flop
        for u in units:
            print(u.summary())

        unit1 = self.get_unit("zach", units)
        unit2 = self.get_unit("wyly 2.1", units)
        unit3 = self.get_unit("riley", units)
        unit4 = self.get_unit("quinn", units)
        lowest_health_guy = unit1
        global last_alive
        last_alive = False
        if unit1.current_health != 0 and unit1.current_health < unit2.current_health and unit1.current_health < unit3.current_health and unit1.current_health < unit4.current_health:
            lowest_health_guy = unit1
        elif unit2.current_health != 0 and unit2.current_health < unit3.current_health and unit2.current_health < unit4.current_health:
            lowest_health_guy = unit2
        elif unit3.current_health != 0 and unit3.current_health < unit4.current_health:
            lowest_health_guy = unit3
        else:
            lowest_health_guy = unit4

        if unit1.current_health == 0 and unit2.current_health == 0 and unit3.current_health == 0:
            last_alive = True
        if unit4.current_health == 0 and unit2.current_health == 0 and unit3.current_health == 0:
            last_alive = True
        if unit4.current_health == 0 and unit1.current_health == 0 and unit3.current_health == 0:
            last_alive = True
        if unit4.current_health == 0 and unit1.current_health == 0 and unit2.current_health == 0:
            last_alive = True

        global rogueWorking
        rogueWorking = True
        if unit4.current_health <= (unit4.health / 4):
            rogueWorking = False

        for u in units:
            current_unit -= 1
            # print("Unit:")
            # print(u)
            # print("Current Effort: ")
            # print(trap.current_effort)
            # print("Current EFfort for me: ")
            # print(trap.current_effort[current_unit])
            # print("Required Effort: ")
            # print(trap.required_effort)
            if trap.trap_type == TrapType.puzzle_box:
                if u == lowest_health_guy and not last_alive:
                    u.trap_action = TrapAction.evade
                else:
                    u.trap_action = TrapAction.little_effort

            if trap.trap_type == TrapType.eldritch_barrier:
                if u.unit_class == UnitClass.rogue and first_turn:
                    u.trap_action = TrapAction.large_effort
                    first_turn = False
                elif trap.current_effort[current_unit] == trap.required_effort:
                    u.trap_action = TrapAction.evade
                else:
                    u.trap_action = TrapAction.little_effort
            if trap.trap_type == TrapType.falling_ceiling:
                u.trap_action = TrapAction.little_effort
            if trap.trap_type == TrapType.pendulum_bridge:
                if u.unit_class == UnitClass.rogue:
                    u.trap_action = TrapAction.little_effort
                elif rogueWorking:
                    u.trap_action = TrapAction.evade
                else:
                    u.trap_action = TrapAction.little_effort

            if trap.trap_type == TrapType.riddles_of_the_sphinx:
                if u.unit_class == UnitClass.rogue:
                    if turns_remaining > 0:
                        u.trap_action = TrapAction.little_effort
                        turns_remaining -= 1
                    else:
                        if ol_flip_flop:
                            u.trap_action = TrapAction.evade
                            ol_flip_flop = False
                        else:
                            u.trap_action = TrapAction.little_effort
                            ol_flip_flop = True
                elif rogueWorking:
                    u.trap_action = TrapAction.evade
                else:
                    u.trap_action = TrapAction.little_effort
            if trap.trap_type == TrapType.spike_trap:
                if u.unit_class == UnitClass.rogue and first_turn:
                    u.trap_action = TrapAction.large_effort
                    first_turn = False
                if trap.current_effort[current_unit] == trap.required_effort:
                    u.trap_action = TrapAction.evade
                else:
                    u.trap_action = TrapAction.little_effort

    ##################
    # Helper Methods #
    ##################

    def get_unit(self, name, units):
        for unit in units:
            if unit.name.lower() == name.lower():
                return unit
        return None


