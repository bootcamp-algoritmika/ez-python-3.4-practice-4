from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Optional

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from ..message.model import Message
from ..base_model import mapper_registry


@mapper_registry.mapped
@dataclass
class User:
    __table__ = Table(
        "user",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("nickname", String),
    )
    id: int = field(init=False)
    name: Optional[str] = None
    nickname: Optional[str] = None
    messages: List[Message] = field(default_factory=list)

    __mapper_args__ = {
        "properties": {
            "messages": relationship("Message", lazy='subquery', back_populates='author')
        }
    }
