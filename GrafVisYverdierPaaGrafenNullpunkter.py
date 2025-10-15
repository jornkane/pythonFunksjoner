import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve
import os
# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')
print()
print('-----------------------------------------------------------')
print()

# selve funksjonen med x og y verdier
x_verdier = np.linspace(-8,8,10) # start, stopp, antall punkter
ey = (2*x_verdier**2 + 3*x_verdier - 6) # F(x) beregnes direkte med xverdiene og blir en array
ey = np.round(ey, 2) # må bruke np.round for å avrunde alle verdier i arrayen
x_verdier = np.round(x_verdier,2) # runder av, men det påvirker nøyaktigheten...
print('X-verdier:',x_verdier)
print('Y-verdier:',ey)

# Finner nullpunktene ved å løse likninga til = 0
x = symbols('x') # We need to define the variable x correctly using sympy's symbols function
eq1 = Eq(2*x**2 + 3*x - 6, 0) # Now we redefine the equation with the correct symbol
sol = solve(eq1, array=True) # gjorde om fra dict til array for å kunne plotte punktene
sol = [round(s, 2) for s in sol]  # Round each solution to 2 decimal places
print("Nullpunktene er:", sol)

# denne loopen setter ut tekst som viser y-verdiene direkte på grafen:
for x, y in enumerate(ey): # jeg kaller det x og y, egentlig i og v (index og value)
    plt.text(x_verdier[x], ey[x], str(ey[x]), color="red", horizontalalignment='center', verticalalignment='bottom')
for x, y in enumerate(sol):
    plt.text(sol[x]+0.5, 0, str(y), fontweight='bold', color="black", verticalalignment='bottom') #sol[x]+0.5 setter den 1 mot høyre

plt.plot(x_verdier, ey, color='violet')
plt.title('Grafen til likninga:2*x**2 + 3*x - 6') # kan ikke hente inn variabel til tittelen dessverre...
plt.scatter(x_verdier, ey) # lager kulepunkter for hver koordinat på grafen
plt.scatter([sol[0], sol[1]], [0, 0], color='black', s=100, marker='X') #x-verdier [], y-verdier [], farge, størrelse
plt.xlabel('x-verdier')
plt.ylabel('f av x')
plt.axhline(y=0, color="green") # legger til en vannrett linje (x-akse)
plt.axvline(x=0, color="green") # legger til en loddrett linje (y-akse)
plt.ylim(ymin=-20, ymax=150) # min og max x og y bestemmer hva som vises på grafikkfeltet
plt.xlim(xmin=-10, xmax=10)
plt.grid() # legger til et rutenett
plt.show()

print('--------------------------------------------------------------------')
print()


'''
x_range = max(x_verdier) - min(x_verdier) # dette, linje 43,44 ble lagt til etter AI spm
print('min og max-verdier:',max(x_verdier), min(x_verdier),'Range:',x_range)
'''