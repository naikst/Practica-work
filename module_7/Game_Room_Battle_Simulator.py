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
        self.strength = random.randint(20, 30)  # Случайная сила
        self.armor = random.randint(10, 20)  # Случайная броня


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

        # Случайный процесс боя
        while player.health > 0 and self.enemy.health > 0:
            # Ход игрока
            player_damage = random.randint(10, 30)  # Случайный урон игрока
            fight_log.append(
                f'{self.enemy.name} получил {player_damage} урона. {self.enemy.take_damage(player_damage)}')

            # Критический удар с шансом 15%
            if self.enemy.health > 0 and random.random() < 0.15:
                critical_damage = 30
                self.enemy.health -= critical_damage
                fight_log.append(f'Критический удар! {self.enemy.name} получает дополнительно {critical_damage} урона.')

            # Проверяем, выжил ли враг
            if self.enemy.health <= 0:
                fight_log.append(f'{player.name} победил {self.enemy.name}!')
                self.enemy = None
                break

            # Ход врага
            enemy_damage = random.randint(15, 35)  # Случайный урон врага
            if random.random() < 0.1:  # 10% шанс уклонения игрока
                fight_log.append(f'{player.name} уклоняется от атаки {self.enemy.name}.')
            else:
                fight_log.append(f'{self.enemy.name} атакует, нанося {enemy_damage} урона.')
                fight_log.append(player.take_damage(enemy_damage))

            # Проверяем, выжил ли игрок
            if player.health <= 0:
                fight_log.append(f'{self.enemy.name} победил {player.name}!')
                break

        return '\n'.join(fight_log)


# Устанавливаем фиксированное значение random.seed
random.seed(42)  # Сделает генерацию случайных чисел воспроизводимой

# Создаём героя и врага
hero = Warrior('Arthas')
enemy_goblin = Enemy('Элитный гоблин', 100)

# Создаём комнату и помещаем туда врага
room = Room('Зал битвы')
room.set_enemy(enemy_goblin)

# Начинаем бой
print(room.fight(hero))