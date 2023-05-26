import os

from colorama import Back, Style, init


init(autoreset=True)  # Сброс цвета Colorama
os.system('cls')  # Очистка консоли

# Описание программы
print(Back.GREEN + Style.BRIGHT + "NetDownloader 05.04.2023 " + Back.RED +
      "Author: Kolesov Arseny")
print(Back.BLUE + Style.BRIGHT + "Available sources: Youtube, VK, Twitter, \
Instagram, Rutube and etc.")

# Ввод данных
url = input(Back.CYAN + Style.BRIGHT + 'URL: ')  # Ввод ссылки на видео
options = '"bv*[ext=mp4]+ba[ext = m4a]/best"'  # Параметры качества видео

# Процесс скачивания
cmd = f'yt-dlp --ffmpeg-location ffmpeg.exe \
-P Downloads -k -f {options} {url}'  # Команда для скачивания
print(cmd)  # Вывод строки
os.system(cmd)  # Системная команда
os.system('cls')
print(Back.GREEN + Style.BRIGHT + 'Successfully!' + Style.RESET_ALL)
input("Press any button to exit...")
