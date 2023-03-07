from dataclasses import dataclass, field
from typing import Optional, List

from modules.text_manage_module.enums import UserRangEnum


@dataclass
class UserRangModel:
    user_rang: UserRangEnum
    min_score: Optional[int] = None
    max_score: Optional[int] = None


@dataclass
class TextManageModuleConfig:
    blocker_user_ranges: List[UserRangModel] = field(default_factory=list)
    inviter_user_ranges: List[UserRangModel] = field(default_factory=list)
