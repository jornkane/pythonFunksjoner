# til slutt eksempel med pylab i stedet for numpy og plt
import pylab as pl
import os
# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

print('Bakterievekst: f(n) = 2 * f(n-1)')
antall_dager = 8
bakterier = pl.zeros(antall_dager)
bakterier[0] = 3 # vi starter med 3 bakterier
print(1,bakterier[0]) # 1 3.0
for i in range(1, antall_dager):
  bakterier[i] = 2*bakterier[i-1]
  print(i+1,bakterier[i])
print(bakterier[2]) # dag 3 antall 12
#dag = linspace(1, antall_dager, antall_dager) 
dag = pl.arange(antall_dager) # her funker det tydeligvis best med bare ett tall, ikke start, stopp og steglengde
pl.plot(dag+1, bakterier)
pl.grid()
pl.title('3 bakterier blir til så mange etter 8 dager:') # Tittel på selve grafene
pl.axhline(y=0, color="blue") # legger til en vannrett linje (x-akse)
pl.axvline(x=0, color="blue") # legger til en loddrett linje (y-akse)
pl.xlabel("Antall dager siden start")
pl.ylabel("Antall bakterier")
pl.show()
print('-----------------------------------------')