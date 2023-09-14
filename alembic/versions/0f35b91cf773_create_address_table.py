"""Create address table

Revision ID: 0f35b91cf773
Revises: 9eade9ebfa53
Create Date: 2023-09-13 19:35:23.135476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0f35b91cf773'
down_revision: Union[str, None] = '9eade9ebfa53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address1", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("state", sa.String(), nullable=False),
                    sa.Column("country", sa.String(), nullable=False),
                    sa.Column("postal_code", sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("address")
