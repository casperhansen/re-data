"""Add namespace column

Revision ID: 3144636397e6
Revises: a9e220c34e56
Create Date: 2021-02-06 12:49:54.450195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3144636397e6"
down_revision = "a9e220c34e56"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("monitored_table", sa.Column("namespace", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("monitored_table", "namespace")
    # ### end Alembic commands ###
