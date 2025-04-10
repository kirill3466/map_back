"""add document relation

Revision ID: 95a91eabc6ff
Revises: c74610c7ee92
Create Date: 2025-01-29 18:19:38.578312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95a91eabc6ff'
down_revision: Union[str, None] = 'c74610c7ee92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('parcel_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'documents', 'parcels', ['parcel_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'documents', type_='foreignkey')
    op.drop_column('documents', 'parcel_id')
    # ### end Alembic commands ###
