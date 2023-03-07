from enum import Enum


class MethodEnum(str, Enum):
    USER = "client/"
    LINKS = 'links/'
    LINKS_CLIENT = 'links_client/'
    GET_LINK = 'get_link/'
