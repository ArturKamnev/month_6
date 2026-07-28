from datetime import date

def validate_age(user):
    if user.birthdate:
        today = date.today()
        if 18 <= today.year - user.birthdate.year - ((today.month, today.day) < (user.birthdate.month, user.birthdate.day)) >= 100:
            return True
        else:
            return False