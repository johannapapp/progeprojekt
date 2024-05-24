import random
f = open("vastused.txt")
kysimus = f.readline().split("\t")
kysimus.pop(0)
suur_sonastik = {}
for rida in f:
    rida = rida.split("\t")
    inimene = {}

    for i in range(len(kysimus)):
        inimene[kysimus[i]] = rida[i + 1]
    name = rida[0]
    suur_sonastik[name] = inimene

while len(kysimus) >= 1:
    for x in kysimus:
        question = (random.choice(kysimus))
        print(question)
        answer = input("Vasta 'Jah' või 'Ei'")
        for nimi in suur_sonastik:
            print(suur_sonastik[nimi])
            if suur_sonastik[nimi][question] != answer:
                print(nimi)


print(kysimus)
# print(suur_sonastik)