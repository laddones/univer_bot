from modules.models.schema import GetLinkSchema, LinkType
from modules.text_manage_module import enums


class TextManageModule:

    def __init__(self):
        self.bad_chars = [".", "!", "_", "*", '-', '=']

    def clear_text(self, text: str) -> str:
        for ch in self.bad_chars:
            text = text.replace(ch, "\\" + ch)
        return text

    @staticmethod
    def get_task_text(link: GetLinkSchema) -> str:
        if not link.description or link.link_type != LinkType.TELEGRAM:
            link.description = 'Заблокуйте ресурс'
        return enums.TextEnum.TASK_TEXT.format(
            description=link.description,
            link=link.link,
        )

    @staticmethod
    def get_start_message(first_name: str) -> str:
        return enums.TextEnum.START.format(
            first_name=first_name
        )
