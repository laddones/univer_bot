from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class LinkType(str, Enum):
    YOUTUBE = 'YOUTUBE'
    TWITTER = 'TWITTER'
    TELEGRAM = 'TELEGRAM'
    INSTAGRAM = 'INSTAGRAM'
    FACEBOOK = 'FACEBOOK'
    TIKTOK = 'TIKTOK'
    OTHER = 'OTHER'


class LinkStatus(str, Enum):
    DELETED = 'DELETED'
    PUBLISHED = 'PUBLISHED'
    PROCESSING = 'PROCESSING'
    BLOCKED = 'BLOCKED'


class LinkClientStatus(str, Enum):
    REPORTED = 'REPORTED'
    SKIPPED = 'SKIPPED'
    DELETED = 'DELETED'
    PROCESSING = 'PROCESSING'


class ClientSchema(BaseModel):
    user_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    status: Optional[bool] = False
    time_create: Optional[datetime] = None
    time_update: Optional[datetime] = None


class LinkSchema(BaseModel):
    id: int
    link: str
    description: Optional[str] = None
    link_status: Optional[LinkStatus] = LinkStatus.PUBLISHED
    link_type: Optional[LinkType] = LinkType.OTHER
    client: Optional[int] = None
    admin: Optional[int] = None
    time_create: Optional[datetime] = None
    time_update: Optional[datetime] = None


class LinkClientSchema(BaseModel):
    id: int
    link_status: Optional[LinkClientStatus] = LinkClientStatus.PROCESSING
    client: int
    link: int
    time_create: Optional[datetime] = None
    time_update: Optional[datetime] = None


class CreateClientSchema(BaseModel):
    user_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UpdateClientSchema(BaseModel):
    user_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    status: Optional[bool] = None


class CreateLinkSchema(BaseModel):
    link: str
    description: Optional[str] = None
    link_status: Optional[LinkStatus] = LinkStatus.PROCESSING
    link_type: Optional[LinkType] = LinkType.OTHER
    client: int


class CreateLinkClientSchema(BaseModel):
    link: int
    client: int
    link_status: Optional[LinkClientStatus] = LinkClientStatus.PROCESSING


class GetLinkSchema(BaseModel):
    id: int
    link: str
    description: Optional[str] = None
    link_type: Optional[LinkType] = LinkType.OTHER
    link_status: Optional[LinkStatus] = LinkStatus.PUBLISHED

