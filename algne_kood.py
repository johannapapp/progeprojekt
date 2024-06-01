import random

# võtab kysimused failist, teeb sellest listi. 
f=open("vastused.txt")
kysimus=f.readline().split("\t")
kysimus.pop(0)
suur_sonastik = {}

# 1. for tsükkel, splittib iga inimese vastused ja teeb igast inimesest eraldi sõnastiku
for rida in f:
    rida = rida.split("\t")
    inimene = {}

# 2. for tsükkel paneb iga inimese sõnastiku ühte suurde sõnastikku
    for i in range(len(kysimus)):
        inimene[kysimus[i]] = rida[i + 1]
    name = rida[0]
    suur_sonastik[name] = inimene

nimed = suur_sonastik.keys()

# while tsükliga valib ühe random küsimuse ning prindib selle välja, inimene vastab jah v ei
while len(kysimus) >= 1:
    # valib random kysimuse, inimene vastab
    for x in kysimus:
        question = (random.choice(kysimus))
        print(question)
        answer = input("Vasta 'Jah' või 'Ei': ")

        # võtab ära kysimuse, mida kysib
        kysimus.remove(question)



        # uus list, kuhu paneme nimed, mille kohta see käib.
        uus = []
        
        # print(nimed)

        for nimi in nimed:
            # print("suur_sonastik[nimi]")
            
            if suur_sonastik[nimi][question] == answer:
                
                uus.append(nimi)
                # print(uus)

                
        nimed = uus
        # list nimedega, mille kohta kysimus käib
        print(nimed)        


# print(kysimus)
# print(suur_sonastik)


