# -*- coding: utf-8 -*-
import os
# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

"""
Created lørdag 3.feb 2024, @author: Jørn Kanestrøm
"""
# Importerer bibliotekene matplotlib.pyplot og NumPy:
import os
os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
# Importerer nødvendige biblioteker for plotting og numeriske operasjoner
import matplotlib.pyplot as plt
import numpy as np

def meny():
    print('Dette er Jørns kompeltte samling av grafer og verditabeller i Python')
    print('Skriv inn tallet som tilsvarer funksjoen du vil se på')
    valg = int(input('Bakterievekst (zeros/arange): 1\n'
            'Temperaturer (loadtxt): 2\n'
            'To grafer i samme bilde (label/legend): 3\n'
            'Verditabell og graf: 4\n'
            'Lag x verdier med linspace og arange: 5\n'
            'Vis verdi i hvert punkt på grafen: 6\n'
            'Stolpediagram: 7\n'
            ''))
    if valg == 1:
        bakterievekst()
    elif valg == 2:
        temperaturerFeb()
    elif valg == 3:
        toGrafer()
    elif valg == 4:
        verditabellGraf()
    elif valg == 5:
        lagXverdier()
    elif valg == 6:
        punktVerdi()
    elif valg == 7:
        stolpediagram()
    else:
        print('Takk for nå!')

def bakterievekst(): #1
    # biologi - bakterievekst
    print('Bakterievekst: f(n) = 2 * f(n-1)')
    antall_dager = 8
    bakterier = np.zeros(antall_dager)
    bakterier[0] = 3 # vi starter med 3 bakterier
    print(1,bakterier[0]) # 1 3.0
    for i in range(1, antall_dager):
        bakterier[i] = 2*bakterier[i-1]
        print(i+1,bakterier[i])
    print(bakterier[2]) # dag 3 antall 12
    #dag = np.linspace(1, antall_dager, antall_dager) 
    dag = np.arange(antall_dager) # her funker det tydeligvis best med bare ett tall, ikke start, stopp og steglengde
    plt.figure(figsize=(8, 6))  # Set a specific size for better visibility
    plt.plot(dag+1, bakterier)
    plt.grid()
    plt.title('3 bakterier blir til så mange etter 8 dager:') # Tittel på selve grafene
    plt.axhline(y=0, color="blue") # legger til en vannrett linje (x-akse)
    plt.axvline(x=0, color="blue") # legger til en loddrett linje (y-akse)
    plt.xlabel("Antall dager siden start")
    plt.ylabel("Antall bakterier")
    plt.show()

def temperaturerFeb(): #2
    try:
        # Load the temperature data
        temp = np.loadtxt("temp.txt")
        # Create the plot
        plt.figure(figsize=(8, 6))  # Set a specific size for better visibility
        plt.plot(temp, 'bx-')
        plt.title('Temperaturer februar i $^\circ$C')
        plt.grid()
        plt.axhline(y=0, color="blue")
        plt.axvline(x=0, color="blue")
        plt.xlabel("Antall dager siden start")
        # Show x-axis ticks (removed plt.xticks([]))
        plt.show()
        #plt.close()  # Clean up the plot
    except FileNotFoundError:
        print("Error: Could not find temp.txt file")
    except Exception as e:
        print(f"An error occurred: {e}")


def toGrafer(): #3
    # to grafer i samme bilde
    x = np.linspace(-2, 2, 30)# # husk at siste tall bør være størst her
    y1 = x**2
    y2 = 2*x + 1
    plt.figure(figsize=(8, 6))  # Set a specific size for better visibility
    plt.scatter(x, y1, color="red", label="y1= x**2", marker='+')
    plt.scatter(x,y2, color="blue", label="y2= 2*x + 1", marker='X')
    plt.grid()
    plt.axhline(y=0, color="black") # legger til en vannrett linje (x-akse)
    plt.axvline(x=0, color="black") # legger til en loddrett linje (y-akse)
    plt.legend()
    plt.show()
    #plt.close()  # Clean up the plot
    # Legg merke til at hvert av plottene må få en label.
    # Det er teksten du skriver i labelen som vises når du bruker legend().


