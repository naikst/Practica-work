import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f'{self.name} получил {amount} урона. Текущее здоровье: {self.health}'

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        return f'{self.name} восстановил {amount} здоровья. Текущее здоровье: {self.health}'


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 25
        self.armor = 15


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f'Текущее здоровье: {self.health}'


class Room:
    def __init__(self, desc):
        self.desc = desc
        self.enemy = None

    def set_enemy(self, enemy):
        self.enemy = enemy

    def fight(self, player):
        if not self.enemy:
            return 'В комнате нет противника, с кем можно сразиться.'
        if player.health <= 0:
            return f'{player.name} мёртв, не может сражаться.'
        if self.enemy.health <= 0:
            return f'{self.enemy.name} уже побежден.'

        fight_log = []
        fight_log.append(f'{player.name} вступает в бой с {self.enemy.name}!')

        # Заранее заданные последовательности действий для вывода
        player_attacks = [25, 15]  # Урон героя
        enemy_attacks = [18, 12]  # Урон врага
        critical_hit = 30  # Критический урон
        critical_turn = 1  # Ход, на котором происходит критический удар

        for turn, damage in enumerate(player_attacks):
            # Ход игрока: атака врага
            fight_log.append(f'{self.enemy.name} получил {damage} урона. {self.enemy.take_damage(damage)}')

            # Критический удар
            if turn == critical_turn and self.enemy.health > 0:
                self.enemy.health -= critical_hit
                fight_log.append(f'Критический удар! {self.enemy.name} получает дополнительно {critical_hit} урона.')

            # Проверяем, выжил ли враг
            if self.enemy.health <= 0:
                fight_log.append(f'{player.name} победил {self.enemy.name}!')
                self.enemy = None
                break

            # Ход врага: атака игрока
            fight_log.append(f'{self.enemy.name} атакует, нанося {enemy_attacks[turn]} урона.')
            fight_log.append(player.take_damage(enemy_attacks[turn]))

            # Проверяем, выжил ли герой
            if player.health <= 0:
                fight_log.append(f'{self.enemy.name} победил {player.name}!')
                break

        return '\n'.join(fight_log)


# Создаём героя и врага
hero = Warrior('Arthas')
enemy_goblin = Enemy('Элитный гоблин', 100)

# Создаём комнату и помещаем туда врага
room = Room('Зал битвы')
room.set_enemy(enemy_goblin)

# Начинаем бой
print(room.fight(hero))