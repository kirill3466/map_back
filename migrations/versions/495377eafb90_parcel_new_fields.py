"""parcel new fields

Revision ID: 495377eafb90
Revises: cfc7a66dcfbb
Create Date: 2025-01-31 00:10:52.797845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '495377eafb90'
down_revision: Union[str, None] = 'cfc7a66dcfbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('documents_parcel_id_fkey', 'documents', type_='foreignkey')
    op.create_foreign_key(None, 'documents', 'parcels', ['parcel_id'], ['id'])
    op.create_unique_constraint(None, 'parcels', ['code_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'parcels', type_='unique')
    op.drop_constraint(None, 'documents', type_='foreignkey')
    op.create_foreign_key('documents_parcel_id_fkey', 'documents', 'parcels', ['parcel_id'], ['id'])
    # ### end Alembic commands ###