def verditabellGraf(): #4
    print('Funksjoner og grafer i Python: verditabell og graf')
    xverdier = np.linspace(-4,4,8) # husk at siste tall bør være størst her
    yverdier=(0.2*3**xverdier -8) #2x-4 altså, hvert svar legges i yverdier-arrayen
    print(type(yverdier))
    print()
    print('Verditabell for 0.2*3**x -8')
    print('x      f(x)') 
    for a in range (8): 
        print(round(xverdier[a],1),'  ', round(yverdier[a],2))
        print('---------------------------------------')
    plt.figure(figsize=(8, 6))  # Set a specific size for better visibility
    plt.plot(xverdier, yverdier)
    plt.axhline(y=0, color="gray") # legger til en vannrett linje (x-akse)
    plt.axvline(x=0, color="gray") # legger til en loddrett linje (y-akse)
    plt.grid() # legger til et rutenett
    plt.title('Grafen til 0.2*3**x -8') # Tittel på selve grafene
    plt.xlabel("X-verdier")
    plt.ylabel("F av x:")
    plt.show()
    #plt.close()  # Clean up the plot
    # du kan også hente ut punkter fra plassering i arrayene
    print('Første xverdi:',round(xverdier[0],2),'og første yverdi:', round(yverdier[0],2))

def lagXverdier(): #5
    print('Eksempler med linspace sammenlignet med arange')
    x2=np.linspace(-5,5,10) #(start=-5,stopp=5,antallPunkter=10) 
    x3=np.arange(-5,5,0.25)#(start=-5,stopp=5,steglengde=0.25)
    y2 = x2**2-6
    y3 = x3**2+1
    print(type(y2))
    print(type(y3))
    print()
    print('Verditabell for x2**2-2')
    for a in range(8):
        print('X=',round(x2[a],2),'og Y=', round(y2[a],2))
    plt.figure(figsize=(8, 6))  # Set a specific size for better visibility
    plt.plot(x2, y2)
    plt.plot(x3,y3)
    # plt fungerer også når man ikke har importert noe som plt...
    plt.grid() # legger til et rutenett 
    plt.title('Grafen til x**2-6 og x**2+1') # Tittel på selve grafene
    plt.axhline(y=0, color="blue") # legger til en vannrett linje (x-akse)
    plt.axvline(x=0, color="blue") # legger til en loddrett linje (y-akse)
    plt.xlabel("X-verdier" )
    plt.ylabel("F av x:")
    plt.show()
    #plt.close()  # Clean up the plot
    print()

def punktVerdi(): #6
    print('Grafen til f(x)=0.5*x**2-3*x+3.5:') 
    def f(ex): # denne brukes i for loopen 5 linjer ned
       return 0.5*ex**2-3*ex+3.5
    #x_verdier = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8]) # x-verdier. Dette fungerer, men arange er bedre
    x_verdier = np.arange(-3,9,1) # x-verdier. arange fungerer best her
    leng = len(x_verdier) # antall x-verdier
    y_verdier = np.zeros([leng]) # y-verdier (null som standardverdi eller placeholder)
    for a in x_verdier:
        y_verdier[a] = f(x_verdier[a]) # y er de utregnede verdiene til f(ex)
    plt.plot(x_verdier, y_verdier) # x og y verdier
    plt.title("Utregnede verdier til f(x)=0.5*x**2-3*x+3.5")
    plt.scatter(x_verdier,y_verdier) # lager kulepunkter for hver koordinat
    # denne loopen setter ut tekst som viser y-verdiene direkte på grafen:
    for index, value in enumerate(y_verdier): # enumerate gir både indeks og verdi
        plt.text(x_verdier[index], value, str(value), color="red")  # Bruker x-verdiene direkte i stedet for indeks
    plt.axhline(y=0, color="black") # legger til en vannrett linje (x-akse)
    plt.axvline(x=0, color="black") # legger til en loddrett linje (y-akse)
    plt.grid()
    plt.show()

def stolpediagram():
    # Choose the height of the bars
    antall = [14, 12, 15, 7, 9]
    print('Undersøkelse om foretrukket arbeidsmåte i en klasse:')
    # Choose the names of the bars
    bars = ('Vil ha arbeidsro', 'Liker gruppearbeid', 'Liker forsøk', 'Liker tavleunderv.', 'Jobber best alene')
    y_pos = np.arange(len(bars))
    # Create bars
    plt.bar(y_pos, antall) # antallet styrer høyden på stolpene
    # Create names on the x-axis
    plt.xticks(y_pos, bars, color='black', rotation=40) # xakse farge, rotering (90 er rett ned)
    plt.yticks(color='purple') # yakse farge
    # Navn på diagrammet
    plt.xlabel('Elevundersøkelse naturfag klasse 1 og 2', fontweight='bold', color = 'orange', fontsize='18')
    # Custom the subplot layout
    plt.subplots_adjust(bottom=0.4, top=0.95)
    # Show graphic
    plt.show()
    # mer om grafer i Python: https://python-graph-gallery.com/ 

meny()


