import requests
from bs4 import BeautifulSoup

# Модуль для простого парсинга заголовков сайтов
class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    # 1. Метод для выполнения GET-запроса к сайту
    def fetch_data(self):
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()  # Проверка на успешный запрос
            print(f"Успешный запрос к {self.url}")
            # Обработка исключений
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else: {err}")

    # 2. Метод для обработки HTML-контента и создания объекта BeautifulSoup (парсер для синтаксического разбора файлов)
    def parse_html(self):
        if self.response:
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            print("HTML успешно обработан")
        else:
            print("Нет данных для обработки")

    # 3. Метод для извлечения заголовков (например, h1) с сайта
    def get_titles(self):
        if self.soup:
            titles = self.soup.find_all('h1')
            return [title.get_text() for title in titles]
        else:
            print("HTML не был обработан")
            return []


# Пример работы модуля
if __name__ == "__main__":
    url = 'https://github.com/'
    scraper = WebScraper(url)

    scraper.fetch_data()  # Выполняем запрос к сайту
    scraper.parse_html()  # Обрабатываем полученные данные
    titles = scraper.get_titles()  # Извлекаем заголовки
    print(f"Заголовки: {titles}")

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

# Далее pandas и matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Создание данных. Мы создаем словарь data с двумя ключами: 'Месяц' и 'Продажи', содержащими соответствующие данные.
data = {
    'Месяц': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь'],
    'Продажи': [1500, 2000, 1800, 2200, 2400, 2100]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение данных в файл input.txt
df.to_csv('input.txt', index=False, sep='\t')  # Используем табуляцию как разделитель
print("Данные сохранены в input.txt")

#----------------------------------------------------------

# Считывание данных с использованием pandas

df = pd.read_csv('input.txt', sep='\t')
print("\nДанные считаны из input.txt:")
print(df)

#----------------------------------------------------------

# Визуализация данных с помощью matplotlib

# Установка стиля графиков. Для просмотра доступных стилей используем вызов метода plt.style.available:
# Выводим доступные стили
# print(plt.style.available)
plt.style.use('Solarize_Light2')

# 1. Линейный график(Линия соединяет точки данных)
plt.figure(figsize=(10, 6))
plt.plot(df['Месяц'], df['Продажи'], marker='o', linestyle='-', color='b')
plt.title('Линейный график продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.grid(True)
plt.savefig('line_plot.png')
plt.show()

# 2. Столбчатая диаграмма(Высота столбцов отображает величину продаж или чего то там)
plt.figure(figsize=(10, 6))
plt.bar(df['Месяц'], df['Продажи'], color='g')
plt.title('Столбчатая диаграмма продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.savefig('bar_chart.png')
plt.show()

# 3. Круговая диаграмма(Круговая нарезка по типу пирога)
plt.figure(figsize=(8, 8))
plt.pie(df['Продажи'], labels=df['Месяц'], autopct='%1.1f%%', startangle=140)
plt.title('Круговая диаграмма распределения продаж по месяцам')
plt.savefig('pie_chart.png')
plt.show()


