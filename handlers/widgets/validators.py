import phonenumbers
from datetime import datetime


def validator_number(phone_number: str) -> bool | str:
    try:
        my_number = phonenumbers.parse(phone_number)
    except Exception as ex:
        return False
    else:
        if phonenumbers.is_valid_number(my_number):
            return '+' + str(my_number.country_code) + str(my_number.national_number)
        return False


def validator_date(date: str) -> bool | str:
    try:
        valid_date = datetime.strptime(date or "", "%d.%m.%Y")
    except ValueError:
        return False
    else:
        return valid_date.strftime("%Y-%m-%d")


def validator_person_id(person_id: str) -> str | bool:
    if " " in person_id:
        referrer_candidate = person_id.split()[1]
        if referrer_candidate.isdigit():
            return referrer_candidate
    return False


if __name__ == '__main__':
    pass


