import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f"User('{self.nickname}', {self.password}, {self.age})"

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Video('{self.title}', {self.duration}, adult_mode={self.adult_mode})"

    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower()


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        user = next((u for u in self.users if u.nickname == nickname and u.password == hash(password)), None)
        if user:
            self.current_user = user
        else:
            print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        if any(u.nickname == nickname for u in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword):
        return [str(v) for v in self.videos if keyword.lower() in str(v).lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if str(v) == title), None)
        if video:
            if video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                for i in range(video.duration):
                    print(i + 1, end=" ")
                    time.sleep(1)
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0
        

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
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