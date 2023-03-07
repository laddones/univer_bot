from modules.models.schema import PersonSchema, PersonCreateSchema
from modules.models.text_enum import Texts


class TextModul:
    @staticmethod
    def checker(item: str) -> str:
        if item is None:
            return '???'
        return item

    @staticmethod
    def show_search_person(person: PersonSchema) -> str:
        if person.images:
            image = person.images[0].image
        else:
            image = 'https://sabilaw.org/wp-content/uploads/2020/11/img_2263-1024x777.jpg'
        return Texts.SHOW_PERSON.format(
            first_name=TextModul.checker(person.first_name),
            last_name=TextModul.checker(person.last_name),
            middle_name=TextModul.checker(person.middle_name if person.show_middle_name else None),
            birthday=TextModul.checker(person.birthday if person.show_birthday else None),
            place_of_living=TextModul.checker(person.place_of_living if person.show_place_of_living else None),
            range=TextModul.checker(person.range if person.show_range else None),
            job_title=TextModul.checker(person.job_title if person.show_job_title else None),
            military_unit=TextModul.checker(person.military_unit if person.show_military_unit else None),
            phone_number=TextModul.checker(person.phone_number if person.show_phone_number else None),
            status_person=TextModul.checker(person.status_person),
            text=TextModul.checker(person.text if person.show_text else None).replace('<p>', '').replace('</p>', ''),
            image=TextModul.checker(image)
        )

    @staticmethod
    def show_add_person(person: PersonCreateSchema) -> str:
        return Texts.SHOW_ADD_PERSON.format(
            first_name=TextModul.checker(person.first_name),
            last_name=TextModul.checker(person.last_name),
            middle_name=TextModul.checker(person.middle_name),
            birthday=TextModul.checker(person.birthday),
            military_unit=TextModul.checker(person.military_unit),
            phone_number=TextModul.checker(person.phone_number),
            status_person=TextModul.checker(person.status_person),
            text=TextModul.checker(person.text).replace('<p>', '').replace('</p>', ''),
            image='https://sabilaw.org/wp-content/uploads/2020/11/img_2263-1024x777.jpg'
        )


