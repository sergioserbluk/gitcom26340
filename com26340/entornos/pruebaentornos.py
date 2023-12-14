import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
print(Fore.RED + "texto en rojo")
print(Back.GREEN + "texto fondo verde")