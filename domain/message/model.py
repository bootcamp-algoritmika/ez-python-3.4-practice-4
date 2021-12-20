from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Optional, TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from ..base_model import mapper_registry
if TYPE_CHECKING:
    from ..user.model import User


@mapper_registry.mapped
@dataclass
class Message:
    __table__ = Table(
        "messages",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("user_id", Integer, ForeignKey("user.id")),
        Column("text", Text),
    )
    id: int = field(init=False)
    user_id: int = field(init=False)
    text: Optional[str] = None
    author: 'User' = field(init=False)
    __mapper_args__ = {
        "properties": {
            "author": relationship('User', back_populates='messages', lazy='subquery')
        }
    }
