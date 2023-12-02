from random import randint, choice


class Monster:
    """"Монстр"""

    def __init__(self):
        self.name_monster = choice(["Голодный пёс", "Чучело", "Роганосец", "Балор", "Наснас", "Немейский лев"])  # Имена
        self.health_monster = randint(10, 100)  # Здоровье
        self.damage_monster = randint(10, 30)  # Урон
        self.experience_monster = randint(20, 100)  # Опыт

    def print_stats_monster(self):
        '''Cтатистика монстра'''
        print(
            "Статистика монстра:\n"
            f"Здоровье: {self.health_monster}\n"
            f"Урон: {self.damage_monster}\n"
            f"Опыт: {self.experience_monster}\n"
        )


class Player:
    '''Игрок'''

    def __init__(self):
        self.health = 100  # Здоровье
        self.damage = 10  # Урон
        self.level = 1  # Уровень
        self.experience = 0  # Опыт

    def recovery(self, amt=10):
        if self.health < 100:
            self.health = min(self.health + amt, 100)
            self.experience -= 20
        if self.experience <= 0 and self.level == 1:
            self.experience = 0
        if self.experience < 0 and self.level != 1:
            self.level -= 1
            self.experience += 100
            self.damage -= 5
        if self.health >= 100:
            print("Твой запас здоровья максимальный. Заходи в другой раз.")

    def change_level(self, experience_monster):
        self.experience += experience_monster
        if self.experience >= 100:
            self.level += 1
            self.damage += 10
            self.experience -= 100
        if self.experience < 0 and self.level > 1:
            self.level -= 1
            self.experience += 100
        if self.experience < 0 and self.level == 1:
            self.experience = 0

    def print_stats(self):
        '''Статистика игрока'''
        print(
            "\nСтатистика твоего персонажа:\n"
            f"Здоровье: {self.health}\n"
            f"Урон: {self.damage}\n"
            f"Уровень: {self.level}\n"
            f"Опыт: {self.experience}\n"

        )
