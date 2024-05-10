import random

# erinevad inimesed
johannapapp = {"nimi": "Johanna Papp", "suund":"progepets", "sugu":"tütarlaps", "juuksed": "pruun", "aasta":"2006", "silmad":"pruunid", "prillid": "Ei", "läätsed": "Ei", "aastaaeg":"sügis", "värv":"roheline"}
johannasimm = {"nimi": "Johanna Simm", "suund":"progepets", "sugu":"tütarlaps", "juuksed": "pruun", "aasta":"2007","silmad":"sinakashallid", "prillid":"Ei", "läätsed": "Ei", "aastaeg": "kevad", "värv":"lilla"}

# kõik kokku
kogumik = []

# lisab neid
kogumik.append(johannapapp)
kogumik.append(johannasimm)

f = open("kysimused.txt")

# kysimuse valimine
kyssad = []
for rida in f:
    k = f.readline()
    kyssad.append(k)


kysimus = random.choice(kyssad)

print(kysimus)
kyssad.remove(kysimus)
vastus = input("Vasta 'Jah' või 'Ei':")