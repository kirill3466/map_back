from typing import Optional

from models import Base


class OptionBase(Base):
    text: str


class OptionCreate(OptionBase):
    id: Optional[int]


class PollBase(Base):
    question: str
    options: Optional[list[OptionBase]]


class PollCreate(PollBase):
    pass


class PollRead(Base):
    id: int
    question: str
    options: Optional[list[OptionBase]]


# class PollUpdate(Base):
#     question: Optional[str]
#     options: Optional[List[OptionBase]]
