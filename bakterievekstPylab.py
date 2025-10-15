# til slutt eksempel med pylab i stedet for numpy og plt

from pylab import *
#tester github
print('Bakterievekst: f(n) = 2 * f(n-1)')
antall_dager = 8
bakterier = zeros(antall_dager)
bakterier[0] = 3 # vi starter med 3 bakterier
print(1,bakterier[0]) # 1 3.0
for i in range(1, antall_dager):
  bakterier[i] = 2*bakterier[i-1]
  print(i+1,bakterier[i])
print(bakterier[2]) # dag 3 antall 12
#dag = linspace(1, antall_dager, antall_dager) 
dag = arange(antall_dager) # her funker det tydeligvis best med bare ett tall, ikke start, stopp og steglengde
plot(dag+1, bakterier)
grid()
title('3 bakterier blir til så mange etter 8 dager:') # Tittel på selve grafene
axhline(y=0, color="blue") # legger til en vannrett linje (x-akse)
axvline(x=0, color="blue") # legger til en loddrett linje (y-akse)
xlabel("Antall dager siden start")
ylabel("Antall bakterier")
show()
print('-----------------------------------------')