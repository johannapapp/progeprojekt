f=open("vastused.txt")
kysimus=f.readline().split("\t")
kysimus.pop(0)
print(kysimus)

for rida in f:
    rida = rida.split("\t")
    inimene = {}

    for i in range(len(kysimus)):
        inimene[kysimus[i]] = rida[i+1]

print(inimene)
                