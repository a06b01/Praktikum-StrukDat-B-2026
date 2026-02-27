# test.py - jalankan setelah install colorama
from colorama import Fore, Back, Style, init

init()
print(Fore.RED + 'Teks Merah')
print(Fore.GREEN + 'Teks Hijau')
print(Fore.BLUE + Back.YELLOW + 'Teks Biru, Bg Kuning')
print(Style.RESET_ALL + 'Kembali Normal')