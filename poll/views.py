from fastapi import APIRouter, HTTPException, status

from auth.auth import CurrUser
from db.core import DbSession

from .schema import PollBase, PollCreate, PollRead
from .service import (
    create,
    delete,
    get,
    get_all,
)

router = APIRouter()


@router.post("", response_model=PollBase)
def create_poll(
    *,
    db_session: DbSession,
    poll_create: PollCreate,
    current_user: CurrUser
):
    poll = create(
        db_session=db_session,
        poll=poll_create,
        user_id=current_user.id
    )
    return poll


@router.get("/{poll_id}", response_model=PollRead)
def get_poll(
    *,
    db_session: DbSession,
    poll_id: int,
    # current_user: CurrUser
):
    poll = get(db_session=db_session, poll_id=poll_id)
    if not poll:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Голосование не найден"}],
        )
    return poll


@router.get("", response_model=list[PollRead])
def get_all_polls(
    *,
    db_session: DbSession,
    # current_user: CurrUser
):
    polls = get_all(db_session=db_session)
    if not polls:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Голосований нет"}],
        )
    return polls


@router.delete("/{poll_id}")
def delete_poll(
    *,
    db_session: DbSession,
    poll_id: int,
    # current_user: CurrUser
):
    poll = get(db_session=db_session, poll_id=poll_id)
    if not poll:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Голосование не найдено"}],
        )
    delete(db_session=db_session, poll_id=poll_id)


# @router.put("/{poll_id}", response_model=PollUpdate)
# def update_poll(
#     *,
#     db_session: DbSession,
#     poll_id: int,
#     poll_update: PollUpdate,
#     # current_user: CurrUser
# ) -> PollUpdate:
#     poll = get(db_session=db_session, poll_id=poll_id)
#     if not poll:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=[{"msg": "Голосование не найдено"}],
#         )
#     poll = update(
#         db_session=db_session,
#         poll=poll,
#         poll_update=poll_update
#     )
#     return poll
