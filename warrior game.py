import math
import random


class Warrior:
    def __init__(self, name="", health=0, atk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.atk_max = atk_max
        self.block_max = block_max

    def attack(self):
        atk_amt = self.atk_max * (random.random() + .5)
        return atk_amt

    def block(self):
        block_amt = self.block_max * (random.random() + .5)
        return block_amt


class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def get_attack_result(warrior_a, warrior_b):

        warrior_a_atk_amt = warrior_a.attack()
        warrior_b_block_amt = warrior_b.block()

        damage_2_warrior_b = math.ceil(warrior_a_atk_amt - warrior_b_block_amt)
        warrior_b.health = warrior_b.health - damage_2_warrior_b

        print("{} attacks {} and deals {} damage".format(warrior_a.name,
                                                         warrior_b.name, damage_2_warrior_b))
        print("{} is down to {} health".format(warrior_b.name, warrior_b.health))

        if warrior_b.health <= 0:
            print("{} has died and {} is Victorious".format(warrior_b.name, warrior_a.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    while True:
        try:
            player_1 = Warrior(input("name"), int(input("health")), int(input("attack")), int(input("defence")))

            player_2 = Warrior(input("name"), int(input("health")), int(input("attack")), int(input("defence")))

            battle = Battle()

            battle.start_fight(player_1, player_2)
            break

        except ValueError:
            print("bro wrong type bro")


main()
