from actions import battle, rest, finish, player, print_stats_game
from time import time

print("Добро пожаловать в игру!\n")
name_player = input("Введите имя своего героя: ").title()
start_time = time()
print(f"{name_player}, что бы победить в этой игре, вам понадобится прокачаться до 10 уровня.\n")
player.print_stats()

while not finish():
    print(
        "\nВыберите чем заняться:\n"
        "1: Пойти на заслуженный отдых.\n"
        "2: Спуститься в подземелье.\n"
    )
    choice = input("Ввод: ")
    while choice not in ["1", "2"]:
        print("\nТакого пункта нет, попробуйте выбрать [1 или 2]")
        choice = input("Ввод: ")

    if choice == "1":
        rest()

    else:
        battle()
end_time = time()
elapsed_time_sec = end_time - start_time
hours = int(elapsed_time_sec / 3600)
remaining_sec = int(elapsed_time_sec % 3600)
minutes = int(remaining_sec / 60)
seconds = int(remaining_sec % 60)
print_stats_game()
print(f"Общее время в игре: {hours} часов, {minutes} минут и {seconds} секунд.\n\n")
print(
    "Поздравляю вы прошли эту невероятно сложную, требующую много сил, времени и умнественной деятельности игру.\n"
    "Свой донат вы можете остаивть здесь 😅🤗: [2202 2014 1323 3020]\n"
    f"Прощайте {name_player}."
)
