cijferICOR=6
cijferPROG=6
cijferCSN=7
cijfers=round((cijferICOR+cijferPROG+cijferCSN))
gemiddelde=round(cijfers/3,1)
beloning=((6*30)+(6*30)+(7*30))
overzicht='Mijn cijfers (Gemiddeld een=' +str(gemiddelde)+ ') beloning van € '  + str(beloning) + ' ''op!'
print(overzicht)