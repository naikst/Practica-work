import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"


class Ball(arcade.Sprite):  # класс мяча
    def __init__(self):  # конструктор
        super().__init__('ball.png', 0.03)  # вызов конструктора
        self.change_x = 3  # скорость по оси X
        self.change_y = 3  # скорость по оси Y

    def update(self):  # метод обновления
        self.center_x += self.change_x  # изменение координаты по оси X
        self.center_y += self.change_y  # изменение координаты по оси Y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x  # изменение скорости по оси X
        if self.left <= 0:
            self.change_x = -self.change_x  # изменение скорости по оси X
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y  # изменение скорости по оси Y
        if self.bottom <= 0:
            self.change_y = -self.change_y  # изменение скорости по оси Y


class Bar(arcade.Sprite):  # класс платформы
    def __init__(self):  # конструктор
        super().__init__('bar.png', 0.07)  # вызов конструктора

    def update(self):  # метод обновления bar
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0  # изменение скорости по оси X


class Game(arcade.Window):  # класс игры
    def __init__(self, width, height, title):  # конструктор
        super().__init__(width, height, title)  # вызов конструктора
        self.bar = Bar()  # создание платформы
        self.ball = Ball()  # создание мяча
        self.setup()  # инициализация начальных значений

    def setup(self):  # функция инициализации
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2  # начальное положение мяча
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):  # функция отрисовки
        arcade.start_render()  # подготовка к отрисовки
        self.clear(arcade.color.WHITE)  # очистка экрана
        self.bar.draw()  # отрисовка платформы
        self.ball.draw()  # отрисовка мяча

    def update(self, delta):  # функция обновления
        if arcade.check_for_collision(self.bar, self.ball): # проверка на пересечение с мячом
            self.ball.change_y = -self.ball.change_y  # изменение скорости по оси Y
        self.ball.update()  # обновление позиции мяча
        self.bar.update()  # обновление позиции платформы
        # проверка на пересечение с платформой

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5  # изменение скорости по оси X bar
        if key == arcade.key.LEFT:
            self.bar.change_x = -5  # изменение скорости по оси X bar

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0  # изменение скорости по оси X bar



if __name__ == "__main__":  # запуск программы
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # создание окна
    arcade.run()  # вызов основного цикла программы
