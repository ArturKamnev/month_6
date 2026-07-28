from datetime import date
from django.utils import timezone
from rest_framework.exceptions import ValidationError

def validate_age(birthdate):
    if birthdate:
        today = date.today()

        try:
            birthdate = date.fromisoformat(birthdate)
        except (TypeError, ValueError):
            raise ValidationError(
                "Некорректная дата рождения в токене"
            )

        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age < 18:
            raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
        else:
            return True
    else:
        raise ValidationError(
            "Укажите дату рождения, чтобы создать продукт."
        )