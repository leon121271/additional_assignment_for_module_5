import hashlib
import time

class User:
    def __init__(self, nickname, password, age):                       # encode()-метод преобразования строки password
        self.nickname = nickname                                       # в байтовый формат.
        self.password = hashlib.sha256(password.encode()).hexdigest()  # hashlib-встроенный модуль Python,предоставляет
        self.age = age                                                 # интерфейсы для различных хэш-функций(MD5,SHA-1,
                                                                       # SHA-256 и т.д.)
    def __str__(self):                                                 # sha256()-функция,создает объект хэширования
        return self.nickname                                           # с использованием алгоритма SHA-256
                                                                       # hexdigest()-метод,возвращает строковое предста-
    def __repr__(self):                                                # вление хэша в шестнадцатеричном формате (удоб-
        return f'User(nickname={self.nickname}, age={self.age})'       # но для хранения и передачи т.к. компактно и
                                                                       # не содержит спец.символов).
    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration                                       # duration - продолжительность (секунды)
        self.time_now = 0                                              # time_now - секунда остановки
        self.adult_mode = adult_mode                                   # adult_mode - ограничение по возрасту

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None                                     # current_user - текущий пользователь

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f'Вход выполнен: {user.nickname}')
                return
        print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже сущуствует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')

    def add(self, *videos):
        for video in videos:
            if not  any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for  video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                while video.time_now < video.duration:
                    print(video.time_now + 1)
                    time.sleep(1)
                    video.time_now += 1

                print('Конец видео')
                video.time_now = 0
                return
        print('Видео не найдено')

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')


