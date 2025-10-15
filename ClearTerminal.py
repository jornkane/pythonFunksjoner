import os
# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

print('Huskelapp for clear terminalen')
print('Bruker os.system() for å kjøre kommandoen')
print('os.name:', os.name)
print('os.system("cls" if os.name == "nt" else "clear")')
print('os.system("cls") for Windows')
print('os.system("clear") for Linux/Unix/Mac')

