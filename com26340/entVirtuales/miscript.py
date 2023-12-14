import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')