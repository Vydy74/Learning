from datetime import datetime
from time import sleep
import threading
def wite_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
time_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()

print(f"Работа функций {time_end - time_start}")

time_start = datetime.now()

threads = [
    threading.Thread(target=wite_words, args=(10, 'example1.txt')),
    threading.Thread(target=wite_words, args=(30, 'example2.txt')),
    threading.Thread(target=wite_words, args=(200, 'example3.txt')),
    threading.Thread(target=wite_words, args=(100, 'example4.txt'))
]

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

time_end = datetime.now()
print(f"Работа потоков {time_end - time_start}")