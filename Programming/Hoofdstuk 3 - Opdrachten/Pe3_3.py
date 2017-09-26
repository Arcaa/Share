line1=int(input('Wat is uw leeftijd'))
line2=str(input('Bezit u over een Nederlands paspoort?'))
if line1 >= 18 and line2 == str('Ja'):
    print('Gefeliciteerd, u mag stemmen')
else :
    print('Helaas, u mag niet stemmen!')