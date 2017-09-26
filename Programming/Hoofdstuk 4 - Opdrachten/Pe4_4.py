oldpassword = str(input('Vul hier je oude wachtwoord in'))
newpassword = str(input('Vul hier je nieuwe wachtwoord in'))

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword)>= 6:
        print('True')
    else:
        print('False')

new_password(oldpassword, newpassword)