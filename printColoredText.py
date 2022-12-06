### This can be used to highlight outputs on many code

# Importing Library
import colorama
from colorama import Fore, Back, Style

# Main logic
colorama.init(autoreset = True)

# Printing outputs
print(Fore.BLUE+Back.YELLOW+"Hello World! "+ Fore.YELLOW+ Back.BLUE+"Hello World!")
print(Back.CYAN+"Hello World! ")
print(Fore.RED + Back.GREEN+ "Hello World! ")