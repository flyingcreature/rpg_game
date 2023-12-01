from classes import Player, Monster
from random import randint
from time import sleep

player = Player()
number_of_defeats = 0
number_of_wins = 0
amount_of_rest = 0
hit = 0
critical_strike = 0
blunder = 0


def battle():
    if player.health > 0:
        monster = Monster()

        print(
            "\nТы спускаешь в подземелье, что бы дать отпор монстрам.\n"
            f"На твоём пути встаёт {monster.name_monster}.\n"
        )
        monster.print_stats_monster()
        print("\nДа начнется битва!")

        while player.health > 0 and monster.health_monster > 0:
            damage_player = (player.damage + randint(-5, 5)) * randint(0, 2)  # от базового урона игрока +- разброс в 5 едениц, и вероятность промаха, удара или 2x удара.
            monster.health_monster -= damage_player
            global hit
            hit += 1
            sleep(3)
            damage_monster = (monster.damage_monster + randint(-5, 5)) * randint(0, 2)  # от базового урона монстра +- разброс в 5 едениц, и вероятность промаха, удара или 2x удара.
            if monster.health_monster < 0:
                monster.health_monster = 0

            if damage_player == 0:
                print("К сожалению вы промахнулись.")
                global blunder
                blunder += 1
            elif damage_player > player.damage:
                print("Сработал критический удар, ваш урон увеличлся в двое.")
                global critical_strike
                critical_strike += 1

            print(
                f'Вы нанесли монстру ({damage_player}) едениц урона. Его здоровье составляет ({monster.health_monster}).')
            if monster.health_monster > 0:  # Если монстр остался жив после атаки игрока, он наносит свою атаку.
                player.health -= damage_monster
                if damage_monster == 0:
                    print("Монстр промахнулся.")
                elif damage_monster > monster.damage_monster:
                    print("Сработал критический удар, урон у монстра увеличлся в двое.")
                if player.health < 0:
                    player.health = 0
                print(f'Вам нанесли ({damage_monster}) едениц урона. Ваше здоровье составляет ({player.health}).\n')

            if player.health <= 0:
                player.health = 100
                player.level = 1
                player.experience = 0
                print("\nВы проиграли!")
                player.print_stats()
                global number_of_defeats
                number_of_defeats += 1
                break

            if monster.health_monster <= 0:
                print("\nВы победили!")
                player.change_level(monster.experience_monster)
                player.print_stats()
                global number_of_wins
                number_of_wins += 1
                break
    else:
        print("Ваше здоровье на 0, вам нужно отдохнуть!")


def rest():
    print("\nНам всем нужно иногда отдохнуть.\n")
    print("Здесь вы сможете поднять здоровье, но придется заплатить своим опытом.\n")
    player.recovery()
    player.print_stats()
    global amount_of_rest
    amount_of_rest += 1


def print_stats_game():
    print(
        f"Количество побед: {number_of_wins}\n"
        f"Количсетво поражений: {number_of_defeats}\n"
        f"Количество заживления: {amount_of_rest}\n"
        f"Количсетво ударов: {hit}\n"
        f"Количество критических ударов: {critical_strike}\n"
        f"Количество промахов: {blunder}"
    )


def finish():
    if player.level == 10:
        return True
    else:
        return False

