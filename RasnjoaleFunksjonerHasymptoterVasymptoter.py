import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve

x = symbols('x')
# skriv inn funksjonen her og to linjer ned også. Om du har nevner skriv i denominator
funksjon = (3*x - 1)/(x + 3) # (2*x**2+2*x+5)/(x-1)  x**3 - 6*x**2 + 11*x - 6  skriv inn funksjonen din her og ned i linje 10

def f(x):
    return (3*x - 1)/(x + 3)

denominator = x +3  # Extract the denominator from the function

x_verdier = np.linspace(-10, 10, 100) # Genererer x-verdier
y_verdier = f(x_verdier)

print()
try: # Bruker sympy til å finne nullpunktene. Ikke alle har nullpunkter så her sjekker vi med try except
    losning = solve(funksjon, x)   # løser funksjon(x)=0
    losning = [float(n) for n in losning] # liste med alle verdier som gir 0
    if not losning:
        raise ValueError("Sjekk meldingen litt lenger ned...")
except Exception as e:
    print(f"Likningen har ingen nullpunkter: {e}")
    losning = []
print(losning)
print(type(losning),type(x),type(funksjon))
print() # Plotter grafen under her
for n in losning: # Markerer nullpunktene
    plt.scatter(n, 0, color='red', s=50, zorder=5)
    plt.text(n, 0.5, f'({n:.2f}, 0)', fontsize=9, ha='center')

# Horisonal asymptote
ha = funksjon.limit(x, np.inf)  # Finding the horizontal asymptote as x approaches infinity
plt.axhline(y=ha, color='blue', linestyle='--', label='Horizontal Asymptote')  # Plotting the horizontal asymptote
print("Horizontal Asymptote:", ha)

# Vertikal asymptote
try: # Finding vertical asymptotes by solving the denominator of the function equal to zero
    vertical_asymptotes = solve(denominator, x)  # Solve denominator = 0
    vertical_asymptotes = [float(v) for v in vertical_asymptotes]
    print("Vertical Asymptotes:", vertical_asymptotes)
except Exception as e:
    print(f"Error finding vertical asymptotes: {e}")
    vertical_asymptotes = []
for va in vertical_asymptotes:
    plt.axvline(x=va, color='red', linestyle='--', label='Vertical Asymptote')

funkLabel = str(funksjon) # kun for å vise funksjonen på label
plt.plot(x_verdier, y_verdier, label=funkLabel)
plt.ylim(-10, 10)
plt.title('Grafen til funksjonen')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='purple',linewidth=1.5)
plt.axvline(0, color='purple',linewidth=1.5)
plt.grid(True)
plt.legend() # plt.legend() is necessary to display the function label on the plot for better understanding of the graph being displayed.
plt.show()

