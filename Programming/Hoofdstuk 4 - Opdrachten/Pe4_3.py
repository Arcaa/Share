lengte1 = int(input('Hoe lang ben je?'))
def lang_genoeg(lengte1):
    if lengte1 >= 120:
        print('Je bent lang genoeg voor de attractie')
    else:
        print('Sorry, je bent te klein.')
(lang_genoeg(lengte1))