from typing import Optional

from sqlalchemy.orm import Session

from .models import Option, Poll
from .schema import PollCreate


def create(*, db_session: Session, poll: PollCreate, user_id: int) -> Poll:
    options = poll.options
    poll = Poll(question=poll.question,  owner_id=user_id)
    db_session.add(poll)
    db_session.commit()
    db_session.refresh(poll)

    for option in options:
        option = Option(text=option.text, poll_id=poll.id)
        db_session.add(option)
    db_session.commit()
    return poll


def get(*, db_session: Session, poll_id: int) -> Optional[Poll]:
    return db_session.query(Poll).filter(
        Poll.id == poll_id
    ).one_or_none()


def get_all(*, db_session: Session) -> list[Poll]:
    poll = db_session.query(Poll).all()
    return poll


def delete(*, db_session: Session, poll_id: int) -> None:
    poll = db_session.query(Poll).filter(Poll.id == poll_id).first()
    db_session.delete(poll)
    db_session.commit()
