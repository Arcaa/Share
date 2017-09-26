def kwadraten_som(lijst):
    totaal = 0
    for getal in lijst:
        if getal > 0:
            totaal = totaal+getal**2
    return totaal

print(kwadraten_som([4,5,3,-81]))