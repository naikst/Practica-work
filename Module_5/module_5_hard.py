import hashlib
import time

class User:
    def __init__(self, nickname: str, password: str, age: int): # Инициализация атрибутов пользователя
        self.nickname = nickname # Имя пользователя
        self.password = self.__hash_password(password)  # Хэширование пароля для безопасности
        self.age = age # Возраст пользователя

    def __hash_password(self, password: str) -> int: # Хэшируем пароль для безопасного хранения
        return int(hashlib.sha256(password.encode()).hexdigest(), 16) # Возвращаем хэш пароля

    def __str__(self): # Выводим 'никнейм' вместо полноценной информации о пользователе
        return self.nickname

    def __repr__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False): # Видео и его характеристики
        self.title = title # Название видео
        self.duration = duration # Продолжительность видео
        self.time_now = time_now # Текущее время просмотра
        self.adult_mode = adult_mode # Флаг, указывающий на возрастное ограничение


class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        self.users = users if users is not None else []
        self.videos = videos if videos is not None else []
        self.current_user = current_user

    # Авторизация пользователя по никнейму и паролю и возраст пользователя
    def log_in(self, nickname: str, password: str) -> bool:
        # Проходим по списку пользователей для проверки правильности пароля и входа
        for user in self.users:
            if user.nickname == nickname and user.password == user.__hash_password(password):
                self.current_user = user # Устанавливаем текущего пользователя
                return True # Возврат успеха входа
        return False # Возврат ошибки входа

    # Регистрация пользователя по никнейму и паролю и возраст пользователя
    def register(self, nickname: str, password: str, age: int) -> bool:
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return False # Отмена регистрации, если пользователь существует
        self.users.append(User(nickname, password, age)) # Добавление нового пользователя
        self.current_user = self.users[-1] # Автоматический вход после регистрации
        return True # Регистрация успешна

    def log_out(self) -> None: # выход из аккаунта
        self.current_user = None

    def add(self, *videos): # Добавление видео в список если его ещё нет
        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video) # Добавляем видео в список


    def get_videos(self, search_word): # Поиск видео по ключевому слову из названия
        search_word = search_word.lower() # Приведение слова к нижнему регистру
        return [video.title for video in self.videos if search_word in video.title.lower()]

    # Воспроизведение видео с учётом возрастных ограничений и авторизации пользователя
    def watch_video(self, title):
        if not self.current_user: # Проверяем, что пользователь вошёл в систему
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = next((v for v in self.videos if v.title == title), None) # Ищем видео по названию
        if not video:
            print(f"Видео '{title}' не найдено.")
            return
        if video.adult_mode and self.current_user.age < 18: # Проверка на возрастные ограничения
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for second in range(1, video.duration + 1): # Имитируем просмотр видео по секундам
            time.sleep(1)
            print(second, end=" ")
            if second == video.duration:
                print("\nКонец видео") # Заканчиваем просмотр


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
