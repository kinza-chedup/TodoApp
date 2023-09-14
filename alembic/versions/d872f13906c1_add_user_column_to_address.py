"""Add user column to address

Revision ID: d872f13906c1
Revises: 0f35b91cf773
Create Date: 2023-09-13 19:43:13.837038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd872f13906c1'
down_revision: Union[str, None] = '0f35b91cf773'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key("address_users_fk", source_table="users",
                          referent_table="address", local_cols=["address_id"],
                          remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
