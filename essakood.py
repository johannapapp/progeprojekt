f=open("vastused.txt")
kysimus=f.readline().split("\t")
kysimus.pop(0)
inimene = {}

for rida in f:
    rida = rida.split("\t")

    for i in range(len(kysimus)):
        inimene[kysimus[i]] = rida[i+1]

print(inimene)
                