import numpy as np

import os
os.system('cls' if os.name == 'nt' else 'clear') # Rydder skjermen

# Simulerte data for karbon-14 nedbrytning
tid_dager = np.array([0, 100, 200, 300, 400, 500, 600]) # x-verdier
antall_karbon14 = np.array([100, 50, 25, 12.5, 6.25, 3.125, 1.5625]) # y-verdier

# Lineær regresjon for å finne halveringstiden
koeffisient, _ = np.polyfit(tid_dager, np.log(antall_karbon14), 1)
halveringstid = -np.log(2) / koeffisient

print()
print(f"Karbons-14 halveringstid: {halveringstid:.2f} dager")
print()

import matplotlib.pyplot as plt

# Plotting dataene
plt.figure(figsize=(10, 5))
plt.plot(tid_dager, antall_karbon14, 'bo-', label='Observert Karbon-14')
plt.title('Nedbrytning av Karbon-14 over tid')
plt.xlabel('Tid (dager)')
plt.ylabel('Antall Karbon-14')
plt.grid(True)
plt.legend() # liten forklaringsboks som ligger i hjørnet av grafen (label)
plt.axhline(0, color='black', linewidth=0.5) # x-aksen
plt.axvline(0, color='black', linewidth=0.5) # y-aksen
plt.fill_between(tid_dager, antall_karbon14, color='blue', alpha=0.1) # fyller mellom linjen og aksen
plt.show()
