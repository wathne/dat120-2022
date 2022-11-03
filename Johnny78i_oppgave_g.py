# Hei John, koden din må foreløpig flyttes ut fra asdf.py.
# Koden nedenfor skapte problemer ved import av funksjoner fra asdf.
# F.eks. "from asdf import Avtale, ny_avtale" vil fylle terminalen.


# oppg. g:

# Initialliserer variabler
liste_over_avtaler = list()

def vis_avtaleliste(avtaleliste,overskrift = "Liste over Avtaler"):
    #Overskrift
    print(overskrift)
    index = 1
    for x in avtaleliste:
        print(f"{index}: {x}")
        index += 1

# Testinput for lang liste med avtaler med samme tid, men (litt) forskjellig tittel
for i in range(24):
    avtaletest = Avtale(f"Test{i}",f"Sted{i}",datetime.fromisoformat("2002-04-24 23:24:24"),15+i)
    liste_over_avtaler.append(avtaletest)

vis_avtaleliste(liste_over_avtaler)


## oppg. g:
#
## Initialliserer variabler
#liste_over_avtaler = dict()
#
#def avtaleliste():
#    #Overskrift
#    print("Liste over Avtaler")
#    for x in liste_over_avtaler:
#        print(f"{x}: {liste_over_avtaler[x].tittel}")
#
## Testinput for lang liste med avtaler med samme tid, men (litt) forskjellig tittel
#for i in range(24):
#    avtaletest = Avtale(f"Test{i}","Sted",datetime.fromisoformat("2002-04-24 23:24:24"),15)
#    liste_over_avtaler[i+1] = avtaletest
#    
#avtaleliste()


