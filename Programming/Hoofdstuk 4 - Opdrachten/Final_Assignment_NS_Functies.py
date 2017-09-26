def standaardprijs(afstandKM):
    prijs=0
    if afstandKM > 50:
        prijs= 15 + (afstandKM *0.60)
    else:
        prijs= afstandKM*0.60
    return prijs


def kortingLeeftijd(leeftijd):
    if leeftijd < 12 or leeftijd > 64:
        return True
    else:
        return False


def ritprijs(leeftijd, weekendrit, afstandKM):
    ritPrijs = standaardprijs(afstandKM)

    leeftijdKorting = kortingLeeftijd(leeftijd)

    if leeftijdKorting == True:
        if weekendrit:
            prijs = ritPrijs * 0.65
        else:
            prijs = ritPrijs * 0.7
    else:
        if weekendrit:
            prijs = ritPrijs * 0.6
        else:
            prijs = ritPrijs

    print(prijs)



# 11 jaar, weekend, 51km
ritprijs(11, True, 51)